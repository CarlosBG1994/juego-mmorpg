"""
Modulo: Mascotas de Snd-Worlds
Gestiona los compañeros de aventura. Tienen nivel, lealtad,
habilidades pasivas y potencial de ataque para rangos superiores.
"""

class Mascota:
    def __init__(self, nombre: str, tipo: str, rareza: str, es_adquirible: bool = False, es_unica: bool = False):
        self.nombre = nombre
        self.tipo = tipo  # Elemental, Bestia, Espiritual, Dracónica
        self.rareza = rareza  # Común, Poco Común, Raro, Ultra Raro, Leyenda, Mítica
        self.nivel = 1
        self.lealtad = 50 
        self.es_adquirible = es_adquirible # Disponibles en tienda
        self.es_unica = es_unica # Eventos o misiones especiales
        self.habilidades_pasivas = [] # Lista de bonos (ej: {"stat": "STR", "valor": 5})
        self.ataque_especial = None # Solo para míticas

    def ganar_experiencia(self, exp: int):
        if self.nivel < 50:
            self.nivel = min(50, self.nivel + (exp // 1000))
            self._actualizar_bonos_pasivos()

    def modificar_lealtad(self, cantidad: int):
        self.lealtad = max(0, min(100, self.lealtad + cantidad))

    def _actualizar_bonos_pasivos(self):
        # A mayor nivel, mayor efectividad de las pasivas
        multiplicador = 1 + (self.nivel * 0.05)
        # Lógica de escalado de stats aplicada aquí...

    def ejecutar_ataque_mitico(self):
        if self.rareza == "Mítica" and self.ataque_especial:
            return f"{self.nombre} usa {self.ataque_especial}!"
        return "Esta mascota no posee capacidad de ataque."

# Registro de tipos de mascotas por procedencia
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

MASCOTAS_UNICAS = [
    {"nombre": "Fénix Cenizo", "fuente": "Misión Oculta - Volcán", "rareza": "Leyenda"},
    {"nombre": "Dragón del Nexo", "fuente": "Misión Oculta - Abismo", "rareza": "Mítica"}
]
