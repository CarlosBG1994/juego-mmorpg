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

HISTORIA_REINOS = {
    "Humano": {
        "reino": "Reino Humano",
        "capital": "Fortaleza Solar",
        "trasfondo": "Custodios del orden, el acero y la fe de los paladines en llanuras abiertas."
    },
    "Elfo": {
        "reino": "Reino Elfo",
        "capital": "Arbol Corazon de Sylva",
        "trasfondo": "Protectores del bosque ancestral; no usan clerigos, sino la comunion druidica."
    },
    "Enano": {
        "reino": "Reino Enano",
        "capital": "Forja Profunda de Kar-Drak",
        "trasfondo": "Maestros forjadores y de la runa, excavando los secretos minerales en las profundidades."
    },
    "Hombre Bestia": {
        "reino": "Reino Hombre Bestia",
        "capital": "Bastion Primordial de los Clanes",
        "subformas": [
            "Hombre Lobo", "Hombre Pantera", "Hombre Tigre",
            "Hombre Leon", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"
        ],
        "trasfondo": "Clanes totemicos de gran ferocidad y tradicion chamanica guiados por el instinto."
    }
}

DESTINOS_DEL_MUNDO = [
    {"fase": 1, "nombre": "Continente Primordial", "limite_nivel": 100, "meta": "Dominar el propio reino y cruzar las Tierras de Nadie."},
    {"fase": 2, "nombre": "Archipielago de los Vientos", "limite_nivel": 150, "meta": "Navegar las corrientes etereas y descubrir islas flotantes."},
    {"fase": 3, "nombre": "Continente Abisal de los Demonios", "limite_nivel": 200, "meta": "Descender a las fosas de fuego y oscuridad."},
    {"fase": 4, "nombre": "Continente Celestial de los Angeles", "limite_nivel": 250, "meta": "Ascender a las agujas sagradas de luz primordial."},
    {"fase": 5, "nombre": "Nucleo Central de Comercio y Nexo Global", "limite_nivel": 300, "meta": "El centro del universo restaurado."}
]

def obtener_prologo_jugador(raza: str) -> str:
    info_raza = HISTORIA_REINOS.get(raza)
    if not info_raza:
        return "Bienvenido a Snd-Worlds. Tu viaje esta por comenzar."
    
    return (
        f"Bienvenido a las tierras de {info_raza['reino']}, con sede en {info_raza['capital']}.\n"
        f"{info_raza['trasfondo']}\n"
        f"Tus primeros pasos seran en las Zonas 1-15. Encuentra habilidades, perfecciona tus ataques "
        f"y forja tu nombre antes de aventurarte hacia las fronteras."
    )
