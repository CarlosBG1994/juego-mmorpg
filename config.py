# --- CONFIGURACIÓN GLOBAL DE SND-WORLDS ---

CONTINENTE_INICIAL = "Valoria (Continente I)"

CONTINENTES_OFICIALES = {
    "Valoria (Continente I)": {
        "tipo": "Nivel 1 - 100 | Tierras Centrales y Reinos Fundacionales",
        "detalle": "Niveles 1-60 divididos en 4 Reinos (Humano, Elfo, Enano, Hombre Bestia). Niveles 61-100 en Zonas Comunes Neutrales (sin gobierno fijo)."
    },
    "Eldoria (Continente II)": {
        "tipo": "Nivel 101 - 150 | Bosques Arcanos y Tierras Elementales",
        "rango": "101-150"
    },
    "Pyoria (Continente III)": {
        "tipo": "Nivel 151 - 200 | Volcanes, Abismos y Tierras de Bestias Primordiales",
        "rango": "151-200"
    },
    "Noxoria (Continente IV)": {
        "tipo": "Nivel 201 - 250 | El Imperio Oscuro y el Nexo Final (Ángeles y Demonios unidos)",
        "rango": "201-250"
    }
}

REINOS_VALORIA = {
    "Reino Humano de Valoria": {"rango_nivel": "1 - 60", "raza_dominante": "Humano", "asentamiento": "Aurelia Capital"},
    "Bosque Ancestral de Eldoria": {"rango_nivel": "1 - 60", "raza_dominante": "Elfo", "asentamiento": "Sylvanis Refugio"},
    "Fortaleza de Hierro de Pyoria": {"rango_nivel": "1 - 60", "raza_dominante": "Enano", "asentamiento": "Khazad Dun Baluarte"},
    "Estepas Salvajes de Noxoria": {"rango_nivel": "1 - 60", "raza_dominante": "Hombre Bestia", "asentamiento": "Garra de la Tormenta"},
    "Tierras Neutras del Vórtice": {"rango_nivel": "61 - 100", "raza_dominante": "Neutral / Zona Libre", "asentamiento": "Puesto Fronterizo del Ocaso"}
}

RAZAS_Y_CLASSES = {
    "Humano": {
        "clases": ["Invocador", "Guerrero", "Mago de Batalla", "Paladín", "Asesino", "Clérigo", "Cazador de Recompensas", "Bardo Táctico"],
        "reino_inicio": "Reino Humano de Valoria",
        "monturas_exclusivas": ["Caballo de Guerra Real", "Lobo Estepario de Valoria"],
        "lore": "Equilibrio, adaptabilidad y diplomacia entre los reinos."
    },
    "Elfo": {
        "clases": ["Arquero Arcano", "Sacerdotisa de la Luna", "Mago Estelar", "Cazador de Sombras", "Druida de los Bosques", "Caballero Silvano", "Elementalista de la Luz"],
        "reino_inicio": "Bosque Ancestral de Eldoria",
        "monturas_exclusivas": ["Ciervo Etéreo de la Luna", "Pantera de las Sombras Silvanas"],
        "lore": "Maestros de la magia ancestral y la arquería precisa en armonía con la naturaleza."
    },
    "Enano": {
        "clases": ["Herrero de Guerra", "Guardián de Runas", "Berserker de Magma", "Artillero de Asedio", "Ingeniero Rúnico", "Tanque de Mithril", "Sanador de Yunque"],
        "reino_inicio": "Fortaleza de Hierro de Pyoria",
        "monturas_exclusivas": ["Oso Acorazado de las Profundidades", "Jabalí Mecánico de Asedio"],
        "lore": "Inquebrantables protectores de las profundidades y maestros absolutos de la forja."
    },
    "Hombre Bestia": {
        "clases": ["Púgil", "Acechador Salvaje", "Chamán Elemental", "Guerrero Totémico", "Señor de la Manada", "Asesino Feral", "Monje de las Garras"],
        "reino_inicio": "Estepas Salvajes de Noxoria",
        "monturas_exclusivas": ["Tigre Dientes de Sable Gigante", "Huargo Alfa de la Estepa"],
        "lore": "Furia primordial y conexión directa con las fuerzas salvajes del continente."
    },
    "Ángeles y Demonios (Unidos)": {
        "clases": ["Serafín del Juicio", "Señor del Abismo", "Inquisidor Estelar", "Portador del Ocaso", "Templario Celestial", "Brujo del Caos"],
        "reino_inicio": "Santuario del Nexo Celestial",
        "monturas_exclusivas": ["Grifo Alado Celestial", "Pesadilla Abisal de Fuego Negro"],
        "lore": "Alianza universal entre facciones celestiales e infernales para frenar la corrupción total."
    }
}

MONTURAS_COMUNES = [
    "Caballo Trotón del Viajero",
    "Pony de Carga Resistente",
    "Lobo Ligero de Pradera",
    "Corcel Acorazado Común"
]

SUBFORMAS_BESTIA = ["Hombre Lobo", "Hombre Tigre", "Oso Berserker", "Águila Tormentosa", "Quimera Feral"]

ESTADISTICAS_BASE_CLASES = {
    "Invocador": {"str": 5, "int": 18, "agi": 6, "vit": 10, "luk": 12, "hp": 100},
    "Guerrero": {"str": 18, "int": 5, "agi": 10, "vit": 15, "luk": 8, "hp": 130},
    "Mago de Batalla": {"str": 8, "int": 16, "agi": 8, "vit": 12, "luk": 10, "hp": 110},
    "Paladín": {"str": 14, "int": 10, "agi": 6, "vit": 18, "luk": 10, "hp": 140},
    "Asesino": {"str": 12, "int": 6, "agi": 18, "vit": 8, "luk": 14, "hp": 95},
    "Arquero Arcano": {"str": 10, "int": 12, "agi": 16, "vit": 8, "luk": 12, "hp": 100},
    "Sacerdotisa de la Luna": {"str": 6, "int": 16, "agi": 8, "vit": 14, "luk": 12, "hp": 110},
    "Mago Estelar": {"str": 4, "int": 20, "agi": 8, "vit": 8, "luk": 12, "hp": 90},
    "Cazador de Sombras": {"str": 14, "int": 8, "agi": 16, "vit": 8, "luk": 14, "hp": 95},
    "Herrero de Guerra": {"str": 16, "int": 8, "agi": 6, "vit": 16, "luk": 10, "hp": 130},
    "Guardián de Runas": {"str": 12, "int": 12, "agi": 6, "vit": 16, "luk": 10, "hp": 125},
    "Berserker de Magma": {"str": 20, "int": 4, "agi": 12, "vit": 14, "luk": 6, "hp": 140},
    "Artillero de Asedio": {"str": 15, "int": 10, "agi": 8, "vit": 12, "luk": 10, "hp": 115},
    "Púgil": {"str": 16, "int": 6, "agi": 16, "vit": 12, "luk": 10, "hp": 120},
    "Acechador Salvaje": {"str": 14, "int": 6, "agi": 18, "vit": 10, "luk": 12, "hp": 105},
    "Chamán Elemental": {"str": 8, "int": 16, "agi": 8, "vit": 12, "luk": 12, "hp": 105},
    "Guerrero Totémico": {"str": 16, "int": 8, "agi": 10, "vit": 14, "luk": 10, "hp": 125},
    "Clérigo": {"str": 8, "int": 14, "agi": 6, "vit": 16, "luk": 12, "hp": 120},
    "Cazador de Recompensas": {"str": 14, "int": 8, "agi": 15, "vit": 10, "luk": 13, "hp": 110},
    "Bardo Táctico": {"str": 8, "int": 15, "agi": 12, "vit": 10, "luk": 15, "hp": 100},
    "Druida de los Bosques": {"str": 10, "int": 15, "agi": 10, "vit": 14, "luk": 10, "hp": 115},
    "Caballero Silvano": {"str": 16, "int": 8, "agi": 12, "vit": 14, "luk": 10, "hp": 130},
    "Elementalista de la Luz": {"str": 6, "int": 18, "agi": 8, "vit": 10, "luk": 12, "hp": 95},
    "Ingeniero Rúnico": {"str": 12, "int": 14, "agi": 10, "vit": 12, "luk": 10, "hp": 110},
    "Tanque de Mithril": {"str": 18, "int": 4, "agi": 6, "vit": 20, "luk": 8, "hp": 160},
    "Sanador de Yunque": {"str": 10, "int": 14, "agi": 6, "vit": 16, "luk": 10, "hp": 125},
    "Señor de la Manada": {"str": 18, "int": 6, "agi": 14, "vit": 14, "luk": 10, "hp": 135},
    "Asesino Feral": {"str": 14, "int": 6, "agi": 20, "vit": 8, "luk": 12, "hp": 95},
    "Monje de las Garras": {"str": 15, "int": 8, "agi": 16, "vit": 12, "luk": 10, "hp": 115},
    "Serafín del Juicio": {"str": 15, "int": 15, "agi": 12, "vit": 15, "luk": 15, "hp": 140},
    "Señor del Abismo": {"str": 18, "int": 12, "agi": 10, "vit": 16, "luk": 10, "hp": 145},
    "Inquisidor Estelar": {"str": 12, "int": 16, "agi": 12, "vit": 12, "luk": 14, "hp": 120},
    "Portador del Ocaso": {"str": 14, "int": 14, "agi": 14, "vit": 12, "luk": 12, "hp": 120},
    "Templario Celestial": {"str": 16, "int": 10, "agi": 8, "vit": 18, "luk": 10, "hp": 150},
    "Brujo del Caos": {"str": 8, "int": 19, "agi": 10, "vit": 10, "luk": 13, "hp": 100}
}