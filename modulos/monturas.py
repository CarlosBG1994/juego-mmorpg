"""
Modulo: Monturas de Snd-Worlds
Gestiona los medios de transporte. Ofrecen velocidad de movimiento
y bonos de capacidad de carga.
"""

class Montura:
    def __init__(self, nombre: str, velocidad: float, bono_carga: int):
        self.nombre = nombre
        self.velocidad = velocidad # Multiplicador de velocidad base
        self.bono_carga = bono_carga # Espacios extra en mochila
        self.fatiga = 0 # Si llega a 100, la montura necesita descansar

    def usar_montura(self):
        if self.fatiga < 100:
            self.fatiga += 5
            return True
        return False # Necesita descanso

    def descansar(self):
        self.fatiga = 0
