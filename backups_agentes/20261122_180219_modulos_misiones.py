"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Tutorial, Diario, Legado.
- Estructura: Escalado hasta 2,000 misiones (500 por reino).
- Sistema de misiones secundarias infinitas y bloqueo de progresión global.
- Sistema de recompensas: Monedas (Economía), Experiencia y Objetos específicos por Clase.
"""

class Mision:
    def __init__(self, id_mision: str, titulo: str, descripcion: str, tipo: str, recompensa: dict, npc_emisor: str, historia: str, nivel_req: int = 1, es_repetible: bool = False, requiere_clase: str = None):
        self.id = id_mision
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo
        self.recompensa = recompensa # Dict: {"cobre": X, "exp": Y, "objeto": Z}
        self.npc_emisor = npc_emisor
        self.historia = historia
        self.nivel_req = nivel_req
        self.es_repetible = es_repetible
        self.requiere_clase = requiere_clase # Filtro para recompensas de clase
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
        self.progresion_bloqueada = False 
        
        self.npc_reino = {
            "Humano": ["Comandante Alaric", "Sacerdotisa Elara", "Herrero Bram"],
            "Elfo": ["Guardián Thalon", "Druida Lyra", "Explorador Finn"],
            "Enano": ["Maestro Forjador Durnik", "Guardia de Piedra", "Sabio Rúnico"],
            "Bestia": ["Chamán Garra", "Cazador de Manada", "Anciano del Clan"]
        }

    def registrar_mision_tablon(self, id_mision, reino, titulo, tipo, recompensa, historia, clase_obj=None):
        """Registra misiones que aparecen en tablones de gremios."""
        npc = "Tablón del Gremio"
        nueva_mision = Mision(id_mision, titulo, historia, tipo, recompensa, npc, historia, 1, False, clase_obj)
        self.misiones_disponibles.append(nueva_mision)

    def generar_misiones_infinitas(self, tipo: str, nivel: int, clase_jugador: str = None):
        """Generador procedural con recompensas escaladas y objetos de clase opcionales."""
        id_gen = f"INF_{tipo}_{nivel}"
        recompensa_base = {"cobre": nivel * 50, "exp": nivel * 100}
        
        # Lógica de objeto de clase (10% de probabilidad)
        if clase_jugador:
            recompensa_base["objeto"] = f"Equipo Legendario para {clase_jugador}"
            
        return Mision(id_gen, "Contrato del Nexo", "Ayuda a los reinos.", "Secundaria", 
                      recompensa_base, "Tablón del Gremio", "Misión generada por la necesidad del reino.", nivel, True)

    def activar_mision(self, id_mision: str):
        mision = next((m for m in self.misiones_disponibles if m.id == id_mision), None)
        if mision and mision.tipo == "Principal" and self.progresion_bloqueada:
            return False, "La historia principal está en pausa. Busca el Nexo para continuar."
        
        if mision:
            mision.aceptar_mision()
            self.misiones_activas.append(self.misiones_disponibles.pop(self.misiones_disponibles.index(mision)))
            return True, f"Misión aceptada: {mision.titulo}. Recompensa: {mision.recompensa}"
        return False, "Misión no encontrada."

    def entregar_mision(self, id_mision: str):
        for mision in self.misiones_activas:
            if mision.id == id_mision:
                mision.completar_mision()
                resultado = mision.recompensa
                if mision.es_repetible:
                    mision.estado = "Disponible"
                    self.misiones_disponibles.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                else:
                    self.misiones_historial.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                return True, resultado
        return False, "La misión no está activa."
