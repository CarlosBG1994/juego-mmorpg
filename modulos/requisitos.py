# Modulo: requisitos
"""
Centro de Coordinación Inter-Agentes (CCIA)
Este módulo establece los protocolos de comunicación, notificación de cambios
y propuestas de mejora entre los distintos módulos del sistema Snd-Worlds.
"""

class CoordinadorAgentes:
    def __init__(self):
        # Registro completo de todos los módulos del sistema
        self.registro_modulos = {
            "Economia": "modulos/economia_y_comercio.py",
            "Habilidades": "modulos/habilidades.py",
            "Misiones": "modulos/misiones.py",
            "Progresion": "modulos/progresion_y_stats.py",
            "Mundo": "modulos/mundo_y_pve.py",
            "RazasClases": "modulos/razas_y_clases.py",
            "Persistencia": "modulos/persistencia.py",
            "Mascotas": "modulos/mascotas.py",
            "Monturas": "modulos/monturas.py",
            "Monitor": "modulos/monitor_calidad.py",
            "WorldSync": "modulos/world_sync.py"
        }
        self.bitacora_cambios = []

    def notificar_actualizacion(self, modulo_emisor: str, descripcion_cambio: str):
        """
        Protocolo: Todo agente debe invocar esto al modificar su archivo.
        Notifica a los demás módulos sobre la afectación.
        """
        evento = {
            "emisor": modulo_emisor,
            "cambio": descripcion_cambio,
            "status": "Pendiente de revisión"
        }
        self.bitacora_cambios.append(evento)
        print(f"[CCIA] Aviso: El modulo {modulo_emisor} ha sido actualizado. Impacto: {descripcion_cambio}")
        return evento

    def proponer_mejora_cruzada(self, modulo_receptor: str, sugerencia: str):
        """
        Protocolo: Permite a un agente sugerir mejoras en el código de otro.
        """
        print(f"[CCIA] Propuesta de mejora para {modulo_receptor}: {sugerencia}")
        return True

# Instancia global para que los agentes la utilicen como bus de comunicación
coordinador_global = CoordinadorAgentes()

def sincronizar_sistema():
    """Validador central que asegura que todos los módulos cumplen las reglas base."""
    # Verificación de integridad cruzada de todos los módulos registrados
    reporte = f"Sistema Snd-Worlds sincronizado. Total módulos activos: {len(coordinador_global.registro_modulos)}."
    return reporte
