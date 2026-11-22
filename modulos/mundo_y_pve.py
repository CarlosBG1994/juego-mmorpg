"""
Modulo: Mundo y PvE de Snd-Worlds
Gestiona los reinos, geografía detallada, NPCs, puntos de interés y jefes.
"""

REINOS_DETALLADOS = {
    "Reino Humano": {
        "extension_km2": 250_000,
        "puntos_interes": ["Gremio de Caballeros", "Taller de Forja Real", "Taberna del Viajero", "Mercado Central"],
        "npcs_activos": ["Comandante Alaric (Misiones)", "Mercader Silas (Comercio)", "Maestro Artesano Bram (Talleres)"],
        "arquitectura": "Calles empedradas, callejones oscuros con misiones ocultas, murallas de piedra caliza y castillo central vigilado."
    },
    "Reino Elfo": {
        "extension_km2": 250_000,
        "puntos_interes": ["Biblioteca Arcana", "Clínica de Druidas", "Santuario del Viento", "Gremio de Exploradores"],
        "npcs_activos": ["Guardián Thalon", "Druida Lyra", "Elfa del Viento (Misiones secretas)"],
        "arquitectura": "Plataformas colgantes, puentes de luz, callejuelas de ramas entrelazadas, castillos de cristal traslúcido."
    },
    "Reino Enano": {
        "extension_km2": 250_000,
        "puntos_interes": ["Gran Forja de Runas", "Taberna de Cerveza Dorada", "Túneles de Entrenamiento", "Banco de Oro"],
        "npcs_activos": ["Maestro Forjador Durnik", "Sabio Rúnico", "Guardia de Piedra"],
        "arquitectura": "Pasillos de granito pulido, callejones subterráneos, fortalezas talladas en roca viva con luz de magma."
    },
    "Reino Hombre Bestia": {
        "extension_km2": 250_000,
        "puntos_interes": ["Arena de Combate", "Chamán de las Tribus", "Mercado de Pieles", "Cueva de los Ancianos"],
        "npcs_activos": ["Chamán Garra", "Cazador de Manada", "Guerrero Frenético"],
        "arquitectura": "Tiendas de campaña de gran tamaño, caminos de tierra batida, fogatas comunitarias y fortalezas de piedra tosca."
    }
}

# SISTEMA DE MUNDO VIVO (Capa de visualización para el motor)
GEOGRAFIA_DETALLADA = {
    "Entornos": ["Montañas escarpadas con picos nevados", "Bosques densos con árboles de éter", "Caminos serpenteantes con piedras rúnicas"],
    "Monstruos_por_Zona": {
        "1-15": ["Lobos de Pradera", "Bandidos de Camino", "Slimes de Eter"],
        "46-60": ["Centinelas de Acero", "Espíritus del Bosque Oscuro", "Bestias Abisales"],
        "86-100": ["Dragones del Nexo", "Caballeros Caídos", "Ecos de Malakor'zeth"]
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
        return f"¡{self.jefe_final} derrotado! Cofre abierto. Respawn en {self.respawn_jefe} min."

# Integración con el Motor de Streaming (World_Sync)
def obtener_escena_jugador(posicion_x, posicion_y):
    """Retorna los datos de visualización para el cliente (árboles, npcs, caminos)."""
    return {"entidades": "Cargando render de alta definición de NPCs y entorno dinámico"}
