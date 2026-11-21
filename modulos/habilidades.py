"""
Modulo: Habilidades de Snd-Worlds
Catalogo, niveles de habilidad (1-50), desbloqueo de ataques (1, 15, 30),
fusiones instantaneas y limites de portadores para Leyenda y Mitica.
"""

from typing import Dict, List, Optional

TIERS = {
    "tier_VI": "Comun",
    "tier_V": "Poco Comun",
    "tier_IV": "Raro",
    "tier_III": "Ultra Raro",
    "tier_II": "Leyenda",
    "tier_I": "Mitica"
}

# Limites maximos globales de jugadores portadores segun las reglas
LIMITES_PORTADORES_GLOBALES = {
    "tier_II": 10,  # Leyenda: solo 10 jugadores
    "tier_I": 5     # Mitica: solo 5 jugadores
}

# Registro global de portadores activos para habilidades unicas
portadores_habilidad_global: Dict[str, List[str]] = {}

class Habilidad:
    def __init__(
        self,
        id_habilidad: str,
        nombre: str,
        tier: str,
        raza_permitida: Optional[str] = None,
        clase_permitida: Optional[str] = None,
        descripcion: str = "",
        ataque_1: str = "Golpe Primario",
        ataque_2: str = "Tactica Avanzada",
        ataque_3: str = "Ataque Maestro"
    ):
        self.id_habilidad = id_habilidad
        self.nombre = nombre
        self.tier = tier
        self.raza_permitida = raza_permitida
        self.clase_permitida = clase_permitida
        self.descripcion = descripcion
        
        self.nivel = 1
        self.experiencia = 0
        
        # Cada habilidad posee 3 ataques que se desbloquean progresivamente
        self.ataque_1 = ataque_1
        self.ataque_2 = ataque_2
        self.ataque_3 = ataque_3

    @property
    def ataques_desbloqueados(self) -> List[str]:
        ataques = [self.ataque_1]
        if self.nivel >= 15:
            ataques.append(self.ataque_2)
        if self.nivel >= 30:
            ataques.append(self.ataque_3)
        return ataques

    def ganar_experiencia(self, cantidad: int):
        if self.nivel >= 50:
            self.nivel = 50
            return
        self.experiencia += cantidad
        while self.experiencia >= self.nivel * 100 and self.nivel < 50:
            self.experiencia -= self.nivel * 100
            self.nivel += 1

class SuperHabilidad:
    """Super ataque resultante de la fusion instantanea de dos habilidades."""
    def __init__(self, hab1: Habilidad, hab2: Habilidad):
        self.nombre = f"Fusion: {hab1.nombre} + {hab2.nombre}"
        self.descripcion = f"Super ataque combinado nacido de {hab1.nombre} y {hab2.nombre}."
        self.ataque_super = f"Impulso Devastador de {hab1.nombre} & {hab2.nombre}"
        self.habilidades_origen = [hab1.id_habilidad, hab2.id_habilidad]

class GestorHabilidadesPersonaje:
    """
    Cada jugador puede llevar 5 habilidades equipadas (dando hasta 15 ataques)
    y generar hasta 10 super ataques por combinaciones/fusiones.
    """
    MAX_HABILIDADES_EQUIPADAS = 5

    def __init__(self, id_jugador: str, raza: str, clase: str):
        self.id_jugador = id_jugador
        self.raza = raza
        self.clase = clase
        self.inventario_habilidades: List[Habilidad] = []
        self.equipadas: List[Habilidad] = []
        self.super_habilidades: List[SuperHabilidad] = []

    def puede_equipar(self, hab: Habilidad) -> bool:
        if hab.raza_permitida and hab.raza_permitida != self.raza:
            return False
        if hab.clase_permitida and hab.clase_permitida != self.clase:
            return False
        
        # Validar cupos globales si es Leyenda o Mitica
        if hab.tier in LIMITES_PORTADORES_GLOBALES:
            limite = LIMITES_PORTADORES_GLOBALES[hab.tier]
            portadores = portadores_habilidad_global.setdefault(hab.id_habilidad, [])
            if self.id_jugador not in portadores and len(portadores) >= limite:
                return False
        return True

    def equipar(self, hab: Habilidad) -> bool:
        if len(self.equipadas) >= self.MAX_HABILIDADES_EQUIPADAS:
            return False
        if not self.puede_equipar(hab):
            return False
        
        self.equipadas.append(hab)
        if hab.tier in LIMITES_PORTADORES_GLOBALES:
            portadores = portadores_habilidad_global.setdefault(hab.id_habilidad, [])
            if self.id_jugador not in portadores:
                portadores.append(self.id_jugador)
        return True

    def desequipar(self, hab_id: str):
        for hab in self.equipadas:
            if hab.id_habilidad == hab_id:
                self.equipadas.remove(hab)
                if hab.tier in LIMITES_PORTADORES_GLOBALES:
                    portadores = portadores_habilidad_global.get(hab.id_habilidad, [])
                    if self.id_jugador in portadores:
                        portadores.remove(self.id_jugador)
                break

    def listar_ataques_disponibles(self) -> List[str]:
        ataques = []
        for hab in self.equipadas:
            ataques.extend(hab.ataques_desbloqueados)
        return ataques

    def fusionar_habilidades(self, hab1: Habilidad, hab2: Habilidad) -> SuperHabilidad:
        super_hab = SuperHabilidad(hab1, hab2)
        self.super_habilidades.append(super_hab)
        return super_hab
