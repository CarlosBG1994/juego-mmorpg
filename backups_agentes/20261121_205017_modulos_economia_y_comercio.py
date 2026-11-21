# (Añadir dentro de la clase SistemaComercio)

    historial_ventas = [] # Registro global de transacciones
    TASA_PUBLICACION = 0.01 # 1% del precio para evitar spam de subastas

    @classmethod
    def publicar_en_subasta_mejorado(cls, vendedor_nombre: str, item: dict, precio_cobre: int, billetera_vendedor: Billetera):
        # Cobrar tasa de publicación
        coste_publicacion = int(precio_cobre * cls.TASA_PUBLICACION)
        if not billetera_vendedor.retirar_cobre(coste_publicacion):
            return False, "Fondos insuficientes para pagar la tasa de publicación."
        
        # ... (aquí iría el resto de la lógica de publicar_en_subasta ya existente)
        return True, "Objeto publicado. Se ha cobrado una tasa de publicación."

    @classmethod
    def registrar_transaccion(cls, vendedor, comprador, item, precio):
        cls.historial_ventas.append({
            "vendedor": vendedor,
            "comprador": comprador,
            "item": item,
            "precio": precio
        })
