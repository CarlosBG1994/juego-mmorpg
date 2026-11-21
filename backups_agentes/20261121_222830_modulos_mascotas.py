"""
Modulo: Mascotas de Snd-Worlds
Gestiona los compañeros de aventura. Tienen nivel, lealtad,
habilidades pasivas, atributos de combate y potencial para PvP.
"""

class Mascota:
    def __init__(self, nombre: str, tipo: str, rareza: str, es_adquirible: bool = False, es_unica: bool = False):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza
        self.nivel = 1
        self.lealtad = 50
        self.es_adquirible = es_adquirible
        self.es_unica = es_unica
        
        # Atributos de combate para PvP
        self.stats_combate = {"ATK": 10, "DEF": 10, "VEL": 10}
        self.puntos_entrenamiento = 0 
        
        # Nueva estructura: Habilidades activas y pasivas
        self.habilidades_pasivas = [] 
        self.habilidades_activas = [] # Habilidades usables en combate (ej: "Rugido de Guerra")
        self.ataque_especial = None 

    def ganar_experiencia(self, exp: int):
        if self.nivel < 50:
            aumento = exp // 1000
            self.nivel = min(50, self.nivel + aumento)
            self.puntos_entrenamiento += (aumento * 2) 
            self._actualizar_bonos_pasivos()

    def mejorar_stat_combate(self, stat: str, cantidad: int):
        if stat in self.stats_combate and cantidad <= self.puntos_entrenamiento:
            self.stats_combate[stat] += cantidad
            self.puntos_entrenamiento -= cantidad
            return True
        return False

    def aplicar_sinergia_clase(self, clase_jugador: str):
        """Aplica un bono extra si la mascota es compatible con la clase del jugador."""
        # Ejemplo de sinergia:
        if clase_jugador == "Caballero" and self.tipo == "Gólem":
            self.stats_combate["DEF"] += 15
            return "¡Sinergia Activa: Defensa de Piedra reforzada!"
        return "Sin sinergia especial."

    def _actualizar_bonos_pasivos(self):
        multiplicador = 1 + (self.nivel * 0.05)
        # Lógica de escalado...

    def ejecutar_ataque_mitico(self):
        if self.rareza == "Mítica" and self.ataque_especial:
            return f"{self.nombre} lanza {self.ataque_especial}!"
        return "Acción no disponible."

# --- CATÁLOGOS AMPLIADOS ---
# [Se mantienen los catálogos anteriores intactos]
MASCOTAS_BASE = {
    "Humano": {"nombre": "Cachorro de Grifo", "pasiva": "STR"},
    "Elfo": {"nombre": "Espíritu del Bosque", "pasiva": "INT"},
    "Enano": {"nombre": "Gólem de Piedra", "pasiva": "VIT"},
    "Hombre Bestia": {"nombre": "Cachorro de Lobo", "pasiva": "AGI"}
}

CATALOGO_TIENDA_MASCOTAS = [
    {"nombre": "Gato Callejero", "precio": 500, "pasiva": "LUK"},
    {"nombre": "Halcón Mensajero", "precio": 1200, "pasiva": "DES"},
    {"nombre": "Zorro de Fuego", "precio": 3000, "pasiva": "INT"},
    {"nombre": "Tortuga de Mar", "precio": 2500, "pasiva": "DEF"}
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
