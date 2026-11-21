"""
Modulo: Persistencia de Snd-Worlds
Gestiona el guardado y carga de los datos del jugador (JSON).
"""
import json

def guardar_partida(jugador, nombre_archivo="partida_jugador.json"):
    """Guarda el estado completo del jugador en un archivo JSON."""
    datos = {
        "nombre": jugador.progresion.nombre,
        "nivel": jugador.progresion.nivel,
        "stats": jugador.progresion.stats,
        "dinero": jugador.mochila.billetera.total_cobre,
        "habilidades_equipadas": [h.id for h in jugador.habilidades_equipadas],
        "continente": jugador.progresion.continente_actual
    }
    with open(nombre_archivo, 'w') as f:
        json.dump(datos, f, indent=4)
    return True

def cargar_partida(jugador, nombre_archivo="partida_jugador.json"):
    """Carga los datos desde el archivo y los aplica a la instancia del jugador."""
    try:
        with open(nombre_archivo, 'r') as f:
            datos = json.load(f)
        
        # Restaurar progresion
        jugador.progresion.nombre = datos["nombre"]
        jugador.progresion.nivel = datos["nivel"]
        jugador.progresion.stats = datos["stats"]
        jugador.progresion.continente_actual = datos["continente"]
        
        # Restaurar economia
        jugador.mochila.billetera.total_cobre = datos["dinero"]
        
        return True, "Partida cargada exitosamente."
    except FileNotFoundError:
        return False, "No se encontro un archivo de guardado previo."
    except Exception as e:
        return False, f"Error al cargar la partida: {str(e)}"
