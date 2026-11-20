# --- CONFIGURACIÓN GLOBAL DE SND-WORLDS MMORPG (config.py) ---

CONTINENTE_INICIAL = "Continente Inicial: Tierras del Origen (Niveles 1–100)"

CONTINENTES_RACIALES = [
    "Continente Racial Humano",
    "Continente Racial Élfico",
    "Continente Racial Enano",
    "Continente Racial Dracónico",
]

CONTINENTE_DEMONIACO = "Continente Demoníaco: Abismo Ígneo (Niveles 301–350)"
CONTINENTE_ANGELICAL = "Continente Angelical: Ciudadela Celestial (Final)"

RANGOS_POR_ORDEN_RACIAL = [
    "101–150",
    "151–200",
    "201–250",
    "251–300",
]

DATOS_MUNDO = {
    "nombre_mundo": "Snd-Worlds (Guerra de los Eones)",
    "superficie_km2": 1500000,
    "escala_mapa_unidades": 120000,
    "continente_inicial": CONTINENTE_INICIAL,
    "continentes_raciales": CONTINENTES_RACIALES,
    "continente_demoniaco": CONTINENTE_DEMONIACO,
    "continente_angelical": CONTINENTE_ANGELICAL,
    "zonas_por_continente": {
        CONTINENTE_INICIAL: [
            "Valoria Inicial",
            "Llanuras del Comienzo",
            "Bosque de Bruma",
            "Puertas del Eón",
        ],
        "Continente Racial Humano": [
            "Aurelia Capital",
            "Murallas de Hojacero",
            "Tierras Fronterizas Humanas",
        ],
        "Continente Racial Élfico": [
            "Santuario Silvestre",
            "Arboleda Eterna",
            "Cañada de los Susurros",
        ],
        "Continente Racial Enano": [
            "Baluarte de Piedra",
            "Grandes Fundiciones",
            "Galerías Profundas",
        ],
        "Continente Racial Dracónico": [
            "Cumbre de Escamas",
            "Caldera de Ceniza",
            "Santuario del Draco",
        ],
        CONTINENTE_DEMONIACO: [
            "Fosas del Abismo",
            "Ciudadela Carmesí",
            "Trono de las Sombras",
        ],
        CONTINENTE_ANGELICAL: [
            "Pináculo de Luz",
            "Jardines del Alba",
            "Umbral del Creador",
        ],
    },
    "clases_personaje": [
        {"nombre": "Púgil", "rol": "Combate cuerpo a cuerpo / Artes marciales", "ataque_base": "Físico"},
        {"nombre": "Guerrero", "rol": "Tanque / Armaduras pesadas", "ataque_base": "Físico"},
        {"nombre": "Mago", "rol": "Daño mágico a distancia", "ataque_base": "Mágico"},
        {"nombre": "Asesino", "rol": "Agilidad y sigilo", "ataque_base": "Físico"},
    ],
    "monturas_disponibles": [
        {"nombre": "A Pie (Velocidad Base)", "bonus_velocidad": 1.0, "coste": 0, "requisito": "Ninguno"},
        {"nombre": "Caballo de Guerra Blindado", "bonus_velocidad": 1.8, "coste": 2500, "requisito": "Nivel 25"},
        {"nombre": "Lobo Huargo del Norte", "bonus_velocidad": 2.3, "coste": 6000, "requisito": "Nivel 50"},
        {"nombre": "Grifo de los Cielos (Vuelo)", "bonus_velocidad": 3.2, "coste": 25000, "requisito": "Nivel 80"},
    ],
}