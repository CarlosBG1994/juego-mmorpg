"""
Modulo: modulos/integrador.py
Verifica y conecta todos los modulos del sistema de Snd-Worlds.
"""

from .razas_y_clases import PersonajeBase
from .habilidades import Habilidad, SuperHabilidad, CatalogoHabilidades
from .economia_y_comercio import Mochila, MercadoComercio
from .progresion_y_stats import ProgresionPersonaje
from .mundo_y_pve import Mazmorra, REINOS_PRIMORDIALES

class MotorJuego:
    def __init__(self):
        self.catalogo_habilidades = CatalogoHabilidades()
        self.mercado = MercadoComercio()

    def crear_jugador_completo(self, nombre: str, raza: str, clase: str, subforma: str = None):
        base = PersonajeBase(nombre=nombre, raza=raza, clase=clase, subforma=subforma)
        progresion = ProgresionPersonaje(base)
        mochila = Mochila()
        return {
            "personaje": base,
            "progresion": progresion,
            "mochila": mochila
        }

    def verificar_sistema(self) -> dict:
        return {
            "estado": "Operativo",
            "reinos_disponibles": list(REINOS_PRIMORDIALES.keys()),
            "habilidades_registradas": self.catalogo_habilidades.total_registradas()
        }
