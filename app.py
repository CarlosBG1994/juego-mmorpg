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

# --- ESTADO DE SESIÓN Y DATOS DE JUEGO ---
for key, default in [
    ("logged_in", False), ("user_email", ""), ("hero_name", ""),
    ("raza", "Humano"), ("subforma", "Hombre Lobo"), ("genero", "Hombre"),
    ("clase", "Invocador"), ("continente", CONTINENTE_INICIAL),
    ("reino_actual", "Reino Humano de Valoria"), ("asentamiento_actual", "Aurelia Capital"),
    ("hero_level", 1), ("hero_hp", 100), ("max_hp", 100), ("hero_xp", 0),
    ("puntos_libres", 0),
    ("str", 5), ("int", 16), ("agi", 6), ("vit", 10), ("luk", 10),
    ("plata", 350), ("oro", 25), ("diamante", 5), ("peso_maximo", 100),
    # Habilidades: Empieza estrictamente con 1 habilidad inicial
    ("habilidades_equipadas", ["Invocación de Golem de Roca"]),
    ("grimorio_inventario", ["Invocación de Golem de Roca"]),
    ("habilidades_fusionadas", []),
    ("inventario", ["Ropa de Viajero", "Raciones de Pan (x3)", "Mineral de Hierro Bruto (x2)"]),
    # Equipamiento con durabilidad
    ("equipamiento", {
        "Cabeza": {"nombre": "Capucha de Tela", "defensa": 5, "durabilidad": 100},
        "Pecho": {"nombre": "Túnica de Iniciado", "defensa": 12, "durabilidad": 90},
        "Arma": {"nombre": "Bastón de Madera", "ataque": 10, "durabilidad": 85},
        "Pies": {"nombre": "Zapatos de Cuero", "defensa": 4, "durabilidad": 95}
    }),
    ("montura_activa", "Ninguna"),
    ("misiones_activas", [
        {"id": "m1", "titulo": "Caza de Goblins en Valoria", "objetivo": "Derrota 5 Goblins", "progreso": 2, "meta": 5, "completada": False}
    ]),
    ("misiones_realizadas", [
        {"id": "m0", "titulo": "El Despertar del Héroe", "recompensa": "+1 Habilidad Inicial"}
    ]),
    # Tratados y Reputación con Reinos
    ("tratados_reinos", {
        "Reino Humano de Valoria": {"confianza": 60, "estado": "Neutral / Respetado", "crimenes": 0},
        "Bosque Ancestral de Eldoria": {"confianza": 50, "estado": "Neutral", "crimenes": 0},
        "Fortaleza de Hierro de Pyoria": {"confianza": 40, "estado": "Neutral", "crimenes": 1},
        "Estepas Salvajes de Noxoria": {"confianza": 20, "estado": "Criminal / Hostil", "crimenes": 3}
    }),
    # Profesiones (Niveles del 1 al 100)
    ("profesiones", {
        "Herrería": 1, "Minería": 1, "Peletería": 1, "Sastrería": 1,
        "Herboristería": 1, "Alquimia": 1, "Cocina": 1, "Pesca": 1,
        "Joyería": 1, "Criadero de Monturas": 1
    }),
    ("gremio", "Sin Gremio asignado"),
    ("amigos", ["Valeria_99", "Thorin_Ironfist"]),
    ("config_volumen", 80),
    ("config_visibilidad", "Alta"),
    ("menu_activo", False), # Toggle del menú flotante
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
            "hero_level": st.session_state.hero_level,
            "hero_hp": st.session_state.hero_hp,
            "habilidades_equipadas": st.session_state.habilidades_equipadas,
            "grimorio_inventario": st.session_state.grimorio_inventario,
            "inventario": st.session_state.inventario,
            "equipamiento": st.session_state.equipamiento,
            "tratados_reinos": st.session_state.tratados_reinos,
            "profesiones": st.session_state.profesiones,
            "has_character": st.session_state.has_character
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Mundo Abierto Masivo | Menú Toggle | Sistema de Profesiones y Tratados</p>", unsafe_allow_html=True)
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
                    st.session_state.habilidades_equipadas = data.get("habilidades_equipadas", ["Invocación de Golem de Roca"])
                    st.session_state.grimorio_inventario = data.get("grimorio_inventario", ["Invocación de Golem de Roca"])
                    st.session_state.inventario = data.get("inventario", ["Ropa de Viajero"])
                    st.session_state.equipamiento = data.get("equipamiento", st.session_state.equipamiento)
                    st.session_state.tratados_reinos = data.get("tratados_reinos", st.session_state.tratados_reinos)
                    st.session_state.profesiones = data.get("profesiones", st.session_state.profesiones)
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
    with col_c2:
        info_raza = RAZAS_Y_CLASSES[st.session_state.raza]
        st.session_state.clase = st.selectbox("Clase Oficial", info_raza["clases"])
        base_stats = ESTADISTICAS_BASE_CLASES.get(st.session_state.clase, {"str": 10, "int": 10, "agi": 10, "vit": 10, "luk": 10, "hp": 100})
        st.session_state.str = base_stats["str"]
        st.session_state.int = base_stats["int"]
        st.session_state.max_hp = base_stats["hp"]
        st.session_state.hero_hp = base_stats["hp"]

    if st.button("🚀 ¡Entrar al Mundo Masivo!", use_container_width=True):
        if st.session_state.hero_name:
            st.session_state.has_character = True
            save_user_data()
            st.rerun()
    st.stop()

# ================= BARRA SUPERIOR CON BOTÓN TOGGLE DE MENÚ =================
col_m1, col_m2, col_m3 = st.columns([3, 1, 1])
with col_m1:
    st.markdown(f"### 🛡️ **{st.session_state.hero_name}** | Nivel: {st.session_state.hero_level} | Raza: {st.session_state.raza} ({st.session_state.clase})")
with col_m2:
    texto_btn_menu = "📂 Ocultar Menú" if st.session_state.menu_activo else "📁 Abrir Menú de Gestión"
    if st.button(texto_btn_menu, use_container_width=True, type="primary"):
        st.session_state.menu_activo = not st.session_state.menu_activo
        st.rerun()
with col_m3:
    if st.button("🚪 Cerrar Sesión", use_container_width=True):
        save_user_data()
        st.session_state.logged_in = False
        st.session_state.has_character = False
        st.rerun()

# ================= SI EL MENÚ ESTÁ ACTIVO: MOSTRAR GESTIÓN COMPLETA =================
if st.session_state.menu_activo:
    st.markdown("---")
    st.markdown("## ⚙️ Panel de Gestión y Menús del Héroe")
    
    menu_tab1, menu_tab2, menu_tab3, menu_tab4, menu_tab5, menu_tab6, menu_tab7, menu_tab8 = st.tabs([
        "⚔️ Habilidades y Equipamiento",
        "🎒 Inventario y Espacio",
        "📜 Misiones",
        "👑 Tratados y Reputación",
        "🛠️ Profesiones (1-100)",
        "🏰 Gremio y Amigos",
        "📊 Atributos y Estado",
        "⚙️ Configuración"
    ])

    # 1. HABILIDADES Y EQUIPAMIENTO
    with menu_tab1:
        st.subheader("⚔️ Gestión de Habilidades Activas")
        st.write("Equipación de habilidades adquiridas (puedes equipar hasta 5 activas en tu barra de combate):")
        
        cols_eq = st.columns(5)
        for i in range(5):
            with cols_eq[i]:
                actual = st.session_state.habilidades_equipadas[i] if i < len(st.session_state.habilidades_equipadas) else "(Vacío)"
                nueva_hab = st.selectbox(f"Ranura {i+1}", ["(Vacío)"] + st.session_state.grimorio_inventario, index=0 if actual=="(Vacío)" else 1, key=f"menu_sk_{i}")
                if nueva_hab != "(Vacío)":
                    if i < len(st.session_state.habilidades_equipadas):
                        st.session_state.habilidades_equipadas[i] = nueva_hab
                    else:
                        st.session_state.habilidades_equipadas.append(nueva_hab)
        
        st.markdown("---")
        st.subheader("🛡️ Equipamiento Actual y Reparación")
        for pieza, datos in st.session_state.equipamiento.items():
            col_eq1, col_eq2, col_eq3 = st.columns([2, 1, 1])
            with col_eq1:
                st.markdown(f"**{pieza}**: {datos['nombre']} (Durabilidad: {datos['durabilidad']}%)")
            with col_eq2:
                if st.button(f"Reparar {pieza}", key=f"rep_{pieza}"):
                    datos['durabilidad'] = 100
                    st.success(f"¡{pieza} reparada al 100%!")
                    st.rerun()
            with col_eq3:
                if st.button(f"Cambiar {pieza}", key=f"camb_{pieza}"):
                    st.info("Pieza cambiada con éxito desde el inventario.")

    # 2. INVENTARIO Y ESPACIO
    with menu_tab2:
        st.subheader("🎒 Inventario y Carga")
        peso_actual = len(st.session_state.inventario) * 5
        st.progress(peso_actual / st.session_state.peso_maximo, text=f"Espacio / Peso Ocupado: {peso_actual} / {st.session_state.peso_maximo} kg")
        st.markdown(f"💰 **Monedas:** Plata: `{st.session_state.plata}` | Oro: `{st.session_state.oro}` | Diamantes: `{st.session_state.diamante}`")
        st.markdown("### Objetos en Mochila:")
        for idx, item in enumerate(st.session_state.inventario):
            col_inv1, col_inv2 = st.columns([3, 1])
            with col_inv1:
                st.markdown(f"- {item}")
            with col_inv2:
                if st.button("Usar / Vender", key=f"inv_usar_{idx}"):
                    st.success(f"Has usado o interactuado con {item}.")

    # 3. MISIONES
    with menu_tab3:
        st.subheader("📜 Registro de Misiones")
        st.markdown("### En Curso:")
        for m in st.session_state.misiones_activas:
            st.markdown(f"- **{m['titulo']}**: {m['objetivo']} (Progreso: {m['progreso']}/{m['meta']})")
        st.markdown("### Realizadas:")
        for mr in st.session_state.misiones_realizadas:
            st.markdown(f"- ✅ **{mr['titulo']}** (Recompensa obtenida: {mr['recompensa']})")

    # 4. TRATADOS Y REPUTACIÓN
    with menu_tab4:
        st.subheader("👑 Tratados y Reputación con los Reinos")
        st.write("Consulta el nivel de confianza diplomática y si has cometido delitos (lo que te convierte en criminal en los reinos):")
        for reino, info in st.session_state.tratados_reinos.items():
            st.markdown(f"**🏰 {reino}**")
            st.markdown(f"- Confianza: `{info['confianza']}/100` | Estado: `{info['estado']}` | Delitos cometidos: `{info['crimenes']}`")
            st.markdown("---")

    # 5. PROFESIONES (1-100)
    with menu_tab5:
        st.subheader("🛠️ Panel de Profesiones (Niveles 1 al 100)")
        st.write("Tus oficios y especialidades en el mundo abierto:")
        cols_prof = st.columns(2)
        idx_p = 0
        for prof, nivel in st.session_state.profesiones.items():
            with cols_prof[idx_p % 2]:
                st.markdown(f"**{prof}**: Nivel `{nivel}/100`")
                st.progress(nivel / 100)
            idx_p += 1

    # 6. GREMIO Y AMIGOS
    with menu_tab6:
        st.subheader("🏰 Gremio y Lista de Amigos")
        st.markdown(f"**Tu Gremio actual:** `{st.session_state.gremio}`")
        st.markdown("### Amigos conectados:")
        for amigo in st.session_state.amigos:
            st.markdown(f"- 🟢 {amigo} (En línea)")

    # 7. ATRIBUTOS
    with menu_tab7:
        st.subheader("📊 Atributos del Héroe")
        st.markdown(f"- **Fuerza (STR):** {st.session_state.str}")
        st.markdown(f"- **Inteligencia (INT):** {st.session_state.int}")
        st.markdown(f"- **HP Máximo:** {st.session_state.max_hp}")

    # 8. CONFIGURACIÓN
    with menu_tab8:
        st.subheader("⚙️ Configuración del Juego")
        st.session_state.config_volumen = st.slider("Volumen General", 0, 100, st.session_state.config_volumen)
        st.session_state.config_visibilidad = st.selectbox("Visibilidad Gráfica", ["Baja", "Media", "Alta", "Ultra"], index=2)

    st.markdown("---")

# ================= MAPA EN PANTALLA COMPLETA (SIEMPRE VISIBLE DE FONDO O PRINCIPAL) =================
st.markdown("### 🌍 Mundo Abierto Masivo — Snd-Worlds (Pantalla Completa)")

# Renderizar el motor canvas a gran escala ocupando toda la vista principal
zona_actual_str = st.session_state.reino_actual
datos_reino = BESTIARIO_ZONAS.get(zona_actual_str, BESTIARIO_ZONAS["Reino Humano de Valoria"])
html_mapa = generar_canvas_html(True, zona_actual_str, datos_reino["mobs"], datos_reino.get("jefes_zona", []))
st.components.v1.html(html_mapa, height=650)