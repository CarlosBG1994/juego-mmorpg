"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona las 4 razas, clases permitidas, sub-formas de Hombre Bestia,
atributos iniciales, bonificadores por clase/sub-forma
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

# Modificadores de atributos iniciales segun Raza (Base total = 60 puntos)
ATRIBUTOS_RAZA = {
    "Humano": {
        "STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10,
        "descripcion": "Equilibrio absoluto y adaptabilidad en cualquier disciplina."
    },
    "Elfo": {
        "STR": 7, "INT": 13, "AGI": 13, "VIT": 8, "LUK": 9, "DES": 10,
        "descripcion": "Gran afinidad magica, agilidad y reflejos naturales; resistencia fisica menor."
    },
    "Enano": {
        "STR": 13, "INT": 8, "AGI": 7, "VIT": 14, "LUK": 8, "DES": 10,
        "descripcion": "Inmensa constitucion fisica, fuerza y temple; menor velocidad de desplazamiento."
    },
    "Hombre Bestia": {
        "STR": 14, "INT": 7, "AGI": 12, "VIT": 12, "LUK": 8, "DES": 7,
        "descripcion": "Furia primordial e instinto de combate cuerpo a cuerpo y resistencia salvaje."
    }
}

# Bonificaciones de atributos segun la Sub-forma elegida por el Hombre Bestia (+5 puntos distribuidos)
BONIFICADORES_SUBFORMA_BESTIA = {
    "Hombre Lobo": {"STR": 2, "INT": 0, "AGI": 3, "VIT": 0, "LUK": 0, "DES": 0},
    "Hombre Pantera": {"STR": 0, "INT": 0, "AGI": 3, "VIT": 0, "LUK": 0, "DES": 2},
    "Hombre Tigre": {"STR": 3, "INT": 0, "AGI": 2, "VIT": 0, "LUK": 0, "DES": 0},
    "Hombre Leon": {"STR": 2, "INT": 0, "AGI": 0, "VIT": 3, "LUK": 0, "DES": 0},
    "Hombre Mono": {"STR": 0, "INT": 0, "AGI": 2, "VIT": 0, "LUK": 2, "DES": 1},
    "Hombre Tortuga": {"STR": 0, "INT": 0, "AGI": 0, "VIT": 4, "LUK": 1, "DES": 0},
    "Hombre Panda": {"STR": 1, "INT": 1, "AGI": 0, "VIT": 3, "LUK": 0, "DES": 0}
}

# Bonificaciones de atributos segun la Clase elegida (+10 puntos de especializacion)
BONIFICADORES_CLASE = {
    # Clases Humanas
    "Caballero": {"STR": 4, "INT": 0, "AGI": 1, "VIT": 4, "LUK": 0, "DES": 1},
    "Paladin": {"STR": 3, "INT": 3, "AGI": 0, "VIT": 3, "LUK": 0, "DES": 1},
    "Mago de Batalla": {"STR": 2, "INT": 5, "AGI": 1, "VIT": 1, "LUK": 0, "DES": 1},
    "Pugil": {"STR": 4, "INT": 0, "AGI": 3, "VIT": 3, "LUK": 0, "DES": 0},
    "Asesino": {"STR": 1, "INT": 0, "AGI": 4, "VIT": 1, "LUK": 1, "DES": 3},
    "Explorador": {"STR": 1, "INT": 0, "AGI": 3, "VIT": 1, "LUK": 1, "DES": 4},
    "Invocador": {"STR": 0, "INT": 5, "AGI": 1, "VIT": 1, "LUK": 2, "DES": 1},
    "Clerigo": {"STR": 1, "INT": 4, "AGI": 0, "VIT": 4, "LUK": 1, "DES": 0},

    # Clases Elficas
    "Guardabosques": {"STR": 1, "INT": 1, "AGI": 4, "VIT": 0, "LUK": 0, "DES": 4},
    "Alcaide": {"STR": 2, "INT": 2, "AGI": 2, "VIT": 3, "LUK": 0, "DES": 1},
    "Druida": {"STR": 0, "INT": 4, "AGI": 1, "VIT": 3, "LUK": 1, "DES": 1},
    "Espadachin Silvano": {"STR": 2, "INT": 1, "AGI": 4, "VIT": 1, "LUK": 0, "DES": 2},
    "Monje del Viento (Pugil)": {"STR": 2, "INT": 1, "AGI": 5, "VIT": 1, "LUK": 0, "DES": 1},
    "Acechador Nocturno (Asesino)": {"STR": 1, "INT": 0, "AGI": 5, "VIT": 0, "LUK": 1, "DES": 3},

    # Clases Enanas
    "Guerrero Pesado": {"STR": 5, "INT": 0, "AGI": 0, "VIT": 5, "LUK": 0, "DES": 0},
    "Defensor Runico de Asedio": {"STR": 3, "INT": 2, "AGI": 0, "VIT": 5, "LUK": 0, "DES": 0},
    "Campeon Runico": {"STR": 4, "INT": 3, "AGI": 0, "VIT": 3, "LUK": 0, "DES": 0},
    "Luchador de Puno de Hierro (Pugil)": {"STR": 5, "INT": 0, "AGI": 1, "VIT": 4, "LUK": 0, "DES": 0},
    "Ballestero (Explorador)": {"STR": 2, "INT": 0, "AGI": 1, "VIT": 2, "LUK": 1, "DES": 4},

    # Clases Hombre Bestia
    "Campeon": {"STR": 5, "INT": 0, "AGI": 1, "VIT": 4, "LUK": 0, "DES": 0},
    "Acechador Salvaje": {"STR": 3, "INT": 0, "AGI": 4, "VIT": 1, "LUK": 0, "DES": 2},
    "Chaman Primordial": {"STR": 1, "INT": 4, "AGI": 1, "VIT": 3, "LUK": 1, "DES": 0}
}


def calcular_atributos_iniciales(raza: str, clase: str, subforma: str = None) -> dict:
    """
    Calcula los atributos iniciales finales combinando:
    Base de Raza + Bono de Sub-forma (Hombre Bestia) + Bono de Clase.
    """
    if raza not in ATRIBUTOS_RAZA:
        raise ValueError(f"Raza no valida: {raza}")
    if clase not in CLASES_POR_RAZA.get(raza, []):
        raise ValueError(f"Clase no valida para {raza}: {clase}")

    stats = {k: ATRIBUTOS_RAZA[raza][k] for k in ESTADISTICAS_BASE}

    # Aplicar bono de sub-forma si es Hombre Bestia
    if raza == "Hombre Bestia":
        if subforma not in SUBFORMAS_HOMBRE_BESTIA:
            raise ValueError(f"Sub-forma no valida para Hombre Bestia: {subforma}")
        bono_subforma = BONIFICADORES_SUBFORMA_BESTIA.get(subforma, {})
        for stat, valor in bono_subforma.items():
            stats[stat] += valor

    # Aplicar bono de clase
    bono_clase = BONIFICADORES_CLASE.get(clase, {})
    for stat, valor in bono_clase.items():
        stats[stat] = stats.get(stat, 0) + valor

    return stats


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
