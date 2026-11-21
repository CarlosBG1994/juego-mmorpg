"""
Modulo: Persistencia de Snd-Worlds
Gestiona el guardado y carga de los datos del jugador (JSON).
Incluye: Backup automático y guardado de inventario.
"""
import json
import shutil
import os

def guardar_partida(jugador, nombre_archivo="partida_jugador.json"):
    # 1. Crear backup previo
    if os.path.exists(nombre_archivo):
        shutil.copy(nombre_archivo, f"{nombre_archivo}.bak")
    
    # 2. Estructura de datos completa
    datos = {
        "nombre": jugador.progresion.nombre,
        "nivel": jugador.progresion.nivel,
        "stats": jugador.progresion.stats,
        "dinero": jugador.mochila.billetera.total_cobre,
        "habilidades": [h.id for h in jugador.habilidades_equipadas],
        "mochila": [item for item in jugador.mochila.items],
        "continente": jugador.progresion.continente_actual
    }
    
    with open(nombre_archivo, 'w') as f:
        json.dump(datos, f, indent=4)
    return True

def cargar_partida(jugador, nombre_archivo="partida_jugador.json"):
    if not os.path.exists(nombre_archivo):
        return False, "No se encontro archivo de guardado."
        
    try:
        with open(nombre_archivo, 'r') as f:
            datos = json.load(f)
        
        # Restauracion detallada
        jugador.progresion.nombre = datos["nombre"]
        jugador.progresion.nivel = datos["nivel"]
        jugador.progresion.stats = datos["stats"]
        jugador.progresion.continente_actual = datos["continente"]
        jugador.mochila.billetera.total_cobre = datos["dinero"]
        jugador.mochila.items = datos["mochila"] # Restauracion de inventario
        
        return True, "Progreso e inventario cargados correctamente."
    except Exception as e:
        return False, f"Error critico de carga: {str(e)}"
