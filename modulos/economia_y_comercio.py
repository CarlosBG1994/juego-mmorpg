"""
Modulo: Economia y Comercio de Snd-Worlds
Reglas:
- 100 Cobre = 1 Plata, 100 Plata = 1 Oro, 100 Oro = 1 Diamante, 100 Diamante = 1 Platino
- Mochila con capacidad para guardar objetos y habilidades con bono de montura.
- Comercio mediante Subasta (con comisión del 5%), Gremio o Intercambio directo.
- Validación de precios mínimos para evitar ventas bajo mercado.
"""

VALOR_COBRE = {
    "cobre": 1,
    "plata": 100,
    "oro": 10_000,
    "diamante": 1_000_000,
    "platino": 100_000_000
}

# Tabla de valores mínimos por rareza (para evitar dumping de mercado)
VALOR_MINIMO_POR_TIER = {
    "VI": 100,          # Comun
    "V": 500,           # Poco Comun
    "IV": 2_000,        # Raro
    "III": 10_000,      # Ultra Raro
    "II": 100_000,      # Leyenda
    "I": 1_000_000      # Mitica
}

class Billetera:
    def __init__(self, cobre: int = 0):
        self.total_cobre = cobre

    def depositar(self, cobre: int = 0, plata: int = 0, oro: int = 0, diamante: int = 0, platino: int = 0):
        suma = (
            cobre * VALOR_COBRE["cobre"]
            + plata * VALOR_COBRE["plata"]
            + oro * VALOR_COBRE["oro"]
            + diamante * VALOR_COBRE["diamante"]
            + platino * VALOR_COBRE["platino"]
        )
        self.total_cobre += suma

    def retirar_cobre(self, total: int) -> bool:
        if self.total_cobre >= total:
            self.total_cobre -= total
            return True
        return False

    def desglose(self) -> dict:
        resto = self.total_cobre
        platino = resto // VALOR_COBRE["platino"]
        resto %= VALOR_COBRE["platino"]
        diamante = resto // VALOR_COBRE["diamante"]
        resto %= VALOR_COBRE["diamante"]
        oro = resto // VALOR_COBRE["oro"]
        resto %= VALOR_COBRE["oro"]
        plata = resto // VALOR_COBRE["plata"]
        resto %= VALOR_COBRE["plata"]
        return {"platino": platino, "diamante": diamante, "oro": oro, "plata": plata, "cobre": resto}


class Mochila:
    def __init__(self, capacidad_base: int = 20):
        self.items = []
        self.billetera = Billetera()
        self.capacidad_base = capacidad_base
        self.bono_carga_montura = 0

    @property
    def capacidad_total(self):
        return self.capacidad_base + self.bono_carga_montura

    def anadir_item(self, item: dict):
        if len(self.items) < self.capacidad_total:
            self.items.append(item)
            return True
        return False

    def eliminar_item(self, item_id: str):
        for index, it in enumerate(self.items):
            if it.get("id") == item_id:
                return self.items.pop(index)
        return None

    def actualizar_bono_montura(self, bono: int):
        self.bono_carga_montura = bono


class SistemaComercio:
    subastas_activas = []
    TASA_COMISION = 0.05  # 5% de comisión del sistema

    @classmethod
    def publicar_en_subasta(cls, vendedor_nombre: str, item: dict, precio_cobre: int):
        tier = item.get("tier", "VI")
        precio_minimo = VALOR_MINIMO_POR_TIER.get(tier, 100)

        if precio_cobre < precio_minimo:
            return False, f"Precio demasiado bajo. El mínimo para este objeto es {precio_minimo} cobre."

        cls.subastas_activas.append({
            "vendedor": vendedor_nombre,
            "item": item,
            "precio": precio_cobre
        })
        return True, "Objeto publicado exitosamente."

    @classmethod
    def procesar_venta(cls, indice_subasta: int, billetera_comprador: Billetera, billetera_vendedor: Billetera):
        subasta = cls.subastas_activas.pop(indice_subasta)
        precio = subasta["precio"]
        comision = int(precio * cls.TASA_COMISION)
        
        if billetera_comprador.retirar_cobre(precio):
            billetera_vendedor.depositar(cobre=(precio - comision))
            return True, f"Venta realizada. Comisión del sistema: {comision} cobre."
        return False, "Fondos insuficientes."

    @classmethod
    def intercambio_directo(cls, jugador_a, jugador_b, item_id_a: str, item_id_b: str):
        item_a = jugador_a.mochila.eliminar_item(item_id_a)
        item_b = jugador_b.mochila.eliminar_item(item_id_b)
        if item_a and item_b:
            if jugador_a.mochila.anadir_item(item_b) and jugador_b.mochila.anadir_item(item_a):
                return True, "Intercambio completado con exito."
            else:
                jugador_a.mochila.anadir_item(item_a)
                jugador_b.mochila.anadir_item(item_b)
                return False, "Uno de los jugadores no tiene espacio suficiente."
        return False, "Uno de los objetos no fue encontrado."
