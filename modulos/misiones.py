"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Tutorial, Diario.
- Estructura: Escalado hasta 2,000 misiones (500 por reino).
"""

class Mision:
    def __init__(self, id_mision: str, titulo: str, descripcion: str, tipo: str, recompensa: dict, nivel_req: int = 1):
        self.id = id_mision
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo  # "Principal", "Secundaria", "Tutorial", "Diaria", "Legado"
        self.recompensa = recompensa
        self.nivel_req = nivel_req
        self.estado = "Disponible"

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
        # Inicialización de bloques de contenido
        self._inicializar_misiones_tutorial()
        self._inicializar_misiones_principales()
        # Nota: El sistema de 500 misiones por reino se cargará mediante 
        # generadores dinámicos según el avance del jugador en la historia.

    def _inicializar_misiones_tutorial(self):
        tutoriales = [
            Mision("T001", "Primeros Pasos", "Equipa tu vestimenta inicial.", "Tutorial", {"exp": 50, "oro": 5, "item": "Vestimenta"}, 1),
            Mision("T002", "Conociendo tu arma", "Realiza 3 ataques básicos.", "Tutorial", {"exp": 150, "oro": 20, "item": "Arma"}, 1),
            Mision("T003", "El primer encargo", "Habla con el instructor.", "Tutorial", {"exp": 200, "oro": 30, "item": "Suministros"}, 2)
        ]
        self.misiones_disponibles.extend(tutoriales)

    def _inicializar_misiones_principales(self):
        catalogo = [
            Mision("P001", "El Despertar del Eter", "Habla con el guía de tu reino.", "Principal", {"exp": 100, "oro": 10}, 1),
            Mision("P002", "Primera Sangre", "Derrota a 5 enemigos.", "Principal", {"exp": 500, "oro": 50}, 5),
            Mision("P003", "El Sello Perdido", "Recupera una habilidad en mazmorra.", "Principal", {"exp": 1200, "oro": 200}, 15)
        ]
        self.misiones_disponibles.extend(catalogo)

    def generar_misiones_reino(self, reino: str, cantidad: int = 500):
        """Genera dinámicamente misiones basadas en la historia del reino."""
        # Integración con modulos/historia_lore.py para definir objetivos según el reino.
        # Estas misiones incluyen: Diálogos con NPCs, interactuar con estatuas de héroes, 
        # cacería de élites y recolección de artefactos antiguos.
        pass

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
