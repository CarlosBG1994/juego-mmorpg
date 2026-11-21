"""
Modulo: modulos/habilidades.py
Gestiona el catalogo de habilidades, niveles 1-50, desbloqueo de ataques (lvl 15 y 30),
fusiones de super-habilidad, limites de portadores (Leyenda y Mitica) y compatibilidad.
"""

TIERS = {
    "TIER_VI": {"nombre": "Comun", "limite_portadores": None},
    "TIER_V": {"nombre": "Poco Comun", "limite_portadores": None},
    "TIER_IV": {"nombre": "Raro", "limite_portadores": None},
    "TIER_III": {"nombre": "Ultra Raro", "limite_portadores": None},
    "TIER_II": {"nombre": "Leyenda", "limite_portadores": 10},
    "TIER_I": {"nombre": "Mitica", "limite_portadores": 5}
}

class Habilidad:
    def __init__(self, id_habilidad: str, nombre: str, tier: str, raza_req: str = None, clase_req: str = None, descripcion: str = ""):
        if tier not in TIERS:
            raise ValueError(f"Tier no valido: {tier}")
        self.id_habilidad = id_habilidad
        self.nombre = nombre
        self.tier = tier
        self.raza_req = raza_req
        self.clase_req = clase_req
        self.descripcion = descripcion
        self.nivel = 1
        self.experiencia = 0
        self.portadores_actuales = 0

    def ataques_desbloqueados(self) -> list:
        """Genera hasta 3 ataques segun el nivel (1-50)."""
        ataques = [f"{self.nombre}: Ataque Primario"]
        if self.nivel >= 15:
            ataques.append(f"{self.nombre}: Segundo Ataque Potenciado")
        if self.nivel >= 30:
            ataques.append(f"{self.nombre}: Tercer Ataque Definitivo")
        return ataques

    def subir_experiencia(self, exp: int):
        if self.nivel >= 50:
            return
        self.experiencia += exp
        # Cada nivel requiere 100 de exp
        nuevo_nivel = min(50, 1 + (self.experiencia // 100))
        self.nivel = nuevo_nivel

    def puede_equiparse(self, personaje) -> bool:
        """Cualquiera puede obtenerla, pero solo equiparla si cumple raza y clase."""
        tier_info = TIERS[self.tier]
        if tier_info["limite_portadores"] is not None:
            if self.portadores_actuales >= tier_info["limite_portadores"]:
                return False
        return personaje.es_compatible(self.raza_req, self.clase_req)

class SuperHabilidad:
    """Super habilidad originada por la fusion instantanea de 2 habilidades."""
    def __init__(self, hab1: Habilidad, hab2: Habilidad):
        self.id_super = f"FUSION_{hab1.id_habilidad}_{hab2.id_habilidad}"
        self.nombre = f"Vortice: {hab1.nombre} + {hab2.nombre}"
        self.hab_origen = (hab1, hab2)
        self.super_ataque = f"Ataque Combinado Supremo de {hab1.nombre} y {hab2.nombre}"

    def ejecutar_super_ataque(self) -> str:
        return f"Activando Super Ataque: {self.super_ataque}"

class CatalogoHabilidades:
    def __init__(self):
        self.habilidades = {}

    def registrar_habilidad(self, habilidad: Habilidad):
        self.habilidades[habilidad.id_habilidad] = habilidad

    def obtener_habilidad(self, id_habilidad: str) -> Habilidad:
        return self.habilidades.get(id_habilidad)

    def total_registradas(self) -> int:
        return len(self.habilidades)
