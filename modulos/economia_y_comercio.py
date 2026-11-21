"""
Modulo: Economia y Comercio de Snd-Worlds
Reglas:
- 100 Cobre = 1 Plata, 100 Plata = 1 Oro, 100 Oro = 1 Diamante, 100 Diamante = 1 Platino
- Mochila: capacidad base 20 + bono por montura.
- Subastas: Tasa de publicación (1%), Comisión venta (5%).
- Límite: Subastas estándar 1 hora. Subastas Tier I-III (15 min) con aviso global.
"""

import time

VALOR_COBRE = {"cobre": 1, "plata": 100, "oro": 10_000, "diamante": 1_000_000, "platino": 100_000_000}
VALOR_MINIMO_POR_TIER = {"VI": 100, "V": 500, "IV": 2_000, "III": 10_000, "II": 100_000, "I": 1_000_000}

class Billetera:
    def __init__(self, cobre: int = 0):
        self.total_cobre = cobre

    def depositar(self, cobre: int = 0, plata: int = 0, oro: int = 0, diamante: int = 0, platino: int = 0):
        suma = (cobre * VALOR_COBRE["cobre"] + plata * VALOR_COBRE["plata"] + oro * VALOR_COBRE["oro"] + diamante * VALOR_COBRE["diamante"] + platino * VALOR_COBRE["platino"])
        self.total_cobre += suma

    def retirar_cobre(self, total: int) -> bool:
        if self.total_cobre >= total:
            self.total_cobre -= total
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
    historial_ventas = []
    TASA_PUBLICACION = 0.01 
    TASA_COMISION = 0.05

    @classmethod
    def publicar_en_subasta(cls, vendedor_nombre: str, item: dict, precio_cobre: int, billetera_vendedor: Billetera):
        # 1. Validación de precio mínimo
        tier = item.get("tier", "VI")
        if precio_cobre < VALOR_MINIMO_POR_TIER.get(tier, 100):
            return False, "Precio inferior al mínimo de mercado."

        # 2. Impuesto de publicación
        coste_publicacion = int(precio_cobre * cls.TASA_PUBLICACION)
        if not billetera_vendedor.retirar_cobre(coste_publicacion):
            return False, "Fondos insuficientes para tasa de publicación."

        # 3. Lógica de tiempo: 15 min para alta gama (I-III), 60 min resto
        duracion = 900 if tier in ["I", "II", "III"] else 3600
        if tier in ["I", "II", "III"]:
            print(f"[AVISO GLOBAL] ¡Subasta de alto nivel {item['nombre']} disponible! Tiempo: 15 min.")

        cls.subastas_activas.append({
            "vendedor": vendedor_nombre,
            "item": item,
            "precio": precio_cobre,
            "fin": time.time() + duracion
        })
        return True, f"Objeto publicado. Se cobró {coste_publicacion} de tasa."

    @classmethod
    def registrar_transaccion(cls, vendedor, comprador, item, precio):
        cls.historial_ventas.append({
            "vendedor": vendedor, "comprador": comprador, "item": item, "precio": precio, "timestamp": time.time()
        })

    @classmethod
    def procesar_venta(cls, indice_subasta: int, billetera_comprador: Billetera, billetera_vendedor: Billetera):
        subasta = cls.subastas_activas[indice_subasta]
        if time.time() > subasta["fin"]:
            return False, "La subasta ha expirado."
            
        precio = subasta["precio"]
        comision = int(precio * cls.TASA_COMISION)
        
        if billetera_comprador.retirar_cobre(precio):
            billetera_vendedor.depositar(cobre=(precio - comision))
            cls.registrar_transaccion(subasta["vendedor"], "Comprador", subasta["item"], precio)
            cls.subastas_activas.pop(indice_subasta)
            return True, "Venta realizada exitosamente."
        return False, "Fondos insuficientes."
