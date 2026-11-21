"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona las 4 razas, sus clases compatibles, sub-formas de Hombres Bestia y verificaciones.
"""

from typing import Dict, List, Optional

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

RAZAS_Y_CLASES: Dict[str, Dict] = {
    "Humano": {
        "descripcion": "Raza equilibrada y adaptable con gran potencial marcial y magico.",
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
        "stats_iniciales": {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10}
    },
    "Elfo": {
        "descripcion": "Raza afin con la naturaleza y los vientos. No usan clerigos; el Druida asume sanacion y soporte.",
        "clases": [
            "Guardabosques",
            "Alcaide",
            "Druida",
            "Espadachin Silvano",
            "Monje del Viento",      # Variante Pugil
            "Acechador Nocturno",    # Variante Asesino
            "Mago de Batalla",
            "Invocador"
        ],
        "stats_iniciales": {"STR": 7, "INT": 12, "AGI": 13, "VIT": 8, "LUK": 10, "DES": 12}
    },
    "Enano": {
        "descripcion": "Maestros de la forja, la runa y la resistencia inquebrantable.",
        "clases": [
            "Guerrero Pesado",
            "Defensor Runico de Asedio",
            "Campeon Runico",
            "Luchador de Puno de Hierro",  # Variante Pugil
            "Ballestero",                  # Variante Explorador
            "Asesino",
            "Mago de Batalla",
            "Invocador",
            "Clerigo"
        ],
        "stats_iniciales": {"STR": 13, "INT": 8, "AGI": 6, "VIT": 14, "LUK": 9, "DES": 10}
    },
    "Hombre Bestia": {
        "descripcion": "Poder salvaje ancestral con 7 sub-formas totemicas.",
        "subformas": SUBFORMAS_HOMBRE_BESTIA,
        "clases": [
            "Campeon",
            "Acechador Salvaje",
            "Chaman Primordial",
            "Pugil",  # Incluye variantes y estado frenetico tipo Berserker
            "Asesino",
            "Explorador",
            "Mago de Batalla",
            "Invocador",
            "Clerigo"
        ],
        "stats_iniciales": {"STR": 12, "INT": 7, "AGI": 11, "VIT": 12, "LUK": 8, "DES": 10}
    }
}

class PersonajeRazaClase:
    def __init__(self, nombre: str, raza: str, clase: str, subforma_bestia: Optional[str] = None):
        if raza not in RAZAS_Y_CLASES:
            raise ValueError(f"Raza invalida: {raza}")
        
        info_raza = RAZAS_Y_CLASES[raza]
        if clase not in info_raza["clases"]:
            raise ValueError(f"La clase '{clase}' no esta disponible para la raza '{raza}'.")
        
        if raza == "Hombre Bestia":
            if not subforma_bestia or subforma_bestia not in SUBFORMAS_HOMBRE_BESTIA:
                raise ValueError(f"Debes seleccionar una subforma valida para Hombre Bestia: {SUBFORMAS_HOMBRE_BESTIA}")
            self.subforma_bestia = subforma_bestia
        else:
            self.subforma_bestia = None

        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.stats = dict(info_raza["stats_iniciales"])

    def es_compatible(self, raza_requerida: Optional[str], clase_requerida: Optional[str]) -> bool:
        """Verifica compatibilidad para equipamiento o habilidades."""
        if raza_requerida and raza_requerida != self.raza:
            return False
        if clase_requerida and clase_requerida != self.clase:
            return False
        return True
