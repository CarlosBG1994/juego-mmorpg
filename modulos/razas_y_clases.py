"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona la identidad visual, atributos, restricciones de equipo, 
personalización estética y maestría de progresión de personajes.
"""

# RAZAS ACTIVAS (El sistema solo permitirá elegir estas)
RAZAS_HABILITADAS = ["Humano", "Elfo", "Enano", "Hombre Bestia"]

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

# 2. RESTRICCIONES VISUALES POR RAZA
RESTRICCIONES_VISUALES = {
    "Enano": {
        "prohibir_estilos": ["Melena salvaje"],
        "solo_tonos_piel": ["Palido", "Bronceado", "Cenizo", "Pétreo"]
    },
    "Elfo": {
        "prohibir_rasgos": ["Vello facial denso"],
        "solo_tonos_piel": ["Palido", "Bronceado", "Albino"]
    },
    "Draconica": { # Aunque está definida, el usuario no puede seleccionarla aún
        "solo_tonos_piel": ["Escamoso"],
        "prohibir_cabello": True
    }
}

# 3. FUNCION DE FILTRADO PARA LA UI
def obtener_opciones_personalizacion(raza: str) -> dict:
    """Retorna las opciones de apariencia filtradas. Si la raza no está habilitada, devuelve vacío."""
    if raza not in RAZAS_HABILITADAS:
        return {}
        
    config = CONFIGURACION_APARIENCIA.copy()
    restricciones = RESTRICCIONES_VISUALES.get(raza, {})

    if "prohibir_estilos" in restricciones:
        config["cabello"]["estilos"] = [s for s in config["cabello"]["estilos"] if s not in restricciones["prohibir_estilos"]]
    
    if "solo_tonos_piel" in restricciones:
        config["tonos_piel"] = restricciones["solo_tonos_piel"]

    if "prohibir_rasgos" in restricciones:
        config["rasgos_faciales"] = [r for r in config["rasgos_faciales"] if r not in restricciones["prohibir_rasgos"]]

    if restricciones.get("prohibir_cabello"):
        config["cabello"] = {"estilos": ["Sin cabello/Cresta"], "colores": ["Escamas metálicas"]}

    return config

def obtener_plantilla_creacion(raza: str) -> dict:
    """Retorna la plantilla adaptada si la raza es permitida."""
    if raza not in RAZAS_HABILITADAS:
        return {}
    
    plantilla = obtener_opciones_personalizacion(raza)
    if raza == "Hombre Bestia":
        plantilla["detalles"].append("Patrón de Pelaje")
    return plantilla

# ... [Mantenimiento de MAESTRIA_CLASES, ARMADURAS_PERMITIDAS, validar_compatibilidad, etc.] ...
