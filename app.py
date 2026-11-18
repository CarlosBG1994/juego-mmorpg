import streamlit as st
from config import DATOS_MUNDO
from misiones_reino import SISTEMA_MISIONES
from canvas_engine import generar_canvas_html

st.set_page_config(page_title="Snd-Worlds MMORPG", page_icon="⚔️", layout="wide")

# Opciones de personalización integradas directamente aquí para evitar KeyErrors
OPCIONES_PERSONALIZACION = {
    "cabello": ["Rubio Legendario", "Castaño Oscuro", "Pelirrojo Fuego", "Platino Arcano", "Negro Sombra"],
    "armadura_color": ["Azul Real (Valoria)", "Rojo Sangre", "Verde Esmeralda", "Dorado Divino", "Oscuro Abisal"]
}

# Inicialización segura de estados de sesión
if "zona_actual" not in st.session_state:
    st.session_state.zona_actual = "Reino Humano de Valoria"
if "clase_pj" not in st.session_state:
    st.session_state.clase_pj = "Púgil"
if "cabello_pj" not in st.session_state:
    st.session_state.cabello_pj = OPCIONES_PERSONALIZACION["cabello"][0]
if "armadura_pj" not in st.session_state:
    st.session_state.armadura_pj = OPCIONES_PERSONALIZACION["armadura_color"][0]
if "oro_jugador" not in st.session_state:
    st.session_state.oro_jugador = 1450
if "monturas_desbloqueadas" not in st.session_state:
    st.session_state.monturas_desbloqueadas = ["A Pie (Velocidad Base)"]
if "montura_equipada" not in st.session_state:
    st.session_state.montura_equipada = "A Pie (Velocidad Base)"

st.title(f"⚔️ {DATOS_MUNDO['nombre_mundo']}")

# BARRA LATERAL: CREADOR DE PERSONAJE, ESTABLO Y ZONAS
with st.sidebar:
    st.header("🎨 Creador y Moldear Personaje")
    st.session_state.clase_pj = st.selectbox("Clase del Héroe:", [c["nombre"] for c in DATOS_MUNDO["clases_personaje"]])
    st.session_state.cabello_pj = st.selectbox("Estilo de Pelo / Casco:", OPCIONES_PERSONALIZACION["cabello"])
    st.session_state.armadura_pj = st.selectbox("Color de Armadura:", OPCIONES_PERSONALIZACION["armadura_color"])
    
    st.markdown("---")
    st.header("🌍 Zonas y Establo")
    st.session_state.zona_actual = st.selectbox("Zona Activa:", [
        "Reino Humano de Valoria", "Bosque Ancestral de Elfos", "Baluarte Enano de Piedra", "Mazmorra Subterránea"
    ])
    
    montura_elegida = st.selectbox("Montura Equipada:", st.session_state.monturas_desbloqueadas)
    st.session_state.montura_equipada = montura_elegida
    
    velocidad_mapa = 4.0
    for m in DATOS_MUNDO["monturas_disponibles"]:
        if m["nombre"] == montura_elegida:
            velocidad_mapa = 4.0 * m["bonus_velocidad"]

    with st.expander("🛒 Comprar Monturas (Oro)"):
        st.write(f"💰 Oro: {st.session_state.oro_jugador}")
        for m in DATOS_MUNDO["monturas_disponibles"]:
            if m["nombre"] != "A Pie (Velocidad Base)":
                if m["nombre"] in st.session_state.monturas_desbloqueadas:
                    st.success(f"✅ {m['nombre']}")
                else:
                    if st.button(f"Comprar {m['nombre']} ({m['coste']} oro)", key=f"buy_{m['nombre']}"):
                        if st.session_state.oro_jugador >= m["coste"]:
                            st.session_state.oro_jugador -= m["coste"]
                            st.session_state.monturas_desbloqueadas.append(m["nombre"])
                            st.rerun()
                        else:
                            st.error("Oro insuficiente.")

# PESTAÑAS PRINCIPALES
tab_juego, tab_misiones, tab_lore = st.tabs(["🎮 Mundo Abierto y Combate", "📜 Misiones", "👑 Lore"])

with tab_juego:
    mobs_zona = [
        {"nombre": "Goblin Guerrero", "nivel": 3, "hp": 80, "ataque": "Físico", "velocidad": 1.8},
        {"nombre": "Lobo Feroz", "nivel": 6, "hp": 95, "ataque": "Físico", "velocidad": 2.3}
    ]
    html_engine = generar_canvas_html(
        st.session_state.zona_actual, 
        st.session_state.montura_equipada, 
        velocidad_mapa, 
        st.session_state.cabello_pj, 
        st.session_state.armadura_pj, 
        mobs_zona
    )
    st.components.v1.html(html_engine, height=750, scrolling=False)

with tab_misiones:
    st.subheader("📋 Registro de Misiones")
    for m in SISTEMA_MISIONES["principales"]:
        with st.expander(f"{m['titulo']} (Nivel {m['nivel_requerido']})"):
            st.write(m['descripcion'])
            st.info(f"Objetivo: {m['objetivo']}")
            st.success(f"Recompensa: {m['recompensa']}")
            
    st.markdown("### 🌟 Misiones Míticas")
    for mo in SISTEMA_MISIONES["ocultas_miticas"]:
        with st.expander(f"Mítica: {mo['titulo']}"):
            st.write(f"**Pista:** {mo['pista_inicial']}")
            st.warning(f"**Recompensa:** {mo['recompensa_mitica']['nombre_recompensa']} ({mo['recompensa_mitica']['rareza']})")

with tab_lore:
    st.subheader("👑 Lore de Snd-Worlds")
    st.write("Un mundo masivo de 1.500.000 km² con reinos fundacionales, mazmorras y combate activo en tiempo real.")