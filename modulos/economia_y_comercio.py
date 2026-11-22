"""
Modulo: Economia y Comercio de Snd-Worlds
Reglas:
- 100 Cobre = 1 Plata
- 100 Plata = 1 Oro
- 100 Oro = 1 Diamante
- 100 Diamante = 1 Platino
- Mochila, Billetera, Subasta, Gremio e Intercambio directo.
"""

VALOR_COBRE = {
    "cobre": 1,
    "plata": 100,
    "oro": 10_000,
    "diamante": 1_000_000,
    "platino": 100_000_000
}

class Billetera:
    def __init__(self, cobre: int = 0):
        self.total_cobre = max(0, int(cobre))

    def depositar(self, cobre: int = 0, plata: int = 0, oro: int = 0, diamante: int = 0, platino: int = 0):
        suma = (
            int(cobre) * VALOR_COBRE["cobre"]
            + int(plata) * VALOR_COBRE["plata"]
            + int(oro) * VALOR_COBRE["oro"]
            + int(diamante) * VALOR_COBRE["diamante"]
            + int(platino) * VALOR_COBRE["platino"]
        )
        self.total_cobre += suma
        return self.total_cobre

    def retirar_cobre(self, cantidad: int, motivo: str = "") -> bool:
        if 0 <= cantidad <= self.total_cobre:
            self.total_cobre -= cantidad
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

        cobre = resto
        return {
            "platino": platino,
            "diamante": diamante,
            "oro": oro,
            "plata": plata,
            "cobre": cobre
        }


class Mochila:
    def __init__(self, capacidad_base: int = 30):
        self.items = []
        self.capacidad_max = capacidad_base
        self.billetera = Billetera()

    def anadir_item(self, item: dict) -> bool:
        if len(self.items) < self.capacidad_max:
            self.items.append(item)
            return True
        return False

    def eliminar_item(self, item_id: str):
        for index, it in enumerate(self.items):
            if it.get("id") == item_id:
                return self.items.pop(index)
        return None

    def actualizar_bono_montura(self, bono_carga: int):
        self.capacidad_max = 30 + max(0, bono_carga)


class SistemaComercio:
    subastas_activas = []
    historial_ventas = []
    busquedas_activas = []

    @classmethod
    def publicar_en_subasta(cls, vendedor_nombre: str, item: dict, precio_cobre: int):
        registro = {
            "vendedor": vendedor_nombre,
            "item": item,
            "precio": precio_cobre
        }
        cls.subastas_activas.append(registro)
        return True, "Item publicado en subasta."

    @classmethod
    def publicar_busqueda(cls, jugador: object, item_nombre: str, precio_oferta: int):
        if hasattr(jugador, "mochila") and jugador.mochila.billetera.retirar_cobre(precio_oferta, "Bloqueo por búsqueda"):
            cls.busquedas_activas.append({
                "jugador": getattr(jugador, "nombre", "Aventurero"),
                "item_nombre": item_nombre,
                "precio": precio_oferta
            })
            return True, "Búsqueda publicada. Dinero reservado."
        return False, "Fondos insuficientes para la oferta."

    @classmethod
    def obtener_notificaciones_mercado(cls, nombre_jugador: str):
        return [h for h in cls.historial_ventas if h.get("vendedor") == nombre_jugador]
