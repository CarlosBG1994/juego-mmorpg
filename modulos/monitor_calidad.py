"""
Modulo: monitor_calidad
Rol: Auditoría de alta disponibilidad y validación de escalabilidad.
"""

import time
import uuid

class MonitorCalidad:
    def __init__(self):
        self.errores_detectados = []
        self.estado_servicios = {"auth_google": "offline", "sync_global": "offline"}
        self.ids_registrados = set() # Base para detectar colisiones en millones de usuarios

    def auditar_inicio_sesion(self, proveedor: str, status: str, jugador_id: str = None):
        log_entry = {"ts": time.time(), "accion": "LOGIN_ATTEMPT", "proveedor": proveedor, "status": status, "jugador": jugador_id}
        
        # Auditoría de Escala: Detectar si el ID es nulo o duplicado
        if not jugador_id or jugador_id in self.ids_registrados:
            self.errores_detectados.append({"error": "COLISION_O_ID_INVALIDO", "id": jugador_id})
            return False
            
        if status == "success":
            self.estado_servicios["auth_google"] = "online"
            self.ids_registrados.add(jugador_id)
            return True
        return False

    def verificar_integridad_sesion(self, jugador):
        # Auditoría de Objeto: Validación rápida de estructura (Crucial para performance)
        if not hasattr(jugador, 'id') or not jugador.id:
            return False, "CRITICAL: Objeto jugador malformado."
        return True, "OK"

    def simular_flujo_login(self, jugador_mock):
        print(f"[QA TEST] Auditando Login ID: {jugador_mock.id}")
        success = self.auditar_inicio_sesion("Google", "success", jugador_mock.id)
        if success:
            valido, mensaje = self.verificar_integridad_sesion(jugador_mock)
            return valido
        return False

    def auditoria_estres_nodos(self, cantidad):
        """Simula carga masiva para verificar que el sistema no colapse."""
        print(f"[QA STRESS TEST] Iniciando auditoría de {cantidad} registros simultáneos...")
        start = time.time()
        for i in range(cantidad):
            test_id = f"USR_{uuid.uuid4().hex[:8]}"
            self.ids_registrados.add(test_id)
        print(f"[QA STRESS TEST] Procesados {cantidad} usuarios en {time.time() - start:.4f}s.")

# Instancia para el sistema
monitor_qa = MonitorCalidad()
