import streamlit as st
from config import (
    DATOS_MUNDO,
    CONTINENTE_INICIAL,
    CONTINENTES_RACIALES,
    CONTINENTE_DEMONIACO,
    CONTINENTE_ANGELICAL,
)
from habilidades import CATALOGO_HABILIDADES, BARRA_HABILIDADES_DEFECTO
from misiones_reino import SISTEMA_MISIONES, obtener_secundarias_disponibles
from progression_engine import (
    obtener_rango_visual_continente,
    verificar_acceso_continente,
)
from canvas_engine import generar_canvas_html

st.set_page_config(page_title="Snd-Worlds MMORPG", page_icon="⚔️", layout="wide")

OPCIONES_PERSONALIZACION = {
    "cabello": ["Rubio Legendario", "Castaño Oscuro", "Pelirrojo Fuego", "Platino Arcano", "Negro Sombra"],
    "armadura_color": ["Azul Real (Valoria)", "Rojo Sangre", "Verde Esmeralda", "Dorado Divino", "Oscuro Abisal"],
}

TODOS_CONTINENTES = (
    [CONTINENTE_INICIAL]
    + CONTINENTES_RACIALES
    + [CONTINENTE_DEMONIACO, CONTINENTE_ANGELICAL]
)

if "continentes_abiertos" not in st.session_state:
    st.session_state.continentes_abiertos = [CONTINENTE_INICIAL]
if "orden_apertura_raciales" not in st.session_state:
    st.session_state.orden_apertura_raciales = []
if "continente_actual" not in st.session_state:
    st.session_state.continente_actual = CONTINENTE_INICIAL
if "zona_actual" not in st.session_state:
    st.session_state.zona_actual = DATOS_MUNDO["zonas_por_continente"][CONTINENTE_INICIAL][0]
if "clase_pj" not in st.session_state:
    st.session_state.clase_pj = "Púgil"
if "cabello_pj" not in st.session_state:
    st.session_state.cabello_pj = OPCIONES_PERSONALIZACION["cabello"][0]
if "armadura_pj" not in st.session_state:
    st.session_state.armadura_pj = OPCIONES_PERSONALIZACION["armadura_color"][0]
if "oro_jugador" not in st.session_state:
    st.session_state.oro_jugador = 1450
if "misiones_completadas_ids" not in st.session_state:
    st.session_state.misiones_completadas_ids = []
if "jugador_completo_principales_abiertas" not in st.session_state:
    st.session_state.jugador_completo_principales_abiertas = False
if "misiones_ocultas_angelical_completadas" not in st.session_state:
    st.session_state.misiones_ocultas_angelical_completadas = False
if "monturas_desbloqueadas" not in st.session_state:
    st.session_state.monturas_desbloqueadas = ["A Pie (Velocidad Base)"]
if "montura_equipada" not in st.session_state:
    st.session_state.montura_equipada = "A Pie (Velocidad Base)"
if "barra_habilidades" not in st.session_state:
    st.session_state.barra_habilidades = BARRA_HABILIDADES_DEFECTO.copy()

principales_ids = {m["id"] for m in SISTEMA_MISIONES["principales"]}
todas_principales_completadas = principales_ids.issubset(set(st.session_state.misiones_completadas_ids))
if todas_principales_completadas:
    st.session_state.jugador_completo_principales_abiertas = True

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
    st.header("🌍 Continentes y Niveles")
    continente_sel = st.selectbox(
        "Seleccionar Continente:",
        TODOS_CONTINENTES,
        format_func=lambda c: f"{c} [{obtener_rango_visual_continente(c, st.session_state.orden_apertura_raciales)}]",
    )

    permitido, msg_cont = verificar_acceso_continente(
        continente_sel,
        st.session_state.continentes_abiertos,
        st.session_state.orden_apertura_raciales,
        st.session_state.jugador_completo_principales_abiertas,
        todas_principales_completadas,
        st.session_state.misiones_ocultas_angelical_completadas,
    )

    if continente_sel not in st.session_state.continentes_abiertos and permitido:
        if st.button(f"🔓 Abrir {continente_sel}", key="btn_abrir_continente"):
            st.session_state.continentes_abiertos.append(continente_sel)
            if continente_sel in CONTINENTES_RACIALES and continente_sel not in st.session_state.orden_apertura_raciales:
                st.session_state.orden_apertura_raciales.append(continente_sel)
            st.session_state.continente_actual = continente_sel
            st.session_state.zona_actual = DATOS_MUNDO["zonas_por_continente"][continente_sel][0]
            st.rerun()

    if continente_sel in st.session_state.continentes_abiertos:
        st.session_state.continente_actual = continente_sel
        st.success(msg_cont)
        zonas_cont = DATOS_MUNDO["zonas_por_continente"][continente_sel]
        idx_z = zonas_cont.index(st.session_state.zona_actual) if st.session_state.zona_actual in zonas_cont else 0
        st.session_state.zona_actual = st.selectbox("Zona Activa:", zonas_cont, index=idx_z)
    else:
        st.warning(msg_cont)

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

tab_juego, tab_misiones, tab_lore = st.tabs(["🎮 Mundo Abierto y Combate", "📜 Registro de Misiones", "👑 Continentes y Progreso"])

with tab_juego:
    mobs_zona = [
        {"nombre": "Goblin Guerrero", "nivel": 3, "hp": 80, "ataque": "Físico", "velocidad": 1.8},
        {"nombre": "Lobo Huargo", "nivel": 6, "hp": 95, "ataque": "Físico", "velocidad": 2.3},
    ]
    habilidades_equipadas = {
        tecla: CATALOGO_HABILIDADES[st.session_state.barra_habilidades[tecla]]
        for tecla in ["1", "2", "3", "4", "q"]
    }
    rango_act = obtener_rango_visual_continente(
        st.session_state.continente_actual,
        st.session_state.orden_apertura_raciales,
    )
    html_engine = generar_canvas_html(
        st.session_state.continente_actual,
        rango_act,
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
    st.subheader(f"📜 Misiones — {st.session_state.continente_actual}")

    st.markdown("### 👑 Historia Principal")
    for m in SISTEMA_MISIONES["principales"]:
        hecha = m["id"] in st.session_state.misiones_completadas_ids
        with st.expander(f"{'✅ ' if hecha else ''}{m['titulo']} (Nivel: {m['nivel_requerido']}) — {m['continente']}"):
            st.write(f"**Zona:** {m['zona']}")
            st.write(f"**Descripción:** {m['descripcion']}")
            st.info(f"**Objetivo:** {m['objetivo']}")
            st.success(f"**Recompensa:** {m['recompensa']}")
            if not hecha and st.button("Completar Misión Principal", key=f"done_mq_{m['id']}"):
                st.session_state.misiones_completadas_ids.append(m["id"])
                st.session_state.oro_jugador += m["recompensa"].get("oro", 0)
                st.rerun()

    st.markdown("### 🔗 Secundarias de Única Vez Encadenadas")
    sec_disponibles = obtener_secundarias_disponibles(st.session_state.misiones_completadas_ids)
    if not sec_disponibles:
        st.info("No hay nuevas secundarias de única vez disponibles en este momento (o ya completaste la cadena actual).")
    for sq in sec_disponibles:
        with st.expander(f"[Cadena: {sq['cadena']} · Paso {sq['paso']}] {sq['titulo']} (Nivel: {sq['nivel_requerido']})"):
            st.write(f"**Zona:** {sq['zona']} | **Única vez:** Sí")
            st.write(f"**Descripción:** {sq['descripcion']}")
            st.info(f"**Objetivo:** {sq['objetivo']}")
            st.success(f"**Recompensa:** {sq['recompensa']}")
            if st.button("Completar Secundaria (Única Vez)", key=f"done_sec_{sq['id']}"):
                st.session_state.misiones_completadas_ids.append(sq["id"])
                st.session_state.oro_jugador += sq["recompensa"].get("oro", 0)
                st.rerun()

    st.markdown("### 🔮 Misiones Míticas Ocultas (Activación Secreta)")
    for mo in SISTEMA_MISIONES["ocultas_miticas"]:
        with st.expander(f"🔒 {mo['titulo']} [Nivel Mínimo: {mo['nivel_minimo']}]"):
            st.write(f"**Estado:** {mo['estado']}")
            st.info(f"**Pista del Rumor:** {mo['pista_rumor']}")
            st.warning("⚠️ *La condición exacta de activación está oculta hasta descubrirla en el mundo.*")

    st.markdown("### 🗝️ Misiones Ocultas de Apertura de Continentes")
    for oc in SISTEMA_MISIONES["ocultas_apertura_continentes"]:
        with st.expander(f"🗝️ {oc['titulo']} — {oc['objetivo_tipo']}"):
            st.write(f"**Estado:** {oc['estado']}")
            st.info(f"**Pista del Rumor:** {oc['pista_rumor']}")
            st.warning("⚠️ *Las condiciones ocultas de apertura requieren exploración y cumplimiento de requisitos.*")

with tab_lore:
    st.subheader("👑 Estado de Continentes, Niveles y Progresión")
    for cont in TODOS_CONTINENTES:
        abierto = cont in st.session_state.continentes_abiertos
        rango = obtener_rango_visual_continente(cont, st.session_state.orden_apertura_raciales)
        estado_txt = "🔓 Abierto" if abierto else "🔒 Cerrado"
        st.write(f"- **{cont}** | Rango: `{rango}` | Estado: {estado_txt}")

    st.markdown("---")
    st.write(f"**Orden de apertura de continentes raciales:** {st.session_state.orden_apertura_raciales or 'Ninguno abierto aún'}")
    st.write(f"**Jugador completó misiones principales abiertas:** {'Sí' if st.session_state.jugador_completo_principales_abiertas else 'No'}")
    st.write(f"**Misiones ocultas específicas para Continente Angelical resueltas:** {'Sí' if st.session_state.misiones_ocultas_angelical_completadas else 'No'}")

# === AUTO-MODULOS START ===
try:
    from modulos import economia_y_comercio as _mod_economia_y_comercio
except Exception as _err:
    _mod_economia_y_comercio = None
try:
    from modulos import habilidades as _mod_habilidades
except Exception as _err:
    _mod_habilidades = None
try:
    from modulos import historia_lore as _mod_historia_lore
except Exception as _err:
    _mod_historia_lore = None
try:
    from modulos import integrador as _mod_integrador
except Exception as _err:
    _mod_integrador = None
try:
    from modulos import mascotas as _mod_mascotas
except Exception as _err:
    _mod_mascotas = None
try:
    from modulos import misiones as _mod_misiones
except Exception as _err:
    _mod_misiones = None
try:
    from modulos import monitor_calidad as _mod_monitor_calidad
except Exception as _err:
    _mod_monitor_calidad = None
try:
    from modulos import monturas as _mod_monturas
except Exception as _err:
    _mod_monturas = None
try:
    from modulos import mundo_y_pve as _mod_mundo_y_pve
except Exception as _err:
    _mod_mundo_y_pve = None
try:
    from modulos import persistencia as _mod_persistencia
except Exception as _err:
    _mod_persistencia = None
try:
    from modulos import progresion_y_stats as _mod_progresion_y_stats
except Exception as _err:
    _mod_progresion_y_stats = None
try:
    from modulos import razas_y_clases as _mod_razas_y_clases
except Exception as _err:
    _mod_razas_y_clases = None
try:
    from modulos import requisitos as _mod_requisitos
except Exception as _err:
    _mod_requisitos = None
try:
    from modulos import world_sync as _mod_world_sync
except Exception as _err:
    _mod_world_sync = None

MODULOS_CARGADOS = {
    "economia_y_comercio": _mod_economia_y_comercio,
    "habilidades": _mod_habilidades,
    "historia_lore": _mod_historia_lore,
    "integrador": _mod_integrador,
    "mascotas": _mod_mascotas,
    "misiones": _mod_misiones,
    "monitor_calidad": _mod_monitor_calidad,
    "monturas": _mod_monturas,
    "mundo_y_pve": _mod_mundo_y_pve,
    "persistencia": _mod_persistencia,
    "progresion_y_stats": _mod_progresion_y_stats,
    "razas_y_clases": _mod_razas_y_clases,
    "requisitos": _mod_requisitos,
    "world_sync": _mod_world_sync
}
# === AUTO-MODULOS END ===
    