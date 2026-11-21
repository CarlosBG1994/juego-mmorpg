# Estructura de Datos para Habilidades Míticas
# La "Potencia" se calcula sobre el Stat base del jugador (STR, INT o AGI).

DETALLES_MITICAS = {
    "M001": { # Ira del Cataclismo (Caballero/Paladín)
        "Efecto": "Invoca ondas sísmicas de luz solar.",
        "Niv1": "Golpe base + 100% STR. Daño físico puro.",
        "Niv15": "Suelo Sagrado: Reduce DEF enemigos 20%.",
        "Niv30": "Cataclismo: Daño en área (AOE) masivo 250% STR."
    },
    "M006": { # Dominio del Nexo Arcano (Mago/Invocador)
        "Efecto": "Manipulación pura del Eter.",
        "Niv1": "Ráfaga de Eter + 100% INT. Daño mágico.",
        "Niv15": "Resonancia: Recupera 10% de maná por golpe.",
        "Niv30": "Colapso del Nexo: Ignora 50% de resistencia mágica."
    },
    "M015": { # Impacto de la Forja Profunda (Guerrero/Campeón Enano)
        "Efecto": "Fuerza telúrica de las montañas.",
        "Niv1": "Martillazo rúnico + 100% STR.",
        "Niv15": "Estampida: Aturde al objetivo principal.",
        "Niv30": "Forja Final: Daño masivo que rompe armaduras permanentes."
    },
    "M003": { # Rugido del Totem Primordial (Bestia)
        "Efecto": "Conexión animal indomable.",
        "Niv1": "Grito de guerra + 100% AGI/STR.",
        "Niv15": "Furia Salvaje: Aumenta velocidad de ataque 30%.",
        "Niv30": "Avatar del Totem: Invoca el espíritu del animal, daño 250%."
    }
}
