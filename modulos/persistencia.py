"""
Modulo: Persistencia de Snd-Worlds
Gestiona el guardado y carga de los datos del jugador (JSON).
"""
import json

def guardar_partida(jugador, nombre_archivo="partida_jugador.json"):
    datos = {
        "nombre": jugador.progresion.nombre,
        "nivel": jugador.progresion.nivel,
        "stats": jugador.progresion.stats,
        "dinero": jugador.mochila.billetera.total_cobre,
        # Aquí se añadiría la lógica para serializar habilidades, mascotas, etc.
    }
    with open(nombre_archivo, 'w') as f:
        json.dump(datos, f, indent=4)
    return True

# (Este sería el módulo que nos falta)
