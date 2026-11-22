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

# --- CINEMÁTICA Y TEXTO DE PRIMERA VEZ (REGISTRO INICIAL) ---
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
    "batalla final provocó el Gran Cataclismo: una catástrofe colosal que partió la tierra que antes "
    "unía todos los reinos, separándola en distintos continentes rodeados por mares indómitos. Con "
    "la caída de los Xylaroth y el desgarro del mundo, toda la civilización antigua se perdió, "
    "dejando sus ciudades, templos y fortalezas sepultadas como ruinas olvidadas que aún hoy "
    "pueden encontrarse repartidas por todo el continente.\n\n"
    "Obligados a empezar de cero tras el cataclismo, los supervivientes de las cuatro razas se "
    "asentaron en sus propios reinos sobre el nuevo continente para levantar un nuevo hogar.\n\n"
    "Hoy el eco de aquella guerra y los secretos de la era antigua siguen latentes... y tu historia empieza aquí."
)

# --- TRASFONDO Y CARACTERÍSTICAS DE LAS RAZAS ---
HISTORIA_RAZAS_DETALLADA = {
    "Humano": {
        "reino": "Reino Humano",
        "capital": "Corona de Luz",
        "historia": (
            "Tras la guerra contra los Xylaroth y el Gran Cataclismo, los humanos se asentaron en tierras "
            "abiertas y fértiles del nuevo continente, fundando Corona de Luz para reconstruir la civilización "
            "y el orden, mientras exploran los restos de la civilización antigua perdida."
        ),
        "estatua_heroe": "Aurelius del Alba",
        "stats_bonus": {"STR": 5, "INT": 5, "AGI": 5, "VIT": 5, "LUK": 5, "DES": 5},
        "clases": ["Caballero", "Paladín", "Mago de Batalla", "Púgil", "Asesino", "Explorador", "Invocador", "Clérigo"]
    },
    "Elfo": {
        "reino": "Reino Élfico",
        "capital": "Árbol de la Aurora",
        "historia": (
            "Tras la caída de sus antiguos hogares, los elfos buscaron refugio en los bosques vivos y enclaves "
            "mágicos del nuevo continente, levantando Árbol de la Aurora en profunda conexión con la naturaleza "
            "y los vestigios antiguos."
        ),
        "estatua_heroe": "Thalor’en",
        "stats_bonus": {"INT": 8, "AGI": 8, "DES": 5, "LUK": 4, "VIT": 3, "STR": 2},
        "clases": ["Guardabosques", "Alcaide", "Druida", "Espadachín Silvano", "Monje del Viento (Púgil)", "Acechador Nocturno (Asesino)", "Mago de Batalla", "Invocador"]
    },
    "Enano": {
        "reino": "Reino Enano",
        "capital": "Baluarte Forjaeterna",
        "historia": (
            "Tras el Gran Cataclismo, los enanos se establecieron en las montañas y profundidades ricas en "
            "minerales del nuevo continente, edificando Baluarte Forjaeterna como un bastión defensivo, centro "
            "de forja, ingeniería y estudio de ruinas antiguas."
        ),
        "estatua_heroe": "Bramir Peñahonda",
        "stats_bonus": {"VIT": 10, "STR": 8, "DES": 5, "LUK": 4, "INT": 3, "AGI": 2},
        "clases": ["Guerrero Pesado", "Defensor Rúnico de Asedio", "Campeón Rúnico", "Luchador de Puño de Hierro (Púgil)", "Ballestero (Explorador)", "Asesino", "Mago de Batalla", "Invocador", "Clérigo"]
    },
    "Hombre Bestia": {
        "reino": "Reino de las Bestias",
        "capital": "Claro Ancestral",
        "historia": (
            "Tras la oscuridad que consumió los antiguos territorios, los Hombres Bestia se reunieron en las tierras "
            "salvajes del nuevo continente, estableciendo Claro Ancestral bajo el signo del instinto, la manada "
            "y la supervivencia frente a los restos de la era antigua."
        ),
        "estatua_heroe": "Kaelen Garraferoz",
        "stats_bonus": {"STR": 8, "AGI": 7, "VIT": 6, "LUK": 4, "DES": 3, "INT": 2},
        "subformas": ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre León", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"],
        "clases": ["Campeón", "Acechador Salvaje", "Chamán Primordial", "Púgil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clérigo"]
    },
    "Draconica": {
        "reino": "Imperio de las Cenizas",
        "capital": "Ciudadela de Escamas",
        "historia": (
            "Descendientes de los antiguos dragones que combatieron en las fallas del Gran Cataclismo. "
            "En la Ciudadela de Escamas mantienen un monumento eterno a los cuatro héroes y preservan el "
            "conocimiento arcano del fuego primordial."
        ),
        "estatua_heroe": "Monumento a los Cuatro Libertadores",
        "stats_bonus": {"STR": 10, "VIT": 10, "INT": 7, "DES": 4, "AGI": 3, "LUK": 2},
        "clases": ["Guerrero Dragón", "Mago de Sangre", "Custodio de Escamas", "Acechador Dracónico"]
    }
}

# Compatibilidad con sistemas existentes
HISTORIA_REINOS = {r: {"reino": d["reino"], "capital": d["capital"], "trasfondo": d["historia"]} for r, d in HISTORIA_RAZAS_DETALLADA.items()}

# --- INSCRIPCIONES Y LEYENDAS DE LAS ESTATUAS HEROICAS ---
INSCRIPCIONES_ESTATUAS = {
    "Aurelius del Alba": {
        "ubicacion": "Plaza Mayor de Corona de Luz",
        "inscripcion": "Que la espada de la rectitud corte las sombras del abismo. Ni un paso atrás ante el miedo.",
        "relato_local": (
            "Los ancianos relatan que Aurelius atravesó el portal de los Xylaroth empuñando una hoja bañada "
            "en luz estelar. Su sacrificio concedió a las razas el tiempo necesario para sellar la grieta."
        )
    },
    "Thalor’en": {
        "ubicacion": "Raíz Central de Árbol de la Aurora",
        "inscripcion": "El viento susurra el dolor de las raíces partidas; la naturaleza jamás olvida el sacrificio.",
        "relato_local": (
            "Thalor’en entregó su propia savia espiritual para erigir las murallas arbóreas que frenaron a las hordas "
            "demoníacas mientras la tierra se resquebrajaba."
        )
    },
    "Bramir Peñahonda": {
        "ubicacion": "Atrio de Piedra en Baluarte Forjaeterna",
        "inscripcion": "Inquebrantables como la roca madre, firmes ante el fuego del cataclismo.",
        "relato_local": (
            "Dicen que Bramir descargó su mazo rúnico directamente contra el artefacto oscuro de Malakor’zeth. "
            "El impacto quebró el artefacto y la tierra, pero salvó la vida de incontables inocentes."
        )
    },
    "Kaelen Garraferoz": {
        "ubicacion": "Tótem Sagrado en Claro Ancestral",
        "inscripcion": "El rugido de la manada resuena en la eternidad. La sangre caída nutre nuestro porvenir.",
        "relato_local": (
            "Kaelen lideró la carga salvaje contra los generales abisales, demostrando que ninguna cadena demoníaca "
            "podía doblegar el espíritu de las bestias."
        )
    }
}

# --- MISIÓN PRINCIPAL 1: ARRANQUE NARRATIVO POR RAZA ---
MISION_PRINCIPAL_1_LORE = {
    "Humano": {
        "id": "MP_HUM_001",
        "titulo": "La Sombra del Alba",
        "npc_emisor": "Comandante Alaric (junto a la Estatua de Aurelius)",
        "dialogo_inicio": (
            "Bienvenido a Corona de Luz, recluta. Las campanas tocan por una razón: cazadores de la frontera "
            "informan de actividad demoníaca residual en las ruinas de la Zona 1-15. Acércate a la estatua de "
            "Aurelius, recibe su bendición y toma tus primeras armas para asegurar el camino."
        ),
        "objetivo_narrativo": "Interactuar con la estatua de Aurelius del Alba y despejar la avanzadilla en la Zona 1-15."
    },
    "Elfo": {
        "id": "MP_ELF_001",
        "titulo": "El Susurro de las Hojas",
        "npc_emisor": "Guardián Thalon (bajo la Estatua de Thalor’en)",
        "dialogo_inicio": (
            "Viajero del bosque, Árbol de la Aurora siente vibraciones inquietantes. La tierra que se partió en el "
            "Gran Cataclismo parece recordar viejas heridas. Escucha el susurro de Thalor’en ante su monumento "
            "y sal a investigar los límites del bosque en la Zona 1-15."
        ),
        "objetivo_narrativo": "Meditar ante la estatua de Thalor’en y neutralizar la corrupción botánica en la Zona 1-15."
    },
    "Enano": {
        "id": "MP_ENA_001",
        "titulo": "Ecos en la Forja",
        "npc_emisor": "Maestro Forjador Durnik (junto a la Estatua de Bramir)",
        "dialogo_inicio": (
            "¡Por las barbas de nuestros ancestros! Las excavaciones en las minas exteriores han dado con vestigios "
            "de la guerra antigua. Bramir Peñahonda no forjó nuestras defensas para que nos escondamos. Toca su roca "
            "sagrada, afila tu acero y baja a limpiar los accesos de la Zona 1-15."
        ),
        "objetivo_narrativo": "Rendir honores a la estatua de Bramir Peñahonda y derrotar a los invasores de la mina en la Zona 1-15."
    },
    "Hombre Bestia": {
        "id": "MP_BES_001",
        "titulo": "El Llamado de la Manada",
        "npc_emisor": "Chamán Garra (junto a la Estatua de Kaelen)",
        "dialogo_inicio": (
            "Joven hermano de clan, el viento arrastra olor a azufre y ceniza antigua. Kaelen Garraferoz nos enseñó "
            "que la debilidad se paga con la extinción. Ruge frente al tótem de Kaelen en el Claro Ancestral y sal "
            "a rastrear las bestias descarriadas en la Zona 1-15."
        ),
        "objetivo_narrativo": "Presentar respetos en el tótem de Kaelen Garraferoz y liderar la primera cacería en la Zona 1-15."
    },
    "Draconica": {
        "id": "MP_DRA_001",
        "titulo": "El Fuego que Nunca se Apaga",
        "npc_emisor": "Custodio de Escamas Ignis",
        "dialogo_inicio": (
            "Las brasas del Imperio de las Cenizas despiertan. Recuerda el juramento hecho a los héroes de la antigua "
            "alianza. Dirígete a la avanzadilla de la Zona 1-15 y demuestra que el linaje de dragón vigila el Continente."
        ),
        "objetivo_narrativo": "Examinar el Monumento a los Cuatro Libertadores y patrullar la frontera volcánica en la Zona 1-15."
    }
}

# --- GEOGRAFÍA Y NARRATIVA DE ZONAS (CONTINENTE PRIMORDIAL: 1 A 100) ---
NARRATIVA_ZONAS_PRIMORDIAL = {
    "1-15": {
        "denominacion": "Periferia del Reino y Caminos Seguros",
        "ambiente": "Colinas verdes, granjas reconstruidas, caminos patrullados por guardias.",
        "conflicto": "Bandidos errantes, bestias menores alteradas por vetas de éter y criaturas de reconocimiento.",
        "jefes_elite": ["Capitán Bandido Garrote", "Lobo Alfa Cicatrizado", "Bruto del Fango"]
    },
    "16-25": {
        "denominacion": "Rutas Comerciales y Puestos de Avanzada",
        "ambiente": "Encrucijadas empedradas, puentes de peaje y asentamientos de mercaderes.",
        "conflicto": "Asaltos a caravanas comerciales y saboteadores que buscan cortar suministros entre reinos.",
        "jefes_elite": ["Salteador de Caminos Voraz", "Arácnida de Bosque Profundo", "Golem de Piedra Fisurado"]
    },
    "26-35": {
        "denominacion": "Fronteras Disputadas y Valles de Niebla",
        "ambiente": "Valles húmedos con neblina constante, atalayas fronterizas y bosques sombríos.",
        "conflicto": "Tensiones territoriales y primeras manifestaciones de vestigios corrompidos por los Xylaroth.",
        "jefes_elite": ["Aparición de la Niebla", "Cazador Sombrío", "Ogro de Trinchera"]
    },
    "36-45": {
        "denominacion": "Campos de la Primera Fractura",
        "ambiente": "Gargantas escarpadas donde la tierra se abrió durante el Gran Cataclismo.",
        "conflicto": "Grietas ardientes donde emana energía del abismo y autómatas antiguos descontrolados.",
        "jefes_elite": ["Centinela de Fuego Rúnico", "Víbora de las Grietas", "Devorador de Éter"]
    },
    "46-60": {
        "denominacion": "Ruinas Olvidadas de la Civilización Antigua",
        "ambiente": "Templos semisepultados, murallas derruidas cubiertas de musgo y cámaras subterráneas.",
        "conflicto": "Guardianes mágicos que protegen los archivos de la era previa al cataclismo.",
        "jefes_elite": ["Custodio del Templo Caído", "Caballero Fantasma de Aurelius", "Leviatán de Ruina"]
    },
    "61-75": {
        "denominacion": "Tierras de Nadie: El Desierto de Ceniza",
        "ambiente": "Páramo estéril que no pertenece a ningún reino. Arena gris y torres de vigía desiertas.",
        "conflicto": "Supervivencia extrema, monstruos errantes de alto nivel y cazadores furtivos sin ley.",
        "jefes_elite": ["Gusano de Ceniza Colosal", "Señor de la Guerra Proscrito", "Quimera del Yermo"]
    },
    "76-85": {
        "denominacion": "Tierras de Nadie: La Garganta de los Ecos",
        "ambiente": "Cañón profundo donde el viento reproduce lamentos de la antigua guerra.",
        "conflicto": "Fuerzas remanentes de demonios menores y barreras arcanas que impiden el paso al Centro.",
        "jefes_elite": ["Inquisidor del Abismo Menor", "Gárgola Pétrea Milenaria", "Pesadilla Aullante"]
    },
    "86-100": {
        "denominacion": "El Umbral del Nexo (Centro del Continente Primordial)",
        "ambiente": "Círculo de monolitos titánicos que rodean el vórtice central sellado tras la victoria de los cuatro héroes.",
        "conflicto": "Ecos directos de Malakor’zeth y los protectores definitivos del Continente Primordial.",
        "jefes_elite": ["Avatar del Nexo Corrupto", "General Xylaroth Resurgido", "Dragón Guardián del Umbral"]
    }
}

# --- MAPA DE NAVEGACIÓN Y COORDINACIÓN CON AGENTE DE MISIONES ---
MAPA_NARRATIVO_MISIONES = {
    "Principal": {
        "origen": "Estatua del Héroe Local en la Capital",
        "progresion": [
            "Capital (Zona 1-15)",
            "Rutas de Enlace y Puestos (Zonas 16-25)",
            "Fronteras y Campos de Batalla (Zonas 26-45)",
            "Ruinas Antiguas (Zonas 46-60)",
            "Tierras de Nadie (Zonas 61-85)",
            "El Umbral del Nexo Central (Zonas 86-100)"
        ],
        "objetivo": "Descubrir la verdad del Gran Cataclismo, recuperar fragmentos antiguos y desbloquear el paso al Archipiélago de los Vientos."
    },
    "Secundaria": {
        "origen": "Tablón de Gremio, Comerciantes y Habitantes de cada ciudad",
        "temas": [
            "Escolta de caravanas entre capitales",
            "Suministro de metal rúnico y materias primas a los talleres",
            "Eliminación de bestias élite que amenazan los asentamientos",
            "Recuperación de reliquias familiares perdidas en el cataclismo"
        ],
        "dinamica": "Generación procedural según la franja de nivel de la zona."
    },
    "Oculta": {
        "origen": "Inscripciones secretas en estatuas, libros en bibliotecas arcanas, objetos en cofres de mazmorras",
        "temas": [
            "Las Memorias Perdidas de Malakor’zeth",
            "El Diario Oculto de Bramir Peñahonda",
            "El Artefacto Oscuro que consumió los antiguos hogares",
            "La Llave del Viento hacia el Nivel 101"
        ],
        "requisito": "Nivel de reputación, inspección minuciosa o tenencia de llaves antiguas."
    }
}

CRONICA_CONTINENTE_PRIMORDIAL = {
    "eje_central": "La Búsqueda del Nexo",
    "objetivo_global": "Unir los fragmentos de la civilización antigua y llegar al Centro del Continente.",
    "pilares_narrativos": {
        "ruta_viajero": "El jugador debe conectar las 4 capitales. Cada tramo exige negociar con NPCs, escoltar caravanas y desbloquear zonas fronterizas (1-15 a 86-100).",
        "estatuas_heroicas": "En cada ciudad, las estatuas de Aurelius, Thalor’en, Bramir y Kaelen guardan inscripciones. Los jugadores deben interactuar con ellas para activar misiones de memoria histórica sobre la guerra contra Malakor’zeth.",
        "vestigios_antiguos": "Las ruinas esparcidas contienen artefactos. Misiones de recolección de registros, fragmentos de metal rúnico o piedras etéreas que, al ser entregadas en el Centro, revelan la verdad del Gran Cataclismo."
    }
}

# --- PROGRESIÓN MUNDIAL Y CONTINENTES OCULTOS (101 A 300) ---
DESTINOS_DEL_MUNDO = [
    {
        "fase": 1,
        "nombre": "Continente Primordial",
        "limite_nivel": 100,
        "meta": "Dominar el propio reino, recorrer las ciudades hermanas y conquistar las Tierras de Nadie hasta el Nexo Central.",
        "lore": "La cuna de los supervivientes tras el Gran Cataclismo."
    },
    {
        "fase": 2,
        "nombre": "Archipielago de los Vientos",
        "limite_nivel": 150,
        "meta": "Surcar corrientes aéreas, dominar islas flotantes y descubrir santuarios celestes.",
        "lore": "Fragmentos de tierra que salieron despedidos hacia la atmósfera superior por la violencia del choque elemental."
    },
    {
        "fase": 3,
        "nombre": "Continente Abisal de los Demonios",
        "limite_nivel": 200,
        "meta": "Descender a las fallas donde los Xylaroth yacen encarcelados y evitar la rotura definitiva de los sellos.",
        "lore": "Tierra calcinada donde la gravedad y el tiempo se distorsionan bajo el influjo de Malakor’zeth."
    },
    {
        "fase": 4,
        "nombre": "Continente Celestial de los Angeles",
        "limite_nivel": 250,
        "meta": "Superar los juicios de las agujas de luz primordial y obtener la bendición cósmica.",
        "lore": "Un reino de luz cegadora que permaneció sellado para aislarse de la corrupción abisal."
    },
    {
        "fase": 5,
        "nombre": "Nucleo Central de Comercio y Nexo Global",
        "limite_nivel": 300,
        "meta": "Conectar todos los mundos restaurados, participar en el mercado universal y alcanzar la maestría suprema.",
        "lore": "El corazón de la realidad donde todas las líneas temporales y rutas comerciales se cruzan."
    }
]

# --- FUNCIONES DE CONSULTA PARA OTROS AGENTES Y MÓDULOS ---
def obtener_cinematica_inicial() -> str:
    """Retorna la cinemática íntegra de introducción para el registro del jugador."""
    return CINEMATICA_INICIAL

def obtener_contexto_mision(tipo: str) -> dict:
    """Permite al Agente de Misiones consultar los pilares narrativos por tipo."""
    return MAPA_NARRATIVO_MISIONES.get(tipo, {})

def obtener_mision_principal_1(raza: str) -> dict:
    """Entrega los datos de inicio de la primera misión de campaña para la raza elegida."""
    return MISION_PRINCIPAL_1_LORE.get(raza, MISION_PRINCIPAL_1_LORE["Humano"])

def obtener_inscripcion_estatua(nombre_heroe: str) -> dict:
    """Entrega el texto de ambientación e inscripción de la estatua solicitada."""
    return INSCRIPCIONES_ESTATUAS.get(nombre_heroe, {})

def obtener_lore_zona(zona_rango: str) -> dict:
    """Retorna la descripción ambiental, conflicto y jefes élite de la zona solicitada."""
    return NARRATIVA_ZONAS_PRIMORDIAL.get(zona_rango, {})

def obtener_prologo_jugador(raza: str) -> str:
    """Genera el mensaje de bienvenida y primer paso según el reino del personaje."""
    info = HISTORIA_RAZAS_DETALLADA.get(raza)
    if not info:
        return "Bienvenido a Snd-Worlds. Tu viaje está por comenzar."
    
    return (
        f"Bienvenido a las tierras de {info['reino']}, con capital en {info['capital']}.\n"
        f"{info['historia']}\n\n"
        f"En la plaza central descansa el monumento a {info['estatua_heroe']}. "
        f"Tus primeros pasos tendrán lugar en las Zonas 1-15. Encuentra habilidades en cofres, "
        f"perfecciona tus ataques y forja tu leyenda antes de adentrarte hacia las fronteras."
    )
