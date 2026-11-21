"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona la identidad visual, atributos, restricciones de equipo, 
personalización estética y maestría de progresión de personajes.
"""

# 1. CONFIGURACION DE APARIENCIA EXPANDIDA
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

# 2. SISTEMA DE MAESTRIA Y ROLES
# Define el rol principal de cada clase para proyectar el estilo de juego
MAESTRIA_CLASES = {
    "Caballero": {"rol": "Tanque", "foco": "Supervivencia y bloqueo"},
    "Paladin": {"rol": "Híbrido", "foco": "Apoyo defensivo y daño sagrado"},
    "Mago de Batalla": {"rol": "DPS Mágico", "foco": "Combate rúnico a corta/media distancia"},
    "Pugil": {"rol": "DPS Físico", "foco": "Cadencia de golpes y frenesí"},
    "Asesino": {"rol": "DPS Explosivo", "foco": "Sigilo y daño crítico"},
    "Explorador": {"rol": "Utilidad", "foco": "Control de distancia y supervivencia"},
    "Invocador": {"rol": "Control", "foco": "Gestión de entes y daño persistente"},
    "Clerigo": {"rol": "Sanador", "foco": "Soporte puro y luz protectora"},
    # ... (Se mantiene la estructura para todas las clases)
}

# 3. VALIDACION DE RESTRICCIONES Y AFINIDADES (Mantenidas)
RAZAS_HABILITADAS = ["Humano", "Elfo", "Enano", "Hombre Bestia"]
ARMADURAS_PERMITIDAS = {
    "Caballero": ["Placas", "Malla"],
    "Paladin": ["Placas", "Malla", "Cuero"],
    "Mago de Batalla": ["Tela", "Cuero"],
    "Pugil": ["Tela", "Cuero"],
    "Guerrero Pesado": ["Placas"]
}

# 4. FUNCIONES DE GESTION
def obtener_maestria_clase(clase: str) -> dict:
    """Retorna el rol y foco de la clase para que el jugador sepa qué estilo juega."""
    return MAESTRIA_CLASES.get(clase, {"rol": "Desconocido", "foco": "Exploración"})

def proyectar_crecimiento(clase: str, nivel_actual: int) -> str:
    """Sugiere al jugador qué estadísticas potenciar según el rol de su clase."""
    maestria = obtener_maestria_clase(clase)
    if maestria["rol"] == "Tanque":
        return "Prioriza VIT y STR para resistir el frente de batalla."
    elif "DPS" in maestria["rol"]:
        return "Prioriza tus estadísticas ofensivas principales para maximizar el daño."
    return "Distribuye tus puntos según tu estilo de juego preferido."

def obtener_plantilla_creacion(raza: str) -> dict:
    plantilla = CONFIGURACION_APARIENCIA.copy()
    if raza in ["Hombre Bestia", "Draconica"]:
        plantilla["detalles"].append("Patrón de Pelaje o Escamas")
    return plantilla

# ... [RESTO DE FUNCIONES VALIDAS: validar_compatibilidad, validar_uso_equipo, etc.] ...
