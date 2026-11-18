import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import random
from datetime import datetime

# Importar módulos de Snd-Worlds
from config import CONTINENTE_INICIAL, CONTINENTES_OFICIALES, REINOS_VALORIA, RAZAS_Y_CLASSES, MONTURAS_COMUNES, SUBFORMAS_BESTIA, ESTADISTICAS_BASE_CLASES
from bestiario import BESTIARIO_ZONAS
from habilidades import CATALOGO_HABILIDADES_GLOBAL_DETALLADO, CATALOGO_EDIFICIOS, CATALOGO_OCULTAS
from canvas_engine import generar_canvas_html
from crafting_talleres import TALLERES_OFICIOS, simular_crafteo

st.set_page_config(
    page_title="Snd-Worlds MMORPG Sandbox",
    page_icon="⚔️",
    layout="wide"
)

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
for key, default in [
    ("logged_in", False), ("user_email", ""), ("hero_name", ""),
    ("raza", "Humano"), ("subforma", "Hombre Lobo"), ("genero", "Hombre"),
    ("clase", "Invocador"), ("continente", CONTINENTE_INICIAL),
    ("reino_actual", "Reino Humano de Valoria"), ("asentamiento_actual", "Aurelia Capital"),
    ("plano_vista", "Exterior (Puertas del Asentamiento)"),
    ("hero_level", 1), ("hero_hp", 100), ("max_hp", 100), ("hero_xp", 0),
    ("puntos_libres", 0),
    ("str", 5), ("int", 16), ("agi", 6), ("vit", 10), ("luk", 10),
    ("cores", 15), ("plata", 200), ("oro", 20), ("diamante", 3),
    ("habilidades_equipadas", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno"]),
    ("grimorio_inventario", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno", "Muro de Hielo Permafrost"]),
    ("habilidades_fusionadas", []),
    ("inventario", ["Ropa de Viajero", "Raciones de Pan", "Escama de Magma", "Mineral de Hierro Bruto", "Piel Desértica", "Bulbo Luminoso"]),
    ("montura_activa", "Ninguna"),
    ("misiones_activas", [{"id": "m1", "titulo": "Caza de Goblins en Valoria", "objetivo": "Derrota 5 Goblins", "progreso": 0, "meta": 5, "completada": False}]),
    ("has_character", False)
]:
    if key not in st.session_state:
        st.session_state[key] = default

def save_user_data():
    if st.session_state.logged_in and st.session_state.user_email:
        user_data = {
            "hero_name": st.session_state.hero_name,
            "raza": st.session_state.raza,
            "clase": st.session_state.clase,
            "continente": st.session_state.continente,
            "reino_actual": st.session_state.reino_actual,
            "asentamiento_actual": st.session_state.asentamiento_actual,
            "hero_level": st.session_state.hero_level,
            "hero_hp": st.session_state.hero_hp,
            "max_hp": st.session_state.max_hp,
            "hero_xp": st.session_state.hero_xp,
            "puntos_libres": st.session_state.puntos_libres,
            "str": st.session_state.str,
            "int": st.session_state.int,
            "agi": st.session_state.agi,
            "vit": st.session_state.vit,
            "luk": st.session_state.luk,
            "cores": st.session_state.cores,
            "plata": st.session_state.plata,
            "oro": st.session_state.oro,
            "diamante": st.session_state.diamante,
            "habilidades_equipadas": st.session_state.habilidades_equipadas,
            "grimorio_inventario": st.session_state.grimorio_inventario,
            "habilidades_fusionadas": st.session_state.habilidades_fusionadas,
            "inventario": st.session_state.inventario,
            "montura_activa": st.session_state.montura_activa,
            "misiones_activas": st.session_state.misiones_activas,
            "has_character": st.session_state.has_character
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Arquitectura Modular | 1,870 Habilidades | Canvas Real-Time | Omni-Oficios</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("### Acceso al Servidor")
        user_input = st.text_input("Correo electrónico o Usuario")
        
        if st.button("Conectar al Servidor", use_container_width=True):
            if user_input:
                email = user_input.strip().lower()
                st.session_state.user_email = email
                user_ref = db.collection("users").document(email)
                user_doc = user_ref.get()
                
                if user_doc.exists:
                    data = user_doc.to_dict()
                    st.session_state.hero_name = data.get("hero_name", email.split("@")[0])
                    st.session_state.raza = data.get("raza", "Humano")
                    st.session_state.clase = data.get("clase", "Invocador")
                    st.session_state.continente = data.get("continente", CONTINENTE_INICIAL)
                    st.session_state.reino_actual = data.get("reino_actual", "Reino Humano de Valoria")
                    st.session_state.asentamiento_actual = data.get("asentamiento_actual", "Aurelia Capital")
                    st.session_state.hero_level = data.get("hero_level", 1)
                    st.session_state.hero_hp = data.get("hero_hp", 100)
                    st.session_state.max_hp = data.get("max_hp", 100)
                    st.session_state.hero_xp = data.get("hero_xp", 0)
                    st.session_state.puntos_libres = data.get("puntos_libres", 0)
                    st.session_state.str = data.get("str", 5)
                    st.session_state.int = data.get("int", 16)
                    st.session_state.agi = data.get("agi", 6)
                    st.session_state.vit = data.get("vit", 10)
                    st.session_state.luk = data.get("luk", 10)
                    st.session_state.habilidades_equipadas = data.get("habilidades_equipadas", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno"])
                    st.session_state.grimorio_inventario = data.get("grimorio_inventario", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno", "Muro de Hielo Permafrost"])
                    st.session_state.habilidades_fusionadas = data.get("habilidades_fusionadas", [])
                    st.session_state.inventario = data.get("inventario", ["Ropa de Viajero", "Raciones de Pan"])
                    st.session_state.montura_activa = data.get("montura_activa", "Ninguna")
                    st.session_state.misiones_activas = data.get("misiones_activas", [])
                    st.session_state.has_character = data.get("has_character", True)
                else:
                    st.session_state.hero_name = email.split("@")[0]
                    st.session_state.has_character = False
                
                st.session_state.logged_in = True
                st.rerun()
    st.stop()

# ================= CREACIÓN DE PERSONAJE =================
if not st.session_state.has_character:
    st.markdown("<h2 style='text-align: center; color: #ffaa00;'>🛡️ Creación de Tu Héroe en Snd-Worlds</h2>", unsafe_allow_html=True)
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.session_state.hero_name = st.text_input("Nombre del Héroe", value=st.session_state.hero_name)
        st.session_state.raza = st.selectbox("Raza / Facción", list(RAZAS_Y_CLASSES.keys()))
        if st.session_state.raza == "Hombre Bestia":
            st.session_state.subforma = st.selectbox("Sub-forma de Bestia", SUBFORMAS_BESTIA)
    with col_c2:
        info_raza = RAZAS_Y_CLASSES[st.session_state.raza]
        st.session_state.clase = st.selectbox("Clase Oficial", info_raza["clases"])
        st.session_state.reino_actual = info_raza["reino_inicio"]
        st.session_state.asentamiento_actual = f"Asentamiento de {st.session_state.raza}"
        
        base_stats = ESTADISTICAS_BASE_CLASES.get(st.session_state.clase, {"str": 10, "int": 10, "agi": 10, "vit": 10, "luk": 10, "hp": 100})
        st.session_state.str = base_stats["str"]
        st.session_state.int = base_stats["int"]
        st.session_state.agi = base_stats["agi"]
        st.session_state.vit = base_stats["vit"]
        st.session_state.luk = base_stats["luk"]
        st.session_state.max_hp = base_stats["hp"]
        st.session_state.hero_hp = base_stats["hp"]

        monturas_disponibles = info_raza["monturas_exclusivas"] + MONTURAS_COMUNES
        st.session_state.montura_activa = monturas_disponibles[0]

        st.info(f"🐎 **Montura Asignada:** `{st.session_state.montura_activa}`\n\n*{info_raza['lore']}*")

    if st.button("🚀 ¡Entrar al Mundo!", use_container_width=True):
        if st.session_state.hero_name:
            st.session_state.has_character = True
            save_user_data()
            st.rerun()
    st.stop()

# ================= BARRA LATERAL =================
st.sidebar.header(f"🛡️ {st.session_state.hero_name}")
st.sidebar.write(f"**Raza:** {st.session_state.raza} | **Clase:** {st.session_state.clase}")
st.sidebar.write(f"⭐ **Nivel:** {st.session_state.hero_level} | ❤️ **HP:** {st.session_state.hero_hp}/{st.session_state.max_hp}")
st.sidebar.write(f"🐎 **Montura:** `{st.session_state.montura_activa}`")
st.sidebar.markdown(f"🌍 **Continente:** `{st.session_state.continente}`")
st.sidebar.markdown(f"🏰 **Reino / Asentamiento:** `{st.session_state.asentamiento_actual}`")

if st.sidebar.button("🚪 Cerrar Sesión"):
    save_user_data()
    st.session_state.logged_in = False
    st.session_state.has_character = False
    st.rerun()

# Pestañas principales
tab_canvas, tab_craft, tab_stats, tab_skills, tab_dungeon, tab_quests, tab_edificio, tab_viaje_local, tab_bag, tab_world = st.tabs([
    "🎮 Motor PvE (Tiempo Real)",
    "🛠️ Talleres & Oficios",
    "📊 Atributos & Nivel",
    "✨ Grimorio (15 Habilidades)",
    "🏰 Mazmorras & Jefes",
    "📜 Misiones",
    "🏪 Tienda Gremio",
    "🗺️ Bestiario y Zonas",
    "🎒 Mochila",
    "🌍 Continentes"
])

# ================= TAB 1: CANVAS PVE EN TIEMPO REAL =================
with tab_canvas:
    col_top1, col_top2 = st.columns([2.5, 1.5])
    with col_top1:
        st.subheader(f"📍 {st.session_state.asentamiento_actual} — Combate en Tiempo Real")
    with col_top2:
        if st.session_state.plano_vista == "Exterior (Puertas del Asentamiento)":
            if st.button("🚪 Cruzar Murallas a Zonas de Caza (PvE)", use_container_width=True, type="primary"):
                st.session_state.plano_vista = "Zona de Caza y Combate"
                st.rerun()
        else:
            if st.button("🏰 Volver al Refugio del Asentamiento", use_container_width=True):
                st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
                st.rerun()

    st.markdown("#### ⚡ Barra de Habilidades Activas (Dominas hasta 15 habilidades)")
    cols_sk = st.columns(5)
    for i, sk_name in enumerate(st.session_state.habilidades_equipadas):
        with cols_sk[i]:
            if sk_name:
                st.button(f"[{i+1}] {sk_name}\n(Poderes x3)", key=f"btn_sk_{i}")
            else:
                st.button(f"[{i+1}] Vacío", disabled=True, key=f"btn_sk_empty_{i}")

    es_caza = "Caza" in st.session_state.plano_vista
    reino_actual_str = st.session_state.reino_actual
    datos_reino_actual = BESTIARIO_ZONAS.get(reino_actual_str, BESTIARIO_ZONAS["Reino Humano de Valoria"])
    
    html_code = generar_canvas_html(es_caza, reino_actual_str, datos_reino_actual["mobs"], datos_reino_actual.get("jefes_zona", []))
    st.components.v1.html(html_code, height=480)

# ================= TAB 2: TALLERES Y OFICIOS =================
with tab_craft:
    st.subheader("🛠️ Centro General de Talleres y Oficios (Omni-Oficios)")
    st.write("Acceso universal a los 10 talleres. Fabrica equipo y objetos 100% libres de ataduras (*0% Soul-Bound*).")
    
    taller_sel = st.selectbox("Selecciona el Taller", list(TALLERES_OFICIOS.keys()))
    info_taller = TALLERES_OFICIOS[taller_sel]
    st.info(info_taller["descripcion"])

    for receta in info_taller["recetas"]:
        with st.expander(f"✨ {receta['nombre']} — Tier: {receta['tier']} ({receta['tipo']})"):
            st.write(f"**Materiales requeridos:**")
            for mat, cant in receta["materiales"].items():
                en_inv = st.session_state.inventario.count(mat)
                col = "green" if en_inv >= cant else "red"
                st.markdown(f"- :{col}[{cant}x {mat}] (Tienes: {en_inv})")
            
            if st.button(f"🔨 Fabricar {receta['nombre']}", key=f"craft_{receta['id']}"):
                exito, msg = simular_crafteo(taller_sel, receta["id"], st.session_state.inventario)
                if exito:
                    for mat, cant in receta["materiales"].items():