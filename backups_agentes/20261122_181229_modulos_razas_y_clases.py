# ... [Mantenemos las estructuras previas intactas] ...

# 4. SISTEMA DE MAESTRIA DRACÓNICA
# Esto define la ventaja táctica única (pasiva) que obtiene el jugador al elegir una de estas clases.
MAESTRIA_DRACONICA = {
    "Guerrero Dragon": {
        "bono": "+10% de daño elemental tras recibir un golpe físico.",
        "efecto_visual": "Brillo de escamas incandescente al activar."
    },
    "Mago de Sangre": {
        "bono": "Convierte el 5% del daño realizado en regeneración de HP.",
        "efecto_visual": "Aura de vapor carmesí alrededor del jugador."
    },
    "Custodio de Escamas": {
        "bono": "Reduce el daño de ataques críticos recibidos en un 15%.",
        "efecto_visual": "Las escamas se vuelven de un tono metálico oscuro."
    },
    "Acechador Draconico": {
        "bono": "Aumenta la velocidad de movimiento un 10% tras atacar.",
        "efecto_visual": "Estela de energía traslúcida al moverse."
    }
}

def obtener_maestria_clase(clase: str) -> dict:
    """
    Retorna rol, foco y la Maestría única de la clase.
    """
    # Si es clase dracónica, devolvemos su maestría especial
    if clase in CLASES_DRACONICAS:
        datos = CLASES_DRACONICAS[clase]
        maestria = MAESTRIA_DRACONICA.get(clase, {"bono": "N/A"})
        return {
            "rol": datos["rol"], 
            "foco": datos["foco"],
            "maestria_unica": maestria["bono"]
        }
    
    # Maestría estándar para las razas iniciales
    maestria_base = MAESTRIA_CLASES.get(clase, {"rol": "Desconocido", "foco": "Exploración", "maestria_unica": "Ninguna"})
    return maestria_base

# ... [RESTO DEL MÓDULO INTACTO] ...
