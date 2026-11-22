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
        "en 1.870 Sellos de Habilidad dispersos por todo el Continente Primordial."
    )
}

# --- COORDINACIÓN CON AGENTE DE MISIONES ---
# Esta estructura permite que el Agente de Misiones extraiga contextos narrativos
# para generar misiones dinámicas.
MAPA_NARRATIVO_MISIONES = {
    "Principal": {
        "origen": "Estatua del Héroe Local",
        "progresion": ["Capital -> Frontera -> Ruinas -> Centro del Continente"],
        "objetivo": "Recuperar el Nexum Divino."
    },
    "Secundaria": {
        "origen": "Tablón de Gremio / NPCs Locales",
        "temas": ["Escolta de caravanas", "Recolección de metal rúnico", "Purga de bestias corrompidas"],
        "dinamica": "Generación procedural basada en la zona del mapa."
    },
    "Oculta": {
        "origen": "Interacción con objetos antiguos / Inscripciones en estatuas",
        "temas": ["Memorias de Malakor’zeth", "Secretos del Gran Cataclismo"],
        "requisito": "Nivel de reputación o hallazgo de ítems especiales."
    }
}

# --- NARRATIVA DINAMICA DE CAMPAÑA ---
CRONICA_CONTINENTE_PRIMORDIAL = {
    "eje_central": "La Búsqueda del Nexo",
    "pilares_narrativos": {
        "ruta_viajero": "El jugador debe conectar las 4 capitales.",
        "estatuas_heroicas": "Interactuar con estatuas para misiones de memoria histórica.",
        "vestigios_antiguos": "Recolección de registros para revelar la verdad del Cataclismo."
    }
}

CINEMATICA_INICIAL = (
    "Hace eones, los mundos se estremecieron en una guerra sin piedad.\n\n"
    "Los Xylaroth... [Cuerpo cinemático preservado] ...y tu historia empieza aquí."
)

HISTORIA_RAZAS_DETALLADA = {
    "Humano": {
        "reino": "Reino Humano",
        "capital": "Corona de Luz",
        "historia": "Tras el Gran Cataclismo, los humanos fundaron Corona de Luz. En su plaza central, la estatua de Aurelius del Alba observa el horizonte, recordando a los ciudadanos la importancia del orden y la justicia ante las ruinas de la civilización antigua.",
        "stats_bonus": {"STR": 5, "INT": 5, "AGI": 5, "VIT": 5, "LUK": 5, "DES": 5},
        "clases": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"]
    },
    "Elfo": {
        "reino": "Reino Élfico",
        "capital": "Árbol de la Aurora",
        "historia": "Los elfos erigieron Árbol de la Aurora como su refugio. Bajo sus ramas, la estatua de Thalor’en permanece como guardián perenne, simbolizando la unión entre la magia natural y el sacrificio hecho para preservar su hogar frente a la sombra.",
        "stats_bonus": {"INT": 8, "AGI": 8, "DES": 5, "LUK": 4, "VIT": 3, "STR": 2},
        "clases": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento (Púgil)", "Acechador Nocturno (Asesino)", "Mago de Batalla", "Invocador"]
    },
    "Enano": {
        "reino": "Reino Enano",
        "capital": "Baluarte Forjaeterna",
        "historia": "Baluarte Forjaeterna es el hogar de los enanos, donde la estatua de Bramir Peñahonda ha sido esculpida en piedra inquebrantable, representando la resistencia y la fortaleza necesaria para reconstruir un mundo fracturado.",
        "stats_bonus": {"VIT": 10, "STR": 8, "DES": 5, "LUK": 4, "INT": 3, "AGI": 2},
        "clases": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Campeón Rúnico", "Luchador de Puño de Hierro (Púgil)", "Ballestero (Explorador)", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"]
    },
    "Hombre Bestia": {
        "reino": "Reino de las Bestias",
        "capital": "Claro Ancestral",
        "historia": "En el Claro Ancestral, la estatua de Kaelen Garraferoz se alza como un tributo al instinto indomable. Su imagen recuerda a los clanes que, aunque las tierras fueron consumidas, la supervivencia siempre será posible si se honra la memoria de los caídos.",
        "stats_bonus": {"STR": 8, "AGI": 7, "VIT": 6, "LUK": 4, "DES": 3, "INT": 2},
        "subformas": ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"],
        "clases": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"]
    },
    "Draconica": {
        "reino": "Imperio de las Cenizas",
        "capital": "Ciudadela de Escamas",
        "historia": "En la Ciudadela de Escamas, los dracónicos mantienen un monumento eterno a los cuatro héroes, reconociendo que sin su batalla, el fuego primordial se habría extinguido.",
        "stats_bonus": {"STR": 10, "VIT": 10, "INT": 7, "DES": 4, "AGI": 3, "LUK": 2},
        "clases": ["Guerrero Dragón", "Mago de Sangre", "Custodio de Escamas", "Acechador Dracónico"]
    }
}

# Funciones de consulta para el Agente de Misiones
def obtener_contexto_mision(tipo: str):
    return MAPA_NARRATIVO_MISIONES.get(tipo, {})

def obtener_cinematica_inicial():
    return CINEMATICA_INICIAL

def obtener_prologo_jugador(raza: str) -> str:
    info = HISTORIA_RAZAS_DETALLADA.get(raza)
    return f"Bienvenido a {info['reino']}. {info['historia']}" if info else "Bienvenido."
