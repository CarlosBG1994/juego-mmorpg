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

# --- LORE, CLASES, ESTADÍSTICAS Y MONTURAS NATIVAS POR RAZA ---
CONTINENTE_INICIAL = "Continente Primordial (Cuna de las 4 Razas)"

RAZAS_Y_CLASSES = {
    "Humano": {
        "clases": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"],
        "reino_inicio": "Reino Humano de Valoria",
        "bioma": "Llanuras Centrales, Puertos Pesqueros y Colinas",
        "lore": "Gobiernan las llanuras fértiles y la costa comercial de Valoria.",
        "monturas": ["Caballo de Guerra de Valoria", "Carromato Mercante Ligeramente Blindado", "Destrero Real de Jousting"]
    },
    "Elfo": {
        "clases": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento", "Acechador Nocturno", "Mago de Batalla", "Invocador"],
        "reino_inicio": "Reino Silvano de Lothar",
        "bioma": "Bosques Milenarios, Ríos Místicos y Arboledas",
        "lore": "Habitan los bosques milenarios protegidos por la naturaleza.",
        "monturas": ["Ciervo Albino de la Aurora", "Pantera Silvana", "Alce Titán de los Ancestros"]
    },
    "Enano": {
        "clases": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Berserker Rúnico", "Luchador de Puño de Hierro", "Ballestero", "Asesino", "Mago de Batalla", "Invocador"],
        "reino_inicio": "Reino Enano de Khazad",
        "bioma": "Cordilleras Rocosas, Minas Profundas y Fraguas",
        "lore": "Dominan las cumbres montañosas y los yacimientos de metal puro.",
        "monturas": ["Jabalí Acorazado de Runa", "Oso de las Cavernas Profundas", "Carro de Asedio Mecánico a Vapor"]
    },
    "Hombre Bestia": {
        "clases": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Invocador"],
        "reino_inicio": "Reino Tribal de las Estepas",
        "bioma": "Estepas Indómitas, Cañones y Sabanas",
        "lore": "Controlan las vastas sabanas y estepas donde rige la ley del clan.",
        "monturas": ["Huargo Alfa de la Estepa", "León de Guerra de las Sabanas", "Rinoceronte Acorazado Tribal"]
    }
}

ESTADISTICAS_BASE_CLASES = {
    "Caballero": {"str": 15, "int": 5, "agi": 8, "vit": 15, "luk": 5, "hp": 120},
    "Paladín": {"str": 14, "int": 8, "agi": 6, "vit": 16, "luk": 6, "hp": 130},
    "Mago de Batalla": {"str": 4, "int": 18, "agi": 7, "vit": 8, "luk": 8, "hp": 90},
    "Invocador": {"str": 5, "int": 16, "agi": 6, "vit": 10, "luk": 10, "hp": 100},
    "Asesino": {"str": 10, "int": 4, "agi": 18, "vit": 8, "luk": 12, "hp": 95},
    "Explorador": {"str": 9, "int": 6, "agi": 16, "vit": 9, "luk": 10, "hp": 100},
    "Púgil": {"str": 14, "int": 5, "agi": 12, "vit": 12, "luk": 5, "hp": 110},
    "Clérigo": {"str": 8, "int": 14, "agi": 5, "vit": 14, "luk": 9, "hp": 115},
    "Guardabosques": {"str": 10, "int": 6, "agi": 15, "vit": 10, "luk": 9, "hp": 105},
    "Druida": {"str": 6, "int": 15, "agi": 8, "vit": 12, "luk": 9, "hp": 105},
    "Guerrero Pesado": {"str": 18, "int": 4, "agi": 5, "vit": 18, "luk": 5, "hp": 140},
    "Campeón": {"str": 16, "int": 6, "agi": 10, "vit": 14, "luk": 8, "hp": 125},
    "Chamán Primordial": {"str": 6, "int": 16, "agi": 7, "vit": 11, "luk": 10, "hp": 100}
}

SUBFORMAS_BESTIA = ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"]

# --- BASE DE DATOS DE HABILIDADES Y TIERS ---
CATALOGO_HABILIDADES_GLOBAL = {
    "Invocación de Golem de Roca": {
        "clase": "Invocador", "tipo": "Invocación Tanque",
        "tier1": "Invoca un pequeño gólem de piedra.",
        "tier2": "Gólem de Granito Rúnico (Provoca a los enemigos).",
        "tier3": "Titán de Obsidiana Viviente (Escudo masivo)."
    },
    "Espíritu Feral de Manada": {
        "clase": "Invocador", "tipo": "Invocación Ofensiva",
        "tier1": "Invoca 1 lobo espiritual de apoyo.",
        "tier2": "Manada Espectral de 3 lobos veloces.",
        "tier3": "Jauría del Dios Salvaje (Desgarra armadura)."
    },
    "Tótem de Rayo Primordial": {
        "clase": "Invocador", "tipo": "Invocación Elemental",
        "tier1": "Tótem estático de descargas débiles.",
        "tier2": "Tótem de Tormenta Feral (Multiobjetivo).",
        "tier3": "Núcleo del Trueno Ancestral (Tormenta permanente)."
    },
    "Bola de Fuego": {
        "clase": "Mago de Batalla", "tipo": "Magia de Fuego",
        "tier1": "Proyectil ígneo básico.",
        "tier2": "Gran Esfera Ígnea con daño en área (AoE).",
        "tier3": "Meteorito Menor (Incinera la zona)."
    },
    "Muro de Fuego": {
        "clase": "Mago de Batalla", "tipo": "Control de Masas",
        "tier1": "Barrera corta de llamas.",
        "tier2": "Muro circular impenetrable.",
        "tier3": "Muralla Infernal (Quema y paraliza)."
    },
    "Tajo Inicial": {
        "clase": "Caballero / Guerrero", "tipo": "Combate Físico",
        "tier1": "Corte rápido con arma.",
        "tier2": "Doble Tajo Cruzado con sangrado.",
        "tier3": "Corte Ciclón (Golpea en área)."
    }
}

# --- BESTIARIO MASIVO Y JEFES DE ZONA POR REINOS (1 A 60) + ZONA CENTRAL ---
BESTIARIO_ZONAS = {
    "Reino Humano de Valoria": {
        "mobs": [
            {"nombre": "Slime de Rocío", "nivel": 3, "grupo": 5, "hp": 50, "drop": "Gelatina Elemental"},
            {"nombre": "Lobos Esteparios", "nivel": 7, "grupo": 4, "hp": 80, "drop": "Colmillo de Lobo"},
            {"nombre": "Goblins Exploradores", "nivel": 15, "grupo": 5, "hp": 130, "drop": "Daga Herrumbrosa"},
            {"nombre": "Bandidos de los Caminos", "nivel": 22, "grupo": 4, "hp": 180, "drop": "Moneda Oxidada"},
            {"nombre": "Orcos Merodeadores", "nivel": 32, "grupo": 3, "hp": 300, "drop": "Hacha de Orco Tosca"},
            {"nombre": "Plantas Carnívoras Gigantes", "nivel": 38, "grupo": 2, "hp": 380, "drop": "Espora Venenosa"},
            {"nombre": "Ogros de las Colinas", "nivel": 48, "grupo": 2, "hp": 600, "drop": "Garrote de Ogro"},
            {"nombre": "Wyverns de la Cresta", "nivel": 57, "grupo": 1, "hp": 850, "drop": "Aguijón de Wyvern"}
        ],
        "jefes": [
            {"nombre": "Barón Zarek (Forajido)", "nivel": 25, "hp": 450, "drop": "Espada de Oro del Forajido"},
            {"nombre": "Gorthor el Rompecráneos", "nivel": 45, "hp": 900, "drop": "Maza de Guerra Gigante"},
            {"nombre": "Valerius, el Caballero Caído", "nivel": 60, "hp": 1600, "drop": "Coraza de Luz Negra (Jefe Zona)"}
        ]
    },
    "Reino Silvano de Lothar": {
        "mobs": [
            {"nombre": "Slime Musgoso", "nivel": 3, "grupo": 5, "hp": 50, "drop": "Núcleo de Musgo"},
            {"nombre": "Lobos Sombra", "nivel": 8, "grupo": 4, "hp": 90, "drop": "Piel de Sombra"},
            {"nombre": "Plantas Carnívoras Devoradoras", "nivel": 16, "grupo": 3, "hp": 150, "drop": "Liana Resistente"},
            {"nombre": "Goblins del Bosque", "nivel": 24, "grupo": 5, "hp": 200, "drop": "Dardo Envenenado"},
            {"nombre": "Osos Grizzly Silvanos", "nivel": 34, "grupo": 2, "hp": 400, "drop": "Piel de Oso Milenario"},
            {"nombre": "Orcos Cazadores", "nivel": 40, "grupo": 3, "hp": 500, "drop": "Arco de Hueso"},
            {"nombre": "Treants Corruptos", "nivel": 50, "grupo": 2, "hp": 750, "drop": "Madera Ancestral Pura"},
            {"nombre": "Wyverns de las Copas", "nivel": 58, "grupo": 1, "hp": 900, "drop": "Garra de Wyvern Silvano"}
        ],
        "jefes": [
            {"nombre": "Arachne (Madre de Sombras)", "nivel": 28, "hp": 500, "drop": "Diadema de Seda Venenosa"},
            {"nombre": "Karnak (Chamán Orco)", "nivel": 48, "hp": 950, "drop": "Bastón de Huesos Ancestrales"},
            {"nombre": "Malacor (Ent Corrompido)", "nivel": 60, "hp": 1700, "drop": "Núcleo de Madera Eterna (Jefe Zona)"}
        ]
    },
    "Reino Enano de Khazad": {
        "mobs": [
            {"nombre": "Murciélagos de Caverna", "nivel": 4, "grupo": 6, "hp": 60, "drop": "Ala Quiróptera"},
            {"nombre": "Slimes de Mineral", "nivel": 9, "grupo": 4, "hp": 95, "drop": "Residuo Metálico"},
            {"nombre": "Goblins Mineros", "nivel": 18, "grupo": 5, "hp": 170, "drop": "Piqueta Rota"},
            {"nombre": "Huargos de las Cavernas", "nivel": 26, "grupo": 3, "hp": 240, "drop": "Colmillo de Huargo"},
            {"nombre": "Orcos Berserkers", "nivel": 35, "grupo": 3, "hp": 450, "drop": "Mineral de Hierro Bruto"},
            {"nombre": "Plantas Subterráneas Luz", "nivel": 42, "grupo": 3, "hp": 520, "drop": "Bulbo Luminoso"},
            {"nombre": "Ogros de Profundidad", "nivel": 52, "grupo": 1, "hp": 800, "drop": "Núcleo de Granito"},
            {"nombre": "Dragones Menores de Magma", "nivel": 59, "grupo": 1, "hp": 1000, "drop": "Escama de Magma"}
        ],
        "jefes": [
            {"nombre": "Grimgor Manoférrea", "nivel": 30, "hp": 550, "drop": "Casco Rúnico de Cobalto"},
            {"nombre": "Vrakthor el Desollador", "nivel": 50, "hp": 1100, "drop": "Piel de Huargo Alfa"},
            {"nombre": "Ignisara (Madre del Magma)", "nivel": 60, "hp": 1800, "drop": "Escama de Magma Pura (Jefe Zona)"}
        ]
    },
    "Reino Tribal de las Estepas": {
        "mobs": [
            {"nombre": "Hienas de la Sabana", "nivel": 5, "grupo": 5, "hp": 70, "drop": "Piel Desértica"},
            {"nombre": "Slimes de Polvo", "nivel": 10, "grupo": 4, "hp": 100, "drop": "Residuo Arenoso"},
            {"nombre": "Goblins Jinetes", "nivel": 20, "grupo": 4, "hp": 190, "drop": "Látigo de Cuero"},
            {"nombre": "Bandidos Nómadas", "nivel": 27, "grupo": 3, "hp": 260, "drop": "Cuchillo Nómada"},
            {"nombre": "Huargos de la Estepa", "nivel": 36, "grupo": 4, "hp": 480, "drop": "Piel de Huargo Veloz"},
            {"nombre": "Orcos Jinetes de Guerra", "nivel": 44, "grupo": 2, "hp": 600, "drop": "Insignia Orca"},
            {"nombre": "Ogros Nómadas", "nivel": 54, "grupo": 2, "hp": 850, "drop": "Maza de Pedernal"},
            {"nombre": "Wyverns de Tormenta", "nivel": 60, "grupo": 1, "hp": 1100, "drop": "Núcleo Eléctrico"}
        ],
        "jefes": [
            {"nombre": "Kesh Corazón de León", "nivel": 32, "hp": 600, "drop": "Garras de Acero Tribal"},
            {"nombre": "Thorgar Rompehuesos", "nivel": 52, "hp": 1200, "drop": "Maza del Gigante"},
            {"nombre": "Typhón (Señor Tormentas)", "nivel": 60, "hp": 1900, "drop": "Núcleo de Tormenta (Jefe Zona)"}
        ]
    },
    "Zona Central Unificada (Nivel 60+ / Confluencia Global)": {
        "mobs": [
            {"nombre": "Titán del Nexo Primordial", "nivel": 65, "grupo": 3, "hp": 1500, "drop": "Fragmento de Núcleo Puro"},
            {"nombre": "Avatar del Vacío Abisal", "nivel": 70, "grupo": 1, "hp": 2500, "drop": "Esencia de Vacío (Diamante)"}
        ],
        "jefes": [
            {"nombre": "SND-OVERLORD (Jefe Supremo)", "nivel": 75, "hp": 4000, "drop": "Corona del Nexo Primordial"}
        ]
    }
}

CONTINENTES OFICIALES = {
    CONTINENTE_INICIAL: {"visible_desde_inicio": True, "tipo": "Continente Inicial (Límite Niv. 100)", "max_nivel": 100},
    "Archipiélago de los Vientos": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Límite Niv. 150)", "max_nivel": 150},
    "Continente Abisal de los Demonios": {"visible_desde_inicio": False, "tipo": "Continente Oculto (Límite Niv. 200)", "max_nivel": 200},
    "El Núcleo Central de Comercio": {"visible_desde_inicio": False, "tipo": "Nexo Global (Límite Niv. 300)", "max_nivel": 300}
}

CATALOGO_EDIFICIOS = {
    "Gremio de Aventureros": {
        "desc": "Tablón oficial de contratos, misiones secundarias de caza de jefes y grimorios.",
        "items": [
            {"id": "inv_golem", "nombre": "Grimorio: Invocación de Golem de Roca", "tipo": "Habilidad Invocador", "tier": "Raro", "metal": "Cores", "precio": 4},
            {"id": "inv_lobo", "nombre": "Grimorio: Espíritu Feral de Manada", "tipo": "Habilidad Invocador", "tier": "Raro", "metal": "Plata", "precio": 50},
            {"id": "muro_fuego", "nombre": "Grimorio: Muro de Fuego", "tipo": "Habilidad Mago", "tier": "Épico", "metal": "Oro", "precio": 5}
        ]
    }
}

CATALOGO_OCULTAS = [
    {"id": "abrir_vientos", "nombre": "La Brújula de las Tormentas", "continente_premio": "Archipiélago de los Vientos", "tier": "Raro", "pista": "Explora las costas del Continente Primordial."},
    {"id": "abrir_demonios", "nombre": "El Portal del Abismo", "continente_premio": "Continente Abisal de los Demonios", "tier": "Épico", "pista": "Reúne Cores oscuros y rompe el sello volcánico."}
]

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
    ("habilidades_equipadas", ["Invocación de Golem de Roca", "Bola de Fuego", "Tajo Inicial", "", ""]),
    ("grimorio_inventario", ["Invocación de Golem de Roca", "Bola de Fuego", "Tajo Inicial", "Muro de Fuego"]),
    ("habilidades_fusionadas", []),
    ("inventario", ["Ropa de Viajero", "Raciones de Pan"]),
    ("montura_activa", "Ninguna"),
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
            "has_character": st.session_state.has_character
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= PANTALLA DE LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Bestiario 1-60 | Monturas por Raza | Atributos Libres | Fusión Nivel 40+</p>", unsafe_allow_html=True)
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
                    st.session_state.habilidades_equipadas = data.get("habilidades_equipadas", ["Invocación de Golem de Roca", "Bola de Fuego", "Tajo Inicial", "", ""])
                    st.session_state.grimorio_inventario = data.get("grimorio_inventario", ["Invocación de Golem de Roca", "Bola de Fuego"])
                    st.session_state.habilidades_fusionadas = data.get("habilidades_fusionadas", [])
                    st.session_state.montura_activa = data.get("montura_activa", "Ninguna")
                    st.session_state.has_character = data.get("has_character", True)
                else:
                    st.session_state.hero_name = email.split("@")[0]
                    st.session_state.has_character = False
                
                st.session_state.logged_in = True
                st.rerun()
    st.stop()

# ================= PANTALLA DE CREACIÓN DE PERSONAJE =================
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
        st.session_state.asentamiento_actual = f"Capital de {st.session_state.raza}"
        
        base_stats = ESTADISTICAS_BASE_CLASES.get(st.session_state.clase, {"str": 10, "int": 10, "agi": 10, "vit": 10, "luk": 10, "hp": 100})
        st.session_state.str = base_stats["str"]
        st.session_state.int = base_stats["int"]
        st.session_state.agi = base_stats["agi"]
        st.session_state.vit = base_stats["vit"]
        st.session_state.luk = base_stats["luk"]
        st.session_state.max_hp = base_stats["hp"]
        st.session_state.hero_hp = base_stats["hp"]

        st.info(f"🐎 **Monturas Nativas Exclusivas:** {', '.join(info_raza['monturas'])}\n\n*{info_raza['lore']}*")

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
st.sidebar.markdown(f"🏰 **Reino:** `{st.session_state.reino_actual}`")

if st.sidebar.button("🚪 Cerrar Sesión"):
    save_user_data()
    st.session_state.logged_in = False
    st.session_state.has_character = False
    st.rerun()

# Pestañas principales
tab_canvas, tab_stats, tab_skills, tab_edificio, tab_viaje_local, tab_bag, tab_world, tab_quests, tab_p2p = st.tabs([
    "🎮 Motor PvE & Canvas",
    "📊 Atributos & Nivel",
    "✨ Grimorio & Fusión",
    "🏪 Tienda & Caza",
    "🗺️ Bestiario 1-60",
    "🎒 Mochila & Monturas",
    "🌍 Continentes",
    "📜 Misiones",
    "🤝 Encargos P2P"
])

# ================= PESTAÑA 1: MOTOR PVE (HTML5 CANVAS) =================
with tab_canvas:
    col_top1, col_top2 = st.columns([2.5, 1.5])
    with col_top1:
        st.subheader(f"📍 {st.session_state.asentamiento_actual} — Plano: {st.session_state.hero_name}")
    with col_top2:
        if st.session_state.plano_vista == "Exterior (Puertas del Asentamiento)":
            if st.button("🚪 Cruzar Murallas a Zonas de Caza (PvE)", use_container_width=True, type="primary"):
                st.session_state.plano_vista = "Zona de Caza y Combate"
                st.rerun()
        else:
            if st.button("🏰 Volver al Refugio de la Ciudad", use_container_width=True):
                st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
                st.rerun()

    st.markdown("#### ⚡ Barra de Habilidades Activas (5 Slots)")
    cols_sk = st.columns(5)
    for i, sk_name in enumerate(st.session_state.habilidades_equipadas):
        with cols_sk[i]:
            if sk_name:
                tier_act = "Tier I"
                if st.session_state.hero_level >= 30: tier_act = "Tier III"
                elif st.session_state.hero_level >= 15: tier_act = "Tier II"
                st.button(f"[{i+1}] {sk_name}\n({tier_act})", key=f"btn_sk_{i}")
            else:
                st.button(f"[{i+1}] Vacío", disabled=True, key=f"btn_sk_empty_{i}")

    # Renderizador visual en Canvas
    es_caza = "true" if "Caza" in st.session_state.plano_vista else "false"
    reino_actual_str = st.session_state.reino_actual
    hero_name_str = st.session_state.hero_name
    hero_level_val = st.session_state.hero_level

    datos_reino_actual = BESTIARIO_ZONAS.get(reino_actual_str, BESTIARIO_ZONAS["Reino Humano de Valoria"])
    mobs_reino_list = datos_reino_actual["mobs"]
    jefes_reino_list = datos_reino_actual["jefes"]

    mobs_js_list = str([{
        "nombre": m["nombre"], "nivel": m["nivel"], "grupo": m["grupo"], 
        "hp": m["hp"], "drop": m["drop"], "tipo": "mob"
    } for m in mobs_reino_list] + [{
        "nombre": j["nombre"], "nivel": j["nivel"], "grupo": 1, 
        "hp": j["hp"], "drop": j["drop"], "tipo": "jefe"
    } for j in jefes_reino_list])

    game_html = f"""
    <div style="text-align: center; background: #111; padding: 10px; border-radius: 10px; border: 2px solid #ffaa00;">
        <canvas id="gameCanvas" width="820" height="480" style="background: #152216; border-radius: 8px; display: block; margin: 0 auto; max-width: 100%;"></canvas>
        <p id="hudInfo" style="color: #ffd700; margin-top: 8px; font-weight: bold; font-size: 14px;">Explora el terreno o enfréntate a las manadas y Jefes de Zona.</p>
    </div>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const esCaza = {es_caza};
        const worldW = esCaza ? 1600 : 820;
        const worldH = esCaza ? 1200 : 480;
        let player = {{ x: worldW / 2, y: worldH / 2, radius: 14, speed: 5, color: "#ffaa00" }};
        let keys = {{}};
        const entities = {mobs_js_list};

        window.addEventListener('keydown', (e) => {{ keys[e.key.toLowerCase()] = true; }});
        window.addEventListener('keyup', (e) => {{ keys[e.key.toLowerCase()] = false; }});

        function actualizar() {{
            if (keys['w'] || keys['arrowup']) player.y -= player.speed;
            if (keys['s'] || keys['arrowdown']) player.y += player.speed;
            if (keys['a'] || keys['arrowleft']) player.x -= player.speed;
            if (keys['d'] || keys['arrowright']) player.x += player.speed;
            if (player.x < player.radius) player.x = player.radius;
            if (player.x > worldW - player.radius) player.x = worldW - player.radius;
            if (player.y < player.radius) player.y = player.radius;
            if (player.y > worldH - player.radius) player.y = worldH - player.radius;
        }}

        function dibujar() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.save();
            if (esCaza) {{
                let camX = Math.max(0, Math.min(player.x - canvas.width / 2, worldW - canvas.width));
                let camY = Math.max(0, Math.min(player.y - canvas.height / 2, worldH - canvas.height));
                ctx.translate(-camX, -camY);
                ctx.fillStyle = "#1e3020";
                ctx.fillRect(0, 0, worldW, worldH);
            }} else {{
                ctx.fillStyle = "#1b3a24";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            }}
            ctx.beginPath();
            ctx.arc(player.x, player.y, player.radius, 0, Math.PI * 2);
            ctx.fillStyle = player.color;
            ctx.fill();
            ctx.lineWidth = 2;
            ctx.strokeStyle = "#fff";
            ctx.stroke();
            ctx.closePath();
            ctx.restore();
        }}

        function loop() {{
            actualizar();
            dibujar();
            requestAnimationFrame(loop);
        }}
        loop();
    </script>
    """
    st.components.v1.html(game_html, height=520)

# ================= PESTAÑA 2: ATRIBUTOS, PUNTOS LIBRES Y NIVELES =================
with tab_stats:
    st.subheader("📊 Panel de Atributos y Progresión de Nivel")
    st.write(f"⭐ **Nivel Actual:** `{st.session_state.hero_level}` | 🎁 **Puntos Libres Disponibles:** `{st.session_state.puntos_libres}`")
    st.info("Cada subida de nivel otorga **+5 puntos libres** para distribuir en tus atributos y **+10 HP máximo**.")

    col_st1, col_st2 = st.columns(2)
    with col_st1:
        st.markdown("### 🧬 Atributos Principales")
        st.write(f"💪 **Fuerza (STR):** {st.session_state.str}")
        st.write(f"🔮 **Inteligencia (INT):** {st.session_state.int}")
        st.write(f"⚡ **Agilidad (AGI):** {st.session_state.agi}")
        st.write(f"❤️ **Vitalidad (VIT):** {st.session_state.vit}")
        st.write(f"🍀 **Suerte (LUK):** {st.session_state.luk}")

        if st.session_state.puntos_libres > 0:
            st.markdown("---")
            st.markdown("#### ➕ Distribuir Puntos Libres")
            attr_elegido = st.selectbox("Selecciona Atributo", ["Fuerza (STR)", "Inteligencia (INT)", "Agilidad (AGI)", "Vitalidad (VIT)", "Suerte (LUK)"])
            cant_a_subir = st.number_input("Cantidad", min_value=1, max_value=st.session_state.puntos_libres, value=1)
            
            if st.button("Confirmar Asignación"):
                st.session_state.puntos_libres -= cant_a_subir
                if "Fuerza" in attr_elegido: st.session_state.str += cant_a_subir
                elif "Inteligencia" in attr_elegido: st.session_state.int += cant_a_subir
                elif "Agilidad" in attr_elegido: st.session_state.agi += cant_a_subir
                elif "Vitalidad" in attr_elegido: 
                    st.session_state.vit += cant_a_subir
                    st.session_state.max_hp += (cant_a_subir * 5)
                    st.session_state.hero_hp += (cant_a_subir * 5)
                elif "Suerte" in attr_elegido: st.session_state.luk += cant_a_subir
                save_user_data()
                st.success("¡Atributos mejorados con éxito!")
                st.rerun()

    with col_st2:
        st.markdown("### 🧪 Simulador de Experiencia y Niveles")
        if st.button("✨ Simular Subida de Nivel (+1 Nivel)", use_container_width=True):
            st.session_state.hero_level += 1
            st.session_state.puntos_libres += 5
            st.session_state.max_hp += 10
            st.session_state.hero_hp = st.session_state.max_hp
            save_user_data()
            st.success(f"¡Has subido al **Nivel {st.session_state.hero_level}**! Has ganado 5 puntos libres y +10 HP.")
            st.rerun()

# ================= PESTAÑA 3: GRIMORIO Y FUSIÓN (NIVEL 40+) =================
with tab_skills:
    st.subheader("✨ Sistema de Habilidades (1,870 Skills) y Fusión Nivel 40+")
    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("### 📋 Tus 5 Ranuras Activas")
        for idx in range(5):
            actual = st.session_state.habilidades_equipadas[idx]
            nueva_sel = st.selectbox(f"Ranura Activa #{idx+1}", ["(Vacío)"] + st.session_state.grimorio_inventario, index=(st.session_state.grimorio_inventario.index(actual) + 1) if actual in st.session_state.grimorio_inventario else 0, key=f"slot_eq_{idx}")
            val_asignar = "" if nueva_sel == "(Vacío)" else nueva_sel
            if st.session_state.habilidades_equipadas[idx] != val_asignar:
                st.session_state.habilidades_equipadas[idx] = val_asignar
                save_user_data()

        st.markdown("### 🧬 Habilidades Fusionadas")
        if st.session_state.habilidades_fusionadas:
            for fus in st.session_state.habilidades_fusionadas:
                st.success(f"🌟 **{fus['nombre']}** (*{fus['padre1']}* + *{fus['padre2']}*)")
        else:
            st.write("Ninguna fusión realizada aún.")

    with col_s2:
        st.markdown("### ⚗️ Laboratorio de Fusión (Nivel 40+)")
        if st.session_state.hero_level >= 40:
            f_p1 = st.selectbox("Primera Habilidad", st.session_state.grimorio_inventario, key="fp1")
            f_p2 = st.selectbox("Segunda Habilidad", st.session_state.grimorio_inventario, key="fp2")
            nombre_custom = st.text_input("Nombre del Super-Poder Híbrido (Ej: Torreta de Fuego)")
            
            if st.button("✨ Fusionar Habilidades") and nombre_custom and f_p1 != f_p2:
                nueva_fusion = {"nombre": nombre_custom, "padre1": f_p1, "padre2": f_p2}
                st.session_state.habilidades_fusionadas.append(nueva_fusion)
                st.session_state.grimorio_inventario.append(nombre_custom)
                save_user_data()
                st.success(f"¡Has creado la habilidad **{nombre_custom}**!")
                st.rerun()
        else:
            st.warning(f"🔒 Se desbloquea al **Nivel 40**. (Tu nivel: {st.session_state.hero_level})")

# ================= PESTAÑA 4: TIENDA =================
with tab_edificio:
    st.subheader("🏪 Gremio de Aventureros — Grimorios")
    for item in CATALOGO_EDIFICIOS["Gremio de Aventureros"]["items"]:
        col_i1, col_i3 = st.columns([3, 1])
        with col_i1:
            st.markdown(f"**{item['nombre']}** — *{item['tipo']}* (Coste: {item['precio']} {item['metal']})")
        with col_i3:
            if st.button("Comprar", key=f"buy_{item['id']}"):
                sk_limpia = item['nombre'].split(": ")[-1]
                if sk_limpia not in st.session_state.grimorio_inventario:
                    st.session_state.grimorio_inventario.append(sk_limpia)
                    save_user_data()
                    st.success(f"¡Aprendido **{sk_limpia}**!")
                    st.rerun()

# ================= PESTAÑA 5: BESTIARIO 1-60 =================
with tab_viaje_local:
    st.subheader("🗺️ Bestiario Masivo y Jefes de Zona (Niveles 1 a 60)")
    reino_sel = st.selectbox("Selecciona Reino / Región", list(BESTIARIO_ZONAS.keys()))
    datos_r = BESTIARIO_ZONAS[reino_sel]

    st.markdown(f"### 🐺 Monstruos Comunes: `{reino_sel}`")
    for mob in datos_r["mobs"]:
        st.markdown(f"- **{mob['nombre']}** (Nivel `{mob['nivel']}`) — Grupo: `{mob['grupo']}` | HP: `{mob['hp']}` | Loot: *{mob['drop']}*")

    st.markdown(f"### 👑 Jefes de Zona (World Bosses)")
    for jefe in datos_r["jefes"]:
        st.markdown(f"- 🔴 **{jefe['nombre']}** (Nivel `{jefe['nivel']}`) — HP: `{jefe['hp']}` | Botín: *{jefe['drop']}*")

    if st.button("🚀 Desplazarse a Cazar en este Reino", use_container_width=True):
        st.session_state.reino_actual = reino_sel
        st.session_state.asentamiento_actual = f"Caza en {reino_sel}"
        save_user_data()
        st.success(f"Te has desplazado a **{reino_sel}**.")
        st.rerun()

# ================= PESTAÑA 6: MOCHILA Y MONTURAS =================
with tab_bag:
    st.subheader("🎒 Mochila, Inventario y Sistema de Monturas")
    col_m1, col_m2 = st.columns(2)
    
    with col_m1:
        st.markdown("### 🐎 Tus Monturas Nativas")
        monturas_raza = RAZAS_Y_CLASSES[st.session_state.raza]["monturas"]
        for mon in monturas_raza:
            es_activa = " ⭐ (Activa)" if st.session_state.montura_activa == mon else ""
            st.markdown(f"- 🐎 **{mon}**{es_activa}")
            if st.button(f"Montar {mon}", key=f"montar_{mon}"):
                st.session_state.montura_activa = mon
                save_user_data()
                st.success(f"¡Has montado a **{mon}**! Velocidad de desplazamiento aumentada.")
                st.rerun()

    with col_m2:
        st.markdown("### 📦 Objetos y Grimorios")
        st.write("Inventario:", st.session_state.inventario)
        st.write("Grimorios:", st.session_state.grimorio_inventario)

# ================= PESTAÑA 7: CONTINENTES Y LÍMITES DE NIVEL =================
with tab_world:
    st.subheader("🌍 Los Continentes y Escalado (+50 Niveles por Continente)")
    for cont, info in CONTINENTES_OFICIALES.items():
        st.markdown(f"- **{cont}** — *{info['tipo']}*")

# ================= PESTAÑA 8: MISIONES SECRETAS =================
with tab_quests:
    st.subheader("📜 Misiones Secretas")
    for oculta in CATALOGO_OCULTAS:
        st.markdown(f"**{oculta['nombre']}** ➔ Abre: `{oculta['continente_premio']}` (*{oculta['pista']}*)")

# ================= PESTAÑA 9: ENCARGOS P2P =================
with tab_p2p:
    st.subheader("🤝 Tablón P2P entre Jugadores")
    docs = db.collection("p2p_quests").stream()
    for doc in docs:
        data = doc.to_dict()
        st.markdown(f"**Autor:** `{data.get('autor')}` — **{data.get('titulo')}** (Premio: `{data.get('recompensa_cant')} {data.get('recompensa_tipo')}`)")

st.markdown("---")
st.caption("Snd-Worlds MMORPG Sandbox - Versión Masiva Completa")