"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Diario.
- Recompensas: Experiencia, Oro, Objetos o Habilidades.
"""

class Mision:
    def __init__(self, id_mision: str, titulo: str, descripcion: str, tipo: str, recompensa: dict, nivel_req: int = 1):
        self.id = id_mision
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo  # "Principal", "Secundaria", "Diaria"
        self.recompensa = recompensa # Ej: {"exp": 500, "oro": 50, "item": None}
        self.nivel_req = nivel_req
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
        self._inicializar_misiones_principales()

    def _inicializar_misiones_principales(self):
        """Genera la estructura narrativa de las misiones principales del juego."""
        catalogo = [
            Mision("P001", "El Despertar del Eter", "Habla con el guía de tu reino para comprender tu legado.", "Principal", {"exp": 100, "oro": 10}, 1),
            Mision("P002", "Primera Sangre", "Derrota a 5 enemigos en la zona de iniciación 1-15.", "Principal", {"exp": 500, "oro": 50}, 5),
            Mision("P003", "El Sello Perdido", "Recupera una habilidad olvidada en una mazmorra de nivel 15.", "Principal", {"exp": 1200, "oro": 200}, 15)
        ]
        self.misiones_disponibles.extend(catalogo)

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
