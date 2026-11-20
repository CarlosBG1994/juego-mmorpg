# --- MOTOR DE PROGRESIÓN Y BLOQUEO DE CONTINENTES ---

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
    if nombre_continente not in REQUISITOS_CONTINENTES:
        return False, "⚠️ Error: El continente especificado no existe."
        
    reqs = REQUISITOS_CONTINENTES[nombre_continente]
    if misiones_completadas_usuario >= reqs["min_misiones"] and miticas_completadas_usuario >= reqs["min_miticas"]:
        return True, f"✅ Acceso concedido a {nombre_continente}."
    else:
        return False, f"🔒 Zona Bloqueada: Requiere {reqs['min_misiones']} misiones y {reqs['min_miticas']} Míticas Ocultas."