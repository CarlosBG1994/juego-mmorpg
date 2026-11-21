"""
Modulo: Mundo y PvE de Snd-Worlds
Gestiona los 4 reinos del Continente Primordial, zonas por nivel,
jefes de zona, mazmorras con respawn y detalles geográficos.
"""

# Geografía: 1.500.000 km2 totales
# Distribución: Humano (250k), Elfo (250k), Enano (250k), Bestia (250k), Nexo Neutral (500k)
REINOS_PRIMORDIALES = {
    "Reino Humano": {
        "capital": "Fortaleza Solar",
        "extension_km2": 250_000,
        "ciudades": ["Ciudadela del Alba", "Puerto del Rey", "Villa Hierro"],
        "pueblos": ["Valle Verde", "Paso del Escudo", "Aldea del Río"],
        "puertas": ["Puerta del Sol Naciente", "Paso de la Guardia"],
        "castillos": ["Castillo de Aurelius", "Baluarte del León"]
    },
    "Reino Elfo": {
        "capital": "Arbol Corazon de Sylva",
        "extension_km2": 250_000,
        "ciudades": ["Refugio de la Hoja", "Santuario Lunar", "Arboleda Susurrante"],
        "pueblos": ["Aldea de los Cánticos", "Puesto del Rocío", "Enclave Silvano"],
        "puertas": ["Arco de Raíces", "Puerta de los Vientos"],
        "castillos": ["Palacio de Cristal Élfico", "Torreón de Thalor'en"]
    },
    "Reino Enano": {
        "capital": "Forja Profunda de Kar-Drak",
        "extension_km2": 250_000,
        "ciudades": ["Yunque de Piedra", "Ciudad Subterránea de Oro", "Mina del Trueno"],
        "pueblos": ["Martillo de Hierro", "Fosa de Carbón", "Pico del Yunque"],
        "puertas": ["Gran Portal de Roca", "Pasaje del Yunque"],
        "castillos": ["Ciudadela Forjaeterna", "Baluarte de Bramir"]
    },
    "Reino Hombre Bestia": {
        "capital": "Bastion Primordial de los Clanes",
        "extension_km2": 250_000,
        "ciudades": ["Claro del Rugido", "Villa de los Huesos", "Campamento de la Luna"],
        "pueblos": ["Aldea de las Garras", "Paso de la Manada", "Santuario de los Ancestros"],
        "puertas": ["Entrada del Tótem", "Cerca de Espinas"],
        "castillos": ["Fortaleza de Kaelen", "Salón del Gran Jefe"]
    }
}

DESCRIPCIONES_ARQUITECTONICAS = {
    "Reino Humano": "Estilo medieval clásico. Puertos llenos de actividad comercial, ciudades de piedra caliza con murallas organizadas y castillos con atalayas que vigilan los caminos.",
    "Reino Elfo": "Arquitectura orgánica. Las ciudades son plataformas suspendidas en árboles, conectadas por puentes de luz. Puertos fluviales que fluyen sin romper la corriente natural.",
    "Reino Enano": "Arquitectura monolítica y subterránea. Sus ciudades son complejos de túneles iluminados por lava, con puertos excavados en lagos subterráneos de aguas termales.",
    "Reino Hombre Bestia": "Arquitectura nómada y tribal. Ciudades de piedra bruta y cuero reforzado. Sus puertos son asentamientos en muelles de madera robusta en las orillas de los grandes ríos."
}

# Zonas Centrales (El Nexo)
ZONAS_NEUTRALES_UNIDAS = {
    "extension_km2": 500_000,
    "asentamientos": ["Metrópolis del Nexo", "Puesto Comercial de Hierro", "Cárcel de los Exiliados"],
    "descripciones": ["Corazón del Continente", "Tierras del Eter Residual", "Meseta de la Convergencia"]
}

RANGOS_ZONAS_REINOS = [
    {"rango": "1-15", "tipo": "Iniciación y Tierras Bajas"},
    {"rango": "16-25", "tipo": "Valles y Bosques Salvajes"},
    {"rango": "26-35", "tipo": "Tierras Fronterizas"},
    {"rango": "36-45", "tipo": "Zonas Hostiles y Cavernas"},
    {"rango": "46-60", "tipo": "Territorio Peligroso y Bastiones de Elite"}
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
