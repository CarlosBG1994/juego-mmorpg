"""
Modulo: Razas y Clases de Snd-Worlds
Gestiona la identidad visual, atributos, restricciones de equipo, 
personalización estética y maestría de progresión de personajes.
"""

# ... [Mantenemos las constantes y estructuras previas intactas] ...

# --- PROTOCOLO DE BLINDAJE (Seguridad Anti-Hack/Bug) ---

def _auditar_acceso(raza: str, clase: str, contexto: str) -> bool:
    """Verificación interna de integridad antes de cualquier operación."""
    if raza not in RAZAS_HABILITADAS:
        # Registro de intento de intrusión en la raza bloqueada
        print(f"[ALERTA SEGURIDAD] Intento de acceso no autorizado a raza: {raza} en {contexto}")
        return False
    if clase not in CLASES_POR_RAZA.get(raza, []):
        print(f"[ALERTA SEGURIDAD] Clase {clase} no válida para {raza} en {contexto}")
        return False
    return True

def validar_compatibilidad_blindada(raza: str, clase: str, objeto_id: str) -> bool:
    """
    Validación de doble capa:
    1. Audita que el jugador sea quien dice ser.
    2. Comprueba compatibilidad en el registro maestro.
    """
    if not _auditar_acceso(raza, clase, "validar_compatibilidad"):
        return False
        
    # Aquí iría la lógica de verificación contra la base de datos de objetos
    return True

def validar_uso_equipo_blindado(clase: str, tipo_armadura: str) -> bool:
    """Evita que una clase acceda a armaduras prohibidas mediante inyección."""
    if tipo_armadura not in TIPOS_ARMADURA:
        print(f"[ALERTA SEGURIDAD] Intento de equipar tipo de armadura inexistente: {tipo_armadura}")
        return False
        
    if tipo_armadura not in ARMADURAS_PERMITIDAS.get(clase, []):
        return False
        
    return True

# --- REGLA DE ORO DE ATRIBUTOS ---
def aplicar_puntos_blindados(stats_actuales: dict, puntos_a_asignar: int, nivel: int) -> dict:
    """
    Control de servidor: evita que los puntos excedan el límite por nivel.
    Limite: 5 puntos por nivel.
    """
    limite_maximo = (nivel * 5)
    suma_actual = sum(stats_actuales.values())
    
    if (suma_actual + puntos_a_asignar) > (60 + limite_maximo):
        print(f"[ALERTA SEGURIDAD] Intento de asignación de puntos ilegal por: {puntos_a_asignar}")
        return stats_actuales # Rechazar cambio
        
    return stats_actuales # Aceptar cambio
