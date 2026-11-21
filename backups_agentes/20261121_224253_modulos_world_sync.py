"""
Modulo: World Sync
Responsabilidad:
- Carga masiva (Streaming) de particiones del mundo.
- Particionamiento lógico de zonas para optimización.
- Sincronización de datos de posición y objetivos para grupos.
"""

import math

class GestorZonas:
    """Gestiona la división del mundo en particiones para optimizar la carga."""
    def __init__(self):
        self.particiones_activas = {}  # {id_zona: [lista_jugadores]}

    def registrar_jugador_en_zona(self, id_jugador: str, zona: str):
        if zona not in self.particiones_activas:
            self.particiones_activas[zona] = []
        self.particiones_activas[zona].append(id_jugador)
        return f"Jugador {id_jugador} asignado a la partición {zona}."

class SincronizadorGrupo:
    """Mantiene la coherencia de datos de minimapa para grupos activos."""
    def __init__(self):
        self.grupos_activos = {} # {id_grupo: {"miembros": [], "posiciones": {}}}

    def actualizar_posicion_miembro(self, id_grupo: str, id_jugador: str, x: float, y: float):
        if id_grupo in self.grupos_activos:
            self.grupos_activos[id_grupo]["posiciones"][id_jugador] = {"x": x, "y": y}
            return True
        return False

    def obtener_vista_grupo(self, id_grupo: str):
        """Retorna las posiciones de todos los miembros para renderizar el minimapa."""
        return self.grupos_activos.get(id_grupo, {}).get("posiciones", {})

class MotorStreamingMundo:
    """Carga y descarga zonas basándose en la proximidad del jugador."""
    @staticmethod
    def calcular_distancia(pos1: dict, pos2: dict):
        return math.sqrt((pos1['x'] - pos2['x'])**2 + (pos1['y'] - pos2['y'])**2)

    def determinar_cargas(self, jugador_pos: dict, radio_carga: int = 500):
        # Lógica para determinar qué zonas deben estar en memoria activa
        return f"Cargando zonas dentro de un radio de {radio_carga} unidades."
