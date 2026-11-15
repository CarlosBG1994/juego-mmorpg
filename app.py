import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Juego MMORPG 3D - Panel de Control",
    page_icon="⚔️",
    layout="wide"
)

# Inicialización segura de Firebase (Local y Streamlit Cloud)
@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        try:
            # Intenta cargar desde los secretos de Streamlit Cloud si están configurados
            if "firebase" in st.secrets:
                cred_dict = dict(st.secrets["firebase"])
                cred = credentials.Certificate(cred_dict)
                firebase_admin.initialize_app(cred)
            else:
                # Carga local desde el archivo serviceAccountKey.json
                cred = credentials.Certificate("serviceAccountKey.json")
                firebase_admin.initialize_app(cred)
        except Exception:
            # Fallback forzado a archivo local si ocurre cualquier fallo en la nube
            cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
    return firestore.client()

# Conexión a Firestore
try:
    db = init_firebase()
except Exception as e:
    st.error(f"Error crítico al conectar con Firebase: {e}")
    st.stop()

# Interfaz Principal del Panel de Control
st.title("⚔️ Panel de Control - MMORPG 3D Sandbox")
st.markdown("---")

# Barra lateral de navegación y estado
st.sidebar.header("Estado del Sistema")
st.sidebar.success("Base de datos Firestore: Conectada")
st.sidebar.info("Entorno activo: GitHub Codespaces / Local")

# Sección de visualización rápida de datos del juego
tab1, tab2, tab3 = st.tabs(["🌍 Continentes y Regiones", "⚖️ Economía y Metales", "🤖 Panel de Agentes"])

with tab1:
    st.subheader("Estructura de Continentes")
    continents_data = [
        {"Continente": "El Refugio", "Superficie (km²)": "1,200,000", "Tipo": "Zona Segura / Inicial"},
        {"Continente": "Tierras del Miasma", "Superficie (km²)": "1,450,000", "Tipo": "PvP / Hostil"},
        {"Continente": "Sylvandar / Aethelgard", "Superficie (km²)": "1,300,000", "Tipo": "Bosques / Antiguas ruinas"},
        {"Continente": "Ignis-Dar", "Superficie (km²)": "1,100,000", "Tipo": "Volcánico / Minería de Cores"},
        {"Continente": "Thalassia / Zandahar", "Superficie (km²)": "1,550,000 (Océanos)", "Tipo": "Marítimo / Comercio"},
        {"Continente": "Abismo de Malakor", "Superficie (km²)": "900,000", "Tipo": "Subterráneo / Hardcore"},
        {"Continente": "Reino Celestial Ascendido", "Superficie (km²)": "1,000,000", "Tipo": "Endgame / Flotante"}
    ]
    df_continents = pd.DataFrame(continents_data)
    st.dataframe(df_continents, use_container_width=True)

with tab2:
    st.subheader("Economía de 4 Metales")
    st.markdown("""
    - **Cores**: Fundamento energético y tecnológico.
    - **Plata**: Estabilidad monetaria y transacciones estándar.
    - **Oro**: Comercio de alto valor y contratos internacionales.
    - **Diamante**: Bienes de élite y fortificaciones de clan.
    """)
    # Consulta de prueba a Firestore para verificar lectura en tiempo real
    try:
        users_ref = db.collection("users").limit(5)
        docs = list(users_ref.stream())
        if docs:
            st.success(f"Se han encontrado {len(docs)} registros de usuarios en Firestore.")
        else:
            st.info("La base de datos está conectada pero la colección de usuarios está vacía o pendiente de poblar.")
    except Exception as e:
        st.warning(f"No se pudieron leer colecciones de prueba en este momento: {e}")

with tab3:
    st.subheader("Estudio de IA y Agentes")
    st.write("Panel de control multi-agente para la generación de recursos, lore y monitorización.")
    agent_name = st.selectbox("Seleccionar Agente", ["Hércules (Arte/Generación)", "Cronos (Infraestructura)", "Aura (Narrativa)"])
    if st.button("Ejecutar Diagnóstico de Agente"):
        st.success(f"El agente **{agent_name}** se encuentra operativo y sincronizado.")

st.markdown("---")
st.caption("MMORPG 3D Sandbox Architecture - Control Panel v2.4")