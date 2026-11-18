# --- MOTOR DE PROGRESIÓN Y BLOQUEO DE CONTINENTES (progression_engine.py) ---

# Configuración de requisitos estrictos para el avance de continente en Snd-Worlds
REQUISITOS_CONTINENTES = {
    "Continente I: Reinos Fundacionales y Zonas Neutras": {
        "min_misiones": 0,
        "min_miticas": 0
    },
    "Continente II: Tierras de Ceniza y Abismos Antiguos": {
        "min_misiones": 50,
        "min_miticas": 3
    },
    "Continente III: El Dominio Celestial y Grietas del Vacío": {
        "min_misiones": 120,
        "min_miticas": 10
    }
}

def verificar_desbloqueo_continente(nombre_continente, misiones_completadas_usuario, miticas_completadas_usuario):
    """
    Verifica si el jugador cumple los requisitos para cruzar a un nuevo continente.
    Regla de diseño: No se puede avanzar sin completar el contenido masivo y las 
    misiones míticas ocultas precedentes.
    """
    if nombre_continente not in REQUISITOS_CONTINENTES:
        return False, "⚠️ Error: El continente especificado no existe en el atlas de Snd-Worlds."
        
    reqs = REQUISITOS_CONTINENTES[nombre_continente]
    req_misiones = reqs["min_misiones"]
    req_miticas = reqs["min_miticas"]
    
    if misiones_completadas_usuario >= req_misiones and miticas_completadas_usuario >= req_miticas:
        return True, f"✅ Acceso concedido a {nombre_continente}."
    else:
        return False, (
            f"🔒 Zona Bloqueada: Para ingresar aquí debes haber completado al menos "
            f"{req_misiones} misiones y resuelto {req_miticas} Misiones Míticas Ocultas. "
            f"(Tu progreso actual: {misiones_completadas_usuario} misiones, {miticas_completadas_usuario} míticas)."
        )

def calcular_experiencia_rango(nivel_personaje):
    """Calcula la progresión de experiencia requerida para subir de nivel en el mundo de 1.5M km²."""
    return int(nivel_personaje * 1500 * 1.15)