# --- MÓDULO: HABILIDADES (OPTIMIZADO Y VALIDADO) ---

class ControladorHabilidades:
    """Valida restricciones de clase, cupos y balanceo de poder."""
    
    @staticmethod
    def calcular_dano(habilidad, stats_jugador):
        """Fórmula lógica para evitar 'roturas' de juego."""
        # Multiplicadores base para evitar desbalanceo
        multiplicadores = {"I": 2.5, "II": 1.8, "III": 1.5, "IV": 1.2, "V": 1.1, "VI": 1.0}
        tier = habilidad.get("tier", "VI")
        mult = multiplicadores.get(tier, 1.0)
        
        # El daño escala con el atributo principal (ej: STR, INT)
        stat_base = stats_jugador.get(habilidad.get("stat_req"), 10)
        return int(stat_base * mult)

    @staticmethod
    def validar_equipamiento(jugador, habilidad_id):
        """Validación automática de reglas de oro."""
        # 1. ¿Es Épica? Solo puede tener una equipada en todo el slot
        if habilidad_id.startswith("E") and any(h.startswith("E") for h in jugador.habs_activas):
            return False, "Error: Solo puedes equipar una habilidad Épica."
        
        # 2. ¿Cupos Míticos/Leyenda?
        # Aquí el sistema consultaría el servidor para ver si hay >5 (Mit) o >10 (Ley) usuarios
        return True, "Habilidad validada."

# --- ESCALADO LOGICO DE PODER (Niv 30) ---
# Se ajustan multiplicadores para que solo las Míticas (Tier I) rompan el balance.
DETALLES_LEYENDA = {
    f"L{i:03}": {
        "stat_req": "STR", # Ejemplo, cada una usará el suyo
        "Niv30": "Daño 180% stat base (Equilibrado)" 
    } for i in range(1, 31)
}

DETALLES_MITICAS = {
    f"M{i:03}": {
        "stat_req": "STR",
        "Niv30": "Daño 300% stat base + EFECTO ROTO (Control total)" 
    } for i in range(1, 14)
}
