"""
Modulo: Mundo y PvE de Snd-Worlds
Gestiona los reinos, geografía, NPCs, sistemas de oficios (talleres) y PvE.
"""

# Sistema de Oficios y Talleres por Reino
TALLERES_POR_REINO = {
    "Reino Humano": ["Forja Real", "Laboratorio de Alquimia", "Taller de Cuero y Telas", "Inscripción de Pergaminos"],
    "Reino Elfo": ["Jardín de Infusión Arcana", "Taller de Cristalería Mágica", "Artesanía de Madera Etérea"],
    "Reino Enano": ["Forja de Magma", "Taller de Ingeniería Rúnica", "Taller de Gemología", "Cantería de Precisión"],
    "Reino Hombre Bestia": ["Taller de Curtido de Pieles", "Forja de Hueso y Acero", "Herbolaria Ancestral"]
}

REINOS_DETALLADOS = {
    "Reino Humano": {
        "extension_km2": 250_000,
        "talleres": TALLERES_POR_REINO["Reino Humano"],
        "puntos_interes": ["Gremio de Caballeros", "Mercado Central", "Taberna del Viajero"],
        "npcs_activos": ["Maestro Artesano Bram", "Comerciante Silas", "Guardia de Ciudad"],
        "arquitectura": "Calles empedradas, callejones con misiones ocultas, murallas de caliza."
    },
    "Reino Elfo": {
        "extension_km2": 250_000,
        "talleres": TALLERES_POR_REINO["Reino Elfo"],
        "puntos_interes": ["Biblioteca Arcana", "Santuario del Viento", "Gremio de Exploradores"],
        "npcs_activos": ["Druida Lyra", "Sabia Thalía", "Elfa del Viento"],
        "arquitectura": "Plataformas colgantes, puentes de luz, torres de cristal traslúcido."
    },
    "Reino Enano": {
        "extension_km2": 250_000,
        "talleres": TALLERES_POR_REINO["Reino Enano"],
        "puntos_interes": ["Gran Forja de Runas", "Banco de Oro", "Túneles de Entrenamiento"],
        "npcs_activos": ["Maestro Durnik", "Sabio Rúnico", "Guardia de Piedra"],
        "arquitectura": "Pasillos de granito pulido, iluminación de magma, fortalezas subterráneas."
    },
    "Reino Hombre Bestia": {
        "extension_km2": 250_000,
        "talleres": TALLERES_POR_REINO["Reino Hombre Bestia"],
        "puntos_interes": ["Arena de Combate", "Chamán de las Tribus", "Mercado de Pieles"],
        "npcs_activos": ["Chamán Garra", "Cazador de Manada", "Guerrero Frenético"],
        "arquitectura": "Tiendas de cuero reforzado, fogatas comunitarias, piedra tosca."
    }
}

# Geografía Dinámica y Jefes
GEOGRAFIA_DETALLADA = {
    "Entornos": ["Montañas escarpadas", "Bosques de éter", "Caminos rúnicos"],
    "Monstruos_y_Jefes": {
        "Zonas_Bajas": {"monstruos": ["Slimes", "Lobos"], "jefes": ["Jefe de Banda Local"]},
        "Zonas_Altas": {"monstruos": ["Centinelas", "Dragones"], "jefes": ["Ecos de Malakor'zeth"]}
    }
}

class Mazmorra:
    def __init__(self, nombre: str, nivel_recomendado: int, zona: str, jefe_final: str):
        self.nombre = nombre
        self.nivel_recomendado = nivel_recomendado
        self.zona = zona
        self.jefe_final = jefe_final
        self.respawn_jefe = 18 # Minutos
        self.npcs_eventos = ["Guía de Mazmorra", "Comerciante de Suministros"]

    def derrotar_jefe(self):
        return f"¡{self.jefe_final} derrotado! Respawn en {self.respawn_jefe} min."

def obtener_escena_jugador(posicion_x, posicion_y):
    return {"entidades": "Renderizado de alta definición con NPCs y talleres activos"}
