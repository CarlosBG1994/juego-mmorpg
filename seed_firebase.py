import firebase_admin
from firebase_admin import credentials, firestore
import sys

# Inicialización segura de Firebase Firestore
def inicializar_firebase():
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
        return firestore.client()
    except Exception as e:
        print(f"❌ Error crítico al conectar con Firebase: {e}")
        print("Asegúrate de que el archivo 'serviceAccountKey.json' está en la raíz.")
        sys.exit(1)

db = inicializar_firebase()

def poblar_base_de_datos_completa():
    print("🚀 Iniciando el volcado completo de la macroarquitectura en Firebase Firestore...")
    
    batch = db.batch()

    # ==========================================
    # BLOQUE 1: MACROARQUITECTURA DE DISEÑO (PUNTOS CLAVE)
    # ==========================================
    puntos_maestros = [
        {
            "id": "point_001",
            "title": "Unicidad Absoluta de Personaje",
            "category": "Fundamentos",
            "status": "active",
            "summary": "Avatares totalmente independientes y aislados, sin legado compartido, cuentas ni banca entre alts.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_002",
            "title": "Cero Gobierno, Legislación o Política de Jugadores",
            "category": "Fundamentos",
            "status": "active",
            "summary": "Las megaciudades e infraestructura son operadas exclusivamente por NPCs. Los jugadores no legislan.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_003",
            "title": "Economía de 4 Metales y 100% Libre Comercio",
            "category": "Economía",
            "status": "active",
            "summary": "Sistema basado en Cores, Plata, Oro y Diamante con cero objetos ligados al alma (cero soul-bound).",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_010",
            "title": "Escala Masiva de 8.5M km² y 7 Continentes",
            "category": "Mundo Abierto",
            "status": "active",
            "summary": "Estructura lineal/temática desde El Refugio hasta el Reino Celestial Ascendido con 1.55M km² de océanos.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_120",
            "title": "Flotas de Pasaje y Barcos Regulares",
            "category": "Infraestructura y Transporte",
            "status": "active",
            "summary": "Transporte marítimo intercontinental operado por NPCs bajo horarios de reloj del servidor.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_126",
            "title": "Puertos Francos Fronterizos y Aduanas",
            "category": "Infraestructura y Transporte",
            "status": "active",
            "summary": "Enclaves costeros fortificados con tasas de aduana fijas en Plata/Oro para ordenar el flujo comercial.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_136",
            "title": "Aduanas Fluviales y Esclusas en Ríos",
            "category": "Infraestructura y Transporte",
            "status": "active",
            "summary": "Regulación del tránsito en ríos navegables hacia el interior de los continentes mediante esclusas hidráulicas.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_140",
            "title": "Puestos de Munición Masiva y Armamento Pesado",
            "category": "Acción y Combate",
            "status": "active",
            "summary": "Venta directa y rápida de proyectiles, explosivos y cargas de sitio en campamentos y bastiones.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_141",
            "title": "Altares de Llamado de Jefes en Mundo Abierto",
            "category": "Acción y Combate",
            "status": "active",
            "summary": "Invocación inmediata de jefes épicos mediante runas y fichas de desafío para acción sin esperas.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_148",
            "title": "Botín por Probabilidad y Suerte Pura (RNG)",
            "category": "Economía y Botín",
            "status": "active",
            "summary": "Cálculo transparente de drop rates y factor suerte al abatir enemigos o abrir cofres.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_150",
            "title": "Arquitectura Distribuida (Kubernetes y Redis)",
            "category": "Tecnología y Servidor",
            "status": "active",
            "summary": "Sharding por regiones, bloqueos atómicos en Redis para transacciones y Firestore como base de datos.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_151",
            "title": "Seguridad Antifraude y Anti-Cheat en Tiempo Real",
            "category": "Tecnología y Servidor",
            "status": "active",
            "summary": "Blindaje absoluto de la economía de 4 metales y validación estricta de acciones en el servidor.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_152",
            "title": "Optimización Multiplataforma Capacitor / WebGL",
            "category": "Tecnología y Servidor",
            "status": "active",
            "summary": "Gestión dinámica de rendimiento para garantizar FPS estables en PC y dispositivos móviles.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        },
        {
            "id": "point_153",
            "title": "Motor de Audio Dinámico e Inmersivo",
            "category": "Tecnología y Servidor",
            "status": "active",
            "summary": "Sonido ambiental adaptativo basado en biomas, condiciones climáticas y alertas de bestias colosales.",
            "rules": {"npc_controlled": True, "player_governance": False, "soulbound": False}
        }
    ]

    for pt in puntos_maestros:
        ref = db.collection("game_design_points").document(pt["id"])
        batch.set(ref, pt)

    # ==========================================
    # BLOQUE 2: HABILIDADES Y CLASES (28 Clases + 5 Runas)
    # ==========================================
    habilidades_maestras = [
        {
            "skill_id": "SKILL_IGNIS_01",
            "name": "Lanzamiento de Ascua Concentrada",
            "category": "Magia Elemental",
            "element": "Ignis",
            "class_restriction": ["Púgil", "Mago de Batalla", "Piromántico"],
            "tier": 1,
            "status": "active",
            "mechanics": {"mana_cost": 15, "cooldown_seconds": 3.5, "soulbound": False}
        },
        {
            "skill_id": "SKILL_GLACIES_01",
            "name": "Filo de Escarcha Perenne",
            "category": "Magia Elemental",
            "element": "Glacies",
            "class_restriction": ["Guerrero de Vanguardia", "Hechicero del Norte"],
            "tier": 1,
            "status": "active",
            "mechanics": {"mana_cost": 20, "cooldown_seconds": 4.0, "soulbound": False}
        },
        {
            "skill_id": "SKILL_VENTUS_01",
            "name": "Ráfaga de Viento Ciclónico",
            "category": "Magia Elemental",
            "element": "Ventus",
            "class_restriction": ["Explorador Ágil", "Arquero de Cima"],
            "tier": 1,
            "status": "active",
            "mechanics": {"mana_cost": 12, "cooldown_seconds": 2.5, "soulbound": False}
        }
    ]

    for sk in habilidades_maestras:
        ref = db.collection("game_skills").document(sk["skill_id"])
        batch.set(ref, sk)

    # ==========================================
    # BLOQUE 3: MISIONES PRINCIPALES Y SECUNDARIAS
    # ==========================================
    misiones_maestras = [
        {
            "quest_id": "MAIN_01_CRUCE_REFUGIO",
            "title": "El Primer Zarpe hacia las Tierras del Miasma",
            "type": "main",
            "continent": "El Refugio / Tierras del Miasma",
            "status": "active",
            "giver": "Capitanía del Puerto Franco del Sur (NPC)",
            "objective": "Comprar billete de pasaje regular, superar la travesía oceánica y atracar en el bastión del nivel 100.",
            "rewards": {"currency": "Oro", "amount": 50, "soulbound_loot": False}
        },
        {
            "quest_id": "SIDE_EXPLORE_012",
            "title": "Rastro y Cartografía del Coloso de Piedra",
            "type": "side",
            "continent": "Ignis-Dar",
            "status": "active",
            "giver": "Taberna de la Gran Plaza (NPC)",
            "objective": "Registrar en el diario de bitácora personal las coordenadas de migración del titán de piedra.",
            "rewards": {"currency": "Plata", "amount": 180, "soulbound_loot": False}
        }
    ]

    for q in misiones_maestras:
        ref = db.collection("game_quests").document(q["quest_id"])
        batch.set(ref, q)

    batch.commit()
    print("✅ ¡Volcado completo ejecutado con éxito en Firebase Firestore!")

if __name__ == "__main__":
    poblar_base_de_datos_completa()