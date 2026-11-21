"""
Modulo: modulos/progresion_y_stats.py
Gestiona los niveles 1-300, continentes, +5 puntos libres por nivel y +10 HP maximo por nivel.
"""

CONTINENTES_Y_LIMITES = {
    "Continente Primordial": 100,
    "Archipielago de los Vientos": 150,
    "Continente Abisal de los Demonios": 200,
    "Continente Celestial de los Angeles": 250,
    "Nucleo Central de Comercio y Nexo Global": 300
}

class ProgresionPersonaje:
    def __init__(self, personaje_base):
        self.personaje = personaje_base
        self.nivel = 1
        self.exp = 0
        self.puntos_libres = 0
        self.hp_maximo = 100 # HP base inicial
        self.continente_actual = "Continente Primordial"

    def limite_actual(self) -> int:
        return CONTINENTES_Y_LIMITES.get(self.continente_actual, 100)

    def subir_nivel(self):
        limite = self.limite_actual()
        if self.nivel >= limite:
            return False, f"Alcanzado nivel maximo para {self.continente_actual} ({limite})"

        self.nivel += 1
        self.puntos_libres += 5
        self.hp_maximo += 10
        return True, f"¡Nivel {self.nivel}! +5 puntos de stats libres y +10 HP maximo."

    def asignar_punto_stat(self, stat: str, cantidad: int = 1) -> bool:
        if stat in self.personaje.stats and self.puntos_libres >= cantidad:
            self.personaje.stats[stat] += cantidad
            self.puntos_libres -= cantidad
            return True
        return False

    def viajar_a_continente(self, continente: str) -> bool:
        if continente in CONTINENTES_Y_LIMITES:
            self.continente_actual = continente
            return True
        return False
