import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Juego MMORPG 3D - Panel del Mundo",
    page_icon="⚔️",
    layout="wide"
)

# Inicialización segura de Firebase (Local y Streamlit Cloud)
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

# Conexión a Firestore
try:
    db = init_firebase()
except Exception as e:
    st.error(f"Error crítico al conectar con Firebase: {e}")
    st.stop()

# Interfaz Principal del Panel del Juego
st.title("⚔️ MMORPG 3D Sandbox - Panel de Control del Mundo")
st.markdown("---")

# Barra lateral de estado
st.sidebar.header("Estado del Servidor")
st.sidebar.success("Base de datos Firestore: Conectada")
st.sidebar.info("Modo: Sandbox JRPG en vivo")

# Pestañas principales del juego
tab1, tab2 = st.tabs(["🌍 Continentes y Geografía", "⚖️ Economía y Metales"])

with tab1:
    st.subheader("Estructura de los 7 Continentes")
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
    st.subheader("Sistema Económico de 4 Metales")
    st.markdown("""
    - **Cores**: Energía, núcleos tecnológicos y progresión avanzada.
    - **Plata**: Estabilidad monetaria y transacciones comerciales estándar.
    - **Oro**: Comercio pesado, rutas de caravanas y contratos de gremios.
    - **Diamante**: Bienes de élite, posesiones y fortificaciones del mundo.
    """)
    
    try:
        users_ref = db.collection("users").limit(5)
        docs = list(users_ref.stream())
        if docs:
            st.success(f"Se han cargado {len(docs)} perfiles de jugadores desde Firestore.")
        else:
            st.info("Base de datos conectada. Colección de usuarios vacía o lista para inicializar.")
    except Exception as e:
        st.warning(f"No se pudieron leer los registros de usuarios: {e}")

st.markdown("---")
st.caption("MMORPG 3D Sandbox Engine v2.4")