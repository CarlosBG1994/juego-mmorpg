"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona la identidad visual, atributos, restricciones de equipo, 
personalización estética y maestría de progresión de personajes.
"""

# --- CONFIGURACIÓN MAESTRA ---
RAZAS_HABILITADAS = ["Humano", "Elfo", "Enano", "Hombre Bestia"]
SUBFORMAS_HOMBRE_BESTIA = ["Hombre Lobo", "Hombre Pantera", "Hombre Tigre", "Hombre Leon", "Hombre Mono", "Hombre Tortuga", "Hombre Panda"]

# --- CONFIGURACIÓN DE APARIENCIA (Editor) ---
CONFIGURACION_APARIENCIA = {
    "genero": ["Masculino", "Femenino"],
    "tonos_piel": ["Palido", "Bronceado", "Oscuro", "Albino", "Sintetico", "Escamoso", "Pétreo", "Cenizo"],
    "cabello": {
        "estilos": ["Corto militar", "Largo ondulado", "Recogido en moño", "Rapado tribal", "Trenzado complejo", "Cresta punk", "Melena salvaje"],
        "colores": ["Negro azabache", "Rubio platino", "Castaño rojizo", "Blanco invernal", "Azul electrico", "Fuego intenso"]
    },
    "rasgos_faciales": ["Cicatrices de batalla", "Tatuajes rituales", "Pintura de guerra", "Piercings de hueso", "Marcas de nacimiento", "Vello facial denso"],
    "constitucion": {"rango_peso": "1-100", "rango_altura": "1-100"},
    "detalles": ["Color de ojos", "Forma de la nariz", "Cicatrices en el torso", "Implantes runicos"]
}

# --- LÓGICA DE ESPECIALIZACIÓN Y VALIDACIÓN ---
ARMADURAS_PERMITIDAS = {
    "Caballero": ["Placas", "Malla"], "Paladin": ["Placas", "Malla", "Cuero"],
    "Mago de Batalla": ["Tela", "Cuero"], "Pugil": ["Tela", "Cuero"],
    "Asesino": ["Cuero", "Tela"], "Explorador": ["Cuero", "Tela"]
}

AFINIDADES_RACIALES = {
    "Humano": "Diplomacia Comercial (+2% Oro)",
    "Elfo": "Paso Silvano (+5% Velocidad)",
    "Enano": "Ojo del Forjador (+5% Identificación)",
    "Hombre Bestia": "Instinto Indómito (Inmunidad a Miedo)"
}

# --- FUNCIONES DE GESTIÓN AVANZADA ---

def obtener_opciones_personalizacion(raza: str) -> dict:
    """Devuelve las opciones filtradas por las restricciones raciales."""
    if raza not in RAZAS_HABILITADAS: return {}
    config = CONFIGURACION_APARIENCIA.copy()
    
    # Aplicar filtros específicos (Ejemplo: Elfos sin vello facial)
    if raza == "Elfo":
        config["rasgos_faciales"] = [r for r in config["rasgos_faciales"] if r != "Vello facial denso"]
        
    return config

def calcular_estadisticas_finales(raza: str, clase: str, subforma: str = None) -> dict:
    """Calcula stats finales para la UI de selección."""
    if raza not in RAZAS_HABILITADAS: return {}
    
    stats = {"STR": 10, "INT": 10, "AGI": 10, "VIT": 10, "LUK": 10, "DES": 10}
    
    # Aplicar bonos de sub-forma si es Hombre Bestia
    if raza == "Hombre Bestia" and subforma in SUBFORMAS_HOMBRE_BESTIA:
        stats["AGI"] += 2 # Ejemplo de bono
        
    return stats

def recrear_personaje_visual(raza: str, clase: str, detalles_esteticos: dict) -> str:
    """Función para que el motor visual sepa qué modelo cargar."""
    return f"Cargando modelo de {raza} clase {clase} con detalles: {detalles_esteticos}"

def validar_uso_equipo(clase: str, tipo_armadura: str) -> bool:
    """Seguridad: Verifica si el jugador puede ponerse el objeto."""
    return tipo_armadura in ARMADURAS_PERMITIDAS.get(clase, [])
