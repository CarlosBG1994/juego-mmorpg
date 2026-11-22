# (Añadir a SistemaComercio)

    busquedas_activas = [] # Lista de {jugador, item_nombre, precio_ofrecido}

    @classmethod
    def publicar_busqueda(cls, jugador: object, item_nombre: str, precio_oferta: int):
        # El jugador bloquea el dinero de la oferta en escrow temporal
        if jugador.mochila.billetera.retirar_cobre(precio_oferta, "Bloqueo por búsqueda"):
            cls.busquedas_activas.append({
                "jugador": jugador.nombre,
                "item_nombre": item_nombre,
                "precio": precio_oferta
            })
            return True, "Búsqueda publicada. Dinero reservado."
        return False, "Fondos insuficientes para la oferta."

    @classmethod
    def obtener_notificaciones_mercado(cls, nombre_jugador: str):
        # Filtra el historial para un jugador específico
        return [h for h in cls.historial_ventas if h.get("vendedor") == nombre_jugador]

# ... (El resto del código anterior permanece igual)
