import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import random

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

# --- ESTRUCTURA OFICIAL DE CLASES, RAZAS Y HABILIDADES POR TIERS ---
RAZAS_Y_CLASES = {
    "Humano": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"],
    "Elfo": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento", "Acechador Nocturno", "Mago de Batalla", "Invocador"],
    "Enano": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Berserker Rúnico", "Luchador de Puño de Hierro", "Ballestero", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"],
    "Hombre Bestia": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"]
}

SUBFORMAS_BESTIA = ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"]

CONTINENTES_MUNDO = [
    "Continente Humano (Región del Miasma)",
    "Dominio Silvano de los Elfos",
    "Cordillera e Imperios Enanos",
    "Tierras Salvajes de los Hombres Bestia",
    "Archipiélago de los Cielos Abiertos",
    "Las Fronteras del Olvido",
    "El Núcleo Central de Comercio"
]

# Catálogo de habilidades por Tiers
CATALOGO_HABILIDADES = [
    {"nombre": "Golpe Base", "tier": "Común", "tipo": "Tienda / Inicial", "desc": "Ataque físico directo equilibrado."},
    {"nombre": "Tajo Inicial", "tier": "Común", "tipo": "Tienda / Inicial", "desc": "Corte rápido que desestabiliza levemente."},
    {"nombre": "Combo Rápido de Púgil", "tier": "Raro", "tipo": "Misión de facción", "desc": "Ráfaga de golpes a velocidad vertiginosa."},
    {"nombre": "Escudo Rúnico de Asedio", "tier": "Raro", "tipo": "Tienda de Metales", "desc": "Barrera defensiva basada en Cores."},
    {"nombre": "Furia del Berserker", "tier": "Épico", "tipo": "Cofre de Mazmorra", "desc": "Incrementa masivamente el daño físico a costa de salud."},
    {"nombre": "Invocación del Vicio Silvano", "tier": "Épico", "tipo": "Misión Oculta", "desc": "Invoca espíritus del bosque para flanquear."},
    {"nombre": "Juicio del Miasma Divino", "tier": "Legendario", "tipo": "Incursión Mundial", "desc": "Haz de energía pura adaptado al continente humano."},
    {"nombre": "Trascendencia de los 4 Metales", "tier": "Místico", "tipo": "Hallazgo Mundial Prohibido", "desc": "Canaliza el poder absoluto de Cores, Plata, Oro y Diamante."}
]

# --- ESTADO DE SESIÓN ---
for key, default in [
    ("logged_in", False), ("user_email", ""), ("hero_name", ""),
    ("raza", "Humano"), ("subforma", "Hombre Lobo"), ("genero", "Hombre"),
    ("clase", "Caballero"), ("continente", CONTINENTES_MUNDO[0]),
    ("hero_level", 1), ("hero_hp", 100), ("hero_xp", 0),
    ("cores", 5), ("plata", 100), ("oro", 10), ("diamante", 1),
    ("skills", ["Golpe Base", "Tajo Inicial"]), ("has_character", False),
    ("mazmorra_reclamada", "Ninguna"), ("montura_activa", "A Pata (Sin Montura)")
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
            "hero_level": st.session_state.hero_level,
            "hero_hp": st.session_state.hero_hp,
            "hero_xp": st.session_state.hero_xp,
            "cores": st.session_state.cores,
            "plata": st.session_state.plata,
            "oro": st.session_state.oro,
            "diamante": st.session_state.diamante,
            "skills": st.session_state.skills,
            "has_character": st.session_state.has_character,
            "mazmorra_reclamada": st.session_state.mazmorra_reclamada,
            "montura_activa": st.session_state.montura_activa
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= PANTALLA DE LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>8.5M km² de tierra | 1.55M km² de océanos | 7 Continentes | Cero Objetos Ligados al Alma</p>", unsafe_allow_html=True)
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
                    st.session_state.continente = data.get("continente", CONTINENTES_MUNDO[0])
                    st.session_state.hero_level = data.get("hero_level", 1)
                    st.session_state.hero_hp = data.get("hero_hp", 100)
                    st.session_state.hero_xp = data.get("hero_xp", 0)
                    st.session_state.cores = data.get("cores", 5)
                    st.session_state.plata = data.get("plata", 100)
                    st.session_state.oro = data.get("oro", 10)
                    st.session_state.diamante = data.get("diamante", 1)
                    st.session_state.skills = data.get("skills", ["Golpe Base"])
                    st.session_state.has_character = data.get("has_character", True)
                    st.session_state.mazmorra_reclamada = data.get("mazmorra_reclamada", "Ninguna")
                    st.session_state.montura_activa = data.get("montura_activa", "A Pata (Sin Montura)")
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
        st.session_state.raza = st.selectbox("Raza", list(RAZAS_Y_CLASES.keys()))
        
        if st.session_state.raza == "Hombre Bestia":
            st.session_state.subforma = st.selectbox("Sub-forma de Bestia", SUBFORMAS_BESTIA)
        
        st.session_state.genero = st.selectbox("Género", ["Hombre", "Mujer"])
        
    with col_c2:
        clases_disponibles = RAZAS_Y_CLASES[st.session_state.raza]
        st.session_state.clase = st.selectbox("Clase Oficial", clases_disponibles)
        st.session_state.continente = st.selectbox("Continente de Inicio", CONTINENTES_MUNDO)
        
        if st.session_state.raza == "Humano":
            st.info("⚠️ **Lore del Continente Humano:** Contiene las zonas de Miasma. Requiere misiones ocultas y objeto de supervivencia.")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 ¡Entrar al Mundo Abierto!", use_container_width=True):
        if st.session_state.hero_name:
            st.session_state.has_character = True
            save_user_data()
            st.rerun()
        else:
            st.warning("Por favor, asigna un nombre a tu héroe.")
    st.stop()

# ================= JUEGO PRINCIPAL =================
st.sidebar.header(f"🛡️ {st.session_state.hero_name}")
st.sidebar.write(f"**Raza:** {st.session_state.raza}" + (f" ({st.session_state.subforma})" if st.session_state.raza == "Hombre Bestia" else ""))
st.sidebar.write(f"**Clase:** {st.session_state.clase} | **Género:** {st.session_state.genero}")
st.sidebar.write(f"**Nivel:** {st.session_state.hero_level} | **XP:** {st.session_state.hero_xp}/100")
st.sidebar.write(f"❤️ **Salud:** {st.session_state.hero_hp}/100")
st.sidebar.markdown(f"📍 **Continente Actual:** \n`{st.session_state.continente}`")
st.sidebar.markdown(f"🏰 **Mazmorra de Clan:** \n`{st.session_state.mazmorra_reclamada}`")
st.sidebar.markdown(f"🐎 **Montura:** \n`{st.session_state.montura_activa}`")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Inventario de Metales")
st.sidebar.markdown(
    f"- 💠 **Cores:** `{st.session_state.cores}`\n"
    f"- 🥈 **Plata:** `{st.session_state.plata}`\n"
    f"- 🪙 **Oro:** `{st.session_state.oro}`\n"
    f"- 💎 **Diamante:** `{st.session_state.diamante}`"
)

if st.sidebar.button("🚪 Cerrar Sesión"):
    save_user_data()
    st.session_state.logged_in = False
    st.session_state.has_character = False
    st.rerun()

# Pestañas principales incluyendo la nueva de Monturas
tab_play, tab_skills, tab_world, tab_dungeons, tab_mounts, tab_market = st.tabs([
    "🎮 Jugar y Explorar", 
    "⚡ Grimorio (Tiers)", 
    "🌍 Mapa de los 7 Continentes", 
    "🏰 Mazmorras y Gremios",
    "🐎 Monturas y Bonus",
    "🏦 Mercado Abierto"
])

with tab_play:
    st.subheader(f"Región: {st.session_state.continente}")
    st.info("Explora el vasto territorio de 8.5 millones de km², enfréntate a amenazas y recolecta metales preciosos para tu progreso.")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⛏️ Explorar y Recolectar", use_container_width=True):
            metal = random.choice(["Cores", "Plata", "Oro"])
            cant = random.randint(1, 4)
            if metal == "Cores": st.session_state.cores += cant
            elif metal == "Plata": st.session_state.plata += cant
            elif metal == "Oro": st.session_state.oro += cant
            
            st.session_state.hero_xp += 25
            if st.session_state.hero_xp >= 100:
                st.session_state.hero_level += 1
                st.session_state.hero_xp = 0
                st.balloons()
            save_user_data()
            st.success(f"¡Has encontrado `{cant}` de **{metal}** en {st.session_state.continente}!")

    with col2:
        if st.button("⚔️ Enfrentar Amenaza", use_container_width=True):
            reward = random.randint(25, 60)
            st.session_state.plata += reward
            st.session_state.hero_xp += 35
            if st.session_state.hero_xp >= 100:
                st.session_state.hero_level += 1
                st.session_state.hero_xp = 0
                st.balloons()
            save_user_data()
            st.info(f"¡Victoria en combate! Obtuviste `{reward}` de Plata.")

    with col3:
        if st.button("🛡️ Descansar y Recuperar", use_container_width=True):
            st.session_state.hero_hp = 100
            save_user_data()
            st.success("Salud restaurada al máximo.")

with tab_skills:
    st.subheader("⚡ Grimorio y Sistema de 500+ Habilidades Activas")
    st.write("Gestiona tus técnicas aprendidas y descubre nuevas habilidades clasificadas por sus **5 Tiers de Rareza** y métodos de adquisición.")

    st.markdown("### 🎒 Tus Habilidades Aprendidas")
    for sk in st.session_state.skills:
        st.markdown(f"- ✨ **{sk}**")
        
    st.markdown("---")
    st.markdown("### 📜 Mercado y Registro de Habilidades por Tier")
    
    catalogo_nombres = [h["nombre"] for h in CATALOGO_HABILIDADES if h["nombre"] not in st.session_state.skills]
    
    if catalogo_nombres:
        sk_select = st.selectbox("Selecciona una habilidad para desbloquear", catalogo_nombres)
        h_info = next(h for h in CATALOGO_HABILIDADES if h["nombre"] == sk_select)
        
        st.info(f"**Tier:** `{h_info['tier']}` | **Adquisición:** `{h_info['tipo']}`\n\n*{h_info['desc']}*")
        
        if st.button("📥 Aprender Habilidad"):
            st.session_state.skills.append(sk_select)
            save_user_data()
            st.success(f"¡Has aprendido la habilidad **{sk_select}** ({h_info['tier']})!")
            st.rerun()
    else:
        st.success("¡Has desbloqueado todas las habilidades del catálogo base actual!")

with tab_world:
    st.subheader("🌍 Estado de los 7 Continentes del Mundo Abierto")
    st.write("Escala global del sandbox: **8.5M km² de tierra** y **1.55M km² de océanos** con economía abierta de 4 metales.")
    
    for idx, cont in enumerate(CONTINENTES_MUNDO, 1):
        is_current = (cont == st.session_state.continente)
        actual_label = "📍 **(Te encuentras aquí)**" if is_current else ""
        
        if "Humano" in cont:
            st.markdown(f"**{idx}. {cont}** {actual_label}\n> *Lore:* Región principal con zonas de Miasma tóxico. Requiere misiones ocultas y objeto de supervivencia.")
        else:
            st.markdown(f"**{idx}. {cont}** {actual_label}")

    st.markdown("---")
    st.subheader("✈️ Sistema de Viaje Continental")
    nuevo_cont = st.selectbox("Selecciona el Continente de Destino", CONTINENTES_MUNDO, key="select_viaje")
    
    if st.button("✈️ Viajar a este Continente", use_container_width=True):
        if nuevo_cont != st.session_state.continente:
            st.session_state.continente = nuevo_cont
            save_user_data()
            st.success(f"¡Has viajado con éxito a **{nuevo_cont}**!")
            st.rerun()
        else:
            st.info("Ya te encuentras en este continente.")

with tab_dungeons:
    st.subheader("🏰 Mazmorras Estacionales y Conquista de Gremios")
    st.info("Reclama mazmorras en los continentes mediante tributos de metales y defiende tu territorio frente a otros gremios.")
    
    st.markdown(f"**Mazmorra Actual de tu Clan / Personaje:** `{st.session_state.mazmorra_reclamada}`")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("### 🏔️ Bastión del Miasma Profundo")
        st.write("Ubicación: Continente Humano")
        st.write("Coste de Reclamación: `2 Oro` + `20 Cores`")
        if st.button("Reclamar Bastión del Miasma"):
            if st.session_state.oro >= 2 and st.session_state.cores >= 20:
                st.session_state.oro -= 2
                st.session_state.cores -= 20
                st.session_state.mazmorra_reclamada = "Bastión del Miasma Profundo"
                save_user_data()
                st.success("¡Mazmorra reclamada con éxito para tu clan!")
                st.rerun()
            else:
                st.error("Recursos insuficientes (Requiere 2 Oro y 20 Cores).")

    with col_d2:
        st.markdown("### 🐉 Guarida del Dragón de Diamante")
        st.write("Ubicación: Las Fronteras del Olvido")
        st.write("Coste de Reclamación: `1 Diamante` + `50 Plata`")
        if st.button("Reclamar Guarida del Dragón"):
            if st.session_state.diamante >= 1 and st.session_state.plata >= 50:
                st.session_state.diamante -= 1
                st.session_state.plata -= 50
                st.session_state.mazmorra_reclamada = "Guarida del Dragón de Diamante"
                save_user_data()
                st.success("¡Mazmorra reclamada con éxito para tu clan!")
                st.rerun()
            else:
                st.error("Recursos insuficientes (Requiere 1 Diamante y 50 Plata).")

with tab_mounts:
    st.subheader("🐎 Establo y Sistema de Monturas")
    st.info("Equipa monturas para acelerar la exploración en los 8.5 millones de km² del mundo abierto.")

    monturas_disponibles = [
        {"nombre": "A Pata (Sin Montura)", "coste": "Gratis", "bono": "Velocidad Base (1x)"},
        {"nombre": "Caballo de Guerra de Infantería", "coste": "30 Plata", "bono": "Velocidad x1.5 (Ideal para Humanos y Enanos)"},
        {"nombre": "Corcel Élfico de los Vientos", "coste": "60 Plata + 5 Cores", "bono": "Velocidad x2.2 (Bonificación en bosques)"},
        {"nombre": "Bestia Primordial de Incursión", "coste": "1 Oro", "bono": "Velocidad x3.0 (Acceso rápido a zonas de Miasma)"}
    ]

    st.markdown(f"**Montura Activa:** `{st.session_state.montura_activa}`")
    st.markdown("---")

    for m in monturas_disponibles:
        st.markdown(f"**{m['nombre']}**\n- *Coste:* `{m['coste']}` | *Efecto:* {m['bono']}")
        if st.button(f"Seleccionar / Comprar: {m['nombre']}", key=f"btn_{m['nombre']}"):
            st.session_state.montura_activa = m['nombre']
            save_user_data()
            st.success(f"¡Has equipado **{m['nombre']}**!")
            st.rerun()
        st.markdown("---")

with tab_market:
    st.subheader("🏦 Mercado Abierto de 4 Metales")
    st.info("Comercio 100% libre. No existen restricciones de objetos ligados al alma.")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown("**🛡️ Kit de Supervivencia (Miasma)**")
        st.write("Necesario para explorar zonas de Miasma en el Continente Humano.")
        st.write("Precio: `10 Plata` + `2 Cores`")
        if st.button("Comprar Kit Miasma"):
            if st.session_state.plata >= 10 and st.session_state.cores >= 2:
                st.session_state.plata -= 10
                st.session_state.cores -= 2
                save_user_data()
                st.success("¡Kit de Supervivencia adquirido!")
            else:
                st.error("Metales insuficientes (requiere 10 Plata y 2 Cores).")

    with col_m2:
        st.markdown("**🪙 Refinería de Metales**")
        st.write("Canjea 50 de Plata por 1 de Oro.")
        if st.button("Canjear 50 Plata ➔ 1 Oro"):
            if st.session_state.plata >= 50:
                st.session_state.plata -= 50
                st.session_state.oro += 1
                save_user_data()
                st.success("¡Canje completado con éxito!")
            else:
                st.error("Necesitas al menos 50 de Plata.")

st.markdown("---")
st.caption("Snd-Worlds MMORPG Sandbox - Servidor Activo en Firebase Firestore")