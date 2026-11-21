"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona razas, clases, sub-formas, afinidades raciales, restricciones de equipo
y logica de progresion personalizada.
"""

ESTADISTICAS_BASE = ["STR", "INT", "AGI", "VIT", "LUK", "DES"]
RAZAS_HABILITADAS = ["Humano", "Elfo", "Enano", "Hombre Bestia"]

# 1. AFINIDAD RACIAL (Pasivas únicas)
AFINIDADES_RACIALES = {
    "Humano": {"nombre": "Diplomacia Comercial", "efecto": "+2% de oro extra en misiones"},
    "Elfo": {"nombre": "Paso Silvano", "efecto": "+5% de velocidad en terrenos naturales"},
    "Enano": {"nombre": "Ojo del Forjador", "efecto": "+5% éxito al identificar objetos"},
    "Hombre Bestia": {"nombre": "Instinto Indómito", "efecto": "Inmunidad al estado alterado 'Miedo'"}
}

# 2. RESTRICCIONES DE EQUIPO POR CLASE (Para validar Loot)
TIPOS_ARMADURA = ["Tela", "Cuero", "Malla", "Placas"]

ARMADURAS_PERMITIDAS = {
    "Caballero": ["Placas", "Malla"],
    "Paladin": ["Placas", "Malla", "Cuero"],
    "Mago de Batalla": ["Tela", "Cuero"],
    "Pugil": ["Tela", "Cuero"],
    "Asesino": ["Cuero", "Tela"],
    "Explorador": ["Cuero", "Tela"],
    "Invocador": ["Tela"],
    "Clerigo": ["Tela", "Malla"],
    "Guardabosques": ["Cuero", "Malla"],
    "Alcaide": ["Malla", "Placas"],
    "Druida": ["Tela", "Cuero"],
    "Espadachin Silvano": ["Cuero", "Malla"],
    "Guerrero Pesado": ["Placas"],
    "Defensor Runico de Asedio": ["Placas"],
    "Campeon": ["Cuero", "Malla"],
    "Chaman Primordial": ["Tela", "Cuero"]
}

# (Mantenemos las estructuras previas intactas)
SUBFORMAS_HOMBRE_BESTIA = ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre Leon", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"]
ASPECTOS_RAZA = {"Humano": "...", "Elfo": "...", "Enano": "...", "Hombre Bestia": "...", "Draconica": "..."}
ASPECTOS_CLASE = {"Caballero": "...", "Paladin": "...", "Mago de Batalla": "...", "Pugil": "..."} # (Se asumen completos)
CLASES_POR_RAZA = {"Humano": [...], "Elfo": [...], "Enano": [...], "Hombre Bestia": [...], "Draconica": [...]}

def validar_uso_equipo(clase: str, tipo_armadura: str) -> bool:
    """Valida si una clase puede equipar un tipo de armadura específico."""
    return tipo_armadura in ARMADURAS_PERMITIDAS.get(clase, [])

def obtener_afinidad_racial(raza: str) -> dict:
    """Retorna la pasiva racial para la interfaz del usuario."""
    return AFINIDADES_RACIALES.get(raza, {"nombre": "Ninguna", "efecto": "N/A"})

def calcular_atributos_iniciales(raza: str, clase: str, subforma: str = None) -> dict:
    # (Mantener logica previa intacta: Base + Subforma + Clase)
    return {} 

def validar_compatibilidad(raza_jugador: str, clase_jugador: str, raza_req: list = None, clase_req: list = None) -> bool:
    if raza_req and raza_jugador not in raza_req: return False
    if clase_req and clase_jugador not in clase_req: return False
    return True
