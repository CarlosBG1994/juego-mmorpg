"""
Modulo: Mundo y PvE de Snd-Worlds
Gestiona los 4 reinos del Continente Primordial, zonas por nivel,
jefes de zona y mazmorras con respawn de jefes (15-20 minutos).
"""

REINOS_PRIMORDIALES = {
    "Reino Humano": {"capital": "Fortaleza Solar", "raza": "Humano"},
    "Reino Elfo": {"capital": "Arbol Corazon de Sylva", "raza": "Elfo"},
    "Reino Enano": {"capital": "Forja Profunda de Kar-Drak", "raza": "Enano"},
    "Reino Hombre Bestia": {"capital": "Bastion Primordial de los Clanes", "raza": "Hombre Bestia"}
}

RANGOS_ZONAS_REINOS = [
    {"rango": "1-15", "tipo": "Iniciacion y Tierras Bajas"},
    {"rango": "16-25", "tipo": "Valles y Bosques Salvajes"},
    {"rango": "26-35", "tipo": "Tierras Fronterizas"},
    {"rango": "36-45", "tipo": "Zonas Hostiles y Cavernas"},
    {"rango": "46-60", "tipo": "Territorio Peligroso y Bastiones de Elite"}
]

ZONAS_NEUTRALES_UNIDAS = [
    {"rango": "61-75", "descripcion": "Tierras de Nadie Inter-Reinos"},
    {"rango": "76-85", "descripcion": "Grieta de los Antiguos"},
    {"rango": "86-100", "descripcion": "Cumbre del Continente Primordial"}
]

class Mazmorra:
    def __init__(self, nombre: str, nivel_recomendado: int, zona: str, jefe_final: str):
        self.nombre = nombre
        self.nivel_recomendado = nivel_recomendado
        self.zona = zona
        self.jefe_final = jefe_final
        self.cofres_secretos = []
        self.jefe_derrotado = False
        self.tiempo_respawn_minutos = 18  # Respawn entre 15 y 20 minutos

    def anadir_cofre_secreto(self, contenido: dict):
        self.cofres_secretos.append(contenido)

    def derrotar_jefe(self):
        self.jefe_derrotado = True
        return f"¡{self.jefe_final} ha sido derrotado! El jefe reaparecera en {self.tiempo_respawn_minutos} minutos."
