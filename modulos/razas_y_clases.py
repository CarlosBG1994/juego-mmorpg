"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona razas, clases, sub-formas de Hombre Bestia y validaciones de equipo.
"""

RAZAS_HABILITADAS = ["Humano", "Elfo", "Enano", "Hombre Bestia"]

SUBFORMAS_HOMBRE_BESTIA = [
    "Hombre Lobo", "Hombre Pantera", "Hombre Tigre",
    "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"
]

CLASES_POR_RAZA = {
    "Humano": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"],
    "Elfo": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento (Púgil)", "Acechador Nocturno (Asesino)", "Mago de Batalla", "Invocador"],
    "Enano": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Campeón Rúnico", "Luchador de Puño de Hierro (Púgil)", "Ballestero (Explorador)", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"],
    "Hombre Bestia": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"]
}

TIPOS_ARMADURA = ["Tela", "Cuero", "Malla", "Placas"]

ARMADURAS_PERMITIDAS = {
    "Caballero": ["Placas", "Malla"],
    "Paladín": ["Placas", "Malla"],
    "Guerrero Pesado": ["Placas"],
    "Defensor Rúnico de Asedio": ["Placas"],
    "Guardabosques": ["Cuero", "Malla"],
    "Druida": ["Tela", "Cuero"],
    "Mago de Batalla": ["Tela", "Cuero"],
    "Clérigo": ["Tela", "Malla"],
    "Púgil": ["Cuero"],
    "Asesino": ["Cuero"],
    "Explorador": ["Cuero", "Malla"],
    "Invocador": ["Tela"],
    "Campeón": ["Malla", "Placas"],
    "Acechador Salvaje": ["Cuero"],
    "Chamán Primordial": ["Cuero", "Tela"]
}

def validar_compatibilidad_blindada(raza: str, clase: str, objeto_id: str = "") -> bool:
    if raza not in RAZAS_HABILITADAS:
        return False
    if clase not in CLASES_POR_RAZA.get(raza, []):
        return False
    return True

def validar_uso_equipo_blindado(clase: str, tipo_armadura: str) -> bool:
    permitidas = ARMADURAS_PERMITIDAS.get(clase, [])
    return tipo_armadura in permitidas
