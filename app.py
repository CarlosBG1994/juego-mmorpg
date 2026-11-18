import streamlit as st
from config import DATOS_MUNDO
from misiones_reino import SISTEMA_MISIONES
from canvas_engine import generar_canvas_html

st.set_page_config(page_title="Snd-Worlds MMORPG", page_icon="⚔️", layout="wide")

# Inicialización de estados del jugador
if "zona_actual" not in st.session_state:
    st.session_state.zona_actual = "Reino Humano de Valoria"
if "clase_pj" not in st.session_state:
    st.session_state.clase_pj = "Púgil"
if "nivel_pj" not in st.session_state:
    st.session_state.nivel_pj = 1
if "oro_jugador" not in st.session_state:
    st.session_state.oro_jugador = 1450
if "monturas_desbloqueadas" not in st.session_state:
    st.session_state.monturas_desbloqueadas = ["A Pie (Velocidad Base)"]
if "montura_equipada" not in st.session_state:
    st.session_state.montura_equipada = "A Pie (Velocidad Base)"

st.title(f"⚔️ {DATOS_MUNDO['nombre_mundo']}")
st.markdown(f"**Clase:** {st.session_state.clase_pj} | **Nivel:** {st.session_state.nivel_pj} | **Oro:** 💰 {st.session_state.oro_jugador} monedas")

# Barra lateral: Economía de Monturas, Selección de Zona y Misiones Rápidas
with st.sidebar:
    st.header("🌍 Panel de Control y Establo")
    
    st.session_state.clase_pj = st.selectbox("Clase del Héroe:", [c["nombre"] for c in DATOS_MUNDO["clases_personaje"]])
    
    st.session_state.zona_actual = st.selectbox("Zona Activa:", [
        "Reino Humano de Valoria", 
        "Bosque Ancestral de Elfos", 
        "Baluarte Enano de Piedra", 
        "Mazmorra Subterránea [Nivel 50]",
        "Puerto Comercial del Sur"
    ])
    
    st.markdown("---")
    st.subheader("🐎 Establo y Mercado")
    montura_elegida = st.selectbox("Montura Equipada:", st.session_state.monturas_desbloqueadas)
    st.session_state.montura_equipada = montura_elegida
    
    # Velocidad base de movimiento calculada según la montura
    velocidad_mapa = 4.0
    for m in DATOS_MUNDO["monturas_disponibles"]:
        if m["nombre"] == montura_elegida:
            velocidad_mapa = 4.0 * m["bonus_velocidad"]

    with st.expander("🛒 Comprar en el Establo Real"):
        for m in DATOS_MUNDO["monturas_disponibles"]:
            if m["nombre"] != "A Pie (Velocidad Base)":
                adquirida = m["nombre"] in st.session_state.monturas_desbloqueadas
                st.markdown(f"**{m['nombre']}**")
                st.caption(f"Coste: {m['coste']} oro | {m['requisito']}")
                if adquirida:
                    st.success("✅ Adquirida")
                else:
                    if st.button(f"Comprar ({m['coste']} oro)", key=f"buy_{m['nombre']}"):
                        if st.session_state.oro_jugador >= m["coste"]:
                            st.session_state.oro_jugador -= m["coste"]
                            st.session_state.monturas_desbloqueadas.append(m["nombre"])
                            st.success(f"¡Has conseguido {m['nombre']}!")
                            st.rerun()
                        else:
                            st.error("Oro insuficiente. ¡Completa misiones!")

    st.markdown("---")
    st.subheader("📜 Misiones Activas")
    for m in SISTEMA_MISIONES["principales"]:
        st.markdown(f"- **{m['titulo']}**")
        st.caption(m["objetivo"])

# Pestañas principales unificadas
tab_juego, tab_habilidades, tab_inventario, tab_misiones, tab_artesania, tab_lore = st.tabs([
    "🎮 Mundo Abierto y Combate", 
    "⚡ Habilidades", 
    "🎒 Inventario", 
    "📜 Misiones", 
    "⚒️ Talleres y Oficios",
    "👑 Lore y Reinos"
])

with tab_juego:
    st.subheader("🌍 Exploración de 1.500.000 km² (Canvas Engine)")
    mobs_zona = [
        {"nombre": "Goblin Guerrero", "nivel": 3, "hp": 80, "ataque": "Físico", "velocidad": 1.8},
        {"nombre": "Lobo Feroz", "nivel": 6, "hp": 95, "ataque": "Físico", "velocidad": 2.3},
        {"nombre": "Slime Ácido", "nivel": 10, "hp": 70, "ataque": "Mágico", "velocidad": 1.5}
    ]
    html_engine = generar_canvas_html(st.session_state.zona_actual, st.session_state.montura_equipada, velocidad_mapa, mobs_zona)
    st.components.v1.html(html_engine, height=750, scrolling=False)

with tab_habilidades:
    st.subheader("⚔️ Gestión de Habilidades Activas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Ranura 1 (Principal)", ["Golpe de Púgil", "Invocación de Golem", "Puño de Fuego"])
    with col2:
        st.selectbox("Ranura 2", ["Escudo Rúnico", "(Vacío)", "Ondas de Choque"])
    with col3:
        st.selectbox("Ranura 3", ["(Vacío)", "Poción de Vida Rápida"])

with tab_inventario:
    st.subheader("🎒 Inventario del Héroe")
    st.info("Espacio usado: 24 / 50 ítems.")
    st.markdown("""
    - 🗡️ **Espada de Bronce Reforzada** (Equipada - Tier I)
    - 🛡️ **Armadura de Viajero** (Equipada)
    - 🧪 **Pociones de Vida x5**
    - ⭐ **Fragmentos Míticos:** 0 / 3
    """)

with tab_misiones:
    st.subheader("📋 Registro Completo de Misiones y Recompensas")
    for m in SISTEMA_MISIONES["principales"]:
        with st.expander(f"Principal: {m['titulo']} (Nivel Requerido: {m['nivel_requerido']})"):
            st.write(f"**Descripción:** {m['descripcion']}")
            st.write(f"**Objetivo:** {m['objetivo']}")
            st.success(f"**Recompensa:** {m['recompensa']}")
            st.info(f"**Desbloquea:** {m['desbloquea']}")
            
    st.markdown("### 🌟 Misiones Míticas y Ocultas")
    for mo in SISTEMA_MISIONES["ocultas_miticas"]:
        with st.expander(f"Mítica: {mo['titulo']} (Nv.{mo['nivel_requerido']})"):
            st.write(f"**Pista:** {mo['pista_inicial']}")
            st.write("**Pasos:**")
            for paso in mo['pasos']:
                st.markdown(f"- {paso}")
            st.warning(f"**Recompensa Mítica:** {mo['recompensa_mitica']['nombre_arma']} ({mo['recompensa_mitica']['rareza']})")

with tab_artesania:
    st.subheader("⚒️ Talleres Omni-Oficios (1-100)")
    st.write("Gestiona la fabricación de armas, armaduras pesadas, pociones y encantamientos rúnicos.")
    oficio_sel = st.selectbox("Seleccionar Taller:", ["Herrería", "Alquimia", "Joyería Mítica", "Sastrería"])
    st.progress(45, text=f"Progreso en {oficio_sel}: Nivel 18 (Experiencia: 4,500 / 10,000)")

with tab_lore:
    st.subheader("👑 Lore de Continentes, Reinos y Zonas")
    for cont in DATOS_MUNDO["continentes"]:
        st.markdown(f"### {cont['nombre']}")
        st.write(f"**Niveles:** {cont['niveles']}")
        if "reinos" in cont:
            for r in cont["reinos"]:
                st.markdown(f"- **{r['nombre']}** (Capital: {r['capital']} | Niveles {r['niveles']})")
        if "zonas_neutras" in cont:
            for zn in cont["zonas_neutras"]:
                st.markdown(f"- *Zona Neutra:* {zn}")