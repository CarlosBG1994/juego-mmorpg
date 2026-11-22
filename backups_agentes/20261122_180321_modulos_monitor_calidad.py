from modulos.monitor_calidad import monitor_qa
from modulos.integrador import Jugador

# 1. Crear un jugador de prueba
jugador_prueba = Jugador(id_jugador="JUGADOR_001", raza="Humano", clase="Caballero")

# 2. Usar el monitor para auditar el flujo
monitor_qa.simular_flujo_login(jugador_prueba)
