"""
Modulo: Monturas de Snd-Worlds
Gestiona los medios de transporte. Ofrecen velocidad, carga, 
identidad visual y efectos de estatus.
"""

class Montura:
    def __init__(self, id_montura: str, nombre: str, velocidad: float, bono_carga: int, 
                 precio: int, rareza: str = "Común", raza_req: str = None, 
                 es_mision: bool = False, visual: dict = None):
        self.id = id_montura
        self.nombre = nombre
        self.velocidad = velocidad
        self.bono_carga = bono_carga
        self.precio = precio
        self.rareza = rareza
        self.raza_req = raza_req
        self.es_mision = es_mision
        # Estructura visual para el juego
        self.visual = visual or {
            "modelo_3d": "generic_mount.obj",
            "particulas": "none",
            "escala": 1.0,
            "color_aura": "transparent"
        }
        self.fatiga = 0

    def usar_montura(self):
        if self.fatiga < 100:
            self.fatiga += 5
            return True
        return False

    def descansar(self):
        self.fatiga = 0

# Catálogo con Estructura Visual
CATALOGO_MONTURAS = [
    # Ejemplo de montura con estructura visual definida
    Montura("H03", "Corcel Paladín del Alba", 1.8, 20, 200000, "Leyenda", "Humano", False, {
        "modelo_3d": "paladin_steed.obj",
        "particulas": "holy_light_aura",
        "escala": 1.2,
        "color_aura": "gold"
    }),
    
    Montura("M002", "Dragón del Cataclismo", 3.5, 100, 0, "Mítica", None, True, {
        "modelo_3d": "cataclysm_dragon.obj",
        "particulas": "abyss_smoke",
        "escala": 2.5,
        "color_aura": "purple_void"
    }),
    
    Montura("E04", "Unicornio de Luz Lunar", 2.1, 20, 900000, "Leyenda", "Elfo", False, {
        "modelo_3d": "moon_unicorn.obj",
        "particulas": "stardust",
        "escala": 1.1,
        "color_aura": "silver"
    }),

    Montura("B04", "León de Crin de Fuego", 2.0, 25, 850000, "Leyenda", "Hombre Bestia", False, {
        "modelo_3d": "fire_lion.obj",
        "particulas": "flame_trail",
        "escala": 1.5,
        "color_aura": "orange_fire"
    })
]

# ... (El resto del catálogo se mantendría con la misma estructura visual añadida)

def obtener_monturas_disponibles(raza: str):
    return [m for m in CATALOGO_MONTURAS if m.raza_req is None or m.raza_req == raza]

def equipar_montura(jugador, montura: Montura):
    jugador.mochila.actualizar_bono_montura(montura.bono_carga)
    # Aquí el juego activaría el asset correspondiente: montura.visual["modelo_3d"]
    return f"Has invocado a {montura.nombre}. Modelo: {montura.visual['modelo_3d']} activado."
