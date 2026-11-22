# Modulo: requisitos
"""
Centro de Coordinación Inter-Agentes (CCIA)
Este módulo establece los protocolos de comunicación, notificación de cambios
y propuestas de mejora entre los distintos módulos del sistema Snd-Worlds.
"""

class CoordinadorAgentes:
    def __init__(self):
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
        self.matriz_dependencias = {}
        self.alertas_conflicto = []

    def validar_integridad_datos(self, modulo: str, datos: dict):
        """
        VID: Comprueba que los datos entrantes sean coherentes con las reglas globales.
        Ejemplo: Si el módulo es Economia, valida contra Tiers de Habilidades.
        """
        # Regla 1: Coherencia de Precios vs Tiers
        if modulo == "Economia" and "tier" in datos and "precio" in datos:
            from modulos.economia_y_comercio import VALOR_MINIMO_POR_TIER
            if datos["precio"] < VALOR_MINIMO_POR_TIER.get(datos["tier"], 0):
                self.alertas_conflicto.append(f"Incoherencia de precio en {datos['tier']}: {datos['precio']} es muy bajo.")
                return False
        
        # Regla 2: Coherencia de Niveles vs Continentes
        if modulo == "Progresion" and "nivel" in datos and "continente" in datos:
            from modulos.progresion_y_stats import CONTINENTES_Y_LIMITES
            if datos["nivel"] > CONTINENTES_Y_LIMITES.get(datos["continente"], 100):
                self.alertas_conflicto.append(f"Nivel {datos['nivel']} excede el límite del continente {datos['continente']}.")
                return False
        
        return True

    def registrar_dependencia(self, modulo_padre: str, modulo_hijo: str):
        if modulo_hijo not in self.matriz_dependencias:
            self.matriz_dependencias[modulo_padre] = modulo_hijo
            return True
        return False

    def detectar_y_reportar_conflictos(self):
        if self.alertas_conflicto:
            print(f"[ALERTA CRÍTICA] Se han detectado {len(self.alertas_conflicto)} conflictos en la sincronización.")
            # Reporte automático al usuario
            for alerta in self.alertas_conflicto:
                print(f" -> {alerta}")
            return self.alertas_conflicto
        return "Estado del sistema: Coordinado."

    def notificar_actualizacion(self, modulo_emisor: str, descripcion_cambio: str):
        evento = {"emisor": modulo_emisor, "cambio": descripcion_cambio, "status": "Auditado"}
        self.bitacora_cambios.append(evento)
        print(f"[CCIA] Aviso: {modulo_emisor} actualizado.")
        self.detectar_y_reportar_conflictos()
        return evento

    def proponer_mejora_cruzada(self, modulo_receptor: str, sugerencia: str):
        print(f"[CCIA] Propuesta de mejora para {modulo_receptor}: {sugerencia}")
        return True

coordinador_global = CoordinadorAgentes()

def sincronizar_sistema():
    return coordinador_global.detectar_y_reportar_conflictos()
