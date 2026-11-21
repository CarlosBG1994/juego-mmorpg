"""
Modulo: Economia y Comercio de Snd-Worlds
Reglas:
- 100 Cobre = 1 Plata, 100 Plata = 1 Oro, 100 Oro = 1 Diamante, 100 Diamante = 1 Platino
- Mochila: capacidad base 20 + bono por montura.
- Subastas: Tasa 1%, Comisión 5%, Sistema Escrow, Soporte Buyout, Protección Sniping.
- Auditoría: Registro de transacciones y logs de billetera.
"""

import time

VALOR_COBRE = {"cobre": 1, "plata": 100, "oro": 10_000, "diamante": 1_000_000, "platino": 100_000_000}
VALOR_MINIMO_POR_TIER = {"VI": 100, "V": 500, "IV": 2_000, "III": 10_000, "II": 100_000, "I": 1_000_000}

class Billetera:
    def __init__(self, cobre: int = 0):
        self.total_cobre = cobre
        self.logs = [] # Auditoría de movimientos

    def depositar(self, cobre: int, razon: str = "General"):
        self.total_cobre += cobre
        self.logs.append({"ts": time.time(), "cambio": +cobre, "razon": razon})

    def retirar_cobre(self, total: int, razon: str = "General") -> bool:
        if self.total_cobre >= total:
            self.total_cobre -= total
            self.logs.append({"ts": time.time(), "cambio": -total, "razon": razon})
            return True
        return False

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

class SistemaComercio:
    subastas_activas = [] 
    almacen_escrow = {}   
    items_en_subasta = set() # Protección contra duplicación
    historial_ventas = []
    TASA_PUBLICACION = 0.01 
    TASA_COMISION = 0.05

    @classmethod
    def publicar_en_subasta(cls, vendedor: object, item: dict, precio_inicio: int, precio_buyout: int = 0):
        if item["id"] in cls.items_en_subasta:
            return False, "Objeto ya en proceso de subasta."

        tier = item.get("tier", "VI")
        if precio_inicio < VALOR_MINIMO_POR_TIER.get(tier, 100):
            return False, "Precio inferior al mínimo."

        item_data = vendedor.mochila.eliminar_item(item.get("id"))
        if not item_data: return False, "Objeto no encontrado."
        
        cls.almacen_escrow[item["id"]] = item_data
        cls.items_en_subasta.add(item["id"])
        
        coste = int(precio_inicio * cls.TASA_PUBLICACION)
        if not vendedor.mochila.billetera.retirar_cobre(coste, "Tasa publicación"):
            return False, "Fondos insuficientes para tasa."

        cls.subastas_activas.append({
            "vendedor": vendedor.nombre,
            "item_id": item["id"],
            "precio_actual": precio_inicio,
            "precio_buyout": precio_buyout,
            "fin": time.time() + (900 if tier in ["I", "II", "III"] else 3600)
        })
        return True, "Objeto publicado."

    @classmethod
    def procesar_compra(cls, indice: int, comprador: object, tipo_compra: str = "normal"):
        subasta = cls.subastas_activas[indice]
        
        # Lógica de Protección Anti-Sniping: Extender 2 min si faltan menos de 5 min
        if (subasta["fin"] - time.time()) < 300:
            subasta["fin"] += 120 
            
        precio = subasta["precio_buyout"] if tipo_compra == "buyout" else subasta["precio_actual"]
        
        if comprador.mochila.billetera.retirar_cobre(precio, "Compra subasta"):
            item = cls.almacen_escrow.pop(subasta["item_id"])
            cls.items_en_subasta.remove(subasta["item_id"])
            comprador.mochila.anadir_item(item)
            cls.subastas_activas.pop(indice)
            cls.historial_ventas.append({"item": item["id"], "precio": precio, "ts": time.time()})
            return True, "Compra exitosa."
        return False, "Fondos insuficientes."

    @classmethod
    def obtener_subastas_por_tier(cls, tier: str):
        return [s for s in cls.subastas_activas if cls.almacen_escrow[s["item_id"]].get("tier") == tier]
