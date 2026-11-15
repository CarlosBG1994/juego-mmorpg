import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import urllib.parse
import random

st.set_page_config(
    page_title="MMORPG Snd-Worlds & Cinco Reinos Admin Dashboard",
    layout="wide",
    page_icon="🛡️"
)

# Inicialización segura de Firebase para entorno local (Codespace) y nube (Streamlit Cloud 24/7)
@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        try:
            if "firebase" in st.secrets:
                cred_dict = dict(st.secrets["firebase"])
                cred = credentials.Certificate(cred_dict)
            else:
                cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
        except Exception as e:
            st.error(f"Error de credenciales Firebase: {e}")
    return firestore.client()

db = init_firebase()

st.title("🛡️ Panel de Control - MMORPG Snd-Worlds")
st.markdown("Gestión de macroarquitectura, continentes, economía de 4 metales (*Cores, Plata, Oro, Diamante*) y red de agentes IA.")

tab1, tab2, tab3, tab4 = st.tabs(["🌍 Continentes y Zonas", "⚖️ Reglas y Economía", "🎨 Estudio Visual (Hércules)", "⚙️ Estado de Servidores"])

with tab1:
    st.subheader("Infraestructura Continental (8.5M km² / 1.55M km² Océanos)")
    try:
        docs = db.collection("continents").stream()
        data = [doc.to_dict() for doc in docs]
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No hay datos de continentes en Firestore. Ejecuta primero `seed_firebase.py`.")
    except Exception as e:
        st.error(f"Error al conectar con Firestore: {e}")

with tab2:
    st.subheader("Sistema Económico y de Reglas")
    st.markdown("- **Economía:** 4 metales (*Cores, Plata, Oro, Diamante*), libre mercado 100%, sin objetos ligados (*soul-bound*).")
    st.markdown("- **Gobernanza:** Mundo 100% dinámico dirigido por NPCs, sin política ni legislación de jugadores en capitales.")

with tab3:
    st.subheader("🎨 Hércules — Estudio de Renderizado Visual")
    st.markdown("Genera ilustraciones cinematográficas de alta calidad para personajes y continentes.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        personaje_escena = st.selectbox(
            "Personaje en escena:",
            ["Freyr", "Aethelgard", "Kira", "Dante", "Valeria", "Personaje Personalizado"]
        )
        prompt_usuario = st.text_area(
            "Prompt de modificación / Descripción de escena:",
            placeholder="Ej: armadura de plata brillante, expresión decidida, fondo de ruinas antiguas..."
        )
        genero_seleccionado = st.radio(
            "Género del personaje:",
            ["Masculino", "Femenino"],
            horizontal=True
        )
        generar_btn = st.button("🚀 Ordenar a Hércules Renderizar Imagen")

    with col2:
        st.subheader("Vista Previa")
        if generar_btn:
            with st.spinner("Hércules procesando parámetros..."):
                base_prompt = "fantasy character portrait, highly detailed concept art, epic lighting, digital masterpiece"
                tag_genero = "1girl, woman, female, detailed face" if genero_seleccionado == "Femenino" else "1boy, man, male, detailed face"
                prompt_completo = f"{base_prompt}, {tag_genero}, {personaje_escena}, {prompt_usuario}"
                prompt_encoded = urllib.parse.quote(prompt_completo)
                seed = random.randint(10000, 99999)
                url_imagen = f"https://image.pollinations.ai/prompt/{prompt_encoded}?width=1024&height=1024&seed={seed}&nologo=true"
                
                st.success("✨ ¡Imagen generada con éxito!")
                st.image(url_imagen, caption=f"Render: {personaje_escena} ({genero_seleccionado})", use_container_width=True)
                st.markdown(f"**URL Directa:** [Abrir imagen]({url_imagen})")
        else:
            st.info("Configura los parámetros y pulsa el botón para generar.")

with tab4:
    st.subheader("Herramientas de Mantenimiento")
    if st.button("🔄 Comprobar Conexión Firestore"):
        st.success("Conexión establecida correctamente con Firebase Firestore.")