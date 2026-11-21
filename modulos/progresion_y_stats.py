"""
Modulo: Progresion y Estadisticas de Snd-Worlds
Reglas:
- Nivel 1 a 100 inicial (Continente Primordial).
- Sistema de experiencia por misiones o combate.
- Ganancia de 5 a 10 puntos libres por nivel según configuración.
- +10 HP maximo automatico por nivel.
- Limite maximo hasta nivel 300 repartido por continentes (+50 por continente).
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
        self.stats = {
            "STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10
        }
        self.continente_actual = "Continente Primordial"

    def ganar_experiencia(self, cantidad: int):
        """Añade experiencia y verifica si el jugador sube de nivel."""
        self.experiencia += cantidad
        subidas = 0
        while self.experiencia >= self.experiencia_siguiente:
            self.experiencia -= self.experiencia_siguiente
            resultado, mensaje = self.subir_nivel()
            if resultado:
                subidas += 1
            else:
                self.experiencia = 0 # Tope alcanzado
                break
        return subidas

    def subir_nivel(self):
        limite_actual = CONTINENTES_Y_LIMITES.get(self.continente_actual, 100)
        if self.nivel >= limite_actual:
            return False, f"Alcanzaste el limite del {self.continente_actual} (Nivel {limite_actual})."

        self.nivel += 1
        # Se otorgan 10 puntos libres para mayor personalización, ajustable a 5 si se prefiere
        self.puntos_libres += 10 
        self.hp_max += 10
        self.hp_actual = self.hp_max
        self.experiencia_siguiente = int(self.experiencia_siguiente * 1.15)
        return True, f"¡Nivel {self.nivel}! +10 puntos libres de stats y +10 HP maximo."

    def asignar_puntos(self, estadistica: str, cantidad: int):
        estadistica = estadistica.upper()
        if estadistica not in self.stats:
            return False, "Estadistica no valida."
        if cantidad <= 0 or cantidad > self.puntos_libres:
            return False, "Cantidad de puntos insuficiente o no valida."
        
        self.stats[estadistica] += cantidad
        self.puntos_libres -= cantidad
        return True, f"{cantidad} puntos asignados a {estadistica}. Puntos libres restantes: {self.puntos_libres}."
