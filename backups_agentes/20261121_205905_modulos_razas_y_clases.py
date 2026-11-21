"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona razas, clases, sub-formas, afinidades raciales, restricciones de equipo,
logica de progresion y configuracion de apariencia fisica.
"""

# ... [Estructuras previas: ESTADISTICAS_BASE, RAZAS_HABILITADAS, AFINIDADES_RACIALES, ARMADURAS_PERMITIDAS, MATRIZ_ESPECIALIZACION permanecen igual] ...

# 4. CONFIGURACION DE APARIENCIA (Sistema para Pantalla de Creación)
# Esta estructura define los parámetros que el sistema de UI debe solicitar al jugador.
CONFIGURACION_APARIENCIA = {
    "genero": ["Masculino", "Femenino", "Andrógino"],
    "tonos_piel": ["Palido", "Bronceado", "Oscuro", "Albino", "Sintético/Escamoso"],
    "cabello": {"estilos": ["Corto", "Largo", "Recogido", "Rapado", "Trenzado"], "colores": ["Naturales", "Fantasía"]},
    "rasgos_faciales": ["Cicatrices", "Tatuajes", "Pintura de Guerra", "Piercings"],
    "constitucion": {"rango_peso": "1-100 (Delgado a Robusto)", "rango_altura": "1-100 (Bajo a Gigante)"},
    "detalles": ["Color de Ojos", "Forma de la Boca", "Forma de la Nariz"]
}

def obtener_plantilla_creacion(raza: str) -> dict:
    """
    Retorna la plantilla de personalización adaptada a la raza.
    Las razas como 'Draconica' o 'Hombre Bestia' tienen parámetros adicionales.
    """
    plantilla = CONFIGURACION_APARIENCIA.copy()
    if raza in ["Hombre Bestia", "Draconica"]:
        plantilla["detalles"].append("Patrón de Pelaje/Escamas")
    return plantilla

def validar_uso_equipo(clase: str, tipo_armadura: str) -> bool:
    return tipo_armadura in ARMADURAS_PERMITIDAS.get(clase, [])

def obtener_afinidad_racial(raza: str) -> dict:
    return AFINIDADES_RACIALES.get(raza, {"nombre": "Ninguna", "efecto": "N/A"})

def obtener_sugerencia_build(clase: str, stats_actuales: dict) -> str:
    prioridades = MATRIZ_ESPECIALIZACION.get(clase, [])
    for stat in prioridades:
        if stats_actuales.get(stat, 0) < 30:
            return f"Tu clase {clase} se beneficia enormemente de {stat}."
    return "Tu distribución actual es equilibrada."

# ... [Mantener funciones anteriores: calcular_atributos_iniciales, validar_compatibilidad, etc.] ...
