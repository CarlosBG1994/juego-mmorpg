"""
Modulo: Economia y Comercio de Snd-Worlds
Reglas:
- 100 Cobre = 1 Plata
- 100 Plata = 1 Oro
- 100 Oro = 1 Diamante
- 100 Diamante = 1 Platino
- Mochila con capacidad para guardar objetos y habilidades obtenidas.
- Comercio mediante Subasta, Gremio o Intercambio directo.
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
        # Todo se contabiliza internamente en cobre base
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

        cobre = resto
        return {
            "platino": platino,
            "diamante": diamante,
            "oro": oro,
            "plata": plata,
            "cobre": cobre
        }


class Mochila:
    def __init__(self):
        self.items = []
        self.billetera = Billetera()

    def anadir_item(self, item: dict):
        self.items.append(item)

    def eliminar_item(self, item_id: str):
        for index, it in enumerate(self.items):
            if it.get("id") == item_id:
                return self.items.pop(index)
        return None


class SistemaComercio:
    subastas_activas = []

    @classmethod
    def publicar_en_subasta(cls, vendedor_nombre: str, item: dict, precio_cobre: int):
        cls.subastas_activas.append({
            "vendedor": vendedor_nombre,
            "item": item,
            "precio": precio_cobre
        })

    @classmethod
    def intercambio_directo(cls, jugador_a, jugador_b, item_id_a: str, item_id_b: str):
        item_a = jugador_a.mochila.eliminar_item(item_id_a)
        item_b = jugador_b.mochila.eliminar_item(item_id_b)
        if item_a and item_b:
            jugador_a.mochila.anadir_item(item_b)
            jugador_b.mochila.anadir_item(item_a)
            return True, "Intercambio completado con exito."
        return False, "Uno de los objetos no fue encontrado."
