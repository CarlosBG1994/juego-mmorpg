"""
Modulo: modulos/razas_y_clases.py
Gestiona las Razas, Subformas de Hombre Bestia, Clases y Estadisticas base de Snd-Worlds.
"""

ESTADISTICAS_BASE = ["STR", "INT", "AGI", "VIT", "LUK", "DES"]

SUBFORMAS_HOMBRE_BESTIA = [
    "Hombre Lobo",
    "Hombre Pantera",
    "Hombre Tigre",
    "Hombre Leon",
    "Hombre Mono",
    "Hombre Tortuga",
    "Hombre Panda"
]

RAZAS_Y_CLASES = {
    "Humano": {
        "clases": [
            "Caballero",
            "Paladin",
            "Mago de Batalla",
            "Pugil",
            "Asesino",
            "Explorador",
            "Invocador",
            "Clerigo"
        ],
        "bono_stats": {"STR": 5, "INT": 5, "AGI": 5, "VIT": 5, "LUK": 5, "DES": 5}
    },
    "Elfo": {
        # Regla: No tienen Clerigo; el Druida asume sanacion y soporte
        "clases": [
            "Guardabosques",
            "Alcaide",
            "Druida",
            "Espadachin Silvano",
            "Monje del Viento", # Pugil elfico
            "Acechador Nocturno", # Asesino elfico
            "Mago de Batalla",
            "Invocador"
        ],
        "bono_stats": {"STR": 2, "INT": 8, "AGI": 8, "VIT": 3, "LUK": 4, "DES": 5}
    },
    "Enano": {
        "clases": [
            "Guerrero Pesado",
            "Defensor Runico de Asedio",
            "Campeon Runico",
            "Luchador de Puno de Hierro", # Pugil enano
            "Ballestero", # Explorador enano
            "Asesino",
            "Mago de Batalla",
            "Invocador",
            "Clerigo"
        ],
        "bono_stats": {"STR": 8, "INT": 3, "AGI": 2, "VIT": 10, "LUK": 3, "DES": 4}
    },
    "Hombre Bestia": {
        "subformas": SUBFORMAS_HOMBRE_BESTIA,
        "clases": [
            "Campeon",
            "Acechador Salvaje",
            "Chaman Primordial",
            "Pugil", # Incluye variantes/estado frenetico tipo Berserker
            "Asesino",
            "Explorador",
            "Mago de Batalla",
            "Invocador",
            "Clerigo"
        ],
        "bono_stats": {"STR": 8, "INT": 2, "AGI": 7, "VIT": 6, "LUK": 4, "DES": 3}
    }
}

class PersonajeBase:
    def __init__(self, nombre: str, raza: str, clase: str, subforma: str = None):
        if raza not in RAZAS_Y_CLASES:
            raise ValueError(f"Raza invalida: {raza}")
        if clase not in RAZAS_Y_CLASES[raza]["clases"]:
            raise ValueError(f"La clase {clase} no es valida para la raza {raza}")
        if raza == "Hombre Bestia" and subforma not in SUBFORMAS_HOMBRE_BESTIA:
            raise ValueError(f"Subforma obligatoria y valida para Hombre Bestia. Opciones: {SUBFORMAS_HOMBRE_BESTIA}")

        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.subforma = subforma
        self.stats = {stat: 10 + RAZAS_Y_CLASES[raza]["bono_stats"].get(stat, 0) for stat in ESTADISTICAS_BASE}

    def es_compatible(self, raza_requerida: str, clase_requerida: str) -> bool:
        """Verifica compatibilidad para equipar habilidades."""
        raza_ok = (raza_requerida is None or raza_requerida == self.raza)
        clase_ok = (clase_requerida is None or clase_requerida == self.clase)
        return raza_ok and clase_ok

    def a_diccionario(self) -> dict:
        return {
            "nombre": self.nombre,
            "raza": self.raza,
            "subforma": self.subforma,
            "clase": self.clase,
            "stats": self.stats
        }
