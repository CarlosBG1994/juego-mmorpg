# --- CATÁLOGO MASIVO DE MISIONES, ZONAS Y MÍTICAS ---

SISTEMA_MISIONES = {
    "principales": [
        {
            "id": "mq_01",
            "titulo": "El Despertar en Valoria",
            "nivel_requerido": 1,
            "zona": "Reino Humano de Valoria",
            "descripcion": "Habla con el Maestro Aldric en Aurelia Capital y elimina a tus primeros 5 Goblins.",
            "objetivo": "Derrotar Goblins (0/5) y hablar con Aldric",
            "recompensa": {"exp": 500, "oro": 150, "item": "Espada de Bronce Reforzada"},
            "desbloquea": "Acceso a los Reinos Fundacionales y Murallas de la Capital"
        },
        {
            "id": "mq_02",
            "titulo": "La Amenaza de las Sombras Profundas",
            "nivel_requerido": 30,
            "zona": "Bosque Ancestral de Elfos",
            "descripcion": "Adéntrate en el territorio de los Ents Corruptos y recupera el Sello Real del bosque.",
            "objetivo": "Derrotar Ents Corruptos (0/10) y recolectar Esencia de Roble",
            "recompensa": {"exp": 3500, "oro": 1200, "item": "Armadura de Malla de Mithril"},
            "desbloquea": "Desbloqueo de Zonas Neutras y Puertas del Eón"
        },
        {
            "id": "mq_03",
            "titulo": "La Conquista de las Puertas del Eón",
            "nivel_requerido": 80,
            "zona": "Zona Neutra - Puertas del Eón",
            "descripcion": "El portal que conecta con los continentes superiores se ha destabilizado.",
            "objetivo": "Derrotar al Guardián de Piedra Corrupto",
            "recompensa": {"exp": 15000, "oro": 5000, "item": "Grimorio del Sol Eterno"},
            "desbloquea": "Acceso al Continente II y Mazmorras de Raid"
        }
    ],
    "secundarias": [
        {
            "id": "sq_01",
            "titulo": "Raciones para la Guardia",
            "nivel_requerido": 5,
            "zona": "Reino Humano de Valoria",
            "descripcion": "El cocinero de la guarnición necesita carne de lobo fresca.",
            "objetivo": "Recolectar Carne de Lobo (0/4)",
            "recompensa": {"exp": 300, "oro": 80}
        },
        {
            "id": "sq_02",
            "titulo": "El Encargo del Herrero Bran",
            "nivel_requerido": 15,
            "zona": "Baluarte Enano de Piedra",
            "descripcion": "Extrae mineral de hierro en las canteras del sur.",
            "objetivo": "Recolectar Mineral de Hierro Puro (0/6)",
            "recompensa": {"exp": 950, "oro": 250}
        },
        {
            "id": "sq_03",
            "titulo": "Limpieza en el Puerto Mercante",
            "nivel_requerido": 25,
            "zona": "Puerto y Archipiélago del Sur",
            "descripcion": "Los slimes ácidos están corroyendo los cascos de los barcos comerciales.",
            "objetivo": "Eliminar Slimes Ácidos (0/8)",
            "recompensa": {"exp": 1800, "oro": 600}
        }
    ],
    "ocultas_miticas": [
        {
            "id": "mq_mythic_01",
            "titulo": "Rumores de Taberna y Susurros Callejeros",
            "nivel_requerido": 50,
            "zona": "Aurelia Capital",
            "pista_inicial": "Habla con los plebeyos y ciudadanos corrientes que pasean por los callejones.",
            "pasos": [
                "1. Escuchar los rumores de 3 ciudadanos diferentes en la calle.",
                "2. Encontrar el Ermitaje Oculto de Maestro Ignis en los límites del bosque.",
                "3. Derrotar al acechador nocturno en la mazmorra secreta.",
                "4. Obtener los 3 Fragmentos de la Estrella Caída."
            ],
            "recompensa_mitica": {
                "nombre_arma": "Sol Invictus (Espada Mítica - Tier IV)",
                "atributos": "+450 Daño Físico, +15% Velocidad de Ataque",
                "rareza": "Mítica"
            }
        },
        {
            "id": "mq_mythic_02",
            "titulo": "El Legado del Rey Caído",
            "nivel_requerido": 90,
            "zona": "Castillo de Hojacero",
            "pista_inicial": "Un misterioso plebeyo mendigo cerca del puerto marítimo menciona un santuario olvidado bajo el castillo.",
            "pasos": [
                "1. Infiltrarse en las catacumbas del Castillo.",
                "2. Resolver el enigma de las baldosas de luz y sombra.",
                "3. Derrotar al Avatar de la Sombra en combate individual."
            ],
            "recompensa_mitica": {
                "nombre_armadura": "Armadura de Placas del Dragón Celestial (Set Mítico)",
                "atributos": "+1200 Armadura, +250 Resistencia Mágica",
                "rareza": "Mítica Absoluta"
            }
        }
    ]
}