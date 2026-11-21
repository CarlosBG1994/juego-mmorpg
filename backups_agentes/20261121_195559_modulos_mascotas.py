"""
Modulo: Mascotas de Snd-Worlds
Gestiona los compañeros de aventura. Tienen nivel, lealtad y 
pueden equipar habilidades pasivas.
"""

class Mascota:
    def __init__(self, nombre: str, tipo: str, rareza: str):
        self.nombre = nombre
        self.tipo = tipo  # Ej: Elemental, Bestia, Espiritual
        self.rareza = rareza # Común a Mítica
        self.nivel = 1
        self.lealtad = 50 # 0 a 100
        self.habilidades_pasivas = []

    def ganar_experiencia(self, exp: int):
        # La mascota gana exp proporcional al jugador
        self.nivel = min(50, self.nivel + (exp // 1000))
        
    def modificar_lealtad(self, cantidad: int):
        self.lealtad = max(0, min(100, self.lealtad + cantidad))
