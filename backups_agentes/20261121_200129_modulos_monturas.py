"""
Modulo: Monturas de Snd-Worlds
Gestiona los medios de transporte. Ofrecen velocidad de movimiento
y bonos de capacidad de carga. Incluye monturas raciales, comunes y de alta rareza.
"""

class Montura:
    def __init__(self, nombre: str, velocidad: float, bono_carga: int, precio: int, rareza: str = "Común", raza_req: str = None, es_mision: bool = False):
        self.nombre = nombre
        self.velocidad = velocidad
        self.bono_carga = bono_carga
        self.precio = precio
        self.rareza = rareza
        self.raza_req = raza_req # Si es None, es para todas las razas
        self.es_mision = es_mision # Si es True, solo se obtiene por evento/misión oculta
        self.fatiga = 0

    def usar_montura(self):
        if self.fatiga < 100:
            self.fatiga += 5
            return True
        return False

    def descansar(self):
        self.fatiga = 0

# Catálogo de Monturas
CATALOGO_MONTURAS = [
    # Monturas Raciales (Humano)
    Montura("Caballo de Guerra de Fortaleza Solar", 1.2, 10, 5000, "Común", "Humano"),
    Montura("Corcel Paladín del Alba", 1.8, 20, 200000, "Leyenda", "Humano"),
    
    # Monturas Raciales (Elfo)
    Montura("Ciervo del Árbol Corazón", 1.3, 5, 6000, "Común", "Elfo"),
    Montura("Pantera de Sombra Silvana", 1.9, 15, 250000, "Leyenda", "Elfo"),
    
    # Monturas Raciales (Enano)
    Montura("Cabra de las Montañas de Hierro", 1.1, 20, 5000, "Común", "Enano"),
    Montura("Jabalí Acorazado Rúnico", 1.5, 30, 220000, "Leyenda", "Enano"),
    
    # Monturas Raciales (Hombre Bestia)
    Montura("Lobo de los Clanes Primordiales", 1.4, 5, 5500, "Común", "Hombre Bestia"),
    Montura("Tigre de Colmillo Blanco", 1.7, 15, 210000, "Leyenda", "Hombre Bestia"),
    
    # Monturas Comunes (Todas las razas)
    Montura("Asno de Carga", 1.0, 50, 1000, "Común"),
    
    # Monturas Míticas (Misiones Ocultas)
    Montura("Grifo Real de Aurelius", 3.0, 50, 0, "Mítica", None, True),
    Montura("Dragón del Cataclismo", 3.5, 100, 0, "Mítica", None, True)
]

def obtener_monturas_disponibles(raza: str):
    """Filtra monturas accesibles para el jugador según su raza."""
    return [m for m in CATALOGO_MONTURAS if m.raza_req is None or m.raza_req == raza]
