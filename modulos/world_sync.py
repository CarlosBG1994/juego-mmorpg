"""
Modulo: World Sync
Responsabilidad: Gestión de carga masiva, particionamiento y sincronización total.
Mejora: Implementación de sistema de prioridades y caché de estado para mazmorras.
"""

import math

class GestorZonas:
    def __init__(self):
        self.particiones_activas = {}
        # Nuevo: Estado de mazmorras para grupos
        self.instancias_mazmorras = {} 

    def registrar_jugador_en_zona(self, id_jugador: str, zona: str):
        if zona not in self.particiones_activas:
            self.particiones_activas[zona] = []
        self.particiones_activas[zona].append(id_jugador)
        return f"Jugador {id_jugador} asignado a la partición {zona}."

class SincronizadorGrupo:
    def __init__(self):
        self.grupos_activos = {}

    def actualizar_posicion_miembro(self, id_grupo: str, id_jugador: str, x: float, y: float):
        if id_grupo in self.grupos_activos:
            self.grupos_activos[id_grupo]["posiciones"][id_jugador] = {"x": x, "y": y}
            return True
        return False

class MotorStreamingMundo:
    entidades_mundo = {
        "jugadores": {}, "enemigos": {}, "mascotas": {}, 
        "monturas": {}, "objetos_interactivos": {}
    }
    
    # Nuevo: Prioridades de visualización
    prioridades = {"jefes": 1, "jugadores": 2, "objetos": 3, "npc_base": 4}

    @classmethod
    def obtener_entidades_priorizadas(cls, jugador_pos: dict, radio: int = 500):
        """Devuelve entidades ordenadas por importancia para el motor gráfico."""
        visibles = []
        # Lógica de filtrado con ordenamiento por prioridad
        for cat, lista in cls.entidades_mundo.items():
            for id_ent, data in lista.items():
                if math.sqrt((data['pos']['x'] - jugador_pos['x'])**2 + (data['pos']['y'] - jugador_pos['y'])**2) <= radio:
                    visibles.append({"id": id_ent, "tipo": cat, "pri": cls.prioridades.get(cat, 5)})
        return sorted(visibles, key=lambda x: x['pri'])

    @classmethod
    def actualizar_entidad(cls, tipo: str, id_entidad: str, datos: dict):
        """Actualiza posición y estado de cualquier entidad."""
        if tipo in cls.entidades_mundo:
            cls.entidades_mundo[tipo][id_entidad] = datos
            return True
        return False
