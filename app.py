import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import random

# Configuración de la página
st.set_page_config(
    page_title="MMORPG 3D Sandbox",
    page_icon="⚔️",
    layout="wide"
)

# Inicialización segura de Firebase
@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        try:
            if "firebase" in st.secrets:
                cred_dict = dict(st.secrets["firebase"])
                cred = credentials.Certificate(cred_dict)
                firebase_admin.initialize_app(cred)
            else:
                cred = credentials.Certificate("serviceAccountKey.json")
                firebase_admin.initialize_app(cred)
        except Exception:
            cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
    return firestore.client()

try:
    db = init_firebase()
except Exception as e:
    st.error(f"Error crítico al conectar con Firebase: {e}")
    st.stop()

# --- ESTADO DE SESIÓN ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

def save_user_data():
    if st.session_state.logged_in and st.session_state.user_email:
        user_data = {
            "hero_name": st.session_state.hero_name,
            "hero_level": st.session_state.hero_level,
            "hero_hp": st.session_state.hero_hp,
            "hero_xp": st.session_state.hero_xp,
            "cores": st.session_state.cores,
            "plata": st.session_state.plata,
            "oro": st.session_state.oro,
            "diamante": st.session_state.diamante,
            "skills": st.session_state.skills,
            "current_location": st.session_state.current_location
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= PANTALLA DE INICIO (ESTILO LOGIN / GOOGLE) =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>⚔️ MUNDO MISTERIOSO - MMORPG ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Sobrevive, explora y comercia en el vasto sandbox global de 4 metales.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        with st.container():
            st.markdown("### Acceso al Servidor")
            user_input = st.text_input("Nombre de usuario o Correo")
            pass_input = st.text_input("Contraseña", type="password")
            
            if st.button("Entrar", use_container_width=True):
                if user_input:
                    st.session_state.user_email = user_input.strip().lower()
                    
                    # Carga o inicialización en Firestore (Cero pérdidas)
                    user_ref = db.collection("users").document(st.session_state.user_email)
                    user_doc = user_ref.get()
                    
                    if user_doc.exists:
                        data = user_doc.to_dict()
                        st.session_state.hero_name = data.get("hero_name", user_input.split("@")[0])
                        st.session_state.hero_level = data.get("hero_level", 1)
                        st.session_state.hero_hp = data.get("hero_hp", 100)
                        st.session_state.hero_xp = data.get("hero_xp", 0)
                        st.session_state.cores = data.get("cores", 5)
                        st.session_state.plata = data.get("plata", 100)
                        st.session_state.oro = data.get("oro", 10)
                        st.session_state.diamante = data.get("diamante", 1)
                        st.session_state.skills = data.get("skills", ["Golpe Base", "Tajo Inicial"])
                        st.session_state.current_location = data.get("current_location", "El Refugio (Zona Inicial)")
                    else:
                        st.session_state.hero_name = user_input.split("@")[0]
                        st.session_state.hero_level = 1
                        st.session_state.hero_hp = 100
                        st.session_state.hero_xp = 0
                        st.session_state.cores = 5
                        st.session_state.plata = 100
                        st.session_state.oro = 10
                        st.session_state.diamante = 1
                        st.session_state.skills = ["Golpe Base", "Tajo Inicial"]
                        st.session_state.current_location = "El Refugio (Zona Inicial)"
                        save_user_data()
                        
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.warning("Introduce un usuario válido.")
            
            if st.button("Entrar con Google", use_container_width=True):
                st.session_state.user_email = "carlos.google@mmorpg.com"
                st.session_state.hero_name = "Carlos_Vanguard"
                st.session_state.hero_level = 1
                st.session_state.hero_hp = 100
                st.session_state.hero_xp = 0
                st.session_state.cores = 5
                st.session_state.plata = 100
                st.session_state.oro = 10
                st.session_state.diamante = 1
                st.session_state.skills = ["Golpe Base", "Tajo Inicial"]
                st.session_state.current_location = "El Refugio (Zona Inicial)"
                st.session_state.logged_in = True
                save_user_data()
                st.rerun()
    st.stop()

# ================= JUEGO PRINCIPAL (ARRANQUE EN EL REFUGIO) =================
st.sidebar.header(f"🛡️ Héroe: {st.session_state.hero_name}")
st.sidebar.write(f"**Nivel:** {st.session_state.hero_level} | **XP:** {st.session_state.hero_xp}/100")
st.sidebar.write(f"❤️ **Salud:** {st.session_state.hero_hp}/100")
st.sidebar.markdown(f"📍 **Ubicación Actual:** `{st.session_state.current_location}`")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Inventario de Metales")
st.sidebar.markdown(
    f"- 💠 **Cores:** `{st.session_state.cores}`\n"
    f"- 🥈 **Plata:** `{st.session_state.plata}`\n"
    f"- 🪙 **Oro:** `{st.session_state.oro}`\n"
    f"- 💎 **Diamante:** `{st.session_state.diamante}`"
)

if st.sidebar.button("🚪 Cerrar Sesión"):
    save_user_data()
    st.session_state.logged_in = False
    st.rerun()

# Pestañas principales limpias de juego
tab_play, tab_skills, tab_world, tab_codex = st.tabs([
    "🎮 Jugar y Explorar", 
    "⚡ Habilidades", 
    "🌍 El Mundo", 
    "📚 Códice"
])

with tab_play:
    st.subheader(f"Zona Actual: {st.session_state.current_location}")
    st.info("Te encuentras en **El Refugio**, el único continente y punto de partida seguro del mundo. Desde aquí debes avanzar, cazar y recolectar para progresar.")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⛏️ Explorar y Recolectar", use_container_width=True):
            metal = random.choice(["Cores", "Plata", "Oro"])
            cant = random.randint(1, 4)
            if metal == "Cores": st.session_state.cores += cant
            elif metal == "Plata": st.session_state.plata += cant
            elif metal == "Oro": st.session_state.oro += cant
            
            st.session_state.hero_xp += 20
            if st.session_state.hero_xp >= 100:
                st.session_state.hero_level += 1
                st.session_state.hero_xp = 0
                st.balloons()
            save_user_data()
            st.success(f"¡Has encontrado `{cant}` de **{metal}** en El Refugio!")

    with col2:
        if st.button("⚔️ Enfrentar Amenaza Local", use_container_width=True):
            reward = random.randint(20, 50)
            st.session_state.plata += reward
            st.session_state.hero_xp += 30
            if st.session_state.hero_xp >= 100:
                st.session_state.hero_level += 1
                st.session_state.hero_xp = 0
                st.balloons()
            save_user_data()
            st.info(f"¡Combate superado! Obtuviste `{reward}` de Plata.")

    with col3:
        if st.button("🛡️ Descansar", use_container_width=True):
            st.session_state.hero_hp = 100
            save_user_data()
            st.success("Salud restaurada al máximo.")

with tab_skills:
    st.subheader("⚡ Habilidades del Personaje")
    st.write("Gestiona y aprende nuevas habilidades para tu estilo de combate:")
    for sk in st.session_state.skills:
        st.markdown(f"- ✨ `{sk}`")
        
    st.markdown("---")
    new_sk = st.text_input("Añadir nueva habilidad")
    if st.button("Registrar Habilidad"):
        if new_sk and new_sk not in st.session_state.skills:
            st.session_state.skills.append(new_sk)
            save_user_data()
            st.success(f"¡Habilidad **{new_sk}** aprendida!")
            st.rerun()

with tab_world:
    st.subheader("🌍 Estado del Mundo Abierto")
    st.write("El mundo se compone de 8,500,000 km² terrestres. Actualmente tu acceso está limitado a **El Refugio** hasta que alcances el nivel necesario para explorar las rutas exteriores.")
    st.markdown("""
    * **El Refugio:** Activo (Zona Inicial Segura)
    * **Tierras del Miasma / Ignis-Dar / Abismo:** Bloqueadas hasta avanzar de nivel.
    """)

with tab_codex:
    st.subheader("📚 Códice y Economía de los 4 Metales")
    st.markdown("""
    * **Cores, Plata, Oro, Diamante:** Ecosistema económico 100% abierto sin restricciones ni objetos ligados.
    * **Persistencia:** Conectado a Firebase Firestore.
    """)

st.markdown("---")
st.caption("MMORPG 3D Sandbox - Servidor Activo")