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
        
        # Posición y Movilidad en mapa reducido
        self.posicion = {"x": 0, "y": 0}
        self.rango_movimiento = 3  # Unidades que puede moverse por turno
        
        # Atributos de combate
        self.stats_combate = {"ATK": 10, "DEF": 10, "VEL": 10}
        self.energia = 100
        self.puntos_entrenamiento = 0 
        
        self.habilidades_pasivas = [] 
        # Estructura: {"nombre": str, "coste": int, "dano": int, "rango": int, "radio_efecto": int}
        self.habilidades_activas = [] 
        self.ataque_especial = None 

    def moverse(self, nueva_x: int, nueva_y: int):
        """Calcula si el movimiento es posible dentro del rango y actualiza posición."""
        distancia = abs(nueva_x - self.posicion["x"]) + abs(nueva_y - self.posicion["y"])
        if distancia <= self.rango_movimiento:
            self.posicion["x"] = nueva_x
            self.posicion["y"] = nueva_y
            return True, f"{self.nombre} se desplazó a ({nueva_x}, {nueva_y})."
        return False, "Destino fuera de rango de movimiento."

    def usar_habilidad(self, indice: int, objetivo_x: int, objetivo_y: int):
        """Ejecuta habilidad validando rango de efecto."""
        if indice < len(self.habilidades_activas):
            hab = self.habilidades_activas[indice]
            # Validar distancia al objetivo
            distancia_al_objetivo = abs(objetivo_x - self.posicion["x"]) + abs(objetivo_y - self.posicion["y"])
            
            if self.energia >= hab["coste"] and distancia_al_objetivo <= hab["rango"]:
                self.energia -= hab["coste"]
                return f"{self.nombre} usa {hab['nombre']} en el área ({objetivo_x}, {objetivo_y}) con radio {hab['radio_efecto']}."
            return "Energía insuficiente o rango de habilidad excedido."
        return "Habilidad no encontrada."

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
        if clase_jugador == "Caballero" and self.tipo == "Gólem":
            self.stats_combate["DEF"] += 15
            return "¡Sinergia Activa: Defensa de Piedra reforzada!"
        return "Sin sinergia especial."

    def _actualizar_bonos_pasivos(self):
        # Escala habilidades pasivas según nivel
        pass

    def ejecutar_ataque_mitico(self):
        if self.rareza == "Mítica" and self.ataque_especial:
            return f"{self.nombre} lanza {self.ataque_especial}!"
        return "Acción no disponible."

# --- CATÁLOGOS AMPLIADOS ---
# [Se mantienen los catálogos previos de Mascotas Base, Tienda, Legendarias y Míticas]
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
