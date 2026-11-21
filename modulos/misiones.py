"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Tutorial, Diario, Legado.
- Estructura: Escalado hasta 2,000 misiones (500 por reino).
- Sistema de misiones secundarias infinitas y bloqueo de progresión global.
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
        self.progresion_bloqueada = False # Control para el salto de continente
        
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
            # ... hasta P99, misión final del Continente Primordial.
        ]
        self.misiones_disponibles.extend(catalogo)

    def generar_misiones_infinitas(self, tipo: str, nivel: int):
        """Generador procedural de misiones secundarias infinitas."""
        id_gen = f"INF_{tipo}_{nivel}"
        misiones_gen = {
            "caza": Mision(id_gen, "Contrato de Caza", "Elimina criaturas peligrosas en la zona.", "Secundaria", {"exp": 500}, nivel, True),
            "recoleccion": Mision(id_gen, "Recursos del Nexo", "Recolecta materiales antiguos.", "Secundaria", {"oro": 200}, nivel, True),
            "purgar": Mision(id_gen, "Justicia sobre Fugitivos", "Caza a los renegados que rompen la paz.", "Secundaria", {"exp": 800}, nivel, True)
        }
        return misiones_gen.get(tipo, None)

    def activar_mision(self, id_mision: str):
        # Bloqueo de progresión: Si es principal y está bloqueado, no permite activar
        mision = next((m for m in self.misiones_disponibles if m.id == id_mision), None)
        if mision and mision.tipo == "Principal" and self.progresion_bloqueada:
            return False, "La historia principal está en pausa. Busca el Nexo para continuar."
        
        return self._procesar_activacion(id_mision)

    def _procesar_activacion(self, id_mision):
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
                # Lógica de persistencia de repetibles
                if mision.es_repetible:
                    mision.estado = "Disponible"
                    self.misiones_disponibles.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                else:
                    self.misiones_historial.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                return True, mision.completar_mision()
        return False, "La misión no está activa o no existe."
