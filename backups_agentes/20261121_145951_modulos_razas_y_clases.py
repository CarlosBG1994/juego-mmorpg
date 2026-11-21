"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona las 4 razas, clases permitidas, sub-formas de Hombre Bestia
y la verificacion de compatibilidad de equipamiento.
"""

ESTADISTICAS_BASE = ["STR", "INT", "AGI", "VIT", "LUK", "DES"]

SUBFORMAS_HOMBRE_BESTIA = [
    "Hombre Lobo",
    "Hombre Pantera",
    "Hombre Tigre",
    "Hombre Leon",
    "Hombre Mono",
    "Hombre Tortuga",
    "Hombre Panda"
]

CLASES_POR_RAZA = {
    "Humano": [
        "Caballero", "Paladin", "Mago de Batalla", "Pugil",
        "Asesino", "Explorador", "Invocador", "Clerigo"
    ],
    "Elfo": [
        # El elfo no tiene clerigo; el druida asume la sanacion y soporte
        "Guardabosques", "Alcaide", "Druida", "Espadachin Silvano",
        "Monje del Viento (Pugil)", "Acechador Nocturno (Asesino)",
        "Mago de Batalla", "Invocador"
    ],
    "Enano": [
        "Guerrero Pesado", "Defensor Runico de Asedio", "Campeon Runico",
        "Luchador de Puno de Hierro (Pugil)", "Ballestero (Explorador)",
        "Asesino", "Mago de Batalla", "Invocador", "Clerigo"
    ],
    "Hombre Bestia": [
        "Campeon", "Acechador Salvaje", "Chaman Primordial",
        "Pugil",  # Incluye variantes/estado frenetico tipo Berserker
        "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clerigo"
    ]
}

# Modificadores de atributos iniciales segun Raza
ATRIBUTOS_RAZA = {
    "Humano": {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10},
    "Elfo": {"STR": 7, "INT": 13, "AGI": 13, "VIT": 8, "LUK": 9, "DES": 10},
    "Enano": {"STR": 13, "INT": 8, "AGI": 7, "VIT": 14, "LUK": 8, "DES": 10},
    "Hombre Bestia": {"STR": 14, "INT": 7, "AGI": 12, "VIT": 12, "LUK": 8, "DES": 7}
}

def validar_compatibilidad(raza_jugador: str, clase_jugador: str, raza_req: list = None, clase_req: list = None) -> bool:
    """
    Comprueba si un jugador puede equipar y usar un objeto o habilidad.
    Cualquiera puede obtenerlos en su mochila, pero solo usarlos si es compatible.
    """
    if raza_req and raza_jugador not in raza_req:
        return False
    if clase_req and clase_jugador not in clase_req:
        return False
    return True

def obtener_clases_disponibles(raza: str) -> list:
    return CLASES_POR_RAZA.get(raza, [])
