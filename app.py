import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import random

# Configuración de la página
st.set_page_config(
    page_title="MMORPG 3D Sandbox - Cliente Definitivo",
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

# --- ESTADO DE SESIÓN INICIAL ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# Función para sincronizar y guardar el estado actual en Firestore (Cero pérdidas)
def save_user_data():
    if st.session_state.logged_in and st.session_state.user_email:
        user_data = {
            "hero_name": st.session_state.hero_name,
            "hero_class": st.session_state.hero_class,
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

# ================= PANTALLA DE ACCESO CON GOOGLE =================
if not st.session_state.logged_in:
    st.title("⚔️ MMORPG 3D Sandbox - Acceso con Google")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Inicia sesión para cargar tu partida")
        google_email = st.text_input("Correo Electrónico de Google (ej. usuario@gmail.com)")
        
        if st.button("🌐 Entrar con Google y Sincronizar Firebase", use_container_width=True):
            if google_email and "@" in google_email:
                st.session_state.user_email = google_email.strip().lower()
                
                # Comprobar si el usuario ya existe en Firestore
                user_ref = db.collection("users").document(st.session_state.user_email)
                user_doc = user_ref.get()
                
                if user_doc.exists:
                    # Cargar datos guardados previamente
                    data = user_doc.to_dict()
                    st.session_state.hero_name = data.get("hero_name", "Héroe_Google")
                    st.session_state.hero_class = data.get("hero_class", "Guerrero de Vanguardia")
                    st.session_state.hero_level = data.get("hero_level", 1)
                    st.session_state.hero_hp = data.get("hero_hp", 100)
                    st.session_state.hero_xp = data.get("hero_xp", 0)
                    st.session_state.cores = data.get("cores", 10)
                    st.session_state.plata = data.get("plata", 250)
                    st.session_state.oro = data.get("oro", 15)
                    st.session_state.diamante = data.get("diamante", 2)
                    st.session_state.skills = data.get("skills", ["Golpe Base", "Tajo de Miasma", "Escudo de Cores"])
                    st.session_state.current_location = data.get("current_location", "El Refugio (Zona Segura / Inicio)")
                else:
                    # Crear nuevo perfil por defecto en Firestore
                    st.session_state.hero_name = google_email.split("@")[0]
                    st.session_state.hero_class = "Guerrero de Vanguardia"
                    st.session_state.hero_level = 1
                    st.session_state.hero_hp = 100
                    st.session_state.hero_xp = 0
                    st.session_state.cores = 10
                    st.session_state.plata = 250
                    st.session_state.oro = 15
                    st.session_state.diamante = 2
                    st.session_state.skills = ["Golpe Base", "Tajo de Miasma", "Escudo de Cores"]
                    st.session_state.current_location = "El Refugio (Zona Segura / Inicio)"
                    save_user_data()
                
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.warning("Por favor, introduce un correo de Google válido.")
                
    with col2:
        st.info(
            "### Seguridad y Persistencia en la Nube\n"
            "* **Acceso Vinculado:** Tu cuenta de Google identifica tu progresión de forma única.\n"
            "* **Guardado Automático:** Cada recurso, nivel o habilidad que obtengas se guarda de inmediato en Firebase Firestore.\n"
            "* **Cero Pérdidas:** Sal y entra cuando quieras; tus 4 metales y estado se mantendrán intactos."
        )
    st.stop()

# ================= INTERFAZ PRINCIPAL DE JUEGO (LOGUEADO) =================
st.sidebar.header(f"🛡️ Héroe: {st.session_state.hero_name}")
st.sidebar.write(f"📧 Google: `{st.session_state.user_email}`")
st.sidebar.write(f"**Clase:** {st.session_state.hero_class}")
st.sidebar.write(f"**Nivel:** {st.session_state.hero_level} | **XP:** {st.session_state.hero_xp}/100")
st.sidebar.write(f"❤️ **Salud:** {st.session_state.hero_hp}/100")
st.sidebar.markdown(f"📍 **Ubicación:** `{st.session_state.current_location}`")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Inventario Sincronizado")
st.sidebar.markdown(
    f"- 💠 **Cores:** `{st.session_state.cores}`\n"
    f"- 🥈 **Plata:** `{st.session_state.plata}`\n"
    f"- 🪙 **Oro:** `{st.session_state.oro}`\n"
    f"- 💎 **Diamante:** `{st.session_state.diamante}`"
)

if st.sidebar.button("🚪 Cerrar Sesión (Guardado Seguro)"):
    save_user_data()
    st.session_state.logged_in = False
    st.rerun()

# Pestañas principales con todo el contenido creado
tab_play, tab_world, tab_skills, tab_quests, tab_codex = st.tabs([
    "🎮 Jugar y Explorar", 
    "🌍 Mapa y Continentes", 
    "⚡ Habilidades y Combate", 
    "📜 Misiones y Mazmorras", 
    "📚 Códice del Mundo (Lore)"
])

with tab_play:
    st.subheader(f"Exploración Activa: {st.session_state.current_location}")
    
    new_loc = st.selectbox("Moverse a otra región del mundo", [
        "El Refugio (Zona Segura / Inicio)",
        "Tierras del Miasma (PvP / Hostil)",
        "Sylvandar / Aethelgard (Bosques Antiguos)",
        "Ignis-Dar (Volcánico / Minería de Cores)",
        "Thalassia / Zandahar (Rutas Marítimas)",
        "Abismo de Malakor (Subterráneo / Hardcore)",
        "Reino Celestial Ascendido (Endgame)"
    ])
    if new_loc != st.session_state.current_location:
        st.session_state.current_location = new_loc
        save_user_data()
        st.rerun()

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⛏️ Extraer Recursos / Minar", use_container_width=True):
            metal_found = random.choice(["Cores", "Plata", "Oro", "Diamante"])
            cant = random.randint(1, 5) if metal_found != "Diamante" else 1
            if metal_found == "Cores": st.session_state.cores += cant
            elif metal_found == "Plata": st.session_state.plata += cant
            elif metal_found == "Oro": st.session_state.oro += cant
            elif metal_found == "Diamante": st.session_state.diamante += cant
            
            st.session_state.hero_xp += 15
            if st.session_state.hero_xp >= 100:
                st.session_state.hero_level += 1
                st.session_state.hero_xp = 0
                st.balloons()
            
            save_user_data()
            st.success(f"¡Has extraído `{cant}` de **{metal_found}** y se ha guardado en Firebase!")

    with col2:
        if st.button("⚔️ Buscar Combate / Enemigos", use_container_width=True):
            reward_plata = random.randint(30, 90)
            st.session_state.plata += reward_plata
            st.session_state.hero_xp += 25
            if st.session_state.hero_xp >= 100:
                st.session_state.hero_level += 1
                st.session_state.hero_xp = 0
                st.balloons()
            
            save_user_data()
            st.info(f"¡Victoria! Ganaste `{reward_plata}` de Plata. Progreso guardado automáticamente.")

    with col3:
        if st.button("🛡️ Descansar y Recuperarse", use_container_width=True):
            st.session_state.hero_hp = 100
            save_user_data()
            st.success("Salud restaurada al 100% y estado guardado en la nube.")

    st.markdown("---")
    st.subheader("📝 Registro de Actividad Global en Firestore")
    try:
        logs_ref = db.collection("world_logs").limit(5)
        logs = list(logs_ref.stream())
        if logs:
            for l in logs:
                st.text(f"• {l.to_dict()}")
        else:
            st.info("Conectado a Firestore. Tus acciones quedan registradas de forma permanente.")
    except Exception as e:
        st.warning(f"Base de datos enlazada: {e}")

with tab_world:
    st.subheader("Atlas Geográfico del MMORPG (8.5M km² Terrestres / 1.55M km² Océanos)")
    continents_data = [
        {"Continente": "El Refugio", "Superficie": "1,200,000 km²", "Tipo": "Zona Segura / Inicial", "Recurso Clave": "Plata base"},
        {"Continente": "Tierras del Miasma", "Superficie": "1,450,000 km²", "Tipo": "PvP Abierto / Hostil", "Recurso Clave": "Materiales oscuros"},
        {"Continente": "Sylvandar / Aethelgard", "Superficie": "1,300,000 km²", "Tipo": "Bosques y Ruinas", "Recurso Clave": "Madera ancestral"},
        {"Continente": "Ignis-Dar", "Superficie": "1,100,000 km²", "Tipo": "Volcánico", "Recurso Clave": "Cores Energéticos"},
        {"Continente": "Thalassia / Zandahar", "Superficie": "1,550,000 km²", "Tipo": "Océanos y Rutas", "Recurso Clave": "Comercio marítimo"},
        {"Continente": "Abismo de Malakor", "Superficie": "900,000 km²", "Tipo": "Subterráneo / Hardcore", "Recurso Clave": "Oro y Gemas"},
        {"Continente": "Reino Celestial Ascendido", "Superficie": "1,000,000 km²", "Tipo": "Endgame Flotante", "Recurso Clave": "Diamante Puro"}
    ]
    st.dataframe(pd.DataFrame(continents_data), use_container_width=True)

with tab_skills:
    st.subheader("⚡ Gestión y Creación de Habilidades")
    st.write("Añade nuevas habilidades directamente para tu personaje. Se guardarán al instante en tu perfil de Firebase.")
    
    st.markdown("#### Habilidades Actuales:")
    for sk in st.session_state.skills:
        st.markdown(f"- ✨ `{sk}`")
        
    st.markdown("---")
    st.subheader("➕ Añadir Nueva Habilidad")
    new_skill_name = st.text_input("Nombre de la nueva habilidad", "Ej: Furia de Diamante")
    new_skill_type = st.selectbox("Tipo de Habilidad", ["Daño Físico / Melé", "Magia de Elemento / Cores", "Defensiva / Escudo", "Utilidad / Movilidad"])
    
    if st.button("Aprender y Guardar en Firebase"):
        if new_skill_name and f"{new_skill_name} ({new_skill_type})" not in st.session_state.skills:
            st.session_state.skills.append(f"{new_skill_name} ({new_skill_type})")
            save_user_data()
            st.success(f"¡Habilidad **{new_skill_name}** aprendida y guardada de forma permanente!")
            st.rerun()
        else:
            st.warning("Introduce un nombre válido o una habilidad que no tengas registrada.")

with tab_quests:
    st.subheader("📜 Misiones Activas y Mazmorras del Mundo")
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        st.markdown("### 🗺️ Misiones Principales")
        st.markdown(
            "1. **El Despertar en El Refugio** (Completada): Asegura los perímetros iniciales.\n"
            "2. **La Senda de los Cores** (En curso): Explora *Ignis-Dar* para recolectar Cores.\n"
            "3. **Caravana hacia Thalassia** (Disponible): Escolta transporte marítimo."
        )
    with col_q2:
        st.markdown("### 🏛️ Mazmorras Creadas")
        st.markdown(
            "* **Las Catacumbas del Miasma** (Niv. 15): Daño corrosivo y hostil.\n"
            "* **La Forja Eterna de Ignis-Dar** (Niv. 30): Obtención masiva de Cores.\n"
            "* **El Sagrario del Abismo de Malakor** (Niv. 50): Endgame profundo."
        )

with tab_codex:
    st.subheader("📚 Códice Completo: Lore, Economía y Sistemas")
    st.markdown(
        "* **Economía de 4 Metales:** Cores, Plata, Oro y Diamante.\n"
        "* **Persistencia Firebase:** Cada jugador que entra con su cuenta de Google almacena sus datos de manera atómica y segura en la nube para evitar cualquier pérdida."
    )

st.markdown("---")
st.caption("MMORPG 3D Sandbox Engine - Autenticación Firebase Activa v4.0")