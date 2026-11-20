# --- GENERADOR AUTOMÁTICO DE MISIONES MULTICONTINENTE (generador_misiones.py) ---
import json
import random

CONTINENTES_MUNDO = {
    "Continente Inicial: Tierras del Origen (Niveles 1–100)": {
        "rango_niveles": (1, 100),
        "zonas": ["Valoria Inicial", "Llanuras del Comienzo", "Bosque de Bruma", "Puertas del Eón"],
    },
    "Continente Racial Humano": {
        "rango_niveles": (101, 300),
        "zonas": ["Aurelia Capital", "Murallas de Hojacero", "Tierras Fronterizas Humanas"],
    },
    "Continente Racial Élfico": {
        "rango_niveles": (101, 300),
        "zonas": ["Santuario Silvestre", "Arboleda Eterna", "Cañada de los Susurros"],
    },
    "Continente Racial Enano": {
        "rango_niveles": (101, 300),
        "zonas": ["Baluarte de Piedra", "Grandes Fundiciones", "Galerías Profundas"],
    },
    "Continente Racial Dracónico": {
        "rango_niveles": (101, 300),
        "zonas": ["Cumbre de Escamas", "Caldera de Ceniza", "Santuario del Draco"],
    },
    "Continente Demoníaco: Abismo Ígneo (Niveles 301–350)": {
        "rango_niveles": (301, 350),
        "zonas": ["Fosas del Abismo", "Ciudadela Carmesí", "Trono de las Sombras"],
    },
    "Continente Angelical: Ciudadela Celestial (Final)": {
        "rango_niveles": (350, 400),
        "zonas": ["Pináculo de Luz", "Jardines del Alba", "Umbral del Creador"],
    },
}

TIPOS_MISION = ["Caza", "Recolección", "Exploración", "Cazarrecompensas de Normas", "Invasión de Grieta"]
ADJ_CRIATURAS = ["Feroz", "Corrupto", "Salvaje", "Sombreado", "Ancestral", "Abisal", "Mutado", "Celestial"]
CRIATURAS = ["Goblin", "Lobo Huargo", "Slime Ácido", "Ent de la Sombra", "Espectro Errante", "Draco Menor", "Engendro Abisal", "Serafín Caído"]
MATERIALES = ["Mineral de Hierro", "Esencia de Roble", "Cristal de Maná", "Escama de Fuego", "Ceniza Demoníaca", "Pluma Astral"]


def generar_mision_multicontinente(id_mision, rng=None):
    r = rng if rng is not None else random
    nombre_continente = r.choice(list(CONTINENTES_MUNDO.keys()))
    datos_cont = CONTINENTES_MUNDO[nombre_continente]
    zona = r.choice(datos_cont["zonas"])
    min_nv, max_nv = datos_cont["rango_niveles"]
    nivel = r.randint(min_nv, max_nv)
    tipo = r.choice(TIPOS_MISION)

    if tipo == "Caza":
        criatura = f"{r.choice(ADJ_CRIATURAS)} {r.choice(CRIATURAS)}"
        cantidad = r.randint(10, 30)
        titulo = f"Caza de Élite: {criatura} en {zona}"
        descripcion = f"Amenaza en {zona} ({nombre_continente}). Elimina {cantidad} unidades de {criatura}."
        objetivo = f"Eliminar {criatura} (0/{cantidad})"
    elif tipo == "Recolección":
        material = r.choice(MATERIALES)
        cantidad = r.randint(5, 20)
        titulo = f"Recursos Avanzados: {material}"
        descripcion = f"Reúne {material} en {zona} para los gremios y forjas."
        objetivo = f"Recolectar {material} (0/{cantidad})"
    elif tipo == "Cazarrecompensas de Normas":
        titulo = f"Orden de Arresto Global: Forajido Nv. {nivel}"
        descripcion = f"Un infractor marcado opera en {zona}. Neutralízalo y restaura el orden."
        objetivo = "Neutralizar al Forajido Marcado (0/1)"
    elif tipo == "Invasión de Grieta":
        cantidad = r.randint(2, 6)
        titulo = f"Grieta Dimensional en {zona}"
        descripcion = f"Una fisura activa libera entidades en {zona}. Sella los nodos."
        objetivo = f"Sellar fisuras activas (0/{cantidad})"
    else:
        titulo = f"Reconocimiento de Frontera en {zona}"
        descripcion = f"Explora las coordenadas clave y anomalías del terreno en {zona}."
        objetivo = "Inspeccionar las 4 balizas de reconocimiento (0/4)"

    return {
        "id": f"mc_proc_{id_mision:06d}",
        "continente": nombre_continente,
        "zona": zona,
        "titulo": titulo,
        "nivel_requerido": nivel,
        "tipo": tipo,
        "descripcion": descripcion,
        "objetivo": objetivo,
        "recompensa": {"exp": nivel * r.randint(300, 700), "oro": nivel * r.randint(50, 120)},
    }


def generar_lote_misiones(cantidad=100, archivo_salida=None, semilla=42):
    rng = random.Random(semilla) if semilla is not None else random
    misiones = [generar_mision_multicontinente(i, rng=rng) for i in range(1, cantidad + 1)]
    if archivo_salida:
        with open(archivo_salida, "w", encoding="utf-8") as f:
            json.dump(misiones, f, ensure_ascii=False, indent=2)
    return misiones