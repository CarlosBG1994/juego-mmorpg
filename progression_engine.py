# --- MOTOR DE PROGRESIÓN Y BLOQUEO DE CONTINENTES (progression_engine.py) ---

REQUISITOS_CONTINENTES = {
    "Continente I: Reinos Fundacionales y Zonas Neutras": {
        "min_misiones": 0,
        "min_miticas": 0,
    },
    "Continente II: Tierras de Ceniza y Abismos Antiguos": {
        "min_misiones": 50,
        "min_miticas": 3,
    },
    "Continente III: El Dominio Celestial y Grietas del Vacío": {
        "min_misiones": 120,
        "min_miticas": 10,
    },
}


def verificar_desbloqueo_continente(nombre_continente, misiones_completadas_usuario, miticas_completadas_usuario):
    if nombre_continente not in REQUISITOS_CONTINENTES:
        return False, "⚠️ Error: El continente especificado no existe en el atlas de Snd-Worlds."

    reqs = REQUISITOS_CONTINENTES[nombre_continente]
    req_misiones = reqs["min_misiones"]
    req_miticas = reqs["min_miticas"]

    if misiones_completadas_usuario >= req_misiones and miticas_completadas_usuario >= req_miticas:
        return True, f"✅ Acceso concedido a {nombre_continente}."

    return False, (
        f"🔒 Bloqueado: Debes completar al menos {req_misiones} misiones y resolver "
        f"{req_miticas} Misiones Míticas Ocultas del continente anterior. "
        f"(Progreso actual: {misiones_completadas_usuario} misiones | {miticas_completadas_usuario}/10 míticas)."
    )