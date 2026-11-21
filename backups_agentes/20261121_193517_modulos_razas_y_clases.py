"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona las 4 razas, clases permitidas, sub-formas de Hombre Bestia,
atributos iniciales, bonificadores por clase/sub-forma
y la verificacion de compatibilidad de equipamiento.
"""

ESTADISTICAS_BASE = ["STR", "INT", "AGI", "VIT", "LUK", "DES"]

# Lista para controlar disponibilidad (La Raza Dracónica está guardada pero no habilitada)
RAZAS_HABILITADAS = ["Humano", "Elfo", "Enano", "Hombre Bestia"]

SUBFORMAS_HOMBRE_BESTIA = [
    "Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre Leon", 
    "Hombre Mono", "Hombre Tortuga", "Hombre Panda"
]

# Aspecto visual para la pantalla de seleccion
ASPECTOS_RAZA = {
    "Humano": "Estatura media, rasgos definidos. Armaduras de metal pulido y mantos de tela práctica.",
    "Elfo": "Alta estatura, orejas puntiagudas, complexión esbelta. Ropajes orgánicos, cueros finos y detalles en seda vegetal.",
    "Enano": "Baja estatura, complexión robusta, vello facial denso. Armaduras pesadas con grabados rúnicos brillantes.",
    "Hombre Bestia": "Complexión poderosa y salvaje, rasgos felinos/caninos. Pieles de caza y accesorios totémicos óseos.",
    "Draconica": "Escamas naturales de tonos metálicos, ojos verticales, rasgos reptilianos imponentes. Armaduras ergonómicas adaptadas a su cola y alas."
}

ASPECTOS_CLASE = {
    "Caballero": "Placas de acero completas, gran escudo heráldico y espada larga.",
    "Paladin": "Armadura de placas brillante con ornamentos sagrados y libro de oraciones.",
    "Mago de Batalla": "Túnica reforzada con cuero, envuelto en un aura elemental activa.",
    "Pugil": "Vendas en las manos, torso despejado o con cuero ligero, musculatura muy marcada.",
    "Asesino": "Capucha oscura, ropas de sigilo con múltiples compartimentos para dagas.",
    "Explorador": "Atuendo de viaje ligero, capa de camuflaje, carcaj y arco de madera reforzada.",
    "Invocador": "Túnica ceremonial con símbolos arcanos y un báculo de esencia etérea.",
    "Clerigo": "Túnica clerical pesada, símbolo sagrado colgante y báculo de luz.",
    "Guardabosques": "Cuero teñido de verde y marrón, con detalles de hojas y plumas.",
    "Alcaide": "Armadura mixta de madera sagrada y metal, lanza larga y emblema del árbol.",
    "Druida": "Pieles de oso o lobo, ramas y flores tejidas en la ropa, bastón de roble.",
    "Espadachin Silvano": "Capa elegante, armadura ligera de placas de mithril, dos espadas finas.",
    "Guerrero Pesado": "Armadura masiva de forja profunda, martillo de guerra de dos manos.",
    "Defensor Runico de Asedio": "Escudo torre que cubre todo el cuerpo, runas grabadas en la armadura.",
    "Campeon": "Pintura de guerra, accesorios de huesos de gran bestia y arma pesada de estilo antiguo.",
    "Chaman Primordial": "Máscara de espíritu, bastón totémico y pieles de chamán con plumas."
}

CLASES_POR_RAZA = {
    "Humano": ["Caballero", "Paladin", "Mago de Batalla", "Pugil", "Asesino", "Explorador", "Invocador", "Clerigo"],
    "Elfo": ["Guardabosques", "Alcaide", "Druida", "Espadachin Silvano", "Monje del Viento (Pugil)", "Acechador Nocturno (Asesino)", "Mago de Batalla", "Invocador"],
    "Enano": ["Guerrero Pesado", "Defensor Runico de Asedio", "Campeon Runico", "Luchador de Puno de Hierro (Pugil)", "Ballestero (Explorador)", "Asesino", "Mago de Batalla", "Invocador", "Clerigo"],
    "Hombre Bestia": ["Campeon", "Acechador Salvaje", "Chaman Primordial", "Pugil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clerigo"],
    "Draconica": ["Guerrero Dragon", "Mago de Sangre", "Custodio de Escamas", "Acechador Draconico"]
}

ATRIBUTOS_RAZA = {
    "Humano": {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10},
    "Elfo": {"STR": 7, "INT": 13, "AGI": 13, "VIT": 8, "LUK": 9, "DES": 10},
    "Enano": {"STR": 13, "INT": 8, "AGI": 7, "VIT": 14, "LUK": 8, "DES": 10},
    "Hombre Bestia": {"STR": 14, "INT": 7, "AGI": 12, "VIT": 12, "LUK": 8, "DES": 7},
    "Draconica": {"STR": 15, "INT": 10, "AGI": 8, "VIT": 15, "LUK": 7, "DES": 5}
}

# ... [BONIFICADORES_SUBFORMA_BESTIA y BONIFICADORES_CLASE permanecen sin cambios] ...
# (He omitido el bloque completo para brevedad en la visualización, pero debe mantenerse en el archivo final)

def calcular_atributos_iniciales(raza: str, clase: str, subforma: str = None) -> dict:
    if raza not in RAZAS_HABILITADAS:
        raise ValueError(f"La raza {raza} no está disponible actualmente.")
    if clase not in CLASES_POR_RAZA.get(raza, []):
        raise ValueError(f"Clase no valida para {raza}: {clase}")

    stats = {k: ATRIBUTOS_RAZA[raza][k] for k in ESTADISTICAS_BASE}
    # ... [Logica de calculo existente intacta] ...
    return stats

def obtener_info_visual(raza: str, clase: str) -> dict:
    """Retorna los datos de aspecto para la interfaz de seleccion."""
    return {
        "aspecto_raza": ASPECTOS_RAZA.get(raza, "Sin descripción"),
        "aspecto_clase": ASPECTOS_CLASE.get(clase, "Sin descripción")
    }

# ... [Funciones validar_compatibilidad y obtener_clases_disponibles permanecen igual] ...
