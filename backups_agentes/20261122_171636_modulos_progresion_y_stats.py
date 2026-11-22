"""
Modulo: Progresion y Estadisticas de Snd-Worlds
Reglas:
- Nivel 1 a 100 inicial.
- Ganancia de 5 puntos libres por nivel.
- +10 HP maximo automatico por nivel.
- Sistema de Estadísticas Derivadas (Equilibrio mediante interdependencia).
- Reespecialización cara y estratégica con pergamino.
- Barra de XP: Sincronizada para UI en tiempo real.
"""

# Importamos el bus de eventos para coordinar con la UI del cliente
from modulos.integrador import EventBus 

CONTINENTES_Y_LIMITES = {
    "Continente Primordial": 100,
    "Archipielago de los Vientos": 150,
    "Continente Abisal de los Demonios": 200,
    "Continente Celestial de los Angeles": 250,
    "Nucleo Central de Comercio y Nexo Global": 300
}

class PersonajeProgresion:
    def __init__(self, nombre: str, raza: str, clase: str, subforma: str = None):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.subforma = subforma
        self.nivel = 1
        self.experiencia = 0
        self.experiencia_siguiente = 100
        
        self.hp_max = 100
        self.hp_actual = 100 
        
        self.puntos_libres = 0
        self.stats = {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10}
        self.continente_actual = "Continente Primordial"

    def ganar_experiencia(self, cantidad: int):
        """
        Añade XP y emite evento para que la barra de XP en la UI se mueva.
        """
        self.experiencia += cantidad
        
        # Notificación al bus de eventos para actualizar la barra en la pantalla del usuario
        EventBus.emit("XP_UPDATE", {
            "jugador": self.nombre, 
            "xp_actual": self.experiencia, 
            "xp_requerida": self.experiencia_siguiente
        })
        
        subidas = 0
        while self.experiencia >= self.experiencia_siguiente:
            self.experiencia -= self.experiencia_siguiente
            resultado, _ = self.subir_nivel()
            if resultado: subidas += 1
            else: break
        return subidas

    def subir_nivel(self):
        limite_actual = CONTINENTES_Y_LIMITES.get(self.continente_actual, 100)
        if self.nivel >= limite_actual: return False, "Límite de nivel alcanzado."

        self.nivel += 1
        self.puntos_libres += 5 
        self.hp_max += 10 
        self.experiencia_siguiente = int(self.experiencia_siguiente * 1.15)
        
        # Notificación de nivel subido para refrescar la UI
        EventBus.emit("LEVEL_UP", {"jugador": self.nombre, "nuevo_nivel": self.nivel})
        return True, f"Nivel {self.nivel} alcanzado."

    # ... (asignar_puntos, calcular_coste, usar_pergamino y obtener_stats_derivadas se mantienen iguales)
    def asignar_puntos(self, estadistica: str, cantidad: int):
        est = estadistica.upper()
        if est not in self.stats or cantidad <= 0 or cantidad > self.puntos_libres:
            return False, "Error en asignación de puntos."
        self.stats[est] += cantidad
        self.puntos_libres -= cantidad
        return True, f"{est} subida a {self.stats[est]}."

    def calcular_coste_reespecializacion(self):
        return (self.nivel ** 2) * 100

    def usar_pergamino_reespecializacion(self, tiene_pergamino: bool, billetera: object):
        coste = self.calcular_coste_reespecializacion()
        if not tiene_pergamino: return False, "Necesitas un Pergamino de Reespecialización."
        if not billetera.retirar_cobre(coste * 10000, "Tasa de reespecialización"): return False, "Fondos insuficientes."
        total_puntos_disponibles = 60 + ((self.nivel - 1) * 5)
        self.stats = {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10}
        self.puntos_libres = total_puntos_disponibles - 60
        return True, "Stats reseteadas."

    def obtener_stats_derivadas(self):
        return {
            "Daño_Fisico": self.stats["STR"] * 2,
            "Defensa": (self.stats["VIT"] * 1.5) + (self.stats["STR"] * 0.5),
            "Precision": (self.stats["DES"] * 2) + (self.stats["AGI"] * 0.5),
            "Evasion": (self.stats["AGI"] * 1.2) + (self.stats["LUK"] * 0.3),
            "Critico": (self.stats["LUK"] * 0.5) + (self.stats["DES"] * 0.2),
            "Poder_Magico": self.stats["INT"] * 2
        }
