"""
Modulo: Progresion y Estadisticas de Snd-Worlds
Reglas:
- Nivel 1 a 100 inicial.
- Ganancia de 5 puntos libres por nivel.
- +10 HP maximo automatico por nivel (No rellena HP actual).
- Sistema de Estadísticas Derivadas: Interdependencia total para evitar personajes rotos.
- Decisiones de stats permanentes (Solo reasignables vía Pergamino de Reespecialización).
"""

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
        # Stats base iniciales
        self.stats = {
            "STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10
        }
        self.continente_actual = "Continente Primordial"

    def ganar_experiencia(self, cantidad: int):
        self.experiencia += cantidad
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
        self.hp_max += 10 # El HP máximo sube, pero el actual NO se rellena.
        self.experiencia_siguiente = int(self.experiencia_siguiente * 1.15)
        return True, f"Nivel {self.nivel} alcanzado."

    def asignar_puntos(self, estadistica: str, cantidad: int):
        """Asignación permanente de puntos."""
        est = estadistica.upper()
        if est not in self.stats or cantidad <= 0 or cantidad > self.puntos_libres:
            return False, "Error en asignación de puntos."
        
        self.stats[est] += cantidad
        self.puntos_libres -= cantidad
        return True, f"{est} subida a {self.stats[est]}."

    def usar_pergamino_reespecializacion(self, pergamino_valido: bool):
        """
        Resetea las stats a sus valores base de Nivel 1.
        Solo puede activarse con un ítem especial.
        """
        if not pergamino_valido:
            return False, "Necesitas un Pergamino de Reespecialización (Muy caro)."
        
        # Devolver puntos totales invertidos (Stats actuales - 10 iniciales)
        puntos_recuperados = sum(self.stats.values()) - 60
        self.stats = {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10}
        self.puntos_libres += puntos_recuperados
        return True, "Stats reseteadas. Elige sabiamente, la decisión es permanente."

    def obtener_stats_derivadas(self):
        """
        Sistema de Equilibrio: Cada stat es necesaria.
        Si un jugador sube solo STR, tendrá daño alto pero fallará ataques (baja PREC) 
        y será frágil (baja DEF).
        """
        return {
            "Daño_Fisico": self.stats["STR"] * 2,
            "Defensa": (self.stats["VIT"] * 1.5) + (self.stats["STR"] * 0.5),
            "Precision": (self.stats["DES"] * 2) + (self.stats["AGI"] * 0.5),
            "Evasion": (self.stats["AGI"] * 1.2) + (self.stats["LUK"] * 0.3),
            "Critico": (self.stats["LUK"] * 0.5) + (self.stats["DES"] * 0.2),
            "Poder_Magico": self.stats["INT"] * 2
        }
