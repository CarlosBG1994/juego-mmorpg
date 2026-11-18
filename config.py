# --- CONFIGURACIÓN GLOBAL DE SND-WORLDS MMORPG ---

DATOS_MUNDO = {
    "nombre_mundo": "Snd-Worlds (Guerra de los Eones)",
    "superficie_km2": 1500000,
    "continentes": [
        {
            "nombre": "Continente I: Valoria y Reinos Fundacionales",
            "niveles": "1 - 100",
            "zonas": [
                "Reino Humano de Valoria",
                "Bosque Ancestral de Elfos",
                "Baluarte Enano de Piedra",
                "Puerto y Archipiélago del Sur"
            ]
        },
        {
            "nombre": "Continente II: Tierras de Raid y Mazmorras Ocultas",
            "niveles": "101 - 250",
            "zonas": ["Santuario de las Sombras", "Islas Brumas del Dragón"]
        }
    ],
    "monturas_disponibles": [
        {"nombre": "A Pie (Velocidad Base)", "bonus_velocidad": 1.0},
        {"nombre": "Caballo de Guerra Blindado", "bonus_velocidad": 1.6},
        {"nombre": "Lobo Huargo del Norte", "bonus_velocidad": 1.9},
        {"nombre": "Grifo de los Cielos (Vuelo)", "bonus_velocidad": 2.5}
    ]
}