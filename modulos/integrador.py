class Jugador:
    # Ahora el jugador es solo una "fachada" que consulta servicios remotos
    def equipar_habilidad(self, habilidad_id):
        # 1. Llama al servicio de validación (rápido y distribuido)
        if not ServicioValidacion.es_compatible(self.raza, self.clase, habilidad_id):
            return False, "Error de compatibilidad"
            
        # 2. Envía orden al EventBus para actualizar en la DB persistente
        EventBus.emit("EQUIPAR_HABILIDAD", {"jugador": self.id, "hab": habilidad_id})
        return True, "Habilidad enviada a sincronización."
