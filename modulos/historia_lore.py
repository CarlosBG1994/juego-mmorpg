"""
Modulo: Historia y Lore de Snd-Worlds
Contiene el prologo, cronicas de los 4 Reinos, misterio de los continentes,
textos de ambientacion y metadatos para el Agente de Sistema de Misiones.
"""

LORE_INTRODUCCION = {
    "titulo": "El Despertar del Eter",
    "evento_historico": "La Gran Fractura del Nexum Divino",
    "resumen": (
        "Tras la fractura del mundo antiguo, el conocimiento magico quedo fragmentado "
        "en 1.870 Sellos de Habilidad dispersos por todo el Continente Primordial. "
        "Los cuatro reinos coexisten mientras los aventureros buscan romper las barreras "
        "hacia los continentes ocultos."
    )
}

CINEMATICA_INICIAL = (
    "Hace eones, los mundos se estremecieron en una guerra sin piedad.\n\n"
    "Los Xylaroth —una raza de demonios guiada por su rey, Malakor’zeth, el Soberano del Abismo— "
    "avanzaban con un único propósito: conquistar todos los mundos. Comenzaron a rasgar el cielo "
    "y a aparecer en todos los territorios, sembrando ruina y terror allí donde pisaban.\n\n"
    "En aquel tiempo, todos los reinos formaban parte de una misma tierra unida. Ante aquella "
    "marea imparable, las razas dejaron atrás sus diferencias y se unieron por primera vez para "
    "hacer frente a un mismo enemigo.\n\n"
    "Cuatro héroes se alzaron: Aurelius del Alba, Thalor’en, Bramir Peñahonda y Kaelen Garraferoz. "
    "Sellar el abismo provocó el Gran Cataclismo que separó la tierra en continentes rodeados de mares indómitos.\n\n"
    "Hoy tu historia empieza en el Continente Primordial."
)

HISTORIA_RAZAS_DETALLADA = {
    "Humano": {
        "reino": "Reino Humano",
        "capital": "Corona de Luz",
        "estatua_heroe": "Aurelius del Alba",
        "stats_bonus": {"STR": 5, "INT": 5, "AGI": 5, "VIT": 5, "LUK": 5, "DES": 5},
        "clases": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"]
    },
    "Elfo": {
        "reino": "Reino Élfico",
        "capital": "Árbol de la Aurora",
        "estatua_heroe": "Thalor’en",
        "stats_bonus": {"INT": 8, "AGI": 8, "DES": 5, "LUK": 4, "VIT": 3, "STR": 2},
        "clases": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento (Púgil)", "Acechador Nocturno (Asesino)", "Mago de Batalla", "Invocador"]
    },
    "Enano": {
        "reino": "Reino Enano",
        "capital": "Baluarte Forjaeterna",
        "estatua_heroe": "Bramir Peñahonda",
        "stats_bonus": {"VIT": 10, "STR": 8, "DES": 5, "LUK": 4, "INT": 3, "AGI": 2},
        "clases": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Campeón Rúnico", "Luchador de Puño de Hierro (Púgil)", "Ballestero (Explorador)", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"]
    },
    "Hombre Bestia": {
        "reino": "Reino de las Bestias",
        "capital": "Claro Ancestral",
        "estatua_heroe": "Kaelen Garraferoz",
        "stats_bonus": {"STR": 8, "AGI": 7, "VIT": 6, "LUK": 4, "DES": 3, "INT": 2},
        "subformas": ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"],
        "clases": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"]
    }
}

def obtener_prologo_jugador(raza: str) -> str:
    datos = HISTORIA_RAZAS_DETALLADA.get(raza)
    if not datos:
        return "Bienvenido a Snd-Worlds. Tu viaje está por comenzar."
    return f"Bienvenido a las tierras de {datos['reino']} (Capital: {datos['capital']}). Forja tu camino bajo el legado de {datos['estatua_heroe']}."
