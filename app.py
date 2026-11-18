import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import random
from datetime import datetime

# Importar módulos de Snd-Worlds
from config import CONTINENTE_INICIAL, RAZAS_Y_CLASSES, ESTADISTICAS_BASE_CLASES, SUBFORMAS_BESTIA, CONTINENTES_OFICIALES
from bestiario import BESTIARIO_ZONAS
from habilidades import CATALOGO_HABILIDADES_GLOBAL, CATALOGO_EDIFICIOS, CATALOGO_OCULTAS
from canvas_engine import generar_canvas_html
from crafting_talleres import TALLERES_OFICIOS, simular_crafteo

# Configuración de la página
st.set_page_config(
    page_title="Snd-Worlds MMORPG Sandbox",
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
    ("habilidades_equipadas", ["Invocación de Golem de Roca", "Bola de Fuego", "Tajo Inicial", "", ""]),
    ("grimorio_inventario", ["Invocación de Golem de Roca", "Bola de Fuego", "Tajo Inicial", "Muro de Fuego"]),
    ("habilidades_fusionadas", []),
    ("inventario", ["Ropa de Viajero", "Raciones de Pan", "Escama de Magma", "Mineral de Hierro Bruto", "Piel Desértica", "Bulbo Luminoso"]),
    ("montura_activa", "Ninguna"),
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
            "has_character": st.session_state.has_character
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= PANTALLA DE LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Arquitectura Modular | Bestiario 1-60 | Omni-Oficios | Canvas PvE</p>", unsafe_allow_html=True)
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
                    st.session_state.habilidades_equipadas = data.get("habilidades_equipadas", ["Invocación de Golem de Roca", "Bola de Fuego", "Tajo Inicial", "", ""])
                    st.session_state.grimorio_inventario = data.get("grimorio_inventario", ["Invocación de Golem de Roca", "Bola de Fuego"])
                    st.session_state.habilidades_fusionadas = data.get("habilidades_fusionadas", [])
                    st.session_state.inventario = data.get("inventario", ["Ropa de Viajero", "Raciones de Pan"])
                    st.session_state.montura_activa = data.get("montura_activa", "Ninguna")
                    st.session_state.has_character = data.get("has_character", True)
                else:
                    st.session_state.hero_name = email.split("@")[0]
                    st.session_state.has_character = False
                
                st.session_state.logged_in = True
                st.rerun()
    st.stop()

# ================= PANTALLA DE CREACIÓN DE PERSONAJE =================
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
        st.session_state.asentamiento_actual = f"Capital de {st.session_state.raza}"
        
        base_stats = ESTADISTICAS_BASE_CLASES.get(st.session_state.clase, {"str": 10, "int": 10, "agi": 10, "vit": 10, "luk": 10, "hp": 100})
        st.session_state.str = base_stats["str"]
        st.session_state.int = base_stats["int"]
        st.session_state.agi = base_stats["agi"]
        st.session_state.vit = base_stats["vit"]
        st.session_state.luk = base_stats["luk"]
        st.session_state.max_hp = base_stats["hp"]
        st.session_state.hero_hp = base_stats["hp"]

        st.info(f"🐎 **Monturas Nativas Exclusivas:** {', '.join(info_raza['monturas'])}\n\n*{info_raza['lore']}*")

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

# Pestañas principales (Incluyendo Talleres y Oficios)
tab_canvas, tab_craft, tab_stats, tab_skills, tab_edificio, tab_viaje_local, tab_bag, tab_world, tab_quests, tab_p2p = st.tabs([
    "🎮 Motor PvE & Canvas",
    "🛠️ Talleres & Oficios",
    "📊 Atributos & Nivel",
    "✨ Grimorio & Fusión",
    "🏪 Tienda & Caza",
    "🗺️ Bestiario 1-60",
    "🎒 Mochila & Monturas",
    "🌍 Continentes",
    "📜 Misiones",
    "🤝 Encargos P2P"
])

# ================= PESTAÑA 1: MOTOR PVE (HTML5 CANVAS) =================
with tab_canvas:
    col_top1, col_top2 = st.columns([2.5, 1.5])
    with col_top1:
        st.subheader(f"📍 {st.session_state.asentamiento_actual} — Plano: {st.session_state.hero_name}")
    with col_top2:
        if st.session_state.plano_vista == "Exterior (Puertas del Asentamiento)":
            if st.button("🚪 Cruzar Murallas a Zonas de Caza (PvE)", use_container_width=True, type="primary"):
                st.session_state.plano_vista = "Zona de Caza y Combate"
                st.rerun()
        else:
            if st.button("🏰 Volver al Refugio de la Ciudad", use_container_width=True):
                st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
                st.rerun()

    st.markdown("#### ⚡ Barra de Habilidades Activas (5 Slots)")
    cols_sk = st.columns(5)
    for i, sk_name in enumerate(st.session_state.habilidades_equipadas):
        with cols_sk[i]:
            if sk_name:
                tier_act = "Tier I"
                if st.session_state.hero_level >= 30: tier_act = "Tier III"
                elif st.session_state.hero_level >= 15: tier_act = "Tier II"
                st.button(f"[{i+1}] {sk_name}\n({tier_act})", key=f"btn_sk_{i}")
            else:
                st.button(f"[{i+1}] Vacío", disabled=True, key=f"btn_sk_empty_{i}")

    es_caza = "Caza" in st.session_state.plano_vista
    reino_actual_str = st.session_state.reino_actual
    datos_reino_actual = BESTIARIO_ZONAS.get(reino_actual_str, BESTIARIO_ZONAS["Reino Humano de Valoria"])
    
    html_code = generar_canvas_html(es_caza, reino_actual_str, datos_reino_actual["mobs"], datos_reino_actual["jefes"])
    st.components.v1.html(html_code, height=520)

# ================= PESTAÑA 2: TALLERES Y OFICIOS (OMNI-OFICIOS) =================
with tab_craft:
    st.subheader("🛠️ Centro General de Talleres y Oficios (Acceso Universal)")
    st.write("Bienvenido al gremio de artesanía unificado de la ciudad. Bajo el sistema de **Omni-Oficios**, puedes acceder a cualquiera de los 10 talleres y fabricar equipo 100% libre de ataduras (*0% Soul-Bound*) utilizando los materiales obtenidos en el bestiario.")
    
    taller_sel = st.selectbox("Selecciona el Taller / Profesión", list(TALLERES_OFICIOS.keys()))
    info_taller = TALLERES_OFICIOS[taller_sel]
    st.info(info_taller["descripcion"])

    st.markdown("### 📋 Recetas Disponibles")
    for receta in info_taller["recetas"]:
        with st.expander(f"✨ {receta['nombre']} — Tier: {receta['tier']} ({receta['tipo']})"):
            st.write(f"**Materiales requeridos:**")
            for mat, cant in receta["materiales"].items():
                en_inventario = st.session_state.inventario.count(mat)
                color_mat = "green" if en_inventario >= cant else "red"
                st.markdown(f"- :{color_mat}[{cant}x {mat}] (Tienes en mochila: {en_inventario})")
            
            st.write(f"**Bonificación de Stats:** {receta['stats_bonus']}")
            
            if st.button(f"🔨 Fabricar {receta['nombre']}", key=f"craft_{receta['id']}"):
                exito, msg = simular_crafteo(taller_sel, receta["id"], st.session_state.inventario)
                if exito:
                    # Consumir materiales
                    for mat, cant in receta["materiales"].items():
                        for _ in range(cant):
                            st.session_state.inventario.remove(mat)
                    # Añadir resultado
                    st.session_state.inventario.append(receta['nombre'])
                    save_user_data()
                    st.success(f"¡Has fabricado con éxito **{receta['nombre']}**! Se ha guardado en tu mochila.")
                    st.rerun()
                else:
                    st.error(f"No se pudo fabricar: {msg}")

# ================= PESTAÑA 3: ATRIBUTOS, PUNTOS LIBRES Y NIVELES =================
with tab_stats:
    st.subheader("📊 Panel de Atributos y Progresión de Nivel")
    st.write(f"⭐ **Nivel Actual:** `{st.session_state.hero_level}` | 🎁 **Puntos Libres Disponibles:** `{st.session_state.puntos_libres}`")
    st.info("Cada subida de nivel otorga **+5 puntos libres** para distribuir en tus atributos y **+10 HP máximo**.")

    col_st1, col_st2 = st.columns(2)
    with col_st1:
        st.markdown("### 🧬 Atributos Principales")
        st.write(f"💪 **Fuerza (STR):** {st.session_state.str}")
        st.write(f"🔮 **Inteligencia (INT):** {st.session_state.int}")
        st.write(f"⚡ **Agilidad (AGI):** {st.session_state.agi}")
        st.write(f"❤️ **Vitalidad (VIT):** {st.session_state.vit}")
        st.write(f"🍀 **Suerte (LUK):** {st.session_state.luk}")

        if st.session_state.puntos_libres > 0:
            st.markdown("---")
            st.markdown("#### ➕ Distribuir Puntos Libres")
            attr_elegido = st.selectbox("Selecciona Atributo", ["Fuerza (STR)", "Inteligencia (INT)", "Agilidad (AGI)", "Vitalidad (VIT)", "Suerte (LUK)"])
            cant_a_subir = st.number_input("Cantidad", min_value=1, max_value=st.session_state.puntos_libres, value=1)
            
            if st.button("Confirmar Asignación"):
                st.session_state.puntos_libres -= cant_a_subir
                if "Fuerza" in attr_elegido: st.session_state.str += cant_a_subir
                elif "Inteligencia" in attr_elegido: st.session_state.int += cant_a_subir
                elif "Agilidad" in attr_elegido: st.session_state.agi += cant_a_subir
                elif "Vitalidad" in attr_elegido: 
                    st.session_state.vit += cant_a_subir
                    st.session_state.max_hp += (cant_a_subir * 5)
                    st.session_state.hero_hp += (cant_a_subir * 5)
                elif "Suerte" in attr_elegido: st.session_state.luk += cant_a_subir
                save_user_data()
                st.success("¡Atributos mejorados con éxito!")
                st.rerun()

    with col_st2:
        st.markdown("### 🧪 Simulador de Experiencia y Niveles")
        if st.button("✨ Simular Subida de Nivel (+1 Nivel)", use_container_width=True):
            st.session_state.hero_level += 1
            st.session_state.puntos_libres += 5
            st.session_state.max_hp += 10
            st.session_state.hero_hp = st.session_state.max_hp
            save_user_data()
            st.success(f"¡Has subido al **Nivel {st.session_state.hero_level}**! Has ganado 5 puntos libres y +10 HP.")
            st.rerun()

# ================= PESTAÑA 4: GRIMORIO Y FUSIÓN (NIVEL 40+) =================
with tab_skills:
    st.subheader("✨ Sistema de Habilidades (1,870 Skills) y Fusión Nivel 40+")
    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("### 📋 Tus 5 Ranuras Activas")
        for idx in range(5):
            actual = st.session_state.habilidades_equipadas[idx]
            nueva_sel = st.selectbox(f"Ranura Activa #{idx+1}", ["(Vacío)"] + st.session_state.grimorio_inventario, index=(st.session_state.grimorio_inventario.index(actual) + 1) if actual in st.session_state.grimorio_inventario else 0, key=f"slot_eq_{idx}")
            val_asignar = "" if nueva_sel == "(Vacío)" else nueva_sel
            if st.session_state.habilidades_equipadas[idx] != val_asignar:
                st.session_state.habilidades_equipadas[idx] = val_asignar
                save_user_data()

        st.markdown("### 🧬 Habilidades Fusionadas")
        if st.session_state.habilidades_fusionadas:
            for fus in st.session_state.habilidades_fusionadas:
                st.success(f"🌟 **{fus['nombre']}** (*{fus['padre1']}* + *{fus['padre2']}*)")
        else:
            st.write("Ninguna fusión realizada aún.")

    with col_s2:
        st.markdown("### ⚗️ Laboratorio de Fusión (Nivel 40+)")
        if st.session_state.hero_level >= 40:
            f_p1 = st.selectbox("Primera Habilidad", st.session_state.grimorio_inventario, key="fp1")
            f_p2 = st.selectbox("Segunda Habilidad", st.session_state.grimorio_inventario, key="fp2")
            nombre_custom = st.text_input("Nombre del Super-Poder Híbrido (Ej: Torreta de Fuego)")
            
            if st.button("✨ Fusionar Habilidades") and nombre_custom and f_p1 != f_p2:
                nueva_fusion = {"nombre": nombre_custom, "padre1": f_p1, "padre2": f_p2}
                st.session_state.habilidades_fusionadas.append(nueva_fusion)
                st.session_state.grimorio_inventario.append(nombre_custom)
                save_user_data()
                st.success(f"¡Has creado la habilidad **{nombre_custom}**!")
                st.rerun()
        else:
            st.warning(f"🔒 Se desbloquea al **Nivel 40**. (Tu nivel: {st.session_state.hero_level})")

# ================= PESTAÑA 5: TIENDA =================
with tab_edificio:
    st.subheader("🏪 Gremio de Aventureros — Grimorios")
    for item in CATALOGO_EDIFICIOS["Gremio de Aventureros"]["items"]:
        col_i1, col_i3 = st.columns([3, 1])
        with col_i1:
            st.markdown(f"**{item['nombre']}** — *{item['tipo']}* (Coste: {item['precio']} {item['metal']})")
        with col_i3:
            if st.button("Comprar", key=f"buy_{item['id']}"):
                sk_limpia = item['nombre'].split(": ")[-1]
                if sk_limpia not in st.session_state.grimorio_inventario:
                    st.session_state.grimorio_inventario.append(sk_limpia)
                    save_user_data()
                    st.success(f"¡Aprendido **{sk_limpia}**!")
                    st.rerun()

# ================= PESTAÑA 6: BESTIARIO 1-60 =================
with tab_viaje_local:
    st.subheader("🗺️ Bestiario Masivo y Jefes de Zona (Niveles 1 a 60)")
    reino_sel = st.selectbox("Selecciona Reino / Región", list(BESTIARIO_ZONAS.keys()))
    datos_r = BESTIARIO_ZONAS[reino_sel]

    st.markdown(f"### 🐺 Monstruos Comunes: `{reino_sel}`")
    for mob in datos_r["mobs"]:
        st.markdown(f"- **{mob['nombre']}** (Nivel `{mob['nivel']}`) — Grupo: `{mob['grupo']}` | HP: `{mob['hp']}` | Loot: *{mob['drop']}*")

    st.markdown(f"### 👑 Jefes de Zona (World Bosses)")
    for jefe in datos_r["jefes"]:
        st.markdown(f"- 🔴 **{jefe['nombre']}** (Nivel `{jefe['nivel']}`) — HP: `{jefe['hp']}` | Botín: *{jefe['drop']}*")

    if st.button("🚀 Desplazarse a Cazar en este Reino", use_container_width=True):
        st.session_state.reino_actual = reino_sel
        st.session_state.asentamiento_actual = f"Caza en {reino_sel}"
        save_user_data()
        st.success(f"Te has desplazado a **{reino_sel}**.")
        st.rerun()

# ================= PESTAÑA 7: MOCHILA Y MONTURAS =================
with tab_bag:
    st.subheader("🎒 Mochila, Inventario y Sistema de Monturas")
    col_m1, col_m2 = st.columns(2)
    
    with col_m1:
        st.markdown("### 🐎 Tus Monturas Nativas")
        monturas_raza = RAZAS_Y_CLASSES[st.session_state.raza]["monturas"]
        for mon in monturas_raza:
            es_activa = " ⭐ (Activa)" if st.session_state.montura_activa == mon else ""
            st.markdown(f"- 🐎 **{mon}**{es_activa}")
            if st.button(f"Montar {mon}", key=f"montar_{mon}"):
                st.session_state.montura_activa = mon
                save_user_data()
                st.success(f"¡Has montado a **{mon}**! Velocidad de desplazamiento aumentada.")
                st.rerun()

    with col_m2:
        st.markdown("### 📦 Objetos y Materiales en Mochila")
        st.write(st.session_state.inventario)

# ================= PESTAÑA 8: CONTINENTES Y LÍMITES DE NIVEL =================
with tab_world:
    st.subheader("🌍 Los Continentes y Escalado (+50 Niveles por Continente)")
    for cont, info in CONTINENTES_OFICIALES.items():
        st.markdown(f"- **{cont}** — *{info['tipo']}*")

# ================= PESTAÑA 9: MISIONES SECRETAS =================
with tab_quests:
    st.subheader("📜 Misiones Secretas")
    for oculta in CATALOGO_OCULTAS:
        st.markdown(f"**{oculta['nombre']}** ➔ Abre: `{oculta['continente_premio']}` (*{oculta['pista']}*)")

# ================= PESTAÑA 10: ENCARGOS P2P =================
with tab_p2p:
    st.subheader("🤝 Tablón P2P entre Jugadores")
    docs = db.collection("p2p_quests").stream()
    for doc in docs:
        data = doc.to_dict()
        st.markdown(f"**Autor:** `{data.get('autor')}` — **{data.get('titulo')}** (Premio: `{data.get('recompensa_cant')} {data.get('recompensa_tipo')}`)")

st.markdown("---")
st.caption("Snd-Worlds MMORPG Sandbox - Arquitectura Modular Definitiva")