"""
Modulo: Monturas de Snd-Worlds
Gestiona los medios de transporte. Ofrecen velocidad, carga, 
identidad visual, efectos de estatus y bonos pasivos.
"""

class Montura:
    def __init__(self, id_montura: str, nombre: str, velocidad: float, bono_carga: int, 
                 precio: int, rareza: str = "Común", raza_req: str = None, 
                 es_mision: bool = False, visual: dict = None, buff: dict = None):
        self.id = id_montura
        self.nombre = nombre
        self.velocidad = velocidad
        self.bono_carga = bono_carga
        self.precio = precio
        self.rareza = rareza
        self.raza_req = raza_req
        self.es_mision = es_mision
        self.visual = visual or {"modelo_3d": "generic.obj", "particulas": "none", "escala": 1.0}
        # Nueva mejora: Buffs pasivos
        self.buff = buff or {"stat": None, "valor": 0} 
        self.fatiga = 0
        self.nivel_mejora = 0 # Permite subir el nivel de la montura

    def alimentar(self):
        """Gasto de recursos para reducir fatiga."""
        self.fatiga = max(0, self.fatiga - 30)
        return f"{self.nombre} ha recuperado energía."

    def usar_montura(self):
        if self.fatiga < 100:
            self.fatiga += 10
            return True
        return False

# Ejemplo de catálogo con Buffs (Nuevos datos añadidos)
CATALOGO_MONTURAS = [
    Montura("H03", "Corcel Paladín del Alba", 1.8, 20, 200000, "Leyenda", "Humano", False, 
            {"modelo_3d": "paladin.obj", "particulas": "gold_aura"}, {"stat": "VIT", "valor": 5}),
            
    Montura("M002", "Dragón del Cataclismo", 3.5, 100, 0, "Mítica", None, True, 
            {"modelo_3d": "dragon.obj", "particulas": "void_smoke"}, {"stat": "STR", "valor": 15})
]

def obtener_monturas_disponibles(raza: str):
    return [m for m in CATALOGO_MONTURAS if m.raza_req is None or m.raza_req == raza]

def equipar_montura(jugador, montura: Montura):
    # Lógica de equipamiento con aplicación de buff al jugador
    jugador.mochila.actualizar_bono_montura(montura.bono_carga)
    if montura.buff["stat"]:
        # Aplicar logicamente el bono a los stats del jugador aquí
        pass
    return f"Invocando a {montura.nombre}. Stats: +{montura.buff['valor']} en {montura.buff['stat']}."
