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

# --- ESTADO DE SESIÓN DEL PERSONAJE Y JUEGO ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "hero_name" not in st.session_state:
    st.session_state.hero_name = "Carlos_Vanguard"
if "hero_class" not in st.session_state:
    st.session_state.hero_class = "Guerrero de Vanguardia"
if "hero_level" not in st.session_state:
    st.session_state.hero_level = 1
if "hero_hp" not in st.session_state:
    st.session_state.hero_hp = 100
if "hero_xp" not in st.session_state:
    st.session_state.hero_xp = 0
# Inventario de los 4 metales y recursos
if "cores" not in st.session_state: st.session_state.cores = 10
if "plata" not in st.session_state: st.session_state.plata = 250
if "oro" not in st.session_state: st.session_state.oro = 15
if "diamante" not in st.session_state: st.session_state.diamante = 2
# Habilidades desbloqueadas
if "skills" not in st.session_state:
    st.session_state.skills = ["Golpe Base", "Tajo de Miasma", "Escudo de Cores"]
# Ubicación actual en el mundo abierto
if "current_location" not in st.session_state:
    st.session_state.current_location = "El Refugio (Zona Segura / Inicio)"

# ================= PANEL DE CREACIÓN / INICIO =================
if not st.session_state.game_started:
    st.title("⚔️ MMORPG 3D Sandbox - Creación de Personaje")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Personaliza tu Héroe")
        input_name = st.text_input("Nombre del Personaje", st.session_state.hero_name)
        input_class = st.selectbox("Clase / Estilo de Combate", [
            "Guerrero de Vanguardia", 
            "Maestro de Forja de Cores", 
            "Explorador de Frontera", 
            "Nómada de las Rutas Comerciales"
        ])
        
        if st.button("🚀 Iniciar Aventura en el Mundo Abierto", use_container_width=True):
            st.session_state.hero_name = input_name
            st.session_state.hero_class = input_class
            st.session_state.game_started = True
            st.rerun()
            
    with col2:
        st.info("""
        ### Lore y Reglas del Servidor
        * **Mundo Abierto Masivo:** 8,500,000 km² terrestres y 1,550,000 km² de océanos interconectados.
        * **Economía de 4 Metales:** Sin restricciones de objetos ligados al alma (*soul-bound*). Todo se rige por **Cores, Plata, Oro y Diamante**.
        * **Libertad Total:** Cero gobierno artificial de jugadores; economía y rutas de caravanas 100% dinámicas.
        """)
    st.stop()

# ================= INTERFAZ PRINCIPAL DE JUEGO =================
st.sidebar.header(f"🛡️ Héroe: {st.session_state.hero_name}")
st.sidebar.write(f"**Clase:** {st.session_state.hero_class}")
st.sidebar.write(f"**Nivel:** {st.session_state.hero_level} | **XP:** {st.session_state.hero_xp}/100")
st.sidebar.write(f"❤️ **Salud:** {st.session_state.hero_hp}/100")
st.sidebar.markdown(f"📍 **Ubicación:** `{st.session_state.current_location}`")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Inventario de Metales")
st.sidebar.markdown(f"""
- 💠 **Cores:** `{st.session_state.cores}`
- 🥈 **Plata:** `{st.session_state.plata}`
- 🪙 **Oro:** `{st.session_state.oro}`
- 💎 **Diamante:** `{st.session_state.diamante}`
""")

if st.sidebar.button("🚪 Volver al Menú Principal"):
    st.session_state.game_started = False
    st.rerun()

# Pestañas principales que recogen todo lo creado
tab_play, tab_world, tab_skills, tab_quests, tab_codex = st.tabs([
    "🎮 Jugar y Explorar", 
    "🌍 Mapa y Continentes", 
    "⚡ Habilidades y Combate", 
    "📜 Misiones y Mazmorras", 
    "📚 Códice del Mundo (Lore)"
])

with tab_play:
    st.subheader(f"Exploración Activa: {st.session_state.current_location}")
    
    # Selector de viaje por el mundo
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
            st.success(f"¡Has extraído `{cant}` de **{metal_found}** en {st.session_state.current_location}!")

    with col2:
        if st.button("⚔️ Buscar Combate / Enemigos", use_container_width=True):
            reward_plata = random.randint(30, 90)
            st.session_state.plata += reward_plata
            st.session_state.hero_xp += 25
            if st.session_state.hero_xp >= 100:
                st.session_state.hero_level += 1
                st.session_state.hero_xp = 0
                st.balloons()
            st.info(f"¡Victoria en combate! Has derrotado a una amenaza local y ganado `{reward_plata}` de Plata y experiencia.")

    with col3:
        if st.button("🛡️ Descansar y Recuperarse", use_container_width=True):
            st.session_state.hero_hp = 100
            st.success("Te has resguardado y recuperado toda tu salud (100 HP).")

    st.markdown("---")
    st.subheader("📝 Registro de Actividad y Base de Datos en Vivo")
    try:
        logs_ref = db.collection("world_logs").limit(5)
        logs = list(logs_ref.stream())
        if logs:
            for l in logs:
                st.text(f"• {l.to_dict()}")
        else:
            st.info("Conectado a Firestore. Realiza acciones para registrar eventos globales en tiempo real.")
    except Exception as e:
        st.warning(f"Base de datos enlazada, sin registros activos aún: {e}")

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
    st.subheader("⚡ Gestión y Descubrimiento de Habilidades")
    st.write("Aquí puedes ver las habilidades de tu personaje y **añadir nuevas habilidades directamente** para probarlas al instante en combate.")
    
    st.markdown("#### Habilidades Actuales del Personaje:")
    for sk in st.session_state.skills:
        st.markdown(f"- ✨ `{sk}` (Activa y lista para usar)")
        
    st.markdown("---")
    st.subheader("➕ Añadir Nueva Habilidad al Personaje")
    new_skill_name = st.text_input("Nombre de la nueva habilidad", "Ej: Furia de Diamante")
    new_skill_type = st.selectbox("Tipo de Habilidad", ["Daño Físico / Melé", "Magia de Elemento / Cores", "Defensiva / Escudo", "Utilidad / Movilidad"])
    
    if st.button("Aprender Habilidad Inmediatamente"):
        if new_skill_name and new_skill_name not in st.session_state.skills:
            st.session_state.skills.append(f"{new_skill_name} ({new_skill_type})")
            st.success(f"¡Has aprendido y equipado con éxito la habilidad **{new_skill_name}**!")
            st.rerun()
        else:
            st.warning("Escribe un nombre válido o una habilidad que no tengas aprendida todavía.")

with tab_quests:
    st.subheader("📜 Misiones Activas y Mazmorras del Mundo")
    
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        st.markdown("### 🗺️ Misiones Principales")
        st.markdown("""
        1. **El Despertar en El Refugio** (Completada): Asegura los perímetros iniciales y comprende el flujo de la Plata.
        2. **La Senda de los Cores** (En curso): Explora las profundidades de *Ignis-Dar* para recolectar 5 Cores energéticos.
        3. **Caravana hacia Thalassia** (Disponible): Escolta una línea de transporte marítimo a través de los océanos.
        """)
    with col_q2:
        st.markdown("### 🏛️ Mazmorras Creadas")
        st.markdown("""
        *