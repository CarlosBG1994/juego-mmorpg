"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona la identidad visual, atributos y restricciones del personaje.
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

# 2. DESCRIPCIONES VISUALES PARA SISTEMA DE RECREACION (Modelado/UI)
DESCRIPCIONES_VISUALES = {
    "Razas": {
        "Humano": "Estructura equilibrada, facciones humanas estándar, postura erguida y proporcionada.",
        "Elfo": "Estructura estilizada y esbelta, orejas largas y puntiagudas, movimientos fluidos.",
        "Enano": "Estructura compacta y densa, hombros anchos, extremidades robustas y vello facial prominente.",
        "Hombre Bestia": "Estructura atlética con rasgos animales, musculatura marcada, presencia de garras y pelaje.",
        "Draconica": "Estructura imponente y poderosa, recubierta de escamas metálicas, postura semi-reptiliana, presencia de crestas óseas."
    },
    "Clases": {
        "Caballero": "Equipado con armadura de placas completa, yelmo cerrado y capa pesada.",
        "Paladin": "Armadura ornamentada con motivos solares, luz constante alrededor de los hombros.",
        "Mago de Batalla": "Túnicas de cuero endurecido, runas elementales brillantes en los antebrazos.",
        "Pugil": "Cinturón de campeón, vendajes místicos en los puños, sin protecciones en el pecho.",
        "Asesino": "Ropas de seda negra ajustadas, cinturones cruzados para dagas, máscara facial ligera.",
        "Explorador": "Atuendo de cuero reforzado, mochila de viaje, botas de cuero de alta tracción.",
        "Invocador": "Túnicas largas con bordados estelares, orbe flotante en la mano izquierda.",
        "Clerigo": "Túnicas sacerdotales pesadas, símbolo sagrado en el pecho, estola ceremonial.",
        "Guardabosques": "Cuero teñido de bosque, plumas decorativas en los hombros, carcaj en la espalda.",
        "Alcaide": "Armadura de placas tallada con motivos de corteza, lanza ornamentada.",
        "Druida": "Pieles curtidas, astas de ciervo integradas en el casco/capucha, hojas naturales adheridas.",
        "Espadachin Silvano": "Armadura de cuero ligero muy ágil, capa larga que ondea con el movimiento.",
        "Guerrero Pesado": "Armadura masiva forjada en negro, hombreras gigantes, aspecto intimidante.",
        "Defensor Runico de Asedio": "Escudo de torre metálico en el brazo, armadura con remaches pesados.",
        "Campeon": "Pieles de bestia mayor, accesorios de hueso, pintura tribal en el rostro.",
        "Chaman Primordial": "Máscara de madera ritual, plumas de aves rapaces, báculo rúnico."
    }
}

# ... [Mantenimiento de RAZAS_HABILITADAS, CLASES_POR_RAZA, ATRIBUTOS_RAZA, etc. intactos] ...

def obtener_plantilla_creacion(raza: str) -> dict:
    plantilla = CONFIGURACION_APARIENCIA.copy()
    if raza in ["Hombre Bestia", "Draconica"]:
        plantilla["detalles"].append("Patrón de Pelaje o Escamas")
    return plantilla

def obtener_descripcion_estetica(raza: str, clase: str) -> str:
    """Combina la descripción racial y de clase para el motor de juego."""
    r = DESCRIPCIONES_VISUALES["Razas"].get(raza, "Humano estándar")
    c = DESCRIPCIONES_VISUALES["Clases"].get(clase, "Vestimenta estándar")
    return f"Aspecto físico: {r} / Indumentaria: {c}"

# ... [Funciones validar_compatibilidad, validar_uso_equipo, etc., intactas] ...
