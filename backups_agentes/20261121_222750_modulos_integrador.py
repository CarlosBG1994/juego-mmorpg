"""
Modulo: Integrador General de Snd-Worlds
Coordina y conecta todos los modulos asegurando que las reglas se cumplan.
"""

from .razas_y_clases import CLASES_POR_RAZA, validar_compatibilidad
from .progresion_y_stats import PersonajeProgresion
from .economia_y_comercio import Mochila
from .habilidades import Habilidad, fusionar_habilidades
from .mundo_y_pve import REINOS_PRIMORDIALES

class Jugador:
    def __init__(self, nombre: str, raza: str, clase: str, subforma: str = None):
        if clase not in CLASES_POR_RAZA.get(raza, []):
            raise ValueError(f"La clase {clase} no es valida para la raza {raza}.")
            
        self.progresion = PersonajeProgresion(nombre, raza, clase, subforma)
        self.mochila = Mochila()
        
        # Maximo 5 habilidades equipadas simultaneamente (15 ataques en total)
        self.habilidades_equipadas = []
        # Hasta 10 super ataques por fusiones
        self.super_habilidades = []

    def equipar_habilidad(self, habilidad: Habilidad):
        if not validar_compatibilidad(self.progresion.raza, self.progresion.clase, habilidad.raza_req, habilidad.clase_req):
            return False, "No cumples los requisitos de raza o clase para equipar esta habilidad (puedes guardarla o venderla)."

        if len(self.habilidades_equipadas) >= 5:
            return False, "Ya tienes el limite de 5 habilidades equipadas (15 ataques)."

        self.habilidades_equipadas.append(habilidad)
        return True, f"Habilidad {habilidad.nombre} equipada correctamente."

    def fusionar_dos_habilidades(self, indice_a: int, indice_b: int):
        if len(self.super_habilidades) >= 10:
            return False, "Limite de 10 super ataques alcanzado."
        if indice_a < len(self.habilidades_equipadas) and indice_b < len(self.habilidades_equipadas):
            hab_a = self.habilidades_equipadas[indice_a]
            hab_b = self.habilidades_equipadas[indice_b]
            super_hab = fusionar_habilidades(hab_a, hab_b)
            self.super_habilidades.append(super_hab)
            return True, f"¡Fusion lograda! Se genero: {super_hab['nombre']}."
        return False, "Indices de habilidad no validos."
