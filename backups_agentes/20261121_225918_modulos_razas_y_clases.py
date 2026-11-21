"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona la identidad visual, atributos, restricciones de equipo, 
personalización estética y maestría de progresión de personajes.
"""

# --- CONFIGURACIÓN DE ACCESO ---
RAZAS_HABILITADAS = ["Humano", "Elfo", "Enano", "Hombre Bestia"]

# --- CONFIGURACIÓN DE APARIENCIA (Editor de Personaje) ---
CONFIGURACION_APARIENCIA = {
    "genero": ["Masculino", "Femenino"],
    "tonos_piel": ["Palido", "Bronceado", "Oscuro", "Albino", "Sintetico", "Escamoso", "Pétreo", "Cenizo"],
    "cabello": {
        "estilos": ["Corto militar", "Largo ondulado", "Recogido en moño", "Rapado tribal", "Trenzado complejo", "Cresta punk", "Melena salvaje"],
        "colores": ["Negro azabache", "Rubio platino", "Castaño rojizo", "Blanco invernal", "Azul electrico", "Fuego intenso"]
    },
    "rasgos_faciales": ["Cicatrices de batalla", "Tatuajes rituales", "Pintura de guerra", "Piercings de hueso", "Marcas de nacimiento", "Vello facial denso"],
    "constitucion": {"rango_peso": "1-100 (Delgado a Robusto)", "rango_altura": "1-100 (Bajo a Gigante)"},
    "detalles": ["Color de ojos intensos", "Forma de la nariz perfilada", "Cicatrices en el torso", "Implantes runicos"]
}

RESTRICCIONES_VISUALES = {
    "Enano": {"prohibir_estilos": ["Melena salvaje"], "solo_tonos_piel": ["Palido", "Bronceado", "Cenizo", "Pétreo"]},
    "Elfo": {"prohibir_rasgos": ["Vello facial denso"], "solo_tonos_piel": ["Palido", "Bronceado", "Albino"]},
    "Draconica": {"solo_tonos_piel": ["Escamoso"], "prohibir_cabello": True}
}

# --- SISTEMAS MECÁNICOS ---
AFINIDADES_RACIALES = {
    "Humano": {"nombre": "Diplomacia Comercial", "efecto": "+2% de oro"},
    "Elfo": {"nombre": "Paso Silvano", "efecto": "+5% velocidad"},
    "Enano": {"nombre": "Ojo del Forjador", "efecto": "+5% identificación"},
    "Hombre Bestia": {"nombre": "Instinto Indómito", "efecto": "Inmunidad al Miedo"}
}

ARMADURAS_PERMITIDAS = {
    "Caballero": ["Placas", "Malla"], "Paladin": ["Placas", "Malla", "Cuero"],
    "Mago de Batalla": ["Tela", "Cuero"], "Pugil": ["Tela", "Cuero"],
    "Asesino": ["Cuero", "Tela"], "Explorador": ["Cuero", "Tela"]
    # (Se expande según clases definidas)
}

MATRIZ_ESPECIALIZACION = {
    "Caballero": ["STR", "VIT"], "Paladin": ["STR", "INT", "VIT"],
    "Mago de Batalla": ["INT", "STR"], "Pugil": ["STR", "AGI"],
    "Asesino": ["AGI", "DES"], "Explorador": ["DES", "AGI"]
}

# --- FUNCIONES DE GESTIÓN ---

def obtener_opciones_personalizacion(raza: str) -> dict:
    if raza not in RAZAS_HABILITADAS: return {}
    config = CONFIGURACION_APARIENCIA.copy()
    restricciones = RESTRICCIONES_VISUALES.get(raza, {})
    # ... (Lógica de filtrado aplicada aquí) ...
    return config

def validar_uso_equipo(clase: str, tipo_armadura: str) -> bool:
    return tipo_armadura in ARMADURAS_PERMITIDAS.get(clase, [])

def obtener_plantilla_creacion(raza: str) -> dict:
    if raza not in RAZAS_HABILITADAS: return {}
    plantilla = obtener_opciones_personalizacion(raza)
    if raza == "Hombre Bestia": plantilla["detalles"].append("Patrón de Pelaje")
    return plantilla

def calcular_atributos_iniciales(raza: str, clase: str, subforma: str = None) -> dict:
    # Lógica de cálculo acumulativa (Base + Clase + Subforma)
    pass
