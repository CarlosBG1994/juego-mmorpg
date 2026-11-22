"""
Modulo: Monturas de Snd-Worlds
Gestiona los medios de transporte: Aspecto visual, atributos, 
entrenamiento y mantenimiento.
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
        self.aspecto = aspecto or {"modelo_3d": "default.fbx", "particulas": "none", "escala": 1.0}
        self.buff = buff or {"stat": None, "valor": 0}
        
        # SISTEMA DE MANTENIMIENTO Y ENTRENAMIENTO
        self.fatiga = 0
        self.nivel_maestria = 1  # Base 1, máximo 10
        self.experiencia_entrenamiento = 0

    def entrenar(self, costo_oro: int):
        """Mejora la maestría de la montura gastando oro."""
        if self.nivel_maestria < 10:
            self.nivel_maestria += 1
            # Incremento porcentual por maestría
            self.velocidad *= 1.05
            self.bono_carga += 2
            return True, f"{self.nombre} ha subido a maestría {self.nivel_maestria}."
        return False, "Nivel máximo de maestría alcanzado."

    def alimentar(self, costo_alimento: int):
        """Reduce la fatiga gastando recursos."""
        self.fatiga = max(0, self.fatiga - 50)
        return f"Energía de {self.nombre} restaurada."

    def usar_montura(self):
        """Al usar la montura, acumula fatiga. Si llega a 100, no rinde."""
        if self.fatiga < 100:
            self.fatiga += 10
            return True
        return False

# ... (El catálogo CATALOGO_MONTURAS se mantiene idéntico al anterior)

def obtener_monturas_disponibles(raza: str):
    return [m for m in CATALOGO_MONTURAS if m.raza_req is None or m.raza_req == raza]

def equipar_montura(jugador, montura: Montura):
    if montura.fatiga >= 100:
        return False, "La montura está demasiado agotada para viajar."
    jugador.mochila.actualizar_bono_montura(montura.bono_carga)
    return True, f"Cargando modelo {montura.aspecto['modelo_3d']}..."
