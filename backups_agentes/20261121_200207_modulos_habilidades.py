"""
Modulo: Habilidades de Snd-Worlds
Catalogo de habilidades con tiers, niveles 1-50, 3 ataques propios por habilidad
y sistema de fusion para crear super habilidades.
"""

TIERS = {
    "VI": "Comun",
    "V": "Poco Comun",
    "IV": "Raro",
    "III": "Ultra Raro",
    "II": "Leyenda",  # Maximo 10 jugadores portadores simultaneos
    "I": "Mitica"     # Maximo 5 jugadores portadores simultaneos
}

PORTADORES_MAXIMOS = {
    "Leyenda": 10,
    "Mitica": 5
}

# Catalogo Base: Estructura para las 1.870 habilidades
# Se puede expandir mediante carga externa o registros sucesivos
CATALOGO_HABILIDADES = {}

class Habilidad:
    def __init__(self, id_hab: str, nombre: str, tier: str, raza_req: list = None, clase_req: list = None):
        self.id = id_hab
        self.nombre = nombre
        self.tier = tier
        self.raza_req = raza_req or []
        self.clase_req = clase_req or []
        
        # Nivel de maestria de la habilidad (1 al 50)
        self.nivel = 1
        self.experiencia = 0
        
        # Ataques desbloqueables
        self.ataque_1 = f"{nombre} - Ataque Inicial"
        self.ataque_2 = None  # Se desbloquea al nivel 15
        self.ataque_3 = None  # Se desbloquea al nivel 30

    def ganar_experiencia(self, cantidad: int):
        if self.nivel >= 50:
            return
        self.experiencia += cantidad
        if self.experiencia >= (self.nivel * 50) and self.nivel < 50:
            self.nivel += 1
            self.experiencia = 0
            if self.nivel == 15:
                self.ataque_2 = f"{self.nombre} - Segundo Ataque (Dominio Intermedio)"
            elif self.nivel == 30:
                self.ataque_3 = f"{self.nombre} - Tercer Ataque (Dominio Maestro)"

    def obtener_ataques_activos(self) -> list:
        ataques = [self.ataque_1]
        if self.ataque_2:
            ataques.append(self.ataque_2)
        if self.ataque_3:
            ataques.append(self.ataque_3)
        return ataques

def registrar_habilidad(id_hab, nombre, tier, razas, clases):
    """Registra una habilidad en el catalogo global del juego."""
    CATALOGO_HABILIDADES[id_hab] = Habilidad(id_hab, nombre, tier, razas, clases)

def fusionar_habilidades(habilidad_a: Habilidad, habilidad_b: Habilidad) -> dict:
    """
    Fusiona dos habilidades al instante generando una Super Habilidad
    con un unico super ataque que combina ambas.
    """
    nombre_super = f"Super: {habilidad_a.nombre} + {habilidad_b.nombre}"
    super_ataque = f"Super Ataque Combinado de {habilidad_a.nombre} y {habilidad_b.nombre}"
    return {
        "nombre": nombre_super,
        "super_ataque": super_ataque,
        "habilidades_origen": [habilidad_a.id, habilidad_b.id]
    }
