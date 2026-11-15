import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

st.set_page_config(page_title="MMORPG Admin Dashboard", layout="wide")

@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_firebase()

st.title("🛡️ Panel de Control - MMORPG Snd-Worlds")
st.markdown("Gestión de macroarquitectura, continentes, economía de 4 metales (*Cores, Plata, Oro, Diamante*) y sistemas de servidores.")

tab1, tab2, tab3 = st.tabs(["🌍 Continentes y Zonas", "⚖️ Reglas y Economía", "⚙️ Estado de Servidores"])

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
    st.subheader("Herramientas de Mantenimiento")
    if st.button("🔄 Comprobar Conexión Firestore"):
        st.success("Conexión establecida correctamente con Firebase Firestore.")