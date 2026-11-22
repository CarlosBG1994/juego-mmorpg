"""
Modulo: Progresion y Estadisticas de Snd-Worlds
Reglas:
- Nivel 1 a 100 inicial (Continente Primordial).
- Sistema de experiencia + UI en tiempo real.
- +10 HP maximo automatico por nivel.
- Coste fijo de 100 Platino para reseteo total.
- Stats Derivadas: Equilibrio mediante interdependencia.
- Restricción de equipo: Basada en nivel del jugador.
- Habilidades: Equipables por Clase/Raza sin restricción de nivel (Solo compatibilidad).
"""

from modulos.integrador import EventBus 

CONTINENTES_Y_LIMITES = {
    "Continente Primordial": 100,
    "Archipielago de los Vientos": 150,
    "Continente Abisal de los Demonios": 200,
    "Continente Celestial de los Angeles": 250,
    "Nucleo Central de Comercio y Nexo Global": 300
}

COSTE_REESPECIALIZACION_PLATINO = 100

class PersonajeProgresion:
    def __init__(self, nombre: str, raza: str, clase: str, subforma: str = None):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.nivel = 1
        self.experiencia = 0
        self.experiencia_siguiente = 100
        self.hp_max = 100
        self.puntos_libres = 0
        self.stats = {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10}
        self.continente_actual = "Continente Primordial"

    def ganar_experiencia(self, cantidad: int):
        self.experiencia += cantidad
        EventBus.emit("XP_UPDATE", {"jugador": self.nombre, "xp_actual": self.experiencia, "xp_requerida": self.experiencia_siguiente})
        
        while self.experiencia >= self.experiencia_siguiente:
            self.experiencia -= self.experiencia_siguiente
            self.subir_nivel()

    def subir_nivel(self):
        limite_actual = CONTINENTES_Y_LIMITES.get(self.continente_actual, 100)
        if self.nivel < limite_actual:
            self.nivel += 1
            self.puntos_libres += 5 
            self.hp_max += 10 
            self.experiencia_siguiente = int(self.experiencia_siguiente * 1.15)
            EventBus.emit("LEVEL_UP", {"jugador": self.nombre, "nuevo_nivel": self.nivel})

    def obtener_modificador_raza(self):
        mod = {"VIT": 1.0, "STR": 1.0, "INT": 1.0}
        if self.raza == "Enano": mod["VIT"] = 1.1
        if self.raza == "Elfo": mod["INT"] = 1.1
        return mod

    def obtener_stats_derivadas(self):
        m = self.obtener_modificador_raza()
        return {
            "Daño_Fisico": self.stats["STR"] * 2 * m["STR"],
            "Defensa": ((self.stats["VIT"] * 1.5) * m["VIT"]) + (self.stats["STR"] * 0.5),
            "Poder_Magico": self.stats["INT"] * 2 * m["INT"],
            "Precision": (self.stats["DES"] * 2) + (self.stats["AGI"] * 0.5),
            "Evasion": (self.stats["AGI"] * 1.2) + (self.stats["LUK"] * 0.3),
            "Critico": (self.stats["LUK"] * 0.5) + (self.stats["DES"] * 0.2)
        }

    def usar_pergamino_reespecializacion(self, tiene_pergamino: bool, billetera: object):
        coste_en_cobre = COSTE_REESPECIALIZACION_PLATINO * 100_000_000
        if not tiene_pergamino: return False, "Pergamino no encontrado."
        if not billetera.retirar_cobre(coste_en_cobre, "Reseteo Total"): return False, "Fondos insuficientes (100 Platino)."
        
        self.stats = {k: 10 for k in self.stats}
        self.puntos_libres = ((self.nivel - 1) * 5)
        return True, "Stats reseteadas con éxito."

    def asignar_puntos(self, estadistica: str, cantidad: int):
        if estadistica.upper() in self.stats and 0 < cantidad <= self.puntos_libres:
            self.stats[estadistica.upper()] += cantidad
            self.puntos_libres -= cantidad
            return True, "Puntos asignados."
        return False, "Error en asignación."

    def puede_equipar_equipo(self, nivel_equipo: int):
        """Validación simple para que el equipo dependa del nivel del jugador."""
        return self.nivel >= nivel_equipo
