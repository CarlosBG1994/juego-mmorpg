"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Tutorial, Diario, Legado.
- Estructura: Escalado hasta 2,000 misiones (500 por reino).
- Sistema de misiones secundarias infinitas y bloqueo de progresión global.
"""

class Mision:
    def __init__(self, id_mision: str, titulo: str, descripcion: str, tipo: str, recompensa: dict, npc_emisor: str, historia: str, nivel_req: int = 1, es_repetible: bool = False):
        self.id = id_mision
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo
        self.recompensa = recompensa
        self.npc_emisor = npc_emisor  # NPC que entrega la misión
        self.historia = historia      # Contexto narrativo del NPC
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
        self.progresion_bloqueada = False 
        
        # Catalogo base de NPCs por Reino para escalado
        self.npc_reino = {
            "Humano": ["Comandante Alaric", "Sacerdotisa Elara", "Herrero Bram"],
            "Elfo": ["Guardián Thalon", "Druida Lyra", "Explorador Finn"],
            "Enano": ["Maestro Forjador Durnik", "Guardia de Piedra", "Sabio Rúnico"],
            "Bestia": ["Chamán Garra", "Cazador de Manada", "Anciano del Clan"]
        }

    def registrar_mision_con_npc(self, id_mision, reino, titulo, tipo, recompensa, historia):
        """Método para poblar el mundo con misiones vinculadas a NPCs."""
        npc = self.npc_reino.get(reino, ["Guía Local"])[0] # Asignación dinámica
        nueva_mision = Mision(id_mision, titulo, f"Objetivo: {historia[:30]}...", tipo, recompensa, 1, False)
        nueva_mision.npc_emisor = npc
        nueva_mision.historia = historia
        self.misiones_disponibles.append(nueva_mision)

    def generar_misiones_infinitas(self, tipo: str, nivel: int):
        """Generador procedural para las 2000 misiones."""
        id_gen = f"INF_{tipo}_{nivel}"
        historia_base = "El conflicto en las fronteras crece, necesitamos tu fuerza."
        return Mision(id_gen, "Contrato del Nexo", "Ayuda a los reinos.", "Secundaria", {"exp": 500}, "NPC del Nexo", historia_base, nivel, True)

    def activar_mision(self, id_mision: str):
        mision = next((m for m in self.misiones_disponibles if m.id == id_mision), None)
        if mision and mision.tipo == "Principal" and self.progresion_bloqueada:
            return False, "La historia principal está en pausa. Busca el Nexo para continuar."
        
        if mision:
            mision.aceptar_mision()
            self.misiones_activas.append(self.misiones_disponibles.pop(self.misiones_disponibles.index(mision)))
            return True, f"Misión '{mision.titulo}' aceptada de {mision.npc_emisor}: '{mision.historia}'"
        return False, "Misión no encontrada."

    def entregar_mision(self, id_mision: str):
        for mision in self.misiones_activas:
            if mision.id == id_mision:
                mision.completar_mision()
                if mision.es_repetible:
                    mision.estado = "Disponible"
                    self.misiones_disponibles.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                else:
                    self.misiones_historial.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                return True, mision.completar_mision()
        return False, "La misión no está activa."
