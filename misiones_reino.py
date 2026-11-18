# --- CATÁLOGO DE MISIONES Y MÍTICAS ---

SISTEMA_MISIONES = {
    "principales": [
        {
            "id": "mq_01",
            "titulo": "El Despertar en Valoria",
            "nivel_requerido": 1,
            "zona": "Reino Humano de Valoria",
            "descripcion": "Habla con el Maestro Aldric en Aurelia Capital y elimina a tus primeros 5 Goblins.",
            "objetivo": "Derrotar Goblins (0/5)",
            "recompensa": {"exp": 500, "oro": 150, "item": "Espada de Bronce"},
            "desbloquea": "Acceso a la Capital"
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
                "1. Escuchar los rumores de 3 ciudadanos.",
                "2. Encontrar el Ermitaje Oculto.",
                "3. Derrotar al acechador nocturno."
            ],
            "recompensa_mitica": {
                "nombre_recompensa": "Sol Invictus (Espada Mítica)",
                "atributos": "+450 Daño Físico",
                "rareza": "Mítica"
            }
        }
    ]
}