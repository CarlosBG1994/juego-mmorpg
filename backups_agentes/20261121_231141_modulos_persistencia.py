"""
Modulo: Persistencia de Snd-Worlds
Gestiona el guardado y carga de los datos del jugador (JSON).
Incluye: Backup automático, guardado de inventario y validación de integridad.
"""
import json
import shutil
import os
import hashlib

def _generar_checksum(datos_dict):
    """Crea una firma única para validar que el archivo no ha sido alterado."""
    datos_str = json.dumps(datos_dict, sort_keys=True)
    return hashlib.sha256(datos_str.encode()).hexdigest()

def guardar_partida(jugador, nombre_archivo="partida_jugador.json"):
    # 1. Crear backup previo de seguridad
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
    
    # 3. Añadir checksum para validación de integridad
    datos["checksum"] = _generar_checksum({k: v for k, v in datos.items() if k != "checksum"})
    
    with open(nombre_archivo, 'w') as f:
        json.dump(datos, f, indent=4)
    return True

def cargar_partida(jugador, nombre_archivo="partida_jugador.json"):
    if not os.path.exists(nombre_archivo):
        return False, "No se encontró archivo de guardado."
        
    try:
        with open(nombre_archivo, 'r') as f:
            datos = json.load(f)
        
        # 1. Validación de integridad
        checksum_almacenado = datos.pop("checksum", None)
        if checksum_almacenado != _generar_checksum(datos):
            return False, "Error: El archivo de guardado está corrupto o ha sido alterado."
        
        # 2. Restauración detallada
        jugador.progresion.nombre = datos["nombre"]
        jugador.progresion.nivel = datos["nivel"]
        jugador.progresion.stats = datos["stats"]
        jugador.progresion.continente_actual = datos["continente"]
        jugador.mochila.billetera.total_cobre = datos["dinero"]
        jugador.mochila.items = datos["mochila"]
        
        return True, "Progreso, inventario e integridad validados y cargados correctamente."
    except Exception as e:
        return False, f"Error crítico de carga: {str(e)}"
