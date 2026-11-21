"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona razas, clases, sub-formas, afinidades raciales, restricciones de equipo
y logica de progresion personalizada.
"""

# ... [Estructuras previas: ESTADISTICAS_BASE, AFINIDADES_RACIALES, ARMADURAS_PERMITIDAS permanecen] ...

# 3. MATRIZ DE ESPECIALIZACION (Potencial de Crecimiento)
# Define qué estadística es "Primaria" para cada clase, facilitando sugerencias de optimización.
MATRIZ_ESPECIALIZACION = {
    "Caballero": ["STR", "VIT"],
    "Paladin": ["STR", "INT", "VIT"],
    "Mago de Batalla": ["INT", "STR"],
    "Pugil": ["STR", "AGI"],
    "Asesino": ["AGI", "DES"],
    "Explorador": ["DES", "AGI"],
    "Invocador": ["INT", "LUK"],
    "Clerigo": ["INT", "VIT"]
    # ... resto de clases seguirían este patrón
}

def obtener_sugerencia_build(clase: str, stats_actuales: dict) -> str:
    """
    Analiza la distribución del jugador y sugiere en qué invertir 
    basándose en la especialización natural de su clase.
    """
    prioridades = MATRIZ_ESPECIALIZACION.get(clase, [])
    for stat in prioridades:
        if stats_actuales.get(stat, 0) < 30: # Umbral de ejemplo
            return f"Tu clase {clase} se beneficia enormemente de {stat}. ¡Considera potenciarla!"
    return "Tu distribución actual es equilibrada para tu clase."

def validar_uso_equipo(clase: str, tipo_armadura: str) -> bool:
    return tipo_armadura in ARMADURAS_PERMITIDAS.get(clase, [])

def obtener_afinidad_racial(raza: str) -> dict:
    return AFINIDADES_RACIALES.get(raza, {"nombre": "Ninguna", "efecto": "N/A"})

# ... [resto de funciones igual] ...
