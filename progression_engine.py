# --- MOTOR DE PROGRESIÓN Y APERTURA DINÁMICA DE CONTINENTES (progression_engine.py) ---

from config import (
    CONTINENTE_INICIAL,
    CONTINENTES_RACIALES,
    CONTINENTE_DEMONIACO,
    CONTINENTE_ANGELICAL,
    RANGOS_POR_ORDEN_RACIAL,
)


def obtener_rango_continente_racial(continente, orden_apertura_raciales):
    """
    Devuelve el rango de niveles asignado a un continente racial según
    el orden en que fue abierto (1º: 101-150, 2º: 151-200, 3º: 201-250, 4º: 251-300).
    Si aún no se ha abierto, indica el siguiente rango disponible.
    """
    if continente in orden_apertura_raciales:
        idx = orden_apertura_raciales.index(continente)
        return RANGOS_POR_ORDEN_RACIAL[idx]
    siguiente_idx = min(len(orden_apertura_raciales), len(RANGOS_POR_ORDEN_RACIAL) - 1)
    return f"Pendiente (será {RANGOS_POR_ORDEN_RACIAL[siguiente_idx]} si se abre ahora)"


def obtener_rango_visual_continente(continente, orden_apertura_raciales):
    if continente == CONTINENTE_INICIAL:
        return "1–100"
    if continente in CONTINENTES_RACIALES:
        return obtener_rango_continente_racial(continente, orden_apertura_raciales)
    if continente == CONTINENTE_DEMONIACO:
        return "301–350"
    if continente == CONTINENTE_ANGELICAL:
        return "Endgame (350+)"
    return "Desconocido"


def todos_los_continentes_anteriores_abiertos(continentes_abiertos):
    requeridos = [CONTINENTE_INICIAL] + CONTINENTES_RACIALES
    return all(c in continentes_abiertos for c in requeridos)


def verificar_acceso_continente(
    continente,
    continentes_abiertos,
    orden_apertura_raciales,
    jugador_completo_principales_abiertas,
    todas_principales_completadas,
    misiones_ocultas_angelical_completadas,
):
    """
    Valida si el jugador puede entrar/abrir el continente solicitado según las reglas de Snd-Worlds.
    """
    if continente == CONTINENTE_INICIAL:
        return True, "✅ Continente Inicial disponible (Niveles 1–100)."

    if continente in CONTINENTES_RACIALES:
        if continente in continentes_abiertos:
            rango = obtener_rango_continente_racial(continente, orden_apertura_raciales)
            return True, f"✅ Continente abierto (Rango asignado: {rango})."
        siguiente_rango = RANGOS_POR_ORDEN_RACIAL[min(len(orden_apertura_raciales), 3)]
        return False, (
            f"🔒 Continente Racial cerrado. Si se abre ahora, su rango será {siguiente_rango}. "
            f"Completa su condición/misión de apertura para desbloquearlo."
        )

    if continente == CONTINENTE_DEMONIACO:
        if continente in continentes_abiertos:
            return True, "✅ Continente Demoníaco abierto (Niveles 301–350)."
        if not todos_los_continentes_anteriores_abiertos(continentes_abiertos):
            return False, (
                "🔒 Continente Demoníaco (301–350) bloqueado: primero deben estar abiertos el "
                "Continente Inicial y los 4 Continentes Raciales."
            )
        if not jugador_completo_principales_abiertas:
            return False, (
                "🔒 Continente Demoníaco (301–350) bloqueado: se requiere que al menos 1 jugador "
                "haya completado todas las misiones principales abiertas."
            )
        return True, "✅ Requisitos cumplidos: ya se puede abrir el Continente Demoníaco (301–350)."

    if continente == CONTINENTE_ANGELICAL:
        if continente in continentes_abiertos:
            return True, "✅ Continente Angelical abierto."
        if not todos_los_continentes_anteriores_abiertos(continentes_abiertos):
            return False, (
                "🔒 Continente Angelical bloqueado: primero deben estar abiertos todos los "
                "continentes anteriores (Inicial, 4 Raciales y Demoníaco)."
            )
        if CONTINENTE_DEMONIACO not in continentes_abiertos:
            return False, (
                "🔒 Continente Angelical bloqueado: el Continente Demoníaco debe estar abierto."
            )
        if not todas_principales_completadas:
            return False, (
                "🔒 Continente Angelical bloqueado: deben estar completadas todas las misiones "
                "principales de los continentes anteriores."
            )
        if not misiones_ocultas_angelical_completadas:
            return False, (
                "🔒 Continente Angelical bloqueado: debes descubrir y completar las misiones "
                "ocultas específicas para abrir el Continente Angelical."
            )
        return True, "✅ Requisitos cumplidos: el Continente Angelical está listo para abrirse."

    return False, "⚠️ Continente no reconocido."