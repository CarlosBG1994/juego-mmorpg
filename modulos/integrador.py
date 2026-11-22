import time

class Jugador:
    """Fachada del jugador optimizada para entornos distribuidos."""
    def __init__(self, id_jugador, raza, clase):
        self.id = id_jugador
        self.raza = raza
        self.clase = clase
        self.version = 1  # Control de concurrencia para evitar race conditions
        self.nodo_actual = "Continente Primordial"

    def equipar_habilidad(self, habilidad_id):
        if not ServicioValidacion.es_compatible(self.raza, self.clase, habilidad_id):
            return False, "Error: Habilidad no compatible con tu clase."
            
        resultado = EventBus.emit("EQUIPAR_HABILIDAD", {
            "jugador": self.id, 
            "hab": habilidad_id,
            "version": self.version
        })
        
        if resultado:
            self.version += 1 
            return True, "Habilidad equipada y sincronizada globalmente."
        return False, "Error en la sincronización del estado."

    def migrar_servidor(self, destino: str):
        """Gestión de Sharding: Mueve el estado del jugador entre continentes."""
        if self.nodo_actual != destino:
            EventBus.emit("MIGRACION_INICIADA", {"jugador": self.id, "origen": self.nodo_actual, "destino": destino})
            self.nodo_actual = destino
            return True, f"Migración a {destino} completada."
        return False, "Ya estás en este nodo."

    def ejecutar_transaccion(self, valor, tipo, target_id):
        """
        Transacción Atómica (2PC):
        1. Pre-validación (Locking de fondos).
        2. Ejecución (Transferencia).
        3. Confirmación (Commit).
        """
        # Se solicita al sistema de economía una transacción segura
        transaccion = EventBus.emit("ECONOMIA_TRANSACCION", {
            "origen": self.id,
            "destino": target_id,
            "monto": valor,
            "tipo": tipo,
            "timestamp": time.time()
        })
        return transaccion

# --- Simulacros de servicios de soporte ---
class ServicioValidacion:
    @staticmethod
    def es_compatible(raza, clase, hab_id):
        return True 

class EventBus:
    @staticmethod
    def emit(evento, datos):
        # En una arquitectura real, esto notifica a RabbitMQ/Kafka
        # garantizando que no se pierdan transacciones bajo carga masiva
        print(f"[EVENTO] {evento} procesado exitosamente para {datos.get('jugador', 'SISTEMA')}")
        return True
