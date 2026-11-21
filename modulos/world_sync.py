"""
Modulo: World Sync
Responsabilidad:
- Carga masiva (Streaming) de particiones del mundo.
- Particionamiento lógico de zonas para optimización.
- Sincronización de datos de posición y objetivos para grupos.
- Registro global de entidades (Jugadores, Enemigos, Mascotas, Monturas, Objetos).
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
    
    # Registro de todas las entidades activas para visibilidad total
    entidades_mundo = {
        "jugadores": {},
        "enemigos": {},
        "mascotas": {},
        "monturas": {},
        "objetos_interactivos": {} # Cofres, elementos de mazmorra, etc.
    }

    @staticmethod
    def calcular_distancia(pos1: dict, pos2: dict):
        return math.sqrt((pos1['x'] - pos2['x'])**2 + (pos1['y'] - pos2['y'])**2)

    @classmethod
    def actualizar_entidad(cls, tipo: str, id_entidad: str, posicion: dict):
        """Actualiza la posición de cualquier entidad para que sea visible por otros jugadores."""
        if tipo in cls.entidades_mundo:
            cls.entidades_mundo[tipo][id_entidad] = posicion
            return True
        return False

    def determinar_cargas(self, jugador_pos: dict, radio_carga: int = 500):
        """Calcula todas las entidades visibles en el radio del jugador (Enemigos, Mascotas, etc)."""
        visibles = []
        for categoria, lista in self.entidades_mundo.items():
            for id_ent, pos in lista.items():
                if self.calcular_distancia(jugador_pos, pos) <= radio_carga:
                    visibles.append({"tipo": categoria, "id": id_ent, "pos": pos})
        return visibles
