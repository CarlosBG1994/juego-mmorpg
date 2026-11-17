import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import random
from datetime import datetime

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

# --- CONTINENTE INICIAL COMPARTIDO POR LAS 4 RAZAS ---
CONTINENTE_INICIAL = "Continente Primordial (Cuna de las 4 Razas)"

RAZAS_Y_CLASES = {
    "Humano": {
        "clases": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"],
        "reino_inicio": "Reino Humano de Valoria",
        "lore": "Gobiernan las grandes llanuras centrales y rutas comerciales del Continente Primordial."
    },
    "Elfo": {
        "clases": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento", "Acechador Nocturno", "Mago de Batalla", "Invocador"],
        "reino_inicio": "Reino Silvano de Lothar",
        "lore": "Habitan los bosques ancestrales del sector oriental del Continente Primordial."
    },
    "Enano": {
        "clases": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Berserker Rúnico", "Luchador de Puño de Hierro", "Ballestero", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"],
        "reino_inicio": "Reino Enano de Khazad",
        "lore": "Dominan las cordilleras del norte con sus fraguas, fortalezas de piedra y minas."
    },
    "Hombre Bestia": {
        "clases": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"],
        "reino_inicio": "Reino Tribal de las Estepas",
        "lore": "Controlan las tierras indómitas del sur donde impera la fuerza y el honor tribal."
    }
}

SUBFORMAS_BESTIA = ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"]

CONTINENTES_OFICIALES = {
    CONTINENTE_INICIAL: {"visible_desde_inicio": True, "tipo": "Continente Inicial (4 Reinos Raciales)"},
    "Archipiélago de los Vientos": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Asentamientos Multi-Raza)"},
    "Tierras Salvajes de Umbra": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Asentamientos Multi-Raza)"},
    "Continente Abisal de los Demonios": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Asentamientos de Todas las Razas)"},
    "Continente Celestial de los Ángeles": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Asentamientos de Todas las Razas)"},
    "Páramos Helados del Norte": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Asentamientos Multi-Raza)"},
    "El Núcleo Central de Comercio": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Zona Franca Global)"}
}

GEOGRAFIA_REINOS = {
    "Reino Humano de Valoria": {
        "ciudades": [
            {"nombre": "Aurelia Capital", "poblacion": "105.000 hab.", "km": "Km 0 (Centro)"},
            {"nombre": "Puerto Real de Solis", "poblacion": "98.000 hab.", "km": "Km 320 Este"},
            {"nombre": "Bastión de Rocablanca", "poblacion": "102.000 hab.", "km": "Km 450 Norte"},
            {"nombre": "Vega Dorada", "poblacion": "95.000 hab.", "km": "Km 280 Oeste"}
        ],
        "pueblos": [
            {"nombre": "Aldea del Molino", "poblacion": "5.200 hab.", "km": "Km 45"},
            {"nombre": "Villa Frontera", "poblacion": "4.800 hab.", "km": "Km 190"}
        ]
    },
    "Reino Silvano de Lothar": {
        "ciudades": [
            {"nombre": "Lothlórien Magna", "poblacion": "100.000 hab.", "km": "Km 0 (Corazón Bosque)"},
            {"nombre": "Ciudad de las Copas", "poblacion": "96.000 hab.", "km": "Km 310 Sur"},
            {"nombre": "Santuario Lunar", "poblacion": "101.000 hab.", "km": "Km 420 Este"},
            {"nombre": "Refugio Esmeralda", "poblacion": "94.000 hab.", "km": "Km 260 Norte"}
        ],
        "pueblos": [
            {"nombre": "Claro de los Arqueros", "poblacion": "5.100 hab.", "km": "Km 60"},
            {"nombre": "Aldea de la Savia", "poblacion": "4.900 hab.", "km": "Km 175"}
        ]
    },
    "Reino Enano de Khazad": {
        "ciudades": [
            {"nombre": "Khazad-Dûm Magna", "poblacion": "110.000 hab.", "km": "Km 0 (Cumbre Central)"},
            {"nombre": "Forja de Hierro Profundo", "poblacion": "99.000 hab.", "km": "Km 290 Oeste"},
            {"nombre": "Ciudadela de Granito", "poblacion": "103.000 hab.", "km": "Km 410 Norte"},
            {"nombre": "Bastión del Yunque", "poblacion": "97.000 hab.", "km": "Km 340 Este"}
        ],
        "pueblos": [
            {"nombre": "Mina de Carbón", "poblacion": "5.400 hab.", "km": "Km 55"},
            {"nombre": "Pueblo Cantero", "poblacion": "4.700 hab.", "km": "Km 210"}
        ]
    },
    "Reino Tribal de las Estepas": {
        "ciudades": [
            {"nombre": "Gran Totem Imperial", "poblacion": "104.000 hab.", "km": "Km 0 (Estepa Central)"},
            {"nombre": "Arena de los Campeones", "poblacion": "98.500 hab.", "km": "Km 300 Sur"},
            {"nombre": "Garra de Piedra", "poblacion": "100.500 hab.", "km": "Km 390 Oeste"},
            {"nombre": "Rugido del Norte", "poblacion": "95.500 hab.", "km": "Km 275 Este"}
        ],
        "pueblos": [
            {"nombre": "Campamento Nómada", "poblacion": "5.000 hab.", "km": "Km 70"},
            {"nombre": "Aldea del Cazador", "poblacion": "4.850 hab.", "km": "Km 180"}
        ]
    }
}

CATALOGO_EDIFICIOS = {
    "Castillo Real / Sede de Gobierno": {
        "desc": "Sede del poder regional, sala del trono, cuartel de la guardia real, mazmorras reales y registro de tierras.",
        "items": [
            {"id": "titulo_noble", "nombre": "Título de Ciudadano Honorario", "tipo": "Documento Oficial", "tier": "Raro", "metal": "Oro", "precio": 5},
            {"id": "salvoconducto", "nombre": "Salvoconducto Real Inter-Reinos", "tipo": "Permiso", "tier": "Común", "metal": "Plata", "precio": 40}
        ]
    },
    "Tienda General y Armería": {
        "desc": "Compra y venta libre de armas, armaduras, escudos y suministros de exploración (0% Soul-Bound).",
        "items": [
            {"id": "espada_acero", "nombre": "Espada de Acero Templado", "tipo": "Arma", "tier": "Común", "metal": "Plata", "precio": 30},
            {"id": "guanteletes_pugil", "nombre": "Guanteletes de Cuero y Hierro", "tipo": "Arma Púgil", "tier": "Raro", "metal": "Plata", "precio": 55},
            {"id": "coraza_pesada", "nombre": "Coraza de Placas Rúnicas", "tipo": "Armadura", "tier": "Épico", "metal": "Oro", "precio": 4}
        ]
    },
    "Gremio de Aventureros": {
        "desc": "Tablón oficial de contratos, ascenso de rango de aventurero y aprendizaje de habilidades base.",
        "items": [
            {"id": "grimorio_ignis", "nombre": "Grimorio: Impacto Ígneo", "tipo": "Habilidad", "tier": "Raro", "metal": "Cores", "precio": 4},
            {"id": "grimorio_eclipse", "nombre": "Grimorio: Golpe del Eclipse", "tipo": "Habilidad", "tier": "Épico", "metal": "Oro", "precio": 6}
        ]
    },
    "Salón de Gremios de Jugadores": {
        "desc": "Sede donde los jugadores fundan sus propios clanes, reclutan miembros y gestionan fortalezas de gremio.",
        "items": [
            {"id": "carta_gremio", "nombre": "Carta Fundacional de Gremio", "tipo": "Licencia de Clan", "tier": "Épico", "metal": "Oro", "precio": 10}
        ]
    },
    "Distrito de Talleres (Todas las Profesiones)": {
        "desc": "Forjas de Herrería, Laboratorios de Alquimia, Sastrería, Carpintería, Encantamiento, Joyería e Ingeniería.",
        "items": [
            {"id": "kit_herreria", "nombre": "Martillo y Yunque de Maestro Herrero", "tipo": "Herramienta Profesión", "tier": "Raro", "metal": "Plata", "precio": 60},
            {"id": "alambique", "nombre": "Alambique de Alquimista", "tipo": "Herramienta Profesión", "tier": "Raro", "metal": "Plata", "precio": 60},
            {"id": "lingote_mitril", "nombre": "Lingote de Mitril Refinado", "tipo": "Material Crafteo", "tier": "Épico", "metal": "Cores", "precio": 5}
        ]
    },
    "Hostal y Restaurante Real": {
        "desc": "Alquiler de habitaciones para recuperar energía al 100% y banquetes gastronómicos con bonificadores.",
        "items": [
            {"id": "banquete", "nombre": "Banquete de Carne Asada y Hidromiel (+Buff)", "tipo": "Comida", "tier": "Común", "metal": "Plata", "precio": 15},
            {"id": "habitacion_vip", "nombre": "Estancia en Suite del Hostal (Descanso Total)", "tipo": "Servicio", "tier": "Común", "metal": "Plata", "precio": 10}
        ]
    },
    "Inmobiliaria Urbana (Casas y Pisos de NPCs)": {
        "desc": "Compra de viviendas, pisos en edificios urbanos o mansiones en barrios residenciales para almacenamiento y comercio.",
        "items": [
            {"id": "piso_barrio", "nombre": "Piso en el Barrio Artesano (Escritura)", "tipo": "Propiedad Inmueble", "tier": "Raro", "metal": "Oro", "precio": 8},
            {"id": "casa_residencial", "nombre": "Casa de Piedra de Dos Plantas (Escritura)", "tipo": "Propiedad Inmueble", "tier": "Épico", "metal": "Oro", "precio": 20},
            {"id": "mansion_noble", "nombre": "Mansión del Distrito Alto (Escritura)", "tipo": "Propiedad Inmueble", "tier": "Legendario", "metal": "Diamante", "precio": 2}
        ]
    },
    "Barrio de Tiendas Prohibidas (Mercado Negro)": {
        "desc": "⚠️ Callejones ocultos sin ley. Contrabando, venenos letales, grimorios prohibidos, falsificaciones y objetos malditos.",
        "items": [
            {"id": "veneno_sombra", "nombre": "Extracto de Viuda Negra (Ilegal)", "tipo": "Consumible Prohibido", "tier": "Épico", "metal": "Cores", "precio": 8},
            {"id": "grimorio_prohibido", "nombre": "Grimorio Prohibido: Drenaje de Alma", "tipo": "Habilidad Oscura", "tier": "Épico", "metal": "Diamante", "precio": 1},
            {"id": "ganzua_maestra", "nombre": "Juego de Ganzúas de Contrabandista", "tipo": "Herramienta Ilegal", "tier": "Raro", "metal": "Oro", "precio": 4}
        ]
    }
}

CATALOGO_OCULTAS = [
    {"id": "abrir_vientos", "nombre": "La Brújula de las Tormentas", "continente_premio": "Archipiélago de los Vientos", "tier": "Raro", "pista": "Explora las costas del Continente Primordial."},
    {"id": "abrir_umbra", "nombre": "Susurros en la Penumbra", "continente_premio": "Tierras Salvajes de Umbra", "tier": "Raro", "pista": "Derrota a los bandidos nocturnos."},
    {"id": "abrir_demonios", "nombre": "El Portal del Abismo", "continente_premio": "Continente Abisal de los Demonios", "tier": "Épico", "pista": "Reúne Cores oscuros y rompe el sello volcánico."},
    {"id": "abrir_angeles", "nombre": "La Escalera de Luz", "continente_premio": "Continente Celestial de los Ángeles", "tier": "Épico", "pista": "Alcanza la cima más alta y ofrece Plata pura."},
    {"id": "abrir_helados", "nombre": "Corazón de Escarcha", "continente_premio": "Páramos Helados del Norte", "tier": "Raro", "pista": "Forja equipo térmico en Khazad."},
    {"id": "abrir_nucleo", "nombre": "La Llave del Comercio Global", "continente_premio": "El Núcleo Central de Comercio", "tier": "Legendario", "pista": "Completa rutas comerciales entre los 4 reinos iniciales."}
]

# --- ESTADO DE SESIÓN ---
for key, default in [
    ("logged_in", False), ("user_email", ""), ("hero_name", ""),
    ("raza", "Humano"), ("subforma", "Hombre Lobo"), ("genero", "Hombre"),
    ("clase", "Caballero"), ("continente", CONTINENTE_INICIAL),
    ("reino_actual", "Reino Humano de Valoria"), ("asentamiento_actual", "Aurelia Capital"),
    ("tipo_asentamiento", "Ciudad (100.000 hab.)"),
    ("plano_vista", "Exterior (Puertas del Asentamiento)"),
    ("edificio_activo", "Tienda General y Armería"),
    ("hero_level", 1), ("hero_hp", 100), ("hero_xp", 0),
    ("cores", 10), ("plata", 150), ("oro", 15), ("diamante", 2),
    ("skills", ["Golpe Base", "Tajo Inicial"]), ("inventario", ["Ropa de Viajero", "Raciones de Pan"]),
    ("propiedades", []), ("gremio_propio", "Sin Gremio"),
    ("has_character", False)
]:
    if key not in st.session_state:
        st.session_state[key] = default

def save_user_data():
    if st.session_state.logged_in and st.session_state.user_email:
        user_data = {
            "hero_name": st.session_state.hero_name,
            "raza": st.session_state.raza,
            "subforma": st.session_state.subforma,
            "genero": st.session_state.genero,
            "clase": st.session_state.clase,
            "continente": st.session_state.continente,
            "reino_actual": st.session_state.reino_actual,
            "asentamiento_actual": st.session_state.asentamiento_actual,
            "tipo_asentamiento": st.session_state.tipo_asentamiento,
            "hero_level": st.session_state.hero_level,
            "hero_hp": st.session_state.hero_hp,
            "hero_xp": st.session_state.hero_xp,
            "cores": st.session_state.cores,
            "plata": st.session_state.plata,
            "oro": st.session_state.oro,
            "diamante": st.session_state.diamante,
            "skills": st.session_state.skills,
            "inventario": st.session_state.inventario,
            "propiedades": st.session_state.propiedades,
            "gremio_propio": st.session_state.gremio_propio,
            "has_character": st.session_state.has_character
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= PANTALLA DE LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Arquitectura Masiva Multi-Jugador | Ciudades de 100.000 NPCs | Barrio Prohibido</p>", unsafe_allow_html=True)
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
                    st.session_state.subforma = data.get("subforma", "Hombre Lobo")
                    st.session_state.genero = data.get("genero", "Hombre")
                    st.session_state.clase = data.get("clase", "Caballero")
                    st.session_state.continente = data.get("continente", CONTINENTE_INICIAL)
                    st.session_state.reino_actual = data.get("reino_actual", "Reino Humano de Valoria")
                    st.session_state.asentamiento_actual = data.get("asentamiento_actual", "Aurelia Capital")
                    st.session_state.tipo_asentamiento = data.get("tipo_asentamiento", "Ciudad (100.000 hab.)")
                    st.session_state.hero_level = data.get("hero_level", 1)
                    st.session_state.hero_hp = data.get("hero_hp", 100)
                    st.session_state.hero_xp = data.get("hero_xp", 0)
                    st.session_state.cores = data.get("cores", 10)
                    st.session_state.plata = data.get("plata", 150)
                    st.session_state.oro = data.get("oro", 15)
                    st.session_state.diamante = data.get("diamante", 2)
                    st.session_state.skills = data.get("skills", ["Golpe Base", "Tajo Inicial"])
                    st.session_state.inventario = data.get("inventario", ["Ropa de Viajero", "Raciones de Pan"])
                    st.session_state.propiedades = data.get("propiedades", [])
                    st.session_state.gremio_propio = data.get("gremio_propio", "Sin Gremio")
                    st.session_state.has_character = data.get("has_character", True)
                else:
                    st.session_state.hero_name = email.split("@")[0]
                    st.session_state.has_character = False
                
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.warning("Introduce un nombre de usuario válido.")
    st.stop()

# ================= PANTALLA DE CREACIÓN DE PERSONAJE =================
if not st.session_state.has_character:
    st.markdown("<h2 style='text-align: center; color: #ffaa00;'>🛡️ Creación de Tu Héroe en Snd-Worlds</h2>", unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.session_state.hero_name = st.text_input("Nombre del Héroe", value=st.session_state.hero_name)
        st.session_state.raza = st.selectbox("Raza / Facción", list(RAZAS_Y_CLASES.keys()))
        if st.session_state.raza == "Hombre Bestia":
            st.session_state.subforma = st.selectbox("Sub-forma de Bestia", SUBFORMAS_BESTIA)
        st.session_state.genero = st.selectbox("Género", ["Hombre", "Mujer"])
        
    with col_c2:
        info_raza = RAZAS_Y_CLASES[st.session_state.raza]
        st.session_state.clase = st.selectbox("Clase Oficial", info_raza["clases"])
        st.session_state.continente = CONTINENTE_INICIAL
        reino_raza = info_raza["reino_inicio"]
        st.session_state.reino_actual = reino_raza
        ciudad_ini = GEOGRAFIA_REINOS[reino_raza]["ciudades"][0]["nombre"]
        st.session_state.asentamiento_actual = ciudad_ini
        st.session_state.tipo_asentamiento = "Ciudad (100.000 hab.)"
        
        st.info(
            f"🌍 **Continente:** `{CONTINENTE_INICIAL}`\n"
            f"🏰 **Reino:** `{reino_raza}`\n"
            f"🏙️ **Ciudad Inicial:** `{ciudad_ini}` (100.000 habitantes)\n\n"
            f"*{info_raza['lore']}*"
        )

    if st.button("🚀 ¡Entrar al Mundo!", use_container_width=True):
        if st.session_state.hero_name:
            st.session_state.has_character = True
            save_user_data()
            st.rerun()
        else:
            st.warning("Asigna un nombre a tu héroe.")
    st.stop()

# ================= BARRA LATERAL DEL JUGADOR =================
st.sidebar.header(f"🛡️ {st.session_state.hero_name}")
st.sidebar.write(f"**Raza:** {st.session_state.raza}" + (f" ({st.session_state.subforma})" if st.session_state.raza == "Hombre Bestia" else ""))
st.sidebar.write(f"**Clase:** {st.session_state.clase} | **Nivel:** {st.session_state.hero_level}")
st.sidebar.write(f"**Gremio:** `{st.session_state.gremio_propio}`")
st.sidebar.write(f"❤️ **Salud:** {st.session_state.hero_hp}/100")

st.sidebar.markdown("---")
st.sidebar.markdown(f"🌍 `{st.session_state.continente}`")
st.sidebar.markdown(f"🏰 `{st.session_state.reino_actual}`")
st.sidebar.markdown(f"🏙️ `{st.session_state.asentamiento_actual}`")
st.sidebar.caption(f"Escala: {st.session_state.tipo_asentamiento}")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Metales")
st.sidebar.markdown(
    f"- 💠 **Cores:** `{st.session_state.cores}` | 🥈 **Plata:** `{st.session_state.plata}`\n"
    f"- 🪙 **Oro:** `{st.session_state.oro}` | 💎 **Diamante:** `{st.session_state.diamante}`"
)

if st.sidebar.button("🚪 Cerrar Sesión"):
    save_user_data()
    st.session_state.logged_in = False
    st.session_state.has_character = False
    st.rerun()

def obtener_continentes_visibles():
    visibles = []
    ahora = datetime.utcnow()
    continentes_db = db.collection("world_continents").stream()
    estado_continentes = {doc.id: doc.to_dict() for doc in continentes_db}
    
    for cont, info in CONTINENTES_OFICIALES.items():
        if info["visible_desde_inicio"]:
            visibles.append(cont)
        else:
            if cont in estado_continentes:
                datos_apertura = estado_continentes[cont]
                descubridor = datos_apertura.get("pionero")
                fecha_apertura = datos_apertura.get("fecha")
                if fecha_apertura:
                    fecha_dt = fecha_apertura.replace(tzinfo=None)
                    diferencia_horas = (ahora - fecha_dt).total_seconds() / 3600
                    if descubridor == st.session_state.hero_name:
                        visibles.append(cont + " 🌟 (Tu Descubrimiento)")
                    elif diferencia_horas >= 24:
                        visibles.append(cont + " 🔓 (Abierto al Servidor)")
                    else:
                        horas_restantes = int(24 - diferencia_horas)
                        visibles.append(cont + f" 🔒 (Exclusivo Pionero: {horas_restantes}h restantes)")
            else:
                visibles.append(cont + " 🔒 (Oculto - Requiere Misión Secreta)")
    return visibles

# Pestañas principales
tab_canvas, tab_edificio, tab_viaje_local, tab_bag, tab_world, tab_quests, tab_p2p = st.tabs([
    "🎮 Exploración Visual (Planos)", 
    "🏪 Interior de Edificio / Tienda",
    "🗺️ Ciudades y Pueblos (Km)",
    "🎒 Mochila y Propiedades",
    "🌍 Los 7 Continentes", 
    "📜 Misiones Secretas",
    "🤝 Encargos P2P"
])

# ================= PESTAÑA 1: MOTOR VISUAL POR PLANOS (EXTERIOR <-> INTERIOR CIUDAD) =================
with tab_canvas:
    col_top1, col_top2 = st.columns([2.5, 1.5])
    with col_top1:
        st.subheader(f"📍 {st.session_state.asentamiento_actual} — Plano: {st.session_state.plano_vista}")
    with col_top2:
        if st.session_state.plano_vista == "Exterior (Puertas del Asentamiento)":
            if st.button("🚪 Cruzar Murallas y Entrar a la Ciudad/Pueblo", use_container_width=True, type="primary"):
                st.session_state.plano_vista = "Interior Urbano (Calles, Castillo y Barrios)"
                st.rerun()
        else:
            if st.button("🌲 Salir a las Afueras (Exterior)", use_container_width=True):
                st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
                st.rerun()

    skills_js = str(st.session_state.skills)
    es_interior = "true" if "Interior" in st.session_state.plano_vista else "false"
    asentamiento_str = st.session_state.asentamiento_actual
    tipo_asentamiento_str = st.session_state.tipo_asentamiento
    es_ciudad_grande = "true" if "100.000" in tipo_asentamiento_str else "false"
    hero_name_str = st.session_state.hero_name

    game_html = f"""
    <div style="text-align: center; background: #111; padding: 10px; border-radius: 10px; border: 2px solid #ffaa00;">
        <canvas id="gameCanvas" width="820" height="460" style="background: #1a241b; border-radius: 8px; display: block; margin: 0 auto; max-width: 100%;"></canvas>
        
        <div style="margin-top: 10px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
            <button onclick="usarHabilidad(0)" style="background: #d9534f; color: white; border: none; padding: 8px 14px; border-radius: 6px; font-weight: bold; cursor: pointer;">⚔️ Ataque [1]</button>
            <button onclick="usarHabilidad(1)" style="background: #0275d8; color: white; border: none; padding: 8px 14px; border-radius: 6px; font-weight: bold; cursor: pointer;">⚡ Habilidad [2]</button>
        </div>
        <p id="hudInfo" style="color: #ffd700; margin-top: 8px; font-weight: bold; font-size: 14px;">Usa WASD o los botones táctiles para recorrer el plano.</p>
    </div>

    <div style="margin-top: 12px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div style="display: grid; grid-template-columns: repeat(3, 50px); gap: 5px;">
            <div></div>
            <button ontouchstart="moverTouch('W')" onmousedown="moverTouch('W')" style="height: 50px; background: #2c2c2c; color: #fff; border: 1px solid #666; border-radius: 8px; font-size: 18px;">⬆️</button>
            <div></div>
            <button ontouchstart="moverTouch('A')" onmousedown="moverTouch('A')" style="height: 50px; background: #2c2c2c; color: #fff; border: 1px solid #666; border-radius: 8px; font-size: 18px;">⬅️</button>
            <button ontouchstart="moverTouch('S')" onmousedown="moverTouch('S')" style="height: 50px; background: #2c2c2c; color: #fff; border: 1px solid #666; border-radius: 8px; font-size: 18px;">⬇️</button>
            <button ontouchstart="moverTouch('D')" onmousedown="moverTouch('D')" style="height: 50px; background: #2c2c2c; color: #fff; border: 1px solid #666; border-radius: 8px; font-size: 18px;">➡️</button>
        </div>
        <div style="text-align: left; color: #ddd; font-size: 12px; background: #1c1c1c; padding: 10px; border-radius: 8px; flex: 1; min-width: 260px;">
            <b>🧭 Guía del Plano Urbano:</b><br>
            • <b>Norte:</b> Gran Castillo Real y Plaza Mayor.<br>
            • <b>Avenida Central:</b> Tienda General, Gremio de Aventureros y Gremios.<br>
            • <b>Sector Este:</b> Talleres, Hostal y Restaurante.<br>
            • <b>Sector Oeste:</b> Distrito Residencial (Casas y Pisos).<br>
            • <b>Callejones Sur:</b> ⚠️ Barrio de Tiendas Prohibidas (Mercado Negro).
        </div>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        const esInterior = {es_interior};
        const esCiudadGrande = {es_ciudad_grande};

        const worldW = esInterior ? 1600 : 820;
        const worldH = esInterior ? 1200 : 460;

        let player = {{ x: esInterior ? 800 : 410, y: esInterior ? 950 : 350, radius: 14, speed: 5, color: "#ffaa00" }};
        let keys = {{}};

        const edificios = [
            {{ nombre: "Castillo Real / Sede de Gobierno", x: 640, y: 60, w: 320, h: 160, color: "#5a5a66", border: "#ffd700" }},
            {{ nombre: "Tienda General y Armería", x: 520, y: 340, w: 180, h: 110, color: "#2980b9", border: "#fff" }},
            {{ nombre: "Gremio de Aventureros", x: 900, y: 340, w: 180, h: 110, color: "#27ae60", border: "#fff" }},
            {{ nombre: "Salón de Gremios de Jugadores", x: 900, y: 520, w: 180, h: 110, color: "#16a085", border: "#fff" }},
            {{ nombre: "Distrito de Talleres (Todas las Profesiones)", x: 1220, y: 340, w: 220, h: 140, color: "#d35400", border: "#fff" }},
            {{ nombre: "Hostal y Restaurante Real", x: 1220, y: 550, w: 220, h: 120, color: "#e67e22", border: "#fff" }},
            {{ nombre: "Inmobiliaria Urbana (Casas y Pisos de NPCs)", x: 160, y: 340, w: 230, h: 280, color: "#8e44ad", border: "#fff" }},
            {{ nombre: "Barrio de Tiendas Prohibidas (Mercado Negro)", x: 140, y: 880, w: 250, h: 140, color: "#2c0b0e", border: "#ff0033" }}
        ];

        const numTranseuntes = esCiudadGrande ? 85 : 22;
        let npcs = [];
        for(let i=0; i<numTranseuntes; i++) {{
            npcs.push({{
                x: Math.random() * (worldW - 100) + 50,
                y: Math.random() * (worldH - 100) + 50,
                vx: (Math.random() - 0.5) * 1.5,
                vy: (Math.random() - 0.5) * 1.5,
                color: i % 3 === 0 ? "#85c1e9" : (i % 3 === 1 ? "#f7dc6f" : "#bb8fce")
            }});
        }}

        window.addEventListener('keydown', (e) => {{
            keys[e.key.toLowerCase()] = true;
            if(e.key === '1') usarHabilidad(0);
            if(e.key === '2') usarHabilidad(1);
        }});
        window.addEventListener('keyup', (e) => {{ keys[e.key.toLowerCase()] = false; }});

        function moverTouch(dir) {{
            if(dir === 'W') player.y -= 28;
            if(dir === 'S') player.y += 28;
            if(dir === 'A') player.x -= 28;
            if(dir === 'D') player.x += 28;
            limites();
        }}

        function limites() {{
            if (player.x < player.radius) player.x = player.radius;
            if (player.x > worldW - player.radius) player.x = worldW - player.radius;
            if (player.y < player.radius) player.y = player.radius;
            if (player.y > worldH - player.radius) player.y = worldH - player.radius;
        }}

        function actualizar() {{
            if (keys['w'] || keys['arrowup']) player.y -= player.speed;
            if (keys['s'] || keys['arrowdown']) player.y += player.speed;
            if (keys['a'] || keys['arrowleft']) player.x -= player.speed;
            if (keys['d'] || keys['arrowright']) player.x += player.speed;
            limites();

            if (esInterior) {{
                npcs.forEach(n => {{
                    n.x += n.vx; n.y += n.vy;
                    if(n.x < 30 || n.x > worldW - 30) n.vx *= -1;
                    if(n.y < 30 || n.y > worldH - 30) n.vy *= -1;
                }});

                let edificioCercano = null;
                edificios.forEach(ed => {{
                    if (player.x > ed.x - 15 && player.x < ed.x + ed.w + 15 &&
                        player.y > ed.y - 15 && player.y < ed.y + ed.h + 15) {{
                        edificioCercano = ed.nombre;
                    }}
                }});

                if (edificioCercano) {{
                    document.getElementById("hudInfo").innerText = "🚪 Frente a: [" + edificioCercano + "] ➔ Ve a '🏪 Interior de Edificio / Tienda'.";
                }}
            }} else {{
                if (player.y < 140) {{
                    document.getElementById("hudInfo").innerText = "🏰 Puertas de {asentamiento_str}. ¡Pulsa el botón superior para entrar!";
                }}
            }}
        }}

        function dibujar() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.save();

            if (!esInterior) {{
                ctx.fillStyle = "#223322";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#6e5d4f";
                ctx.fillRect(360, 110, 100, 350);

                ctx.fillStyle = "#4a4a4a";
                ctx.fillRect(50, 20, 720, 100);
                ctx.strokeStyle = "#888";
                ctx.lineWidth = 4;
                ctx.strokeRect(50, 20, 720, 100);

                ctx.fillStyle = "#2b1d0e";
                ctx.fillRect(360, 40, 100, 80);
                ctx.fillStyle = "#ffd700";
                ctx.font = "bold 14px sans-serif";
                ctx.textAlign = "center";
                ctx.fillText("PUERTAS DE {asentamiento_str.upper()}", 410, 35);
                ctx.fillStyle = "#fff";
                ctx.font = "12px sans-serif";
                ctx.fillText("({tipo_asentamiento_str})", 410, 85);
            }} else {{
                let camX = player.x - canvas.width / 2;
                let camY = player.y - canvas.height / 2;
                camX = Math.max(0, Math.min(camX, worldW - canvas.width));
                camY = Math.max(0, Math.min(camY, worldH - canvas.height));
                ctx.translate(-camX, -camY);

                ctx.fillStyle = "#252629";
                ctx.fillRect(0, 0, worldW, worldH);

                ctx.fillStyle = "#3c3f45";
                ctx.fillRect(740, 220, 120, 950);
                ctx.fillRect(150, 470, 1300, 70);

                ctx.fillStyle = "#161618";
                ctx.fillRect(220, 540, 45, 360);
                ctx.fillRect(220, 860, 520, 40);

                ctx.fillStyle = "#4b3832";
                for(let row=0; row<3; row++) {{
                    for(let col=0; col<3; col++) {{
                        ctx.fillRect(175 + col*70, 365 + row*80, 50, 50);
                    }}
                }}

                edificios.forEach(ed => {{
                    ctx.fillStyle = ed.color;
                    ctx.fillRect(ed.x, ed.y, ed.w, ed.h);
                    ctx.strokeStyle = ed.border;
                    ctx.lineWidth = 3;
                    ctx.strokeRect(ed.x, ed.y, ed.w, ed.h);

                    ctx.fillStyle = "#fff";
                    ctx.font = "bold 12px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(ed.nombre, ed.x + ed.w/2, ed.y + ed.h/2);
                }});

                npcs.forEach(n => {{
                    ctx.beginPath();
                    ctx.arc(n.x, n.y, 6, 0, Math.PI * 2);
                    ctx.fillStyle = n.color;
                    ctx.fill();
                    ctx.closePath();
                }});
            }}

            ctx.beginPath();
            ctx.arc(player.x, player.y, player.radius, 0, Math.PI * 2);
            ctx.fillStyle = player.color;
            ctx.fill();
            ctx.lineWidth = 2;
            ctx.strokeStyle = "#fff";
            ctx.stroke();
            ctx.closePath();

            ctx.fillStyle = "#ffaa00";
            ctx.font = "bold 12px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText("{hero_name_str}", player.x, player.y - 20);

            ctx.restore();
        }}

        function loop() {{
            actualizar();
            dibujar();
            requestAnimationFrame(loop);
        }}

        function usarHabilidad(index) {{
            const skillsList = {skills_js};
            const skillName = skillsList[index] || "Golpe Base";
            document.getElementById("hudInfo").innerText = "⚡ ¡Ejecutaste: " + skillName + "!";
        }}

        loop();
    </script>
    """
    st.components.v1.html(game_html, height=580)

# ================= PESTAÑA 2: INTERIOR DE EDIFICIO / TIENDA =================
with tab_edificio:
    st.subheader(f"🏪 Distritos y Edificios de {st.session_state.asentamiento_actual}")
    st.info("Selecciona el edificio al que has entrado desde las calles para comerciar, alquilar, fundar gremios o comprar propiedades.")

    edificio_sel = st.selectbox("Edificio / Establecimiento Activo", list(CATALOGO_EDIFICIOS.keys()))
    datos_ed = CATALOGO_EDIFICIOS[edificio_sel]

    st.markdown(f"### 🏛️ {edificio_sel}")
    st.write(f"*{datos_ed['desc']}*")

    if "Gremios de Jugadores" in edificio_sel:
        st.markdown("#### 🛡️ Gestión de Gremio de Jugadores")
        nuevo_gremio = st.text_input("Nombre de tu nuevo Gremio (Coste: 10 Oro)")
        if st.button("Fundar Gremio Oficial"):
            if nuevo_gremio and st.session_state.oro >= 10:
                st.session_state.oro -= 10
                st.session_state.gremio_propio = nuevo_gremio
                save_user_data()
                st.success(f"¡Has fundado el gremio **{nuevo_gremio}**!")
                st.rerun()
            else:
                st.error("Necesitas 10 de Oro y un nombre válido.")

    st.markdown("---")
    st.markdown("#### 🛒 Catálogo Disponible (Comprar)")
    for item in datos_ed["items"]:
        col_i1, col_i2, col_i3 = st.columns([3, 1.5, 1])
        with col_i1:
            st.markdown(f"**{item['nombre']}** (`{item['tier']}`) — *{item['tipo']}*")
        with col_i2:
            st.markdown(f"💰 `{item['precio']}` **{item['metal']}**")
        with col_i3:
            if st.button("Adquirir", key=f"buy_{item['id']}"):
                metal = item["metal"]
                coste = item["precio"]
                puede = False
                if metal == "Plata" and st.session_state.plata >= coste:
                    st.session_state.plata -= coste; puede = True
                elif metal == "Oro" and st.session_state.oro >= coste:
                    st.session_state.oro -= coste; puede = True
                elif metal == "Cores" and st.session_state.cores >= coste:
                    st.session_state.cores -= coste; puede = True
                elif metal == "Diamante" and st.session_state.diamante >= coste:
                    st.session_state.diamante -= coste; puede = True

                if puede:
                    if "Habilidad" in item["tipo"]:
                        sk_name = item["nombre"].split(": ")[-1]
                        if sk_name not in st.session_state.skills:
                            st.session_state.skills.append(sk_name)
                        else:
                            st.session_state.inventario.append(item["nombre"])
                    elif "Propiedad" in item["tipo"]:
                        st.session_state.propiedades.append(f"{item['nombre']} en {st.session_state.asentamiento_actual}")
                    else:
                        st.session_state.inventario.append(item["nombre"])
                    save_user_data()
                    st.success(f"¡Has adquirido **{item['nombre']}**!")
                    st.rerun()
                else:
                    st.error(f"No tienes suficiente {metal}.")

    st.markdown("---")
    st.markdown("#### 💰 Vender Objetos de tu Mochila")
    if st.session_state.inventario:
        obj_vender = st.selectbox("Selecciona objeto para vender (Valor: 10 Plata)", st.session_state.inventario)
        if st.button("Vender Objeto"):
            st.session_state.inventario.remove(obj_vender)
            st.session_state.plata += 10
            save_user_data()
            st.success(f"Vendiste **{obj_vender}** por 10 de Plata.")
            st.rerun()

# ================= PESTAÑA 3: CIUDADES Y PUEBLOS POR KILÓMETROS =================
with tab_viaje_local:
    st.subheader(f"🗺️ Distribución Geográfica en {st.session_state.continente}")
    
    if st.session_state.continente == CONTINENTE_INICIAL:
        reino_sel = st.selectbox("Selecciona Reino del Continente Primordial", list(GEOGRAFIA_REINOS.keys()))
        datos_reino = GEOGRAFIA_REINOS[reino_sel]

        st.markdown("### 🏙️ Las 4 Grandes Ciudades (~100.000 Habitantes cada una)")
        for c in datos_reino["ciudades"]:
            col_c1, col_c2 = st.columns([3, 1])
            with col_c1:
                st.markdown(f"**{c['nombre']}** — Población: `{c['poblacion']}` | Ubicación: `{c['km']}`")
            with col_c2:
                if st.button("Viajar", key=f"civ_{c['nombre']}"):
                    st.session_state.reino_actual = reino_sel
                    st.session_state.asentamiento_actual = c["nombre"]
                    st.session_state.tipo_asentamiento = f"Ciudad ({c['poblacion']})"
                    st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
                    save_user_data()
                    st.rerun()

        st.markdown("### 🏘️ Pueblos y Aldeas (~5.000 Habitantes)")
        for p in datos_reino["pueblos"]:
            col_p1, col_p2 = st.columns([3, 1])
            with col_p1:
                st.markdown(f"**{p['nombre']}** — Población: `{p['poblacion']}` | Ubicación: `{p['km']}`")
            with col_p2:
                if st.button("Viajar", key=f"pue_{p['nombre']}"):
                    st.session_state.reino_actual = reino_sel
                    st.session_state.asentamiento_actual = p["nombre"]
                    st.session_state.tipo_asentamiento = f"Pueblo ({p['poblacion']})"
                    st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
                    save_user_data()
                    st.rerun()
    else:
        st.info(f"Estás en **{st.session_state.continente}**. Asentamientos de exploradores de todas las razas.")
        asentamientos_ext = [
            "Bastión de Exploradores Humanos (5.000 hab.)",
            "Enclave Silvano de los Elfos (5.000 hab.)",
            "Fortaleza Avanzada Enana (5.000 hab.)",
            "Campamento de Caza Bestia (5.000 hab.)"
        ]
        sel_ext = st.selectbox("Selecciona Asentamiento Multi-Raza", asentamientos_ext)
        if st.button("Desplazarse al Asentamiento"):
            st.session_state.asentamiento_actual = sel_ext.split(" (")[0]
            st.session_state.tipo_asentamiento = "Asentamiento Fronterizo (5.000 hab.)"
            st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
            save_user_data()
            st.rerun()

# ================= PESTAÑA 4: MOCHILA, GRIMORIO Y PROPIEDADES =================
with tab_bag:
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        st.subheader("🎒 Mochila (0% Soul-Bound)")
        for obj in st.session_state.inventario:
            st.markdown(f"- 📦 **{obj}**")
    with col_b2:
        st.subheader("🏠 Tus Casas y Pisos")
        if st.session_state.propiedades:
            for prop in st.session_state.propiedades:
                st.markdown(f"- 🔑 **{prop}**")
        else:
            st.write("Aún no has comprado propiedades.")
    with col_b3:
        st.subheader("⚡ Grimorio Activo")
        for sk in st.session_state.skills:
            st.markdown(f"- ✨ **{sk}**")

# ================= PESTAÑA 5: LOS 7 CONTINENTES =================
with tab_world:
    st.subheader("🌍 Los 7 Continentes y Niebla de Guerra")
    lista_viaje = obtener_continentes_visibles()
    destino_elegido_raw = st.selectbox("Continentes del Mundo", lista_viaje)
    destino_limpio = destino_elegido_raw.split(" 🌟")[0].split(" 🔓")[0].split(" 🔒")[0]

    if st.button("✈️ Viajar a este Continente", use_container_width=True):
        if "🔒 (Exclusivo Pionero" in destino_elegido_raw:
            st.error("⚠️ Este continente está bajo el periodo de exclusividad de 24 horas.")
        elif "🔒 (Oculto" in destino_elegido_raw:
            st.error("🔒 Este continente está oculto por la niebla de guerra.")
        else:
            st.session_state.continente = destino_limpio
            if destino_limpio == CONTINENTE_INICIAL:
                st.session_state.reino_actual = "Reino Humano de Valoria"
                st.session_state.asentamiento_actual = "Aurelia Capital"
                st.session_state.tipo_asentamiento = "Ciudad (100.000 hab.)"
            else:
                st.session_state.reino_actual = "Territorio de Exploración Multi-Raza"
                st.session_state.asentamiento_actual = "Bastión de Exploradores Humanos"
                st.session_state.tipo_asentamiento = "Asentamiento Fronterizo (5.000 hab.)"
            st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
            save_user_data()
            st.rerun()

# ================= PESTAÑA 6: MISIONES SECRETAS =================
with tab_quests:
    st.subheader("📜 Misiones Secretas y Descubrimiento de Continentes")
    for oculta in CATALOGO_OCULTAS:
        cont_objetivo = oculta["continente_premio"]
        doc_cont = db.collection("world_continents").document(cont_objetivo).get()
        abierto = doc_cont.exists
        estado_txt = f"🔓 Descubierto por: {doc_cont.to_dict().get('pionero')}" if abierto else f"🔒 Continente Oculto | Tier: {oculta['tier']}"
        
        with st.expander(f"Misión Secreta: {oculta['nombre']} ➔ Abre: {cont_objetivo} ({estado_txt})"):
            st.write(f"*Pista:* {oculta['pista']}")
            if not abierto:
                if st.button(f"Completar y Descubrir {cont_objetivo}", key=f"abrir_{oculta['id']}"):
                    db.collection("world_continents").document(cont_objetivo).set({
                        "pionero": st.session_state.hero_name,
                        "fecha": datetime.utcnow()
                    })
                    st.success(f"🌟 ¡Has descubierto **{cont_objetivo}**! 24h de exclusividad.")
                    st.balloons()
                    st.rerun()

# ================= PESTAÑA 7: ENCARGOS P2P =================
with tab_p2p:
    st.subheader("🤝 Tablón P2P (Encargos entre Jugadores)")
    with st.form("form_p2p"):
        titulo = st.text_input("Qué necesitas (Ej: 'Compro Lingote de Mitril Refinado')")
        tipo_meta = st.selectbox("Metal de Recompensa", ["Plata", "Oro", "Cores", "Diamante"])
        cant_meta = st.number_input("Cantidad", min_value=1, value=15)
        if st.form_submit_button("Publicar Encargo") and titulo:
            suficiente = False
            if tipo_meta == "Plata" and st.session_state.plata >= cant_meta:
                st.session_state.plata -= cant_meta; suficiente = True
            elif tipo_meta == "Oro" and st.session_state.oro >= cant_meta:
                st.session_state.oro -= cant_meta; suficiente = True
            elif tipo_meta == "Cores" and st.session_state.cores >= cant_meta:
                st.session_state.cores -= cant_meta; suficiente = True
            elif tipo_meta == "Diamante" and st.session_state.diamante >= cant_meta:
                st.session_state.diamante -= cant_meta; suficiente = True

            if suficiente:
                db.collection("p2p_quests").add({"autor": st.session_state.hero_name, "titulo": titulo, "recompensa_tipo": tipo_meta, "recompensa_cant": cant_meta})
                save_user_data()
                st.success("¡Encargo publicado!")
                st.rerun()

    st.markdown("---")
    docs = db.collection("p2p_quests").stream()
    for doc in docs:
        data = doc.to_dict(); doc_id = doc.id
        col_p1, col_p2 = st.columns([3, 1])
        with col_p1:
            st.markdown(f"**Autor:** `{data.get('autor')}` — **{data.get('titulo')}** (Premio: `{data.get('recompensa_cant')} {data.get('recompensa_tipo')}`)")
        with col_p2:
            if st.button("Completar", key=f"p2p_{doc_id}"):
                tipo, cant = data.get('recompensa_tipo'), data.get('recompensa_cant')
                if tipo == "Plata": st.session_state.plata += cant
                elif tipo == "Oro": st.session_state.oro += cant
                elif tipo == "Cores": st.session_state.cores += cant
                elif tipo == "Diamante": st.session_state.diamante += cant
                db.collection("p2p_quests").document(doc_id).delete()
                save_user_data()
                st.rerun()

st.markdown("---")
st.caption("Snd-Worlds MMORPG Sandbox - Arquitectura Escalable Multi-Jugador")