"""
Modulo: Monturas de Snd-Worlds
Gestiona los medios de transporte con estructura visual, 
atributos de combate y bonos pasivos.
"""

class Montura:
    def __init__(self, id_montura: str, nombre: str, velocidad: float, bono_carga: int, 
                 precio: int, rareza: str = "Común", raza_req: str = None, 
                 es_mision: bool = False, aspecto: dict = None, buff: dict = None):
        self.id = id_montura
        self.nombre = nombre
        self.velocidad = velocidad
        self.bono_carga = bono_carga
        self.precio = precio
        self.rareza = rareza
        self.raza_req = raza_req
        self.es_mision = es_mision
        self.fatiga = 0
        self.buff = buff or {"stat": None, "valor": 0}
        
        # ESTRUCTURA VISUAL (Para el Motor Gráfico)
        # Define cómo se ve y se comporta la montura en el mundo
        self.aspecto = aspecto or {
            "modelo_3d": "default_mount.fbx",
            "textura": "default_diffuse.png",
            "animacion_idle": "breath_loop",
            "efecto_particulas": "dust_kick",
            "escala": 1.0,
            "color_luz": "#FFFFFF"
        }

    def usar_montura(self):
        if self.fatiga < 100:
            self.fatiga += 5
            return True
        return False

# Catálogo con estructura de Aspecto definida
CATALOGO_MONTURAS = [
    # Ejemplo de montura Leyenda con aspecto definido
    Montura("H03", "Corcel Paladín del Alba", 1.8, 20, 200000, "Leyenda", "Humano", False, {
        "modelo_3d": "horse_paladin.fbx",
        "textura": "gold_armor.png",
        "animacion_idle": "head_toss",
        "efecto_particulas": "holy_glimmer",
        "escala": 1.2,
        "color_luz": "#FFD700"
    }, {"stat": "VIT", "valor": 5}),

    # Ejemplo de montura Mítica con efectos avanzados
    Montura("M002", "Dragón del Cataclismo", 3.5, 100, 0, "Mítica", None, True, {
        "modelo_3d": "dragon_void.fbx",
        "textura": "void_scales.png",
        "animacion_idle": "wing_flap",
        "efecto_particulas": "void_smoke_aura",
        "escala": 2.5,
        "color_luz": "#800080"
    }, {"stat": "STR", "valor": 15})
]

def obtener_monturas_disponibles(raza: str):
    return [m for m in CATALOGO_MONTURAS if m.raza_req is None or m.raza_req == raza]

def equipar_montura(jugador, montura: Montura):
    # Aquí es donde el juego notifica al motor que cargue el 'aspecto'
    print(f"Cargando modelo {montura.aspecto['modelo_3d']} con partículas {montura.aspecto['efecto_particulas']}...")
    jugador.mochila.actualizar_bono_montura(montura.bono_carga)
    return True
