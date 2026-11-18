# --- CONFIGURACIÓN GLOBAL DE SND-WORLDS MMORPG ---

DATOS_MUNDO = {
    "nombre_mundo": "Snd-Worlds (Guerra de los Eones)",
    "superficie_km2": 1500000,
    "escala_niveles": "1 - 100 (Continente I: Niveles 1-60 Reinos Fundacionales, 61-100 Zonas Neutras)",
    "continentes": [
        {
            "nombre": "Continente I: Reinos Fundacionales y Zonas Neutras",
            "niveles": "1 - 100",
            "reinos": [
                {"nombre": "Reino Humano de Valoria", "niveles": "1 - 15", "capital": "Aurelia Capital"},
                {"nombre": "Bosque Ancestral de Elfos", "niveles": "16 - 30", "capital": "Santuario Silvestre"},
                {"nombre": "Baluarte Enano de Piedra", "niveles": "31 - 45", "capital": "Fortaleza de Hierro"},
                {"nombre": "Dominio de los Magos", "niveles": "46 - 60", "capital": "Torre de los Arcanos"}
            ],
            "zonas_neutras": [
                "Puertas del Eón",
                "Archipiélago y Mazmorras del Mar Abierto"
            ]
        },
        {
            "nombre": "Continente II: Tierras de Raid, Santuarios de Ángeles y Demonios",
            "niveles": "101 - 250",
            "zonas": ["Santuario Celestial", "Abismo Demoniaco", "Islas Brumas del Dragón"]
        }
    ],
    "clases_personaje": [
        {"nombre": "Púgil", "rol": "Combate cuerpo a cuerpo / Artes marciales a tiempo real", "ataque_base": "Físico"},
        {"nombre": "Guerrero", "rol": "Tanque / Armaduras pesadas y espada", "ataque_base": "Físico"},
        {"nombre": "Mago", "rol": "Daño mágico a distancia / Hechizos", "ataque_base": "Mágico"},
        {"nombre": "Asesino", "rol": "Agilidad / Críticos y sigilo", "ataque_base": "Físico"}
    ],
    "monturas_disponibles": [
        {"nombre": "A Pie (Velocidad Base)", "bonus_velocidad": 1.0},
        {"nombre": "Caballo de Guerra Blindado", "bonus_velocidad": 1.6},
        {"nombre": "Lobo Huargo del Norte", "bonus_velocidad": 1.9},
        {"nombre": "Grifo de los Cielos (Vuelo)", "bonus_velocidad": 2.5}
    ]
}