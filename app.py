import streamlit as st
from config import DATOS_MUNDO
from habilidades import CATALOGO_HABILIDADES, BARRA_HABILIDADES_DEFECTO
from misiones_reino import SISTEMA_MISIONES
from progression_engine import verificar_desbloqueo_continente
from canvas_engine import generar_canvas_html

st.set_page_config(page_title="Snd-Worlds MMORPG", page_icon="⚔️", layout="wide")

OPCIONES_PERSONALIZACION = {
    "cabello": ["Rubio Legendario", "Castaño Oscuro", "Pelirrojo Fuego", "Platino Arcano", "Negro Sombra"],
    "armadura_color": ["Azul Real (Valoria)", "Rojo Sangre", "Verde Esmeralda", "Dorado Divino", "Oscuro Abisal"],
}

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
if "barra_habilidades" not in st.session_state:
    st.session_state.barra_habilidades = BARRA_HABILIDADES_DEFECTO.copy()

st.title(f"⚔️ {DATOS_MUNDO['nombre_mundo']} — {DATOS_MUNDO['superficie_km2']:,} km²")

with st.sidebar:
    st.header("🎨 Creador y Moldear Personaje")
    st.session_state.clase_pj = st.selectbox("Clase del Héroe:", [c["nombre"] for c in DATOS_MUNDO["clases_personaje"]])
    st.session_state.cabello_pj = st.selectbox("Estilo de Pelo / Casco:", OPCIONES_PERSONALIZACION["cabello"])
    st.session_state.armadura_pj = st.selectbox("Color de Armadura:", OPCIONES_PERSONALIZACION["armadura_color"])

    st.markdown("---")
    st.header(f"⚡ Banco de Habilidades ({len(CATALOGO_HABILIDADES)})")
    with st.expander("Equipar Habilidades en Teclas (1, 2, 3, 4, Q)", expanded=True):
        filtro_cat = st.selectbox(
            "Filtrar por Categoría:",
            ["Todas", "Tier I", "Tier II", "Tier III", "Tier IV", "Tier V", "Mítica"],
        )
        ids_filtrados = [
            sid for sid, sk in CATALOGO_HABILIDADES.items()
            if filtro_cat == "Todas" or sk["categoria"] == filtro_cat
        ]

        for tecla in ["1", "2", "3", "4", "q"]:
            actual = st.session_state.barra_habilidades.get(tecla, "skill_0001")
            opciones_tecla = ids_filtrados if actual in ids_filtrados else [actual] + ids_filtrados
            elegida = st.selectbox(
                f"Ranura [{tecla.upper()}]:",
                options=opciones_tecla,
                index=opciones_tecla.index(actual),
                format_func=lambda k: f"#{CATALOGO_HABILIDADES[k]['numero']:04d} {CATALOGO_HABILIDADES[k]['icono']} {CATALOGO_HABILIDADES[k]['nombre']}",
                key=f"equip_slot_{tecla}",
            )
            st.session_state.barra_habilidades[tecla] = elegida

    st.markdown("---")
    st.header("🌍 Progresión de Continentes")
    lista_continentes = [c["nombre"] for c in DATOS_MUNDO["continentes"]]
    continente_sel = st.selectbox("Seleccionar Continente:", lista_continentes)

    acceso_permitido, mensaje_estado = verificar_desbloqueo_continente(
        continente_sel,
        st.session_state.misiones_completadas,
        st.session_state.miticas_resueltas,
    )

    if acceso_permitido:
        st.session_state.continente_actual = continente_sel
        st.success(mensaje_estado)
        cont_data = next(c for c in DATOS_MUNDO["continentes"] if c["nombre"] == continente_sel)
        zonas_cont = [r["nombre"] for r in cont_data["reinos"]] + cont_data["zonas_neutras"]
        st.session_state.zona_actual = st.selectbox("Zona Activa en el Continente:", zonas_cont)
    else:
        st.error(mensaje_estado)
        st.info(f"📊 Progreso actual: {st.session_state.misiones_completadas} misiones | {st.session_state.miticas_resueltas}/10 Míticas Ocultas.")

    st.markdown("---")
    st.header("🐴 Establo y Movilidad")
    montura_elegida = st.selectbox("Montura Equipada:", st.session_state.monturas_desbloqueadas)
    st.session_state.montura_equipada = montura_elegida

    velocidad_mapa = 4.5
    for m in DATOS_MUNDO["monturas_disponibles"]:
        if m["nombre"] == montura_elegida:
            velocidad_mapa = 4.5 * m["bonus_velocidad"]

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

tab_juego, tab_misiones, tab_lore = st.tabs(["🎮 Mundo Abierto y Combate", "📜 Registro de Misiones", "👑 Lore y Progreso"])

with tab_juego:
    mobs_zona = [
        {"nombre": "Goblin Guerrero", "nivel": 3, "hp": 80, "ataque": "Físico", "velocidad": 1.8},
        {"nombre": "Lobo Huargo", "nivel": 6, "hp": 95, "ataque": "Físico", "velocidad": 2.3},
    ]
    habilidades_equipadas = {
        tecla: CATALOGO_HABILIDADES[st.session_state.barra_habilidades[tecla]]
        for tecla in ["1", "2", "3", "4", "q"]
    }
    html_engine = generar_canvas_html(
        st.session_state.continente_actual,
        st.session_state.zona_actual,
        st.session_state.montura_equipada,
        velocidad_mapa,
        st.session_state.cabello_pj,
        st.session_state.armadura_pj,
        mobs_zona,
        habilidades_equipadas,
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
    st.caption("⚠️ Debes completar todas las misiones regulares y estas cadenas míticas antes de desbloquear el siguiente continente.")
    for mo in SISTEMA_MISIONES["ocultas_miticas"]:
        with st.expander(f"🔒 {mo['titulo']} [Nivel Mínimo: {mo['nivel_minimo']}]"):
            st.write(f"**Estado:** {mo['estado_conocido']}")
            st.info(f"**Pista del Rumor:** {mo['pista_inicial']}")
            st.warning("⚠️ *Los pasos exactos y la recompensa están sellados hasta descubrir el detonante secreto.*")

with tab_lore:
    st.subheader("👑 Lore, Escala del Mundo y Estado del Servidor")
    st.write(f"**Extensión Total del Mundo:** {DATOS_MUNDO['superficie_km2']:,} km²")
    st.write(f"**Continente Activo:** {st.session_state.continente_actual}")
    st.write(f"**Misiones Completadas:** {st.session_state.misiones_completadas}")
    st.write(f"**Cadenas Míticas Resueltas:** {st.session_state.miticas_resueltas} / 10")
    st.info("💡 **Regla de Avance:** Ningún aventurero puede cruzar a los continentes superiores sin haber completado todas las misiones y las cadenas míticas ocultas del continente anterior.")