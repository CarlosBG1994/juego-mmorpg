import streamlit as st
import json
from config import DATOS_MUNDO
from misiones_reino import SISTEMA_MISIONES
from canvas_engine import generar_canvas_html
from generador_misiones import verificar_acceso_continente

st.set_page_config(page_title="Snd-Worlds MMORPG", page_icon="⚔️", layout="wide")

OPCIONES_PERSONALIZACION = {
    "cabello": ["Rubio Legendario", "Castaño Oscuro", "Pelirrojo Fuego", "Platino Arcano", "Negro Sombra"],
    "armadura_color": ["Azul Real (Valoria)", "Rojo Sangre", "Verde Esmeralda", "Dorado Divino", "Oscuro Abisal"]
}

# Inicialización de estado de sesión para el jugador y progresión
if "continente_actual" not in st.session_state:
    st.session_state.continente_actual = "Continente I: Reinos Fundacionales y Zonas Neutras"
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
if "misiones_completadas" not in st.session_state:
    st.session_state.misiones_completadas = 12
if "miticas_resueltas" not in st.session_state:
    st.session_state.miticas_resueltas = 1
if "monturas_desbloqueadas" not in st.session_state:
    st.session_state.monturas_desbloqueadas = ["A Pie (Velocidad Base)"]
if "montura_equipada" not in st.session_state:
    st.session_state.montura_equipada = "A Pie (Velocidad Base)"

st.title(f"⚔️ {DATOS_MUNDO['nombre_mundo']}")

# BARRA LATERAL: CREADOR Y GESTIÓN DE CONTINENTES
with st.sidebar:
    st.header("🎨 Creador y Moldear Personaje")
    st.session_state.clase_pj = st.selectbox("Clase del Héroe:", [c["nombre"] for c in DATOS_MUNDO["clases_personaje"]])
    st.session_state.cabello_pj = st.selectbox("Estilo de Pelo / Casco:", OPCIONES_PERSONALIZACION["cabello"])
    st.session_state.armadura_pj = st.selectbox("Color de Armadura:", OPCIONES_PERSONALIZACION["armadura_color"])
    
    st.markdown("---")
    st.header("🌍 Progresión de Continentes")
    
    lista_continentes = [
        "Continente I: Reinos Fundacionales y Zonas Neutras",
        "Continente II: Tierras de Ceniza y Abismos Antiguos",
        "Continente III: El Dominio Celestial y Grietas del Vacío"
    ]
    
    continente_sel = st.selectbox("Seleccionar Continente:", lista_continentes)
    
    # Validar bloqueo estricto por misiones y míticas
    acceso_permitido, mensaje_estado = verificar_acceso_continente(
        continente_sel, 
        st.session_state.misiones_completadas, 
        st.session_state.miticas_resueltas
    )
    
    if acceso_permitido:
        st.session_state.continente_actual = continente_sel
        st.success(f"✅ {mensaje_estado}")
        st.session_state.zona_actual = st.selectbox("Zona Activa en el Continente:", [
            "Aurelia Capital", "Santuario Silvestre", "Fortaleza de Hierro", "Torre de los Arcanos", "Puertas del Eón"
        ])
    else:
        st.error(mensaje_estado)
        st.info(f"📊 Tu progreso actual: {st.session_state.misiones_completadas} misiones | {st.session_state.miticas_resueltas}/10 Míticas Ocultas.")

    st.markdown("---")
    st.header("🐴 Establo y Movilidad")
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

# PESTAÑAS PRINCIPALES DEL JUEGO
tab_juego, tab_misiones, tab_lore = st.tabs(["🎮 Mundo Abierto y Combate", "📜 Registro de Misiones", "👑 Lore y Progreso"])

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
    st.subheader(f"📜 Tablón de Misiones — {st.session_state.continente_actual}")
    
    st.markdown("### 👑 Historia Principal")
    for m in SISTEMA_MISIONES["principales"]:
        with st.expander(f"{m['titulo']} (Nivel Requerido: {m['nivel_requerido']})"):
            st.write(f"**Descripción:** {m['descripcion']}")
            st.info(f"**Objetivo:** {m['objetivo']}")
            st.success(f"**Recompensa:** {m['recompensa']}")
            
    st.markdown("### 🗓️ Misiones Diarias, Secundarias y de Caza")
    for sq in SISTEMA_MISIONES["diarias_y_secundarias"]:
        with st.expander(f"[{sq['tipo']}] {sq['titulo']} (Nivel: {sq['nivel']})"):
            st.write(f"**Descripción:** {sq['descripcion']}")
            st.info(f"**Objetivo:** {sq['objetivo']}")
            st.warning(f"**Restricción:** {sq['reinicio']}")
            st.success(f"**Recompensa:** {sq['recompensa']}")

    st.markdown("### 🔮 Cadenas de Misiones Míticas y Secretas (10 Ocultas)")
    st.caption("⚠️ Debes investigar los rumores por el mundo para desbloquear y completar estas cadenas antes de avanzar de continente.")
    for mo in SISTEMA_MISIONES["ocultas_miticas"]:
        with st.expander(f"🔒 {mo['titulo']} [Nivel Mínimo: {mo['nivel_minimo']}]"):
            st.write(f"**Estado:** {mo['estado_conocido']}")
            st.info(f"**Pista del Rumor:** {mo['pista_inicial']}")
            st.warning("⚠️ *Los pasos exactos y la recompensa están sellados hasta descubrir el detonante secreto.*")

with tab_lore:
    st.subheader("👑 Lore, Mapas y Estado del Servidor")
    st.write(f"**Continente Activo:** {st.session_state.continente_actual}")
    st.write(f"**Misiones Completadas:** {st.session_state.misiones_completadas}")
    st.write(f"**Cadenas Míticas Resueltas:** {st.session_state.miticas_resueltas} / 10")
    st.info("💡 **Regla de Avance:** Ningún aventurero puede cruzar a los continentes superiores sin haber completado rigurosamente el contenido y las cadenas míticas del precedente.")