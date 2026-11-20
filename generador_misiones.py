# --- GENERADOR AUTOMÁTICO DE MISIONES MULTICONTINENTE (generador_misiones.py) ---
import json
import random

CONTINENTES_MUNDO = {
    "Continente I: Reinos Fundacionales y Zonas Neutras": {
        "rango_niveles": (1, 100),
        "zonas": [
            "Reino Humano de Valoria", "Bosque Ancestral de Elfos",
            "Baluarte Enano de Piedra", "Torre de los Arcanos",
            "Puertas del Eón", "Archipiélago del Mar Abierto",
        ],
    },
    "Continente II: Tierras de Ceniza y Abismos Antiguos": {
        "rango_niveles": (101, 200),
        "zonas": [
            "Desierto de Obsidiana", "Cavernas del Dragón Ciego",
            "Ciudadela del Rey Caído", "Fosas Abisales del Titán",
            "Picos de los Vientos Eternos",
        ],
    },
    "Continente III: El Dominio Celestial y Grietas del Vacío": {
        "rango_niveles": (201, 300),
        "zonas": [
            "Santuario de las Estrellas Caídas", "Bastión Interdimensional",
            "Jardines del Dios Olvidado", "Grieta Cuántica del Eón",
            "Catedral del Creador",
        ],
    },
}

TIPOS_MISION = ["Caza", "Recolección", "Exploración", "Cazarrecompensas de Normas", "Invasión de Grieta"]
ADJ_CRIATURAS = ["Feroz", "Corrupto", "Salvaje", "Sombreado", "Ancestral", "Abisal", "Mutado", "Divino"]
CRIATURAS = ["Goblin", "Lobo Huargo", "Slime Ácido", "Ent de la Sombra", "Espectro Errante", "Draco Menor", "Bandido Forajido", "Guardián del Vacío"]
MATERIALES = ["Mineral de Hierro", "Esencia de Roble", "Cristal de Maná", "Escama de Fuego", "Pluma de Tormenta", "Esencia Estelar"]


def generar_mision_multicontinente(id_mision):
    nombre_continente = random.choice(list(CONTINENTES_MUNDO.keys()))
    datos_cont = CONTINENTES_MUNDO[nombre_continente]
    zona = random.choice(datos_cont["zonas"])
    min_nv, max_nv = datos_cont["rango_niveles"]
    nivel = random.randint(min_nv, max_nv)
    tipo = random.choice(TIPOS_MISION)

    if tipo == "Caza":
        criatura = f"{random.choice(ADJ_CRIATURAS)} {random.choice(CRIATURAS)}"
        cantidad = random.randint(10, 30)
        titulo = f"Caza de Élite: {criatura} en {zona}"
        descripcion = f"Amenaza crítica en {zona} ({nombre_continente}). Elimina {cantidad} unidades de {criatura}."
        objetivo = f"Eliminar {criatura} (0/{cantidad})"
    elif tipo == "Recolección":
        material = random.choice(MATERIALES)
        cantidad = random.randint(5, 20)
        titulo = f"Recursos Avanzados: {material}"
        descripcion = f"Se requieren suministros de {material} recolectados en {zona}."
        objetivo = f"Recolectar {material} (0/{cantidad})"
    elif tipo == "Cazarrecompensas de Normas":
        titulo = f"Orden de Arresto Global: Forajido Nv. {nivel}"
        descripcion = f"Un infractor ha violado las leyes del servidor en {zona}. Neutralízalo."
        objetivo = "Neutralizar al Forajido Marcado"
    else:
        titulo = f"Exploración de Frontera: {zona}"
        descripcion = f"Cartografía las anomalías dimensionales en {zona}."
        objetivo = "Inspeccionar las 4 balizas de reconocimiento"

    return {
        "id": f"mc_proc_{id_mision:06d}",
        "continente": nombre_continente,
        "zona": zona,
        "titulo": titulo,
        "nivel_requerido": nivel,
        "tipo": tipo,
        "descripcion": descripcion,
        "objetivo": objetivo,
        "recompensa": {"exp": nivel * random.randint(300, 700), "oro": nivel * random.randint(50, 120)},
    }