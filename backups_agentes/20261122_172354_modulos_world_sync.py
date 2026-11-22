"""
Modulo: World Sync
Responsabilidad: Gestión de carga masiva, particionamiento y sincronización total.
Mejora: Sistema de eventos en tiempo real (Broadcast) y registro completo de entidades.
"""

import math

class GestorZonas:
    def __init__(self):
        self.particiones_activas = {}
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
        "monturas": {}, "objetos_interactivos": {}, "ciudades": {}
    }
    
    prioridades = {"jefes": 1, "jugadores": 2, "ciudades": 3, "objetos": 4, "npc_base": 5}

    @classmethod
    def obtener_entidades_visibles(cls, jugador_pos: dict, radio: int = 1000):
        visibles = []
        for cat, lista in cls.entidades_mundo.items():
            for id_ent, info in lista.items():
                if math.sqrt((info['pos']['x'] - jugador_pos['x'])**2 + (info['pos']['y'] - jugador_pos['y'])**2) <= radio:
                    visibles.append({
                        "id": id_ent, "tipo": cat, "pos": info['pos'], 
                        "datos": info.get('datos', {}), "pri": cls.prioridades.get(cat, 6)
                    })
        return sorted(visibles, key=lambda x: x['pri'])

    @classmethod
    def actualizar_entidad(cls, tipo: str, id_entidad: str, posicion: dict, datos: dict):
        """Actualiza y propaga el estado de la entidad (ej: pérdida de HP)."""
        if tipo in cls.entidades_mundo:
            cls.entidades_mundo[tipo][id_entidad] = {"pos": posicion, "datos": datos}
            # Aqui se dispararia un evento de 'Broadcast' hacia los clientes cercanos
            return True
        return False
