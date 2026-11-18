# --- MÓDULO DE MISIONES, PROGRESIÓN DE CONTINENTES Y OBJETOS MÍTICOS ---

SISTEMA_MISIONES = {
    "principales": [
        {
            "id": "mq_01",
            "titulo": "El Despertar en Valoria",
            "nivel_requerido": 1,
            "continente": "Continente I",
            "descripcion": "Habla con el Maestro Aldric en Aurelia Capital y elimina a tus primeros 5 Goblins para asegurar los caminos del reino.",
            "objetivo": "Derrotar Goblins (0/5) y hablar con Aldric",
            "recompensa": {"exp": 500, "oro": 150, "item": "Espada de Bronce Reforzada"},
            "desbloquea": "Acceso libre a los Reinos Fundacionales (Niveles 1-60)"
        },
        {
            "id": "mq_02",
            "titulo": "La Amenaza de las Sombras Profundas",
            "nivel_requerido": 30,
            "continente": "Continente I",
            "descripcion": "Las criaturas corruptas del bosque central han mutado. Adéntrate en el territorio de los Ents Corruptos y recupera el Sello Real.",
            "objetivo": "Derrotar Ents Corruptos (0/10) y recolectar Esencia de Roble",
            "recompensa": {"exp": 3500, "oro": 1200, "item": "Armadura de Malla de Mithril"},
            "desbloquea": "Desbloqueo de Zonas Neutras del Continente I (Niveles 61-100)"
        },
        {
            "id": "mq_03",
            "titulo": "La Conquista de las Puertas del Eón",
            "nivel_requerido": 80,
            "continente": "Continente I (Zona Neutra)",
            "descripcion": "El portal que conecta con los continentes superiores e inferiores se ha destabilizado. Debes derrotar al Guardián del Abismo.",
            "objetivo": "Derrotar al Jefe de Zona: Guardián de Piedra Corrupto",
            "recompensa": {"exp": 15000, "oro": 5000, "item": "Grimorio del Sol Eterno (Tier Épico)"},
            "desbloquea": "Acceso a los Continentes II y III (Mazmorras de Raid y Santuarios de Ángeles y Demonios)"
        }
    ],
    "secundarias": [
        {
            "id": "sq_01",
            "titulo": "Raciones para la Guardia",
            "nivel_requerido": 5,
            "descripcion": "El cocinero de la guarnición necesita carne de lobo fresca para alimentar a las patrullas nocturnas.",
            "objetivo": "Recolectar Carne de Lobo (0/4)",
            "recompensa": {"exp": 300, "oro": 80, "reputacion": "Valoria +15"}
        },
        {
            "id": "sq_02",
            "titulo": "El Encargo del Herrero Bran",
            "nivel_requerido": 15,
            "descripcion": "El mineral de hierro escasea en los talleres de la capital. Extrae mineral en las canteras del sur.",
            "objetivo": "Recolectar Mineral de Hierro Puro (0/6)",
            "recompensa": {"exp": 950, "oro": 250, "profesion": "Herrería +50 XP"}
        }
    ],
    "ocultas_miticas": [
        {
            "id": "mq_mythic_01",
            "titulo": "Rumores de Taberna y Susurros Callejeros",
            "nivel_requerido": 50,
            "pista_inicial": "Habla con los plebeyos y ciudadanos corrientes que pasean por los callejones de Aurelia Capital.",
            "pasos": [
                "1. Escuchar los rumores de 3 ciudadanos diferentes en la calle.",
                "2. Encontrar al Ermitaje Oculto de Maestro Ignis en los límites del bosque.",
                "3. Derrotar al acechador nocturno sin recibir daño crítico.",
                "4. Obtener los 3 Fragmentos de la Estrella Caída."
            ],
            "recompensa_mitica": {
                "nombre_arma": "Sol Invictus (Espada Mítica - Tier IV)",
                "atributos": "+450 Daño Físcio, +15% Velocidad de Ataque, Efecto pasivo: Quemadura estelar al golpear",
                "rareza": "Mítica (Soul-Bound: No, intercambiable en comercio global)"
            }
        },
        {
            "id": "mq_mythic_02",
            "titulo": "El Legado del Rey Caído",
            "nivel_requerido": 90,
            "pista_inicial": "Un misterioso plebeyo mendigo cerca del puerto marítimo menciona un santuario olvidado bajo el castillo.",
            "pasos": [
                "1. Infiltrarse en las catacumbas del Castillo de Hojacero.",
                "2. Resolver el enigma de las baldosas de luz y sombra.",
                "3. Derrotar al Avatar de la Sombra en combate individual."
            ],
            "recompensa_mitica": {
                "nombre_armadura": "Armadura de Placas del Dragón Celestial (Set Mítico)",
                "atributos": "+1200 Armadura, +250 Resistencia Mágica, Inmunidad a estados alterados de miedo",
                "rareza": "Mítica Absoluta"
            }
        }
    ]
}