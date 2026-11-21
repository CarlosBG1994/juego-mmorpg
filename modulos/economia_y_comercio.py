"""
Modulo: Economia y Comercio de Snd-Worlds
Conversion de monedas (Cobre, Plata, Oro, Diamante, Platino con base 100).
Mochila, Subastas, Comercio de Gremio e Intercambio directo.
"""

from typing import Dict, List, Optional, Any

COBRE_POR_PLATA = 100
PLATA_POR_ORO = 100
ORO_POR_DIAMANTE = 100
DIAMANTE_POR_PLATINO = 100

class Monedero:
    """Gestiona el saldo en la unidad base (cobre) con conversion automatica."""
    def __init__(self, cobre_total: int = 0):
        self.cobre_total = max(0, cobre_total)

    def agregar_cobre(self, cantidad: int):
        self.cobre_total += max(0, cantidad)

    def retirar_cobre(self, cantidad: int) -> bool:
        if cantidad <= self.cobre_total:
            self.cobre_total -= cantidad
            return True
        return False

    def desglose(self) -> Dict[str, int]:
        total = self.cobre_total
        cobre = total % COBRE_POR_PLATA
        total //= COBRE_POR_PLATA
        
        plata = total % PLATA_POR_ORO
        total //= PLATA_POR_ORO
        
        oro = total % ORO_POR_DIAMANTE
        total //= ORO_POR_DIAMANTE
        
        diamante = total % DIAMANTE_POR_PLATINO
        platino = total // DIAMANTE_POR_PLATINO
        
        return {
            "platino": platino,
            "diamante": diamante,
            "oro": oro,
            "plata": plata,
            "cobre": cobre
        }

    @staticmethod
    def a_cobre(platino: int = 0, diamante: int = 0, oro: int = 0, plata: int = 0, cobre: int = 0) -> int:
        return (
            cobre +
            plata * 100 +
            oro * 10000 +
            diamante * 1000000 +
            platino * 100000000
        )

class ItemInventario:
    def __init__(self, id_item: str, nombre: str, tipo: str, datos: Optional[Dict] = None):
        self.id_item = id_item
        self.nombre = nombre
        self.tipo = tipo  # 'habilidad', 'equipo', 'material', 'consumible'
        self.datos = datos or {}

class Mochila:
    def __init__(self, capacidad_maxima: int = 100):
        self.capacidad_maxima = capacidad_maxima
        self.items: List[ItemInventario] = []
        self.monedero = Monedero()

    def agregar_item(self, item: ItemInventario) -> bool:
        if len(self.items) < self.capacidad_maxima:
            self.items.append(item)
            return True
        return False

    def remover_item(self, id_item: str) -> Optional[ItemInventario]:
        for i, it in enumerate(self.items):
            if it.id_item == id_item:
                return self.items.pop(i)
        return None

class MercadoSubasta:
    def __init__(self):
        self.lotes: List[Dict[str, Any]] = []
        self.siguiente_lote_id = 1

    def publicar_lote(self, vendedor_id: str, item: ItemInventario, precio_cobre: int) -> int:
        lote_id = self.siguiente_lote_id
        self.siguiente_lote_id += 1
        self.lotes.append({
            "lote_id": lote_id,
            "vendedor_id": vendedor_id,
            "item": item,
            "precio_cobre": precio_cobre,
            "estado": "activo"
        })
        return lote_id

    def comprar_lote(self, lote_id: int, comprador_mochila: Mochila) -> Optional[ItemInventario]:
        for lote in self.lotes:
            if lote["lote_id"] == lote_id and lote["estado"] == "activo":
                if comprador_mochila.monedero.retirar_cobre(lote["precio_cobre"]):
                    lote["estado"] = "vendido"
                    comprador_mochila.agregar_item(lote["item"])
                    return lote["item"]
        return None

class IntercambioDirecto:
    @staticmethod
    def realizar_intercambio(
        jugador_a_mochila: Mochila, item_a_id: str,
        jugador_b_mochila: Mochila, item_b_id: str
    ) -> bool:
        item_a = jugador_a_mochila.remover_item(item_a_id)
        item_b = jugador_b_mochila.remover_item(item_b_id)
        
        if not item_a or not item_b:
            # Revertir si fallo alguno
            if item_a:
                jugador_a_mochila.agregar_item(item_a)
            if item_b:
                jugador_b_mochila.agregar_item(item_b)
            return False

        jugador_a_mochila.agregar_item(item_b)
        jugador_b_mochila.agregar_item(item_a)
        return True
