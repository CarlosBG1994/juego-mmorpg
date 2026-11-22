# --- ADJUNTO A modulos/requisitos.py ---

def auditoria_interagente():
    """
    Protocolo de verificación:
    1. El Agente de Misiones debe llamar a Razas.validar_compatibilidad() antes de entregar misión.
    2. El Agente de Mundo debe llamar a Razas.validar_uso_equipo() para verificar drops.
    3. El Agente de Estética debe usar Razas.obtener_opciones_personalizacion() para el Editor.
    """
    registro_dependencias = {
        "Misiones": "Uso obligatorio de validar_compatibilidad()",
        "Mundo": "Uso obligatorio de validar_uso_equipo()",
        "UI_Personalizacion": "Uso obligatorio de obtener_plantilla_creacion()"
    }
    return registro_dependencias
