"""
Modulo: Integrador General de Snd-Worlds
Conecta todos los modulos conservando las reglas existentes.
"""

from modulos.razas_y_clases import PersonajeRazaClase, RAZAS_Y_CLASES
from modulos.progresion_y_stats import ProgresionPersonaje
from modulos.habilidades import GestorHabilidadesPersonaje, Habilidad
from modulos.economia_y_comercio import Mochila, MercadoSubasta
from modulos.mundo_y_pve import Mazmorra, JefeElite

class PersonajeSndWorlds:
    """Clase principal que une las caracteristicas de un avatar en el juego."""
    def __init__(self, id_jugador: str, nombre: str, raza: str, clase: str, subforma_bestia: str = None):
        self.id_jugador = id_jugador
        self.identidad = PersonajeRazaClase(nombre, raza, clase, subforma_bestia)
        self.progresion = ProgresionPersonaje(nombre, self.identidad.stats)
        self.habilidades = GestorHabilidadesPersonaje(id_jugador, raza, clase)
        self.mochila = Mochila()

    def estado_general(self) -> dict:
        return {
            "id": self.id_jugador,
            "nombre": self.identidad.nombre,
            "raza": self.identidad.raza,
            "clase": self.identidad.clase,
            "subforma": self.identidad.subforma_bestia,
            "nivel": self.progresion.nivel,
            "hp": f"{self.progresion.hp_actual}/{self.progresion.hp_max}",
            "stats": self.progresion.stats,
            "puntos_libres": self.progresion.puntos_libres,
            "continente": self.progresion.continente_actual,
            "monedero": self.mochila.monedero.desglose(),
            "ataques_equipados": self.habilidades.listar_ataques_disponibles()
        }

def verificar_integridad_sistema() -> bool:
    """Comprobacion automatica de conexion entre modulos."""
    pj = PersonajeSndWorlds("jugador_01", "Valerius", "Humano", "Caballero")
    pj.progresion.ganar_experiencia(200)
    pj.progresion.asignar_punto("STR", 2)
    pj.mochila.monedero.agregar_cobre(15234)
    
    hab_prueba = Habilidad(
        id_habilidad="hab_corte_01",
        nombre="Corte de Luz",
        tier="tier_VI",
        raza_permitida="Humano",
        clase_permitida="Caballero"
    )
    pj.habilidades.equipar(hab_prueba)
    
    resumen = pj.estado_general()
    assert resumen["nivel"] >= 1
    assert "Corte de Luz" in str(resumen["ataques_equipados"][0])
    return True

if __name__ == "__main__":
    if verificar_integridad_sistema():
        print("Snd-Worlds: Todos los modulos base han sido cargados e integrados correctamente.")
