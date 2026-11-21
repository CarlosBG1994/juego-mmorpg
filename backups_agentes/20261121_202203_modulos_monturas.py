"""
Modulo: Monturas de Snd-Worlds
Gestiona los medios de transporte. Ofrecen velocidad de movimiento
y bonos de capacidad de carga. Incluye monturas raciales, comunes y de alta rareza.
"""

class Montura:
    def __init__(self, id_montura: str, nombre: str, velocidad: float, bono_carga: int, precio: int, rareza: str = "Común", raza_req: str = None, es_mision: bool = False):
        self.id = id_montura
        self.nombre = nombre
        self.velocidad = velocidad
        self.bono_carga = bono_carga
        self.precio = precio
        self.rareza = rareza
        self.raza_req = raza_req # Si es None, es para todas las razas
        self.es_mision = es_mision 
        self.fatiga = 0

    def usar_montura(self):
        # Aumenta fatiga al moverse
        if self.fatiga < 100:
            self.fatiga += 5
            return True
        return False

    def descansar(self):
        self.fatiga = 0

# Catálogo ampliado de Monturas
CATALOGO_MONTURAS = [
    # --- HUMANOS ---
    Montura("H01", "Caballo de Guerra", 1.2, 10, 5000, "Común", "Humano"),
    Montura("H02", "Corcel de Carga Real", 1.4, 40, 50000, "Ultra Raro", "Humano"),
    Montura("H03", "Corcel Paladín del Alba", 1.8, 20, 200000, "Leyenda", "Humano"),
    
    # --- ELFOS ---
    Montura("E01", "Ciervo del Bosque", 1.3, 5, 6000, "Común", "Elfo"),
    Montura("E02", "Gran Alce de Guerra", 1.5, 25, 65000, "Ultra Raro", "Elfo"),
    Montura("E03", "Pantera de Sombra Silvana", 1.9, 15, 250000, "Leyenda", "Elfo"),
    
    # --- ENANOS ---
    Montura("N01", "Cabra de las Montañas", 1.1, 20, 5000, "Común", "Enano"),
    Montura("N02", "Oso de Túnel Acorazado", 1.3, 60, 70000, "Ultra Raro", "Enano"),
    Montura("N03", "Jabalí Acorazado Rúnico", 1.5, 30, 220000, "Leyenda", "Enano"),
    
    # --- HOMBRE BESTIA ---
    Montura("B01", "Lobo de los Clanes", 1.4, 5, 5500, "Común", "Hombre Bestia"),
    Montura("B02", "Warg de Guerra Alpha", 1.6, 20, 75000, "Ultra Raro", "Hombre Bestia"),
    Montura("B03", "Tigre de Colmillo Blanco", 1.7, 15, 210000, "Leyenda", "Hombre Bestia"),
    
    # --- NEUTRALES / TODOS ---
    Montura("N001", "Asno de Carga", 1.0, 50, 1000, "Común"),
    Montura("N002", "Coche de Comercio", 0.8, 200, 25000, "Poco Común"),
    
    # --- MÍTICAS (Misiones Ocultas) ---
    Montura("M001", "Grifo Real de Aurelius", 3.0, 50, 0, "Mítica", None, True),
    Montura("M002", "Dragón del Cataclismo", 3.5, 100, 0, "Mítica", None, True),
    Montura("M003", "Fénix de las Llamas Eternas", 3.2, 30, 0, "Mítica", None, True)
]

def obtener_monturas_disponibles(raza: str):
    """Filtra monturas accesibles para el jugador según su raza."""
    return [m for m in CATALOGO_MONTURAS if m.raza_req is None or m.raza_req == raza]

def equipar_montura(jugador, montura: Montura):
    """Lógica para equipar la montura y aplicar el bono de carga al jugador."""
    jugador.mochila.actualizar_bono_montura(montura.bono_carga)
    return f"Has montado a {montura.nombre}. Velocidad aumentada a {montura.velocidad}x."
