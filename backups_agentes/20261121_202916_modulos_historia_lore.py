"""
Modulo: Historia y Lore de Snd-Worlds
Contiene el prologo, cronicas de los 4 Reinos, misterio de los continentes
y textos de ambientacion para misiones e introduccion del jugador.
"""

LORE_INTRODUCCION = {
    "titulo": "El Despertar del Eter",
    "evento_historico": "La Gran Fractura del Nexum Divino",
    "resumen": (
        "Tras la fractura del mundo antiguo, el conocimiento magico quedo fragmentado "
        "en 1.870 Sellos de Habilidad dispersos por todo el Continente Primordial. "
        "Los cuatro reinos (Humano, Elfo, Enano y Hombre Bestia) coexisten mientras "
        "los aventureros buscan romper las barreras hacia los continentes ocultos."
    )
}

CINEMATICA_INICIAL = (
    "Hace eones, los mundos se estremecieron en una guerra sin piedad.\n\n"
    "Los Xylaroth —una raza de demonios guiada por su rey, Malakor’zeth, el Soberano del Abismo— "
    "avanzaban con un único propósito: conquistar todos los mundos. Comenzaron a rasgar el cielo "
    "y a aparecer en todos los territorios, sembrando ruina y terror allí donde pisaban.\n\n"
    "En aquel tiempo, todos los reinos formaban parte de una misma tierra unida. Ante aquella "
    "marea imparable, las razas dejaron atrás sus diferencias y se unieron por primera vez para "
    "hacer frente a un mismo enemigo. Durante largo tiempo resistieron golpe a golpe, hasta que "
    "un artefacto demoníaco desató una oscuridad absoluta que terminó consumiendo sus hogares.\n\n"
    "Cuando todo parecía perdido, cuatro héroes se alzaron en medio del desastre: Aurelius del Alba, "
    "Thalor’en, Bramir Peñahonda y Kaelen Garraferoz. Liderando la última resistencia, libraron una "
    "gran batalla que diezmó a los Xylaroth y consiguieron encerrarlos dentro de su propio reino.\n\n"
    "Pero el precio de sellar el abismo quebró el mundo para siempre. El poder desatado en aquella "
    "baatalla final provocó el Gran Cataclismo: una catástrofe colosal que partió la tierra que antes "
    "unía todos los reinos, separándola en distintos continentes rodeados por mares indómitos. Con "
    "la caída de los Xylaroth y el desgarro del mundo, toda la civilización antigua se perdió, "
    "dejando sus ciudades, templos y fortalezas sepultadas como ruinas olvidadas que aún hoy "
    "pueden encontrarse repartidas por todo el continente.\n\n"
    "Obligados a empezar de cero tras el cataclismo, los supervivientes de las cuatro razas se "
    "asentaron en sus propios reinos sobre el nuevo continente para levantar un nuevo hogar.\n\n"
    "Hoy el eco de aquella guerra y los secretos de la era antigua siguen latentes... y tu historia empieza aquí."
)

HISTORIA_RAZAS_DETALLADA = {
    "Humano": {
        "reino": "Reino Humano",
        "capital": "Corona de Luz",
        "historia": "Tras la guerra contra los Xylaroth y el Gran Cataclismo, los humanos se asentaron en tierras abiertas y fértiles del nuevo continente, fundando Corona de Luz para reconstruir la civilización y el orden, mientras exploran los restos de la civilización antigua perdida.",
        "stats_bonus": {"STR": 5, "INT": 5, "AGI": 5, "VIT": 5, "LUK": 5, "DES": 5},
        "clases": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"]
    },
    "Elfo": {
        "reino": "Reino Élfico",
        "capital": "Árbol de la Aurora",
        "historia": "Tras la caída de sus antiguos hogares, los elfos buscaron refugio en los bosques vivos y enclaves mágicos del nuevo continente, levantando Árbol de la Aurora en profunda conexión con la naturaleza y los vestigios antiguos.",
        "stats_bonus": {"INT": 8, "AGI": 8, "DES": 5, "LUK": 4, "VIT": 3, "STR": 2},
        "clases": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento (Púgil)", "Acechador Nocturno (Asesino)", "Mago de Batalla", "Invocador"]
    },
    "Enano": {
        "reino": "Reino Enano",
        "capital": "Baluarte Forjaeterna",
        "historia": "Tras el Gran Cataclismo, los enanos se establecieron en las montañas y profundidades ricas en minerales del nuevo continente, edificando Baluarte Forjaeterna como un bastión defensivo, centro de forja, ingeniería y estudio de ruinas antiguas.",
        "stats_bonus": {"VIT": 10, "STR": 8, "DES": 5, "LUK": 4, "INT": 3, "AGI": 2},
        "clases": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Campeón Rúnico", "Luchador de Puño de Hierro (Púgil)", "Ballestero (Explorador)", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"]
    },
    "Hombre Bestia": {
        "reino": "Reino de las Bestias",
        "capital": "Claro Ancestral",
        "historia": "Tras la oscuridad que consumió los antiguos territorios, los Hombres Bestia se reunieron en las tierras salvajes del nuevo continente, estableciendo Claro Ancestral bajo el signo del instinto, la manada y la supervivencia frente a los restos de la era antigua.",
        "stats_bonus": {"STR": 8, "AGI": 7, "VIT": 6, "LUK": 4, "DES": 3, "INT": 2},
        "subformas": ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"],
        "clases": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"]
    },
    "Draconica": {
        "reino": "Imperio de las Cenizas",
        "capital": "Ciudadela de Escamas",
        "historia": "Descendientes de los antiguos dragones que protegieron el mundo durante el Gran Cataclismo, los Dracónicos emergieron de los picos volcánicos. Se asentaron en la Ciudadela de Escamas, preservando el conocimiento arcano y el fuego primordial en un mundo que aún teme su poder absoluto.",
        "stats_bonus": {"STR": 10, "VIT": 10, "INT": 7, "DES": 4, "AGI": 3, "LUK": 2},
        "clases": ["Guerrero Dragón", "Mago de Sangre", "Custodio de Escamas", "Acechador Dracónico"]
    }
}

# Diccionario heredado para compatibilidad
HISTORIA_REINOS = {r: {"reino": d["reino"], "capital": d["capital"], "trasfondo": d["historia"]} for r, d in HISTORIA_RAZAS_DETALLADA.items()}

DESTINOS_DEL_MUNDO = [
    {"fase": 1, "nombre": "Continente Primordial", "limite_nivel": 100, "meta": "Dominar el propio reino y cruzar las Tierras de Nadie."},
    {"fase": 2, "nombre": "Archipielago de los Vientos", "limite_nivel": 150, "meta": "Navegar las corrientes etereas y descubrir islas flotantes."},
    {"fase": 3, "nombre": "Continente Abisal de los Demonios", "limite_nivel": 200, "meta": "Descender a las fosas de fuego y oscuridad."},
    {"fase": 4, "nombre": "Continente Celestial de los Angeles", "limite_nivel": 250, "meta": "Ascender a las agujas sagradas de luz primordial."},
    {"fase": 5, "nombre": "Nucleo Central de Comercio y Nexo Global", "limite_nivel": 300, "meta": "El centro del universo restaurado."}
]

def obtener_cinematica_inicial():
    return CINEMATICA_INICIAL

def obtener_prologo_jugador(raza: str) -> str:
    info = HISTORIA_RAZAS_DETALLADA.get(raza)
    if not info:
        return "Bienvenido a Snd-Worlds. Tu viaje esta por comenzar."
    
    return (
        f"Bienvenido a las tierras de {info['reino']}, con sede en {info['capital']}.\n"
        f"{info['historia']}\n"
        f"Tus primeros pasos seran en las Zonas 1-15. Encuentra habilidades, perfecciona tus ataques "
        f"y forja tu nombre antes de aventurarte hacia las fronteras."
    )
