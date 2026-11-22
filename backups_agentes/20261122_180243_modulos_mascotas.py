"""
Modulo: Mascotas de Snd-Worlds
Gestiona los compañeros de aventura. Incluye sistemas de movimiento,
habilidades con rango de efecto (AoE) y combate táctico.
"""

class Mascota:
    def __init__(self, nombre: str, tipo: str, rareza: str, es_adquirible: bool = False, es_unica: bool = False):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
        self.nivel = 1
        self.lealtad = 50
        self.posicion = {"x": 0, "y": 0}
        self.rango_movimiento = 3
        self.stats_combate = {"ATK": 10, "DEF": 10, "VEL": 10}
        self.energia = 100
        self.puntos_entrenamiento = 0 
        self.habilidades_pasivas = [] 
        self.habilidades_activas = [] 
        self.ataque_especial = None 

    def moverse(self, nueva_x: int, nueva_y: int):
        distancia = abs(nueva_x - self.posicion["x"]) + abs(nueva_y - self.posicion["y"])
        if distancia <= self.rango_movimiento:
            self.posicion["x"] = nueva_x
            self.posicion["y"] = nueva_y
            return True, f"{self.nombre} se desplazó a ({nueva_x}, {nueva_y})."
        return False, "Destino fuera de rango."

    def usar_habilidad(self, indice: int, objetivo_x: int, objetivo_y: int):
        if indice < len(self.habilidades_activas):
            hab = self.habilidades_activas[indice]
            distancia = abs(objetivo_x - self.posicion["x"]) + abs(objetivo_y - self.posicion["y"])
            if self.energia >= hab["coste"] and distancia <= hab["rango"]:
                self.energia -= hab["coste"]
                return f"{self.nombre} usa {hab['nombre']} en ({objetivo_x}, {objetivo_y})."
            return "Energía insuficiente o fuera de rango."
        return "Habilidad no encontrada."

# --- GESTOR DE REGISTRO ---
class RegistroMascotas:
    """Clase para añadir nuevas mascotas al juego de forma dinámica."""
    catalogo_global = []

    @classmethod
    def anadir_mascota(cls, nombre, tipo, rareza, es_adquirible=False):
        nueva = {"nombre": nombre, "tipo": tipo, "rareza": rareza, "es_adquirible": es_adquirible}
        cls.catalogo_global.append(nueva)
        return f"Mascota '{nombre}' registrada exitosamente."

# --- CATÁLOGOS BASE ---
MASCOTAS_BASE = {
    "Humano": {"nombre": "Cachorro de Grifo", "pasiva": "STR"},
    "Elfo": {"nombre": "Espíritu del Bosque", "pasiva": "INT"},
    "Enano": {"nombre": "Gólem de Piedra", "pasiva": "VIT"},
    "Hombre Bestia": {"nombre": "Cachorro de Lobo", "pasiva": "AGI"}
}

CATALOGO_TIENDA_MASCOTAS = [
    {"nombre": "Gato Callejero", "precio": 500, "pasiva": "LUK"},
    {"nombre": "Halcón Mensajero", "precio": 1200, "pasiva": "DES"}
]

MASCOTAS_LEGENDARIAS = [
    {"nombre": "Pegaso", "mitologia": "Romana", "rareza": "Leyenda"},
    {"nombre": "Qilin", "mitologia": "China", "rareza": "Leyenda"}
]

MASCOTAS_MITICAS = [
    {"nombre": "Byakko", "elemento": "Metal", "rareza": "Mítica", "ataque": "Zarpazo del Tigre Blanco"},
    {"nombre": "Suzaku", "elemento": "Fuego", "rareza": "Mítica", "ataque": "Llamarada Carmesí"},
    {"nombre": "Genbu", "elemento": "Agua", "rareza": "Mítica", "ataque": "Escudo del Norte"},
    {"nombre": "Seiryu", "elemento": "Madera", "rareza": "Mítica", "ataque": "Aliento del Dragón Azur"},
    {"nombre": "Dragón del Nexo", "elemento": "Eter", "rareza": "Mítica", "ataque": "Pulso del Vacío"}
]
