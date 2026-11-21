"""
Modulo: Progresion y Estadisticas de Snd-Worlds
Nivel 1-100 inicial, +5 puntos libres por nivel, +10 HP max por nivel.
Desbloqueo de continentes de expansion hasta nivel 300 (+50 niveles por continente).
"""

from typing import Dict

PUNTOS_LIBRES_POR_NIVEL = 5
HP_MAX_POR_NIVEL = 10

CONTINENTES = [
    {"nombre": "Continente Primordial", "limite_nivel": 100},
    {"nombre": "Archipielago de los Vientos", "limite_nivel": 150},
    {"nombre": "Continente Abisal de los Demonios", "limite_nivel": 200},
    {"nombre": "Continente Celestial de los Angeles", "limite_nivel": 250},
    {"nombre": "Nucleo Central de Comercio y Nexo Global", "limite_nivel": 300}
]

class ProgresionPersonaje:
    def __init__(self, nombre: str, stats_iniciales: Dict[str, int], hp_base: int = 100):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        self.experiencia_siguiente = 100
        
        self.stats = dict(stats_iniciales)
        self.puntos_libres = 0
        
        self.hp_base = hp_base
        self.hp_max = hp_base + (self.nivel - 1) * HP_MAX_POR_NIVEL
        self.hp_actual = self.hp_max
        
        self.continente_actual = CONTINENTES[0]["nombre"]
        self.limite_nivel_actual = CONTINENTES[0]["limite_nivel"]

    def ganar_experiencia(self, exp: int):
        self.experiencia += max(0, exp)
        while self.experiencia >= self.experiencia_siguiente and self.nivel < self.limite_nivel_actual:
            self.experiencia -= self.experiencia_siguiente
            self.subir_nivel()

    def subir_nivel(self):
        if self.nivel < self.limite_nivel_actual:
            self.nivel += 1
            self.puntos_libres += PUNTOS_LIBRES_POR_NIVEL
            self.hp_max += HP_MAX_POR_NIVEL
            self.hp_actual = self.hp_max
            self.experiencia_siguiente = int(self.experiencia_siguiente * 1.15) + 50

    def asignar_punto(self, stat: str, cantidad: int = 1) -> bool:
        if stat in self.stats and 0 < cantidad <= self.puntos_libres:
            self.stats[stat] += cantidad
            self.puntos_libres -= cantidad
            return True
        return False

    def desbloquear_siguiente_continente(self) -> bool:
        """Permite avanzar al siguiente continente expandiendo el tope de nivel en +50."""
        for c in CONTINENTES:
            if c["limite_nivel"] > self.limite_nivel_actual:
                self.continente_actual = c["nombre"]
                self.limite_nivel_actual = c["limite_nivel"]
                return True
        return False
