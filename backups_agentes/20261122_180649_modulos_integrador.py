import time

class Jugador:
    """Fachada del jugador optimizada para entornos distribuidos."""
    def __init__(self, id_jugador, raza, clase):
        self.id = id_jugador
        self.raza = raza
        self.clase = clase
        self.version = 1  # Para control de concurrencia (Locking)
        self.nodo_actual = "Continente Primordial"

    def equipar_habilidad(self, habilidad_id):
        # 1. Validación de compatibilidad (Servicio distribuido)
        if not ServicioValidacion.es_compatible(self.raza, self.clase, habilidad_id):
            return False, "Error: Habilidad no compatible con tu clase."
            
        # 2. Emisión de evento para persistencia (Desacoplamiento)
        # EventBus garantiza que el cambio se replique en la DB y caché global
        resultado = EventBus.emit("EQUIPAR_HABILIDAD", {
            "jugador": self.id, 
            "hab": habilidad_id,
            "version": self.version
        })
        
        if resultado:
            self.version += 1 # Incrementar versión para el siguiente estado
            return True, "Habilidad equipada y sincronizada globalmente."
        return False, "Error en la sincronización del estado."

    def migrar_servidor(self, destino: str):
        """Gestiona el paso entre continentes (Sharding)."""
        if self.nodo_actual != destino:
            # Bloqueo preventivo de acciones durante la migración
            EventBus.emit("MIGRACION_INICIADA", {"jugador": self.id, "origen": self.nodo_actual, "destino": destino})
            self.nodo_actual = destino
            return True, f"Has migrado exitosamente al {destino}."
        return False, "Ya te encuentras en este continente."

# --- Simulacros de servicios de soporte ---
class ServicioValidacion:
    @staticmethod
    def es_compatible(raza, clase, hab_id):
        # Lógica maestra que consulta la base de reglas centralizada
        return True 

class EventBus:
    @staticmethod
    def emit(evento, datos):
        # Conecta con RabbitMQ/Kafka para actualizar el estado global
        print(f"Evento {evento} procesado en cluster para jugador {datos.get('jugador')}")
        return True
