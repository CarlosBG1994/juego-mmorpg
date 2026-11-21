"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Tutorial, Diario, Legado.
- Estructura: Escalado hasta 2,000 misiones (500 por reino).
"""

class Mision:
    def __init__(self, id_mision: str, titulo: str, descripcion: str, tipo: str, recompensa: dict, nivel_req: int = 1, es_repetible: bool = False):
        self.id = id_mision
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo  # "Principal", "Secundaria", "Tutorial", "Diaria", "Legado"
        self.recompensa = recompensa
        self.nivel_req = nivel_req
        self.es_repetible = es_repetible
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
        # Inicialización base
        self._inicializar_misiones_tutorial()
        self._inicializar_misiones_principales()

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

    def generar_misiones_secundarias_y_diarias(self, zona: str, nivel: int):
        """Genera dinámicamente misiones de caza, recolección y diarias."""
        # 1. Caza de Criminales (Secundaria)
        self.misiones_disponibles.append(Mision(f"S_{zona}_01", "Justicia del Continente", "Caza al jugador fugitivo de esta zona.", "Secundaria", {"oro": 500}, nivel))
        # 2. Mazmorras (Secundaria)
        self.misiones_disponibles.append(Mision(f"M_{zona}_01", "Limpieza de Mazmorra", "Derrota al Jefe Final de la zona.", "Secundaria", {"exp": 2000, "item": "Cofre Raro"}, nivel))
        # 3. Diario (Repetible)
        self.misiones_disponibles.append(Mision(f"D_{zona}_01", "Patrulla Diaria", "Derrota a 20 enemigos de la zona.", "Diaria", {"exp": 1000, "oro": 100}, nivel, True))

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
                # Si es diaria/repetible, la movemos de nuevo a disponibles tras un tiempo
                if mision.es_repetible:
                    mision.estado = "Disponible"
                    self.misiones_disponibles.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                else:
                    self.misiones_historial.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                return True, mision.completar_mision()
        return False, "La misión no está activa o no existe."
