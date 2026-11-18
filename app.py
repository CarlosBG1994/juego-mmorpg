import streamlit as st
from canvas_engine import generar_canvas_html
from misiones_reino import SISTEMA_MISIONES

# Configuración inicial de la página en ancho completo
st.set_page_config(
    page_title="Snd-Worlds MMORPG",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado de sesión si no existe
if "reino_actual" not in st.session_state:
    st.session_state.reino_actual = "Reino Humano de Valoria"
if "nivel_pj" not in st.session_state:
    st.session_state.nivel_pj = 1
if "clase_pj" not in st.session_state:
    st.session_state.clase_pj = "Púgil"

# ================= TÍTULO Y CABECERA DEL JUEGO =================
st.title("⚔️ Snd-Worlds — Open-World MMORPG Sandbox")
st.markdown(f"**Clase:** {st.session_state.clase_pj} | **Nivel:** {st.session_state.nivel_pj} | **Zona Actual:** {st.session_state.reino_actual}")

# ================= BARRA LATERAL DE GESTIÓN Y MENÚS =================
with st.sidebar:
    st.header("⚙️ Panel de Control y Módulos")
    
    st.session_state.reino_actual = st.selectbox(
        "Seleccionar Zona / Continente:",
        [
            "Reino Humano de Valoria", 
            "Bosque Ancestral (Niveles 30-60)", 
            "Zona Neutra - Puertas del Eón", 
            "Archipiélago y Mazmorras del Mar Abierto"
        ]
    )
    
    st.markdown("---")
    st.subheader("📜 Estado de Misiones")
    for m in SISTEMA_MISIONES["principales"]:
        st.markdown(f"- **{m['titulo']}** (Nv.{m['nivel_requerido']})")
        st.caption(m["objetivo"])
        
    st.markdown("---")
    st.subheader("⭐ Misiones Míticas / Ocultas")
    for mo in SISTEMA_MISIONES["ocultas_miticas"]:
        st.markdown(f"- 🌟 *{mo['titulo']}*")
        st.caption(mo["pista_inicial"])

# ================= PESTAÑAS DE GESTIÓN DEL HÉROE =================
tab_juego, tab_habilidades, tab_inventario, tab_misiones, tab_artesania = st.tabs([
    "🎮 Motor de Juego (Canvas)", 
    "⚡ Habilidades y Equipamiento", 
    "🎒 Inventario y Espacio", 
    "📜 Misiones y Lore", 
    "⚒️ Talleres y Oficios"
])

with tab_juego:
    st.subheader("🌍 Vista de Mundo Abierto (1.500.000 km² + Mar y Archipiélagos)")
    st.markdown("Usa las teclas **W, A, S, D** o las flechas para moverte, y presiona **ESPACIO** o **Q** para atacar a los monstruos en tiempo real.")
    
    # Definición de mobs según la zona actual seleccionada
    mobs_activos = [
        {"nombre": "Goblin", "nivel": 2, "hp": 70, "ataque": "Físico", "velocidad": 1.8},
        {"nombre": "Lobo de Pradera", "nivel": 5, "hp": 85, "ataque": "Físico", "velocidad": 2.2},
        {"nombre": "Slime Ácido", "nivel": 8, "hp": 60, "ataque": "Mágico", "velocidad": 1.4},
        {"nombre": "Oso Pardo Enorme", "nivel": 15, "hp": 180, "ataque": "Físico", "velocidad": 1.5}
    ]
    
    # Renderizar el motor HTML5 / JS en pantalla completa dentro de Streamlit
    html_mapa = generar_canvas_html(True, st.session_state.reino_actual, mobs_activos, [])
    st.components.v1.html(html_mapa, height=750, scrolling=False)

with tab_habilidades:
    st.subheader("⚔️ Gestión de Habilidades Activas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Ranura 1 (Principal)", ["Golpe de Púgil", "Invocación de Golem de Roca", "Puño de Fuego"])
    with col2:
        st.selectbox("Ranura 2", ["Escudo Rúnico", "(Vacío)", "Ondas de Choque"])
    with col3:
        st.selectbox("Ranura 3", ["(Vacío)", "Poción de Vida Rápida"])

with tab_inventario:
    st.subheader("🎒 Inventario del Héroe")
    st.info("Espacio de almacenamiento: 24 / 50 ítems usados.")
    st.markdown("""
    - 🗡️ **Espada de Bronce Reforzada** (Equipada - Tier I)
    - 🛡️ **Armadura de Viajero** (Equipada)
    - 🧪 **Pociones de Vida x5**
    - 🪙 **Oro:** 1,450 monedas
    - ⭐ **Fragmentos Míticos:** 0 / 3
    """)

with tab_misiones:
    st.subheader("📜 Registro Completo de Misiones")
    for m in SISTEMA_MISIONES["principales"]:
        with st.expander(f"Principal: {m['titulo']} (Nivel Requerido: {m['nivel_requerido']})"):
            st.write(f"**Descripción:** {m['descripcion']}")
            st.write(f"**Objetivo:** {m['objetivo']}")
            st.success(f"**Recompensa:** {m['recompensa']}")
            st.info(f"**Desbloquea:** {m['desbloquea']}")

with tab_artesania:
    st.subheader("⚒️ Talleres Omni-Oficios (1-100)")
    st.write("Gestiona la fabricación de armas, armaduras pesadas, pociones y encantamientos rúnicos.")
    oficio_sel = st.selectbox("Seleccionar Taller:", ["Herrería", "Alquimia", "Joyería Mítica", "Sastrería"])
    st.progress(45, text=f"Progreso en {oficio_sel}: Nivel 18 (Experiencia: 4,500 / 10,000)")