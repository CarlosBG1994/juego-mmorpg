"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona la identidad visual, atributos, restricciones de equipo, 
personalización estética y maestría de progresión de personajes.
"""

# ... [MANTENEMOS CONFIGURACIONES PREVIAS DE APARIENCIA Y RAZAS] ...

# 1. CLASES DRACÓNICAS (Ocultas hasta nueva orden)
CLASES_DRACONICAS = {
    "Guerrero Dragon": {
        "rol": "Tanque/DPS", 
        "foco": "Combate cuerpo a cuerpo con aliento elemental", 
        "armadura": ["Placas"],
        "atributos_maestros": ["STR", "VIT"]
    },
    "Mago de Sangre": {
        "rol": "DPS Mágico", 
        "foco": "Manipulación de energía vital y fuego", 
        "armadura": ["Tela"],
        "atributos_maestros": ["INT", "VIT"]
    },
    "Custodio de Escamas": {
        "rol": "Tanque Defensivo", 
        "foco": "Absorción de daño mediante escamas reforzadas", 
        "armadura": ["Placas", "Malla"],
        "atributos_maestros": ["VIT", "DES"]
    },
    "Acechador Draconico": {
        "rol": "DPS Ágil", 
        "foco": "Velocidad sobrehumana y ataques de precisión", 
        "armadura": ["Cuero"],
        "atributos_maestros": ["AGI", "DES"]
    }
}

# 2. INTEGRACIÓN EN EL SISTEMA
# Añadimos las clases a la lógica de validación pero NO habilitamos la raza
CLASES_POR_RAZA = {
    "Humano": ["Caballero", "Paladin", "Mago de Batalla", "Pugil", "Asesino", "Explorador", "Invocador", "Clerigo"],
    "Elfo": ["Guardabosques", "Alcaide", "Druida", "Espadachin Silvano", "Monje del Viento (Pugil)", "Acechador Nocturno (Asesino)", "Mago de Batalla", "Invocador"],
    "Enano": ["Guerrero Pesado", "Defensor Runico de Asedio", "Campeon Runico", "Luchador de Puno de Hierro (Pugil)", "Ballestero (Explorador)", "Asesino", "Mago de Batalla", "Invocador", "Clerigo"],
    "Hombre Bestia": ["Campeon", "Acechador Salvaje", "Chaman Primordial", "Pugil", "Asesino", "Explorador", "Mago de Batalla", "Invocador", "Clerigo"],
    "Draconica": list(CLASES_DRACONICAS.keys())
}

# Actualizamos ARMADURAS_PERMITIDAS para incluir las dracónicas
for clase, datos in CLASES_DRACONICAS.items():
    ARMADURAS_PERMITIDAS[clase] = datos["armadura"]

# 3. MATRIZ DE ESPECIALIZACIÓN PARA LAS CLASES NUEVAS
for clase, datos in CLASES_DRACONICAS.items():
    MATRIZ_ESPECIALIZACION[clase] = datos["atributos_maestros"]

# ... [RESTO DE FUNCIONES DE GESTIÓN INTACTAS] ...

def obtener_maestria_clase(clase: str) -> dict:
    """Retorna rol y foco. Incluye clases dracónicas."""
    if clase in CLASES_DRACONICAS:
        return {"rol": CLASES_DRACONICAS[clase]["rol"], "foco": CLASES_DRACONICAS[clase]["foco"]}
    return MAESTRIA_CLASES.get(clase, {"rol": "Desconocido", "foco": "Exploración"})
