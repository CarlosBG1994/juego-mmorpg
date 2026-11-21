"""
Modulo: Mundo y PVE de Snd-Worlds
Reinos por raza, rangos de nivel por zonas, jefes elite,
zonas neutrales y mazmorras con respawn de jefes (15-20 minutos).
"""

from typing import Dict, List, Optional
import time

RANGOS_ZONAS_REINO = [
    "1-15",
    "16-25",
    "26-35",
    "36-45",
    "46-60"
]

RANGOS_ZONAS_NEUTRALES = [
    "61-75",
    "76-85",
    "86-100"
]

REINOS_PRIMORDIALES = {
    "Reino Humano de Valoria": {"raza": "Humano", "capital": "Fortaleza del Alba"},
    "Dominio Silvano de Elyria": {"raza": "Elfo", "capital": "Arbol Corazon"},
    "Bastion de Kazad-Mor": {"raza": "Enano", "capital": "Forja Profunda"},
    "Tierras Primigenias de Garra y Colmillo": {"raza": "Hombre Bestia", "capital": "Campamento Ancestral"}
}

class JefeElite:
    def __init__(self, nombre: str, nivel: int, zona_rango: str, es_jefe_mazmorra: bool = False):
        self.nombre = nombre
        self.nivel = nivel
        self.zona_rango = zona_rango
        self.es_jefe_mazmorra = es_jefe_mazmorra
        self.vivo = True
        self.ultimo_derribo: Optional[float] = None
        self.tiempo_respawn_segundos = 15 * 60  # 15 a 20 minutos (en seg)

    def derrotar(self):
        self.vivo = False
        self.ultimo_derribo = time.time()

    def verificar_respawn(self, tiempo_actual: Optional[float] = None) -> bool:
        if self.vivo:
            return True
        if self.ultimo_derribo is None:
            self.vivo = True
            return True
        ahora = tiempo_actual or time.time()
        if ahora - self.ultimo_derribo >= self.tiempo_respawn_segundos:
            self.vivo = True
            self.ultimo_derribo = None
            return True
        return False

class Mazmorra:
    def __init__(self, nombre: str, nivel_recomendado: int, zona_asociada: str, jefe_final: JefeElite):
        self.nombre = nombre
        self.nivel_recomendado = nivel_recomendado
        self.zona_asociada = zona_asociada
        self.jefe_final = jefe_final
        self.zonas_secretas: List[str] = ["Camara Oculta de Runas", "Cofre del Velo"]

    def entrar(self) -> str:
        self.jefe_final.verificar_respawn()
        estado_jefe = "Vivo" if self.jefe_final.vivo else "En espera de reaparicion (15-20 min)"
        return f"Entrando a {self.nombre} (Nivel {self.nivel_recomendado}). Jefe final: {self.jefe_final.nombre} [{estado_jefe}]"
