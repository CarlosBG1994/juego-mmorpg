"""
Modulo: Mundo y PvE de Snd-Worlds
Gestiona los 4 reinos del Continente Primordial, zonas por nivel,
jefes de zona, mazmorras con respawn y detalles geográficos.
"""

# Geografía: 1.500.000 km2 totales
# Distribución: Humano (350k), Elfo (400k), Enano (300k), Bestia (350k), Neutral (100k)
REINOS_PRIMORDIALES = {
    "Reino Humano": {
        "capital": "Fortaleza Solar",
        "extension_km2": 350_000,
        "ciudades": ["Ciudadela del Alba", "Puerto del Rey", "Villa Hierro"],
        "pueblos": ["Valle Verde", "Paso del Escudo", "Aldea del Río"],
        "puertas": ["Puerta del Sol Naciente", "Paso de la Guardia"],
        "castillos": ["Castillo de Aurelius", "Baluarte del León"]
    },
    "Reino Elfo": {
        "capital": "Arbol Corazon de Sylva",
        "extension_km2": 400_000,
        "ciudades": ["Refugio de la Hoja", "Santuario Lunar", "Arboleda Susurrante"],
        "pueblos": ["Aldea de los Cánticos", "Puesto del Rocío", "Enclave Silvano"],
        "puertas": ["Arco de Raíces", "Puerta de los Vientos"],
        "castillos": ["Palacio de Cristal Élfico", "Torreón de Thalor'en"]
    },
    "Reino Enano": {
        "capital": "Forja Profunda de Kar-Drak",
        "extension_km2": 300_000,
        "ciudades": ["Yunque de Piedra", "Ciudad Subterránea de Oro", "Mina del Trueno"],
        "pueblos": ["Martillo de Hierro", "Fosa de Carbón", "Pico del Yunque"],
        "puertas": ["Gran Portal de Roca", "Pasaje del Yunque"],
        "castillos": ["Ciudadela Forjaeterna", "Baluarte de Bramir"]
    },
    "Reino Hombre Bestia": {
        "capital": "Bastion Primordial de los Clanes",
        "extension_km2": 350_000,
        "ciudades": ["Claro del Rugido", "Villa de los Huesos", "Campamento de la Luna"],
        "pueblos": ["Aldea de las Garras", "Paso de la Manada", "Santuario de los Ancestros"],
        "puertas": ["Entrada del Tótem", "Cerca de Espinas"],
        "castillos": ["Fortaleza de Kaelen", "Salón del Gran Jefe"]
    }
}

DESCRIPCIONES_ARQUITECTONICAS = {
    "Reino Humano": "Casas de piedra y madera con techos de teja. Ciudades organizadas en cuadrícula alrededor de castillos de piedra caliza con altas torres vigía.",
    "Reino Elfo": "Construcciones vivas integradas en árboles gigantes y cristal. Los castillos son estructuras translúcidas que parecen flotar sobre los bosques.",
    "Reino Enano": "Arquitectura tallada directamente en la roca de las montañas. Casas robustas con arcos de hierro, castillos que son fortalezas impenetrables de granito reforzado.",
    "Reino Hombre Bestia": "Aldeas de tiendas circulares de cuero reforzado y madera tallada. Castillos construidos sobre colinas escarpadas con huesos y piedra tosca."
}

ZONAS_NEUTRALES_UNIDAS = {
    "extension_km2": 100_000,
    "asentamientos": ["Puesto Comercial del Nexo", "Refugio de los Perdidos"],
    "descripciones": ["Tierras de Nadie", "Grieta de los Antiguos", "Cumbre del Continente"]
}

RANGOS_ZONAS_REINOS = [
    {"rango": "1-15", "tipo": "Iniciacion y Tierras Bajas"},
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
