"""
Modulo: modulos/mundo_y_pve.py
Zonas de caza, los 4 reinos del Continente Primordial, zonas neutrales intermedias,
jefes de zona/elites y mazmorras con salas secretas y respawn de 15-20 min.
"""

REINOS_PRIMORDIALES = {
    "Reino Humano": {"capital": "Corona de Luz", "raza": "Humano"},
    "Reino Elfico": {"capital": "Arbol de la Aurora", "raza": "Elfo"},
    "Reino Enano": {"capital": "Baluarte Forjaeterna", "raza": "Enano"},
    "Reino de las Bestias": {"capital": "Claro Ancestral", "raza": "Hombre Bestia"}
}

RANGOS_ZONAS_REINO = [
    (1, 15),
    (16, 25),
    (26, 35),
    (36, 45),
    (46, 60)
]

RANGOS_ZONAS_NEUTRALES = [
    (61, 75),
    (76, 85),
    (86, 100)
]

class Mazmorra:
    def __init__(self, nombre: str, nivel_recomendado: int, jefe_final: str, tiempo_respawn_minutos: int = 15):
        self.nombre = nombre
        self.nivel_recomendado = nivel_recomendado
        self.jefe_final = jefe_final
        self.tiempo_respawn_minutos = tiempo_respawn_minutos
        self.zonas_secretas = []
        self.jefe_derrotado = False

    def anadir_zona_secreta(self, nombre_secreto: str, cofre_drops: list):
        self.zonas_secretas.append({
            "zona": nombre_secreto,
            "cofre": cofre_drops,
            "descubierta": False
        })

    def completar_mazmorra(self) -> dict:
        self.jefe_derrotado = True
        return {
            "mensaje": f"Mazmorra {self.nombre} completada.",
            "respawn_jefe_en": f"{self.tiempo_respawn_minutos} minutos"
        }
