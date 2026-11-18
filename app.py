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
                        for _ in range(cant): st.session_state.inventario.remove(mat)
                    st.session_state.inventario.append(receta['nombre'])
                    save_user_data()
                    st.success(f"¡Fabricado con éxito **{receta['nombre']}**!")
                    st.rerun()
                else:
                    st.error(f"Error: {msg}")

# ================= TAB 3: ATRIBUTOS Y NIVEL =================
with tab_stats:
    st.subheader("📊 Panel de Atributos y Escalado de Nivel")
    st.write(f"⭐ **Nivel Actual:** `{st.session_state.hero_level}` | 🎁 **Puntos Libres:** `{st.session_state.puntos_libres}`")
    
    col_st1, col_st2 = st.columns(2)
    with col_st1:
        st.write(f"💪 **STR:** {st.session_state.str} | 🔮 **INT:** {st.session_state.int} | ⚡ **AGI:** {st.session_state.agi} | ❤️ **VIT:** {st.session_state.vit} | 🍀 **LUK:** {st.session_state.luk}")
        if st.session_state.puntos_libres > 0:
            attr = st.selectbox("Atributo a subir", ["Fuerza", "Inteligencia", "Agilidad", "Vitalidad", "Suerte"])
            if st.button("Asignar Punto"):
                st.session_state.puntos_libres -= 1
                if attr == "Fuerza": st.session_state.str += 1
                elif attr == "Inteligencia": st.session_state.int += 1
                elif attr == "Agilidad": st.session_state.agi += 1
                elif attr == "Vitalidad": 
                    st.session_state.vit += 1
                    st.session_state.max_hp += 5
                    st.session_state.hero_hp += 5
                elif attr == "Suerte": st.session_state.luk += 1
                save_user_data()
                st.success("¡Atributo mejorado!")
                st.rerun()
    with col_st2:
        if st.button("✨ Simular Subida de Nivel (+1 Nivel)", use_container_width=True):
            st.session_state.hero_level += 1
            st.session_state.puntos_libres += 5
            st.session_state.max_hp += 10
            st.session_state.hero_hp = st.session_state.max_hp
            save_user_data()
            st.success(f"¡Subiste a Nivel {st.session_state.hero_level}!")
            st.rerun()

# ================= TAB 4: GRIMORIO Y FUSIÓN =================
with tab_skills:
    st.subheader("✨ Grimorio, Habilidades y Laboratorio de Fusión")
    st.write("Cada habilidad cuenta con **3 poderes únicos**. Domina hasta 15 habilidades y fusiona pares para crear super-poderes.")
    
    col_sk1, col_sk2 = st.columns(2)
    with col_sk1:
        st.markdown("### 📋 Tus 5 Ranuras Activas de Combate")
        for idx in range(5):
            actual = st.session_state.habilidades_equipadas[idx]
            nueva = st.selectbox(f"Ranura #{idx+1}", ["(Vacío)"] + st.session_state.grimorio_inventario, index=(st.session_state.grimorio_inventario.index(actual)+1) if actual in st.session_state.grimorio_inventario else 0, key=f"slot_{idx}")
            val = "" if nueva == "(Vacío)" else nueva
            if st.session_state.habilidades_equipadas[idx] != val:
                st.session_state.habilidades_equipadas[idx] = val
                save_user_data()

    with col_sk2:
        st.markdown("### ⚗️ Laboratorio de Fusión de Habilidades")
        if st.session_state.hero_level >= 30:
            fp1 = st.selectbox("Habilidad 1", st.session_state.grimorio_inventario, key="f1")
            fp2 = st.selectbox("Habilidad 2", st.session_state.grimorio_inventario, key="f2")
            nombre_fus = st.text_input("Nombre del Poder Híbrido")
            if st.button("✨ Fusionar Poderes") and nombre_fus and fp1 != fp2:
                st.session_state.habilidades_fusionadas.append({"nombre": nombre_fus, "p1": fp1, "p2": fp2})
                st.session_state.grimorio_inventario.append(nombre_fus)
                save_user_data()
                st.success(f"¡Habilidad fusionada **{nombre_fus}** creada con éxito!")
                st.rerun()
        else:
            st.warning("🔒 Se desbloquea al Nivel 30.")

# ================= TAB 5: MAZMORRAS Y JEFES =================
with tab_dungeon:
    st.subheader("🏰 Mazmorras del Reino y Jefes de Instancia")
    reino_d = BESTIARIO_ZONAS.get(st.session_state.reino_actual, {})
    mazmorras = reino_d.get("mazmorras", [])
    if mazmorras:
        for maz in mazmorras:
            st.markdown(f"**{maz['nombre']}** (Nivel mínimo: `{maz['nivel_min']}`)")
            st.write(f"Boss: **{maz['jefe']}** (HP: {maz['hp_jefe']}) | Drop: *{maz['drop_jefe']}*")
            if st.button(f"⚔️ Entrar a {maz['nombre']}", key=f"entrar_{maz['nombre']}"):
                if st.session_state.hero_level >= maz['nivel_min']:
                    st.success(f"¡Has derrotado a **{maz['jefe']}** en la mazmorra y obtenido {maz['drop_jefe']}!")
                    st.session_state.inventario.append(maz['drop_jefe'])
                    save_user_data()
                    st.rerun()
                else:
                    st.error(f"Nivel insuficiente. Requieres nivel {maz['nivel_min']}.")
    else:
        st.info("No hay mazmorras registradas en esta zona exacta. Explora otro reino.")

# ================= TAB 6: MISIONES =================
with tab_quests:
    st.subheader("📜 Tablón de Misiones del Asentamiento")
    for m in st.session_state.misiones_activas:
        estado = "✅ Completada" if m['completada'] else f"Progreso: {m['progreso']}/{m['meta']}"
        st.markdown(f"**{m['titulo']}** — *{m['objetivo']}* [{estado}]")
        if not m['completada'] and st.button(f"Completar Misión", key=f"m_comp_{m['id']}"):
            m['completada'] = True
            m['progreso'] = m['meta']
            st.session_state.puntos_libres += 2
            st.session_state.plata += 100
            save_user_data()
            st.success("¡Misión completada! +2 Puntos libres y +100 plata.")
            st.rerun()

# ================= TAB 7: TIENDA GREMIO =================
with tab_edificio:
    st.subheader("🏪 Tienda del Gremio de Aventureros")
    for item in CATALOGO_EDIFICIOS["Gremio de Aventureros"]["items"]:
        col_t1, col_t2 = st.columns([3, 1])
        with col_t1:
            st.markdown(f"**{item['nombre']}** — Coste: {item['precio']} {item['metal']}")
        with col_t2:
            if st.button("Comprar", key=f"comprar_{item['id']}"):
                sk_limpia = item['nombre'].split(": ")[-1]
                if sk_limpia not in st.session_state.grimorio_inventario:
                    st.session_state.grimorio_inventario.append(sk_limpia)
                    save_user_data()
                    st.success(f"¡Aprendiste **{sk_limpia}**!")
                    st.rerun()

# ================= TAB 8: BESTIARIO Y ZONAS =================
with tab_viaje_local:
    st.subheader("🗺️ Bestiario y Viaje entre Reinos (Continente I: Niveles 1-100)")
    reino_sel = st.selectbox("Selecciona Reino o Zona Común", list(BESTIARIO_ZONAS.keys()))
    info_r = BESTIARIO_ZONAS[reino_sel]
    st.write(f"**Rango de Nivel:** `{info_r['rango']}`")

    st.markdown("### 🐺 Enemigos Comunes")
    for mob in info_r["mobs"]:
        st.markdown(f"- **{mob['nombre']}** (Nivel {mob['nivel']}) | Tipo: `{mob['tipo']}` | HP: {mob['hp']} | Ataque: `{mob['ataque']}` | Loot: *{mob['drop']}*")

    st.markdown("### 👑 Jefes de Zona")
    for j in info_r.get("jefes_zona", []):
        st.markdown(f"- 🔴 **{j['nombre']}** (Nivel {j['nivel']}) | HP: {j['hp']} | Loot: *{j['drop']}*")

    if st.button("🚀 Viajar a este Reino o Zona", use_container_width=True):
        st.session_state.reino_actual = reino_sel
        st.session_state.asentamiento_actual = f"Asentamiento en {reino_sel}"
        save_user_data()
        st.success(f"Te has desplazado a **{reino_sel}**.")
        st.rerun()

# ================= TAB 9: MOCHILA =================
with tab_bag:
    st.subheader("🎒 Inventario y Objetos en Mochila")
    st.write(st.session_state.inventario)

# ================= TAB 10: CONTINENTES =================
with tab_world:
    st.subheader("🌍 Mapa de Continentes y Escalado de Niveles")
    for cont, info in CONTINENTES_OFICIALES.items():
        st.markdown(f"**{cont}**")
        st.write(f"- {info['tipo']}")

st.markdown("---")
st.caption("Snd-Worlds MMORPG Sandbox - Arquitectura Modular Definitiva con Canvas Real-Time")