import streamlit as st
import os
import json
import time

st.set_page_config(page_title="Snd-Worlds Mobile", layout="centered")

# --- CONTROL SEGURO DE ESTADO COMPARTIDO (MULTIJUGADOR) ---
ESTADO_MUNDO_PATH = "world_state.json"

def leer_mundo() -> dict:
    if not os.path.exists(ESTADO_MUNDO_PATH):
        return {"jugadores": {}}
    try:
        with open(ESTADO_MUNDO_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"jugadores": {}}

def guardar_mundo(datos: dict):
    try:
        tmp_file = f"{ESTADO_MUNDO_PATH}.tmp"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False)
        os.replace(tmp_file, ESTADO_MUNDO_PATH)
    except Exception:
        pass

# --- INICIALIZACIÓN DE SESIÓN LOCAL ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "raza" not in st.session_state:
    st.session_state.raza = "Humano"
if "clase" not in st.session_state:
    st.session_state.clase = "Caballero"
if "x" not in st.session_state:
    st.session_state.x = 0
if "y" not in st.session_state:
    st.session_state.y = 0
if "hp" not in st.session_state:
    st.session_state.hp = 100
if "zona" not in st.session_state:
    st.session_state.zona = "Corona de Luz (Reino Humano)"

# --- PANTALLA 1: ACCESO / CREACIÓN ---
if not st.session_state.autenticado:
    st.title("⚔️ Snd-Worlds")
    st.subheader("Entrada al Continente Primordial")

    # Importación protegida de clases según raza
    try:
        from modulos.razas_y_clases import CLASES_POR_RAZA, SUBFORMAS_HOMBRE_BESTIA
    except Exception:
        CLASES_POR_RAZA = {"Humano": ["Caballero", "Paladín", "Mago de Batalla"]}
        SUBFORMAS_HOMBRE_BESTIA = ["Hombre Lobo"]

    nombre_input = st.text_input("Nombre de Aventurero:", value=st.session_state.nombre)
    raza_sel = st.selectbox("Raza:", list(CLASES_POR_RAZA.keys()))
    
    subforma_sel = None
    if raza_sel == "Hombre Bestia":
        subforma_sel = st.selectbox("Sub-forma:", SUBFORMAS_HOMBRE_BESTIA)

    clases_disponibles = CLASES_POR_RAZA.get(raza_sel, ["Aventurero"])
    clase_sel = st.selectbox("Clase:", clases_disponibles)

    if st.button("🌟 Entrar al Mundo", use_container_width=True):
        if nombre_input.strip():
            st.session_state.nombre = nombre_input.strip()
            st.session_state.raza = raza_sel
            st.session_state.clase = clase_sel
            st.session_state.autenticado = True
            
            # Registrar al jugador en el mundo compartido
            mundo = leer_mundo()
            mundo["jugadores"][st.session_state.nombre] = {
                "raza": raza_sel,
                "clase": clase_sel,
                "x": st.session_state.x,
                "y": st.session_state.y,
                "zona": st.session_state.zona,
                "ultimo_mov": time.time()
            }
            guardar_mundo(mundo)
            st.rerun()
        else:
            st.warning("Escribe un nombre de personaje.")

# --- PANTALLA 2: JUEGO EN VIVO ---
else:
    st.markdown(f"### 🛡️ {st.session_state.nombre} — {st.session_state.clase} ({st.session_state.raza})")
    st.caption(f"📍 Zona: {st.session_state.zona} | Coords: ({st.session_state.x}, {st.session_state.y}) | HP: {st.session_state.hp}/100")

    # Actualizar posición en el estado global
    mundo = leer_mundo()
    mundo["jugadores"][st.session_state.nombre] = {
        "raza": st.session_state.raza,
        "clase": st.session_state.clase,
        "x": st.session_state.x,
        "y": st.session_state.y,
        "zona": st.session_state.zona,
        "ultimo_mov": time.time()
    }
    guardar_mundo(mundo)

    # CONTROLES TÁCTILES MÓVILES (PAD DIRECCIONAL GRANDE)
    st.markdown("#### 🎮 Movimiento")
    fila1_col1, fila1_col2, fila1_col3 = st.columns([1, 1, 1])
    with fila1_col2:
        if st.button("⬆️ ARRIBA", use_container_width=True):
            st.session_state.y += 1
            st.rerun()

    fila2_col1, fila2_col2, fila2_col3 = st.columns([1, 1, 1])
    with fila2_col1:
        if st.button("⬅️ IZQ", use_container_width=True):
            st.session_state.x -= 1
            st.rerun()
    with fila2_col2:
        if st.button("⚔️ ATACAR", use_container_width=True):
            st.toast("¡Ataque ejecutado con éxito!", icon="💥")
    with fila2_col3:
        if st.button("➡️ DER", use_container_width=True):
            st.session_state.x += 1
            st.rerun()

    fila3_col1, fila3_col2, fila3_col3 = st.columns([1, 1, 1])
    with fila3_col2:
        if st.button("⬇️ ABAJO", use_container_width=True):
            st.session_state.y -= 1
            st.rerun()

    st.divider()

    # MULTIJUGADOR EN VIVO (QUIÉN ESTÁ CERCA)
    st.markdown("#### 👥 Aventureros en el Continente Primordial")
    ahora = time.time()
    jugadores_vivos = {}
    for p_nombre, p_data in mundo.get("jugadores", {}).items():
        # Mostrar jugadores activos en los últimos 5 minutos
        if ahora - p_data.get("ultimo_mov", 0) < 300:
            jugadores_vivos[p_nombre] = p_data

    col_izq, col_der = st.columns(2)
    with col_izq:
        if st.button("🔄 Sincronizar Mapa", use_container_width=True):
            st.rerun()
    with col_der:
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.session_state.autenticado = False
            st.rerun()

    for p_nombre, p_data in jugadores_vivos.items():
        icono = "👑" if p_nombre == st.session_state.nombre else "👤"
        st.write(f"{icono} **{p_nombre}** [{p_data.get('raza')} - {p_data.get('clase')}] en ({p_data.get('x')}, {p_data.get('y')})")
