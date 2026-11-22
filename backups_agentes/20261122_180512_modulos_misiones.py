"""
Modulo: Misiones de Snd-Worlds
Gestiona la creación, seguimiento y finalización de misiones.
- Tipos: Principal, Secundaria, Tutorial, Diario, Legado.
- Sistema de Escrow para contratos de jugadores.
- Recompensas: Monedas (cobre/plata/oro/diamante/platino), Exp, y Objetos (Tier VI a I).
"""

class Mision:
    def __init__(self, id_mision: str, titulo: str, descripcion: str, tipo: str, recompensa: dict, npc_emisor: str, historia: str, nivel_req: int = 1, es_repetible: bool = False, requiere_clase: str = None, emisor_jugador: str = None):
        self.id = id_mision
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo # "Principal", "Secundaria", "Diaria"
        self.recompensa = recompensa # {"cobre": X, "exp": Y, "objeto": {"nombre": Z, "tier": T}}
        self.npc_emisor = npc_emisor
        self.historia = historia
        self.nivel_req = nivel_req
        self.es_repetible = es_repetible
        self.requiere_clase = requiere_clase
        self.emisor_jugador = emisor_jugador # ID si fue creada por un jugador
        self.estado = "Disponible"

    def aceptar_mision(self):
        self.estado = "Activa"

class GestorMisiones:
    def __init__(self):
        self.misiones_disponibles = []
        self.misiones_activas = []
        self.misiones_historial = []
        self.escrow_recompensas = {} # Almacena depósitos de jugadores
        self.progresion_bloqueada = False

    def publicar_mision_jugador(self, id_mision, titulo, recompensa, jugador_id, clase_req):
        """
        Publica una misión creada por un jugador en el tablón.
        La recompensa se retiene en escrow.
        """
        # Validación de tier de objeto: VI a I (ajuste según economía global)
        if "objeto" in recompensa and recompensa["objeto"].get("tier") not in ["VI", "V", "IV", "III", "II", "I"]:
            return False, "Tier de objeto no válido."
        
        nueva_mision = Mision(
            id_mision, titulo, "Misión de jugador", "Secundaria", 
            recompensa, "Tablón del Gremio", "Contrato privado", 
            1, False, clase_req, jugador_id
        )
        
        # Guardar en Escrow
        self.escrow_recompensas[id_mision] = recompensa
        self.misiones_disponibles.append(nueva_mision)
        return True, "Misión publicada y recompensa depositada en escrow."

    def entregar_mision(self, id_mision: str):
        for mision in self.misiones_activas:
            if mision.id == id_mision:
                recompensa = mision.recompensa
                
                # Si era una misión de jugador, liberamos el escrow
                if mision.emisor_jugador:
                    del self.escrow_recompensas[mision.id]
                
                mision.estado = "Completada"
                self.misiones_historial.append(self.misiones_activas.pop(self.misiones_activas.index(mision)))
                return True, recompensa
        return False, "La misión no está activa."

    def generar_misiones_infinitas(self, tipo: str, nivel: int, clase_jugador: str = None):
        """Generador procedural de misiones para el tablón (Secundarias)."""
        id_gen = f"INF_{tipo}_{nivel}"
        tier_obj = "VI" if nivel < 20 else "IV"
        recompensa_base = {
            "cobre": nivel * 100, 
            "exp": nivel * 200, 
            "objeto": {"nombre": f"Equipo de nivel {nivel}", "tier": tier_obj}
        }
        
        return Mision(id_gen, "Contrato del Tablón", "Ayuda solicitada.", "Secundaria", 
                      recompensa_base, "Tablón del Gremio", "Misión del Gremio.", nivel, True, clase_jugador)

    def activar_mision(self, id_mision: str):
        mision = next((m for m in self.misiones_disponibles if m.id == id_mision), None)
        if mision:
            mision.aceptar_mision()
            self.misiones_activas.append(self.misiones_disponibles.pop(self.misiones_disponibles.index(mision)))
            return True, f"Misión '{mision.titulo}' iniciada."
        return False, "Misión no encontrada."
