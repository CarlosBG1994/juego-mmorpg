# --- CONFIGURACIÓN GLOBAL DE SND-WORLDS MMORPG ---

DATOS_MUNDO = {
    "nombre_mundo": "Snd-Worlds (Guerra de los Eones)",
    "superficie_km2": 1500000,
    "escala_niveles": "1 - 300+ (Sistema Multicontinente)",
    "continentes": [
        {
            "id": "c1",
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
            "id": "c2",
            "nombre": "Continente II: Tierras de Ceniza y Abismos Antiguos",
            "niveles": "101 - 200",
            "reinos": [
                {"nombre": "Desierto de Obsidiana", "niveles": "101 - 130", "capital": "Ciudadela del Sol Negro"},
                {"nombre": "Cavernas del Dragón", "niveles": "131 - 160", "capital": "Guarida de Escamas"}
            ],
            "zonas_neutras": ["Fosas Abisales del Titán", "Picos de los Vientos Eternos"]
        },
        {
            "id": "c3",
            "nombre": "Continente III: El Dominio Celestial y Grietas del Vacío",
            "niveles": "201 - 300",
            "reinos": [
                {"nombre": "Santuario Estelar", "niveles": "201 - 250", "capital": "Catedral del Creador"}
            ],
            "zonas_neutras": ["Grieta Cuántica del Eón"]
        }
    ],
    "clases_personaje": [
        {"nombre": "Púgil", "rol": "Combate cuerpo a cuerpo / Artes marciales", "ataque_base": "Físico"},
        {"nombre": "Guerrero", "rol": "Tanque / Armaduras pesadas", "ataque_base": "Físico"},
        {"nombre": "Mago", "rol": "Daño mágico a distancia", "ataque_base": "Mágico"},
        {"nombre": "Asesino", "rol": "Agilidad y sigilo", "ataque_base": "Físico"}
    ],
    "monturas_disponibles": [
        {"nombre": "A Pie (Velocidad Base)", "bonus_velocidad": 1.0, "coste": 0, "requisito": "Ninguno"},
        {"nombre": "Caballo de Guerra Blindado", "bonus_velocidad": 1.6, "coste": 2500, "requisito": "Nivel 25"},
        {"nombre": "Lobo Huargo del Norte", "bonus_velocidad": 1.9, "coste": 6000, "requisito": "Nivel 50"},
        {"nombre": "Grifo de los Cielos (Vuelo)", "bonus_velocidad": 2.5, "coste": 25000, "requisito": "Nivel 80"}
    ]
}