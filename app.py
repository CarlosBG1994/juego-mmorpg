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

# --- RAZAS, CLASES Y CONTINENTES DE INICIO POR FACCIÓN ---
RAZAS_Y_CLASES = {
    "Humano": {
        "clases": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"],
        "continente_inicio": "Imperio Humano (Dividido en 4 Reinos)",
        "lore": "Tierra natal de los humanos, dividida en 4 grandes reinos con ciudades, castillos y pueblos propios."
    },
    "Elfo": {
        "clases": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento", "Acechador Nocturno", "Mago de Batalla", "Invocador"],
        "continente_inicio": "Dominio Silvano de los Elfos",
        "lore": "Bosques ancestrales y santuarios ocultos bajo la protección de la naturaleza."
    },
    "Enano": {
        "clases": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Berserker Rúnico", "Luchador de Puño de Hierro", "Ballestero", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"],
        "continente_inicio": "Cordillera e Imperios Enanos",
        "lore": "Fortalezas excavadas en la roca viva, colosales fraguas y minas de metales profundos."
    },
    "Hombre Bestia": {
        "clases": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"],
        "continente_inicio": "Tierras Salvajes de los Hombres Bestia",
        "lore": "Praderas indomables y territorios tribales donde impera la ley del más fuerte."
    }
}

SUBFORMAS_BESTIA = ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"]

CONTINENTES_OFICIALES = {
    "Imperio Humano (Dividido en 4 Reinos)": {"visible_desde_inicio": True, "tipo": "Facción Humana"},
    "Dominio Silvano de los Elfos": {"visible_desde_inicio": True, "tipo": "Facción Élfica"},
    "Cordillera e Imperios Enanos": {"visible_desde_inicio": True, "tipo": "Facción Enana"},
    "Tierras Salvajes de los Hombres Bestia": {"visible_desde_inicio": True, "tipo": "Facción Bestia"},
    "Archipiélago de los Cielos Abiertos": {"visible_desde_inicio": False, "tipo": "Continente Oculto / Exploración"},
    "Las Fronteras del Olvido": {"visible_desde_inicio": False, "tipo": "Continente Oculto / Incursión"},
    "El Núcleo Central de Comercio": {"visible_desde_inicio": True, "tipo": "Zona Franca Global"}
}

CATALOGO_OCULTAS = [
    {"id": "abrir_cielos", "nombre": "El Despertar de los Vientos", "continente_premio": "Archipiélago de los Cielos Abiertos", "tier": "Épico (Ultrararo)", "pista": "Reúne 50 de Plata y medita en la cima de la cordillera enana."},
    {"id": "abrir_olvido", "nombre": "El Sello del Vacío", "continente_premio": "Las Fronteras del Olvido", "tier": "Legendario", "pista": "Posee al menos 1 Diamante y derrota a la amenaza local en modo experto."}
]

POOL_SECUNDARIAS = [
    {"tipo": "Recolección", "titulo": "Extracción de Minerales en Bruto", "desc": "Recolecta muestras de suelo para los artesanos locales.", "recompensa": {"cores": 4, "plata": 20}},
    {"tipo": "Caza", "titulo": "Cacería de Bandidos del Páramo", "desc": "Limpia los caminos comerciales de amenazas hostiles.", "recompensa": {"plata": 40, "xp": 30}}
]

# --- ESTADO DE SESIÓN ---
for key, default in [
    ("logged_in", False), ("user_email", ""), ("hero_name", ""),
    ("raza", "Humano"), ("subforma", "Hombre Lobo"), ("genero", "Hombre"),
    ("clase", "Caballero"), ("continente", "Imperio Humano (Dividido en 4 Reinos)"),
    ("hero_level", 1), ("hero_hp", 100), ("hero_xp", 0),
    ("cores", 5), ("plata", 100), ("oro", 10), ("diamante", 1),
    ("skills", ["Golpe Base", "Tajo Inicial"]), ("has_character", False),
    ("mazmorra_reclamada", "Ninguna"), ("montura_activa", "A Pata (Sin Montura)"),
    ("indice_mision_principal", 0), ("misiones_ocultas_completadas", [])
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
            "montura_activa": st.session_state.montura_activa,
            "indice_mision_principal": st.session_state.indice_mision_principal,
            "misiones_ocultas_completadas": st.session_state.misiones_ocultas_completadas
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= PANTALLA DE LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Inicios por Facción | Continentes Ocultos | Exclusividad de 1 Día para el Pionero</p>", unsafe_allow_html=True)
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
                    st.session_state.continente = data.get("continente", "Imperio Humano (Dividido en 4 Reinos)")
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
                    st.session_state.indice_mision_principal = data.get("indice_mision_principal", 0)
                    st.session_state.misiones_ocultas_completadas = data.get("misiones_ocultas_completadas", [])
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
        st.session_state.continente = info_raza["continente_inicio"]
        
        st.info(f"🏰 **Territorio de Inicio ({st.session_state.raza}):**\n`{st.session_state.continente}`\n\n*{info_raza['lore']}*")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 ¡Despertar en tu Territorio!", use_container_width=True):
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
st.sidebar.markdown(f"📍 **Ubicación:** \n`{st.session_state.continente}`")

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
tab_play, tab_skills, tab_world, tab_dungeons, tab_mounts, tab_quests, tab_p2p, tab_market = st.tabs([
    "🎮 Mundo Abierto (Canvas)", 
    "⚡ Grimorio (Tiers)", 
    "🌍 Mapa y Continentes", 
    "🏰 Mazmorras",
    "🐎 Monturas",
    "📜 Misiones Dinámicas",
    "🤝 Encargos P2P",
    "🏦 Mercado Abierto"
])

with tab_play:
    st.subheader(f"Exploración Activa en: {st.session_state.continente}")
    st.info("🎮 **Controles:** Muévete con las teclas **WASD** o **Flechas** en tu ordenador. En móvil, utiliza el **Joystick virtual** y los botones de habilidades en pantalla.")

    # Generamos la lista de habilidades del jugador en formato JS
    skills_js = str(st.session_state.skills)

    # Componente HTML5 / JS con Canvas interactivo, Joystick móvil y soporte de teclado
    game_html = f"""
    <div style="text-align: center; background: #111; padding: 10px; border-radius: 10px; border: 2px solid #ffaa00;">
        <canvas id="gameCanvas" width="700" height="400" style="background: #222; border-radius: 8px; display: block; margin: 0 auto; max-width: 100%;"></canvas>
        <div style="margin-top: 15px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
            <button onclick="usarHabilidad(0)" style="background: #ff4500; color: white; border: none; padding: 10px 15px; border-radius: 5px; font-weight: bold; cursor: pointer;">✨ {st.session_state.skills[0] if len(st.session_state.skills)>0 else 'Ataque'} [1]</button>
            <button onclick="usarHabilidad(1)" style="background: #1e90ff; color: white; border: none; padding: 10px 15px; border-radius: 5px; font-weight: bold; cursor: pointer;">⚡ {st.session_state.skills[1] if len(st.session_state.skills)>1 else 'Habilidad'} [2]</button>
        </div>
        <p id="infoAccion" style="color: #00ffcc; margin-top: 10px; font-weight: bold;"></p>
    </div>

    <!-- Controles Táctiles (Joystick móvil simulado y botones de movimiento) -->
    <div style="margin-top: 15px; display: flex; justify-content: space-around; align-items: center;">
        <div style="display: grid; grid-template-columns: repeat(3, 50px); gap: 5px;">
            <div></div>
            <button ontouchstart="moverTouch('W')" onmousedown="moverTouch('W')" style="height: 50px; background: #333; color: #fff; border: 1px solid #777; font-size: 20px;">⬆️</button>
            <div></div>
            <button ontouchstart="moverTouch('A')" onmousedown="moverTouch('A')" style="height: 50px; background: #333; color: #fff; border: 1px solid #777; font-size: 20px;">⬅️</button>
            <button ontouchstart="moverTouch('S')" onmousedown="moverTouch('S')" style="height: 50px; background: #333; color: #fff; border: 1px solid #777; font-size: 20px;">⬇️</button>
            <button ontouchstart="moverTouch('D')" onmousedown="moverTouch('D')" style="height: 50px; background: #333; color: #fff; border: 1px solid #777; font-size: 20px;">➡️</button>
        </div>
        <div style="text-align: left; color: #aaa; font-size: 14px;">
            <b>Héroe:</b> {st.session_state.hero_name}<br>
            <b>Clase:</b> {st.session_state.clase}<br>
            Usa <b>WASD</b> o los botones táctiles para moverte.
        </div>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        let player = {{
            x: 350,
            y: 200,
            radius: 15,
            speed: 4,
            color: "#ffaa00"
        }};

        let keys = {{}};

        window.addEventListener('keydown', (e) => {{
            keys[e.key.toLowerCase()] = true;
            if(e.key === '1') usarHabilidad(0);
            if(e.key === '2') usarHabilidad(1);
        }});

        window.addEventListener('keyup', (e) => {{
            keys[e.key.toLowerCase()] = false;
        }});

        function moverTouch(dir) {{
            if(dir === 'W') player.y -= 20;
            if(dir === 'S') player.y += 20;
            if(dir === 'A') player.x -= 20;
            if(dir === 'D') player.x += 20;
            limites();
        }}

        function limites() {{
            if (player.x < player.radius) player.x = player.radius;
            if (player.x > canvas.width - player.radius) player.x = canvas.width - player.radius;
            if (player.y < player.radius) player.y = player.radius;
            if (player.y > canvas.height - player.radius) player.y = canvas.height - player.radius;
        }}

        function actualizar() {{
            if (keys['w'] || keys['arrowup']) player.y -= player.speed;
            if (keys['s'] || keys['arrowdown']) player.y += player.speed;
            if (keys['a'] || keys['arrowleft']) player.x -= player.speed;
            if (keys['d'] || keys['arrowright']) player.x += player.speed;
            limites();
        }}

        function dibujar() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Dibujar fondo de cuadrícula del mundo abierto
            ctx.strokeStyle = "#333";
            ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=40) {{
                ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
            }}
            for(let j=0; j<canvas.height; j+=40) {{
                ctx.beginPath(); ctx.moveTo(0, j); ctx.lineTo(canvas.width, j); ctx.stroke();
            }}

            // Dibujar al Jugador
            ctx.beginPath();
            ctx.arc(player.x, player.y, player.radius, 0, Math.PI * 2);
            ctx.fillStyle = player.color;
            ctx.fill();
            ctx.lineWidth = 2;
            ctx.strokeStyle = "#fff";
            ctx.stroke();
            ctx.closePath();

            // Nombre del Héroe flotante
            ctx.fillStyle = "#fff";
            ctx.font = "12px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText("{st.session_state.hero_name}", player.x, player.y - 20);
        }}

        function loop() {{
            actualizar();
            dibujar();
            requestAnimationFrame(loop);
        }}

        function usarHabilidad(index) {{
            const skillsList = {skills_js};
            const skillName = skillsList[index] || "Golpe Base";
            document.getElementById("infoAccion").innerText = "⚡ ¡Usaste la habilidad: " + skillName + "!";
            setTimeout(() => {{
                document.getElementById("infoAccion").innerText = "";
            }, 3000);
        }}

        loop();
    </script>
    """
    st.components.v1.html(game_html, height=580)

with tab_skills:
    st.subheader("⚡ Grimorio de Habilidades Activas")
    for sk in st.session_state.skills:
        st.markdown(f"- ✨ **{sk}**")

with tab_world:
    st.subheader("🌍 Estado del Mundo y Niebla de Guerra")
    lista_viaje = obtener_continentes_visibles()
    destino_elegido_raw = st.selectbox("Continentes Accesibles", lista_viaje)
    destino_limpio = destino_elegido_raw.split(" 🌟")[0].split(" 🔓")[0].split(" 🔒")[0]

    if st.button("✈️ Viajar a este Continente", use_container_width=True):
        if "🔒 (Exclusivo Pionero" in destino_elegido_raw:
            st.error("⚠️ Este continente está bajo el periodo de exclusividad de 24 horas de su descubridor.")
        elif "🔒 (Oculto" in destino_elegido_raw:
            st.error("🔒 Este continente está oculto por la niebla de guerra. ¡Completa las misiones secretas!")
        else:
            st.session_state.continente = destino_limpio
            save_user_data()
            st.success(f"¡Has viajado a **{destino_limpio}**!")
            st.rerun()

with tab_dungeons:
    st.subheader("🏰 Mazmorras Estacionales")
    st.markdown(f"**Mazmorra Reclamada:** `{st.session_state.mazmorra_reclamada}`")
    if st.button("Reclamar Bastión Local"):
        if st.session_state.oro >= 1:
            st.session_state.oro -= 1
            st.session_state.mazmorra_reclamada = f"Bastión en {st.session_state.continente}"
            save_user_data()
            st.success("¡Mazmorra reclamada!")
            st.rerun()

with tab_mounts:
    st.subheader("🐎 Establo y Monturas")
    st.markdown(f"**Montura Activa:** `{st.session_state.montura_activa}`")
    if st.button("Equipar Corcel"):
        st.session_state.montura_activa = "Corcel de Exploración"
        save_user_data()
        st.success("¡Montura equipada!")
        st.rerun()

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
            else:
                st.info(f"Descubierto por **{doc_cont.to_dict().get('pionero')}**.")

with tab_p2p:
    st.subheader("🤝 Tablón P2P (Encargos entre Jugadores)")
    with st.form("form_p2p"):
        titulo = st.text_input("Qué necesitas (Ej: 'Busco 5 Cores')")
        tipo_meta = st.selectbox("Metal de Recompensa", ["Plata", "Oro", "Cores", "Diamante"])
        cant_meta = st.number_input("Cantidad", min_value=1, value=10)
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
                st.success("¡Publicado!")
                st.rerun()

with tab_market:
    st.subheader("🏦 Mercado Abierto de Metales")
    if st.button("Canjear 50 Plata por 1 Oro"):
        if st.session_state.plata >= 50:
            st.session_state.plata -= 50; st.session_state.oro += 1
            save_user_data()
            st.success("¡Canje exitoso!")
            st.rerun()

st.markdown("---")
st.caption("Snd-Worlds MMORPG Sandbox - Servidor Activo en Firebase Firestore")