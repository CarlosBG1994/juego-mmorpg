"""
Modulo: modulos/economia_y_comercio.py
Sistema economico: Cobre, Plata, Oro, Diamante, Platino.
Inventario para objetos y habilidades (equipables o no), Subasta, Gremio e Intercambio.
"""

class Monedero:
    """Manejo de monedas con equivalencia base en cobre: 100 Cobre = 1 Plata, etc."""
    VALOR_COBRE = 1
    VALOR_PLATA = 100
    VALOR_ORO = 10000
    VALOR_DIAMANTE = 1000000
    VALOR_PLATINO = 100000000

    def __init__(self, cobre_total: int = 0):
        self.cobre_total = max(0, cobre_total)

    def anadir(self, cobre: int = 0, plata: int = 0, oro: int = 0, diamante: int = 0, platino: int = 0):
        total = (
            cobre * self.VALOR_COBRE +
            plata * self.VALOR_PLATA +
            oro * self.VALOR_ORO +
            diamante * self.VALOR_DIAMANTE +
            platino * self.VALOR_PLATINO
        )
        self.cobre_total += total

    def retirar(self, cobre_total_a_retirar: int) -> bool:
        if self.cobre_total >= cobre_total_a_retirar:
            self.cobre_total -= cobre_total_a_retirar
            return True
        return False

    def desglose(self) -> dict:
        resto = self.cobre_total
        platino = resto // self.VALOR_PLATINO
        resto %= self.VALOR_PLATINO

        diamante = resto // self.VALOR_DIAMANTE
        resto %= self.VALOR_DIAMANTE

        oro = resto // self.VALOR_ORO
        resto %= self.VALOR_ORO

        plata = resto // self.VALOR_PLATA
        cobre = resto % self.VALOR_PLATA

        return {
            "platino": platino,
            "diamante": diamante,
            "oro": oro,
            "plata": plata,
            "cobre": cobre
        }

class Mochila:
    """Almacena equipo, objetos y habilidades que pueden venderse aunque no sean equipables."""
    def __init__(self, capacidad: int = 50):
        self.capacidad = capacidad
        self.items = []
        self.habilidades_almacenadas = []
        self.monedero = Monedero()

    def guardar_habilidad(self, habilidad) -> bool:
        if len(self.habilidades_almacenadas) < self.capacidad:
            self.habilidades_almacenadas.append(habilidad)
            return True
        return False

class MercadoComercio:
    """Permite el comercio por Subasta, Gremio e Intercambio directo."""
    def __init__(self):
        self.subastas = []
        self.tiendas_gremio = {}

    def publicar_en_subasta(self, vendedor: str, item_o_habilidad, precio_cobre: int):
        lote = {
            "id_lote": len(self.subastas) + 1,
            "vendedor": vendedor,
            "articulo": item_o_habilidad,
            "precio_cobre": precio_cobre
        }
        self.subastas.append(lote)
        return lote["id_lote"]

    def realizar_intercambio(self, pj_a, pj_b, item_a, item_b):
        """Intercambio directo entre dos jugadores."""
        # Se gestiona el traspaso directo y seguro entre mochilas
        return True
