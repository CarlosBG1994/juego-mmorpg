"""
Modulo: Mundo y PvE de Snd-Worlds
Gestiona los 4 reinos del Continente Primordial, zonas por nivel,
jefes de zona, mazmorras con respawn y detalles geográficos.
"""

# Configuración de los 4 Reinos: Geografía y Estructura
REINOS_PRIMORDIALES = {
    "Reino Humano": {
        "capital": "Fortaleza Solar",
        "raza": "Humano",
        "extension_km2": 450_000,
        "ciudades_principales": ["Ciudadela del Alba", "Puerto del Rey", "Villa Hierro"],
        "puertas_y_fronteras": ["Puerta del Sol Naciente", "Paso de la Guardia"],
        "castillos": ["Castillo de Aurelius", "Baluarte del León"]
    },
    "Reino Elfo": {
        "capital": "Arbol Corazon de Sylva",
        "raza": "Elfo",
        "extension_km2": 520_000,
        "ciudades_principales": ["Refugio de la Hoja", "Santuario Lunar", "Arboleda Susurrante"],
        "puertas_y_fronteras": ["Arco de Raíces", "Puerta de los Vientos"],
        "castillos": ["Palacio de Cristal Élfico", "Torreón de Thalor'en"]
    },
    "Reino Enano": {
        "capital": "Forja Profunda de Kar-Drak",
        "raza": "Enano",
        "extension_km2": 380_000,
        "ciudades_principales": ["Yunque de Piedra", "Ciudad Subterránea de Oro", "Mina del Trueno"],
        "puertas_y_fronteras": ["Gran Portal de Roca", "Pasaje del Yunque"],
        "castillos": ["Ciudadela Forjaeterna", "Baluarte de Bramir"]
    },
    "Reino Hombre Bestia": {
        "capital": "Bastion Primordial de los Clanes",
        "raza": "Hombre Bestia",
        "extension_km2": 600_000,
        "ciudades_principales": ["Claro del Rugido", "Villa de los Huesos", "Campamento de la Luna"],
        "puertas_y_fronteras": ["Entrada del Tótem", "Cerca de Espinas"],
        "castillos": ["Fortaleza de Kaelen", "Salón del Gran Jefe"]
    }
}

RANGOS_ZONAS_REINOS = [
    {"rango": "1-15", "tipo": "Iniciacion y Tierras Bajas"},
    {"rango": "16-25", "tipo": "Valles y Bosques Salvajes"},
    {"rango": "26-35", "tipo": "Tierras Fronterizas"},
    {"rango": "36-45", "tipo": "Zonas Hostiles y Cavernas"},
    {"rango": "46-60", "tipo": "Territorio Peligroso y Bastiones de Elite"}
]

ZONAS_NEUTRALES_UNIDAS = [
    {"rango": "61-75", "descripcion": "Tierras de Nadie Inter-Reinos"},
    {"rango": "76-85", "descripcion": "Grieta de los Antiguos"},
    {"rango": "86-100", "descripcion": "Cumbre del Continente Primordial"}
]

class Mazmorra:
    def __init__(self, nombre: str, nivel_recomendado: int, zona: str, jefe_final: str):
        self.nombre = nombre
        self.nivel_recomendado = nivel_recomendado
        self.zona = zona
        self.jefe_final = jefe_final
        self.cofres_secretos = []
        self.jefe_derrotado = False
        self.tiempo_respawn_minutos = 18

    def anadir_cofre_secreto(self, contenido: dict):
        self.cofres_secretos.append(contenido)

    def derrotar_jefe(self):
        self.jefe_derrotado = True
        return f"¡{self.jefe_final} ha sido derrotado! El jefe reaparecera en {self.tiempo_respawn_minutos} minutos."
