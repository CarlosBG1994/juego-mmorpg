"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Diario.
- Recompensas: Experiencia, Oro, Objetos o Habilidades.
"""

class Mision:
    def __init__(self, id_mision: str, titulo: str, descripcion: str, tipo: str, recompensa: dict):
        self.id = id_mision
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo  # "Principal", "Secundaria", "Diaria"
        self.recompensa = recompensa # Ej: {"exp": 500, "oro": 50, "item": None}
        self.estado = "Disponible" # Disponible, Activa, Completada

    def aceptar_mision(self):
        self.estado = "Activa"

    def completar_mision(self):
        self.estado = "Completada"
        return self.recompensa

class GestorMisiones:
    def __init__(self):
        self.misiones_disponibles = []
        self.misiones_activas = []
        self.misiones_historial = []

    def agregar_mision(self, mision: Mision):
        self.misiones_disponibles.append(mision)

    def activar_mision(self, id_mision: str):
        for mision in self.misiones_disponibles:
            if mision.id == id_mision:
                mision.aceptar_mision()
                self.misiones_activas.append(self.misiones_disponibles.pop(self.misiones_disponibles.index(mision)))
                return True, f"Misión '{mision.titulo}' iniciada."
        return False, "Misión no encontrada."

    def entregar_mision(self, id_mision: str):
        for mision in self.misiones_activas:
            if mision.id == id_mision:
                mision.completar_mision()
                self.misiones_historial.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                return True, mision.completar_mision()
        return False, "La misión no está activa o no existe."
