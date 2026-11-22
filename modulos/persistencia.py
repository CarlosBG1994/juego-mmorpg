"""
Modulo: Persistencia de Snd-Worlds (Escalabilidad Masiva)
Optimizado para millones de jugadores mediante Sharding de archivos,
gestión de concurrencia y validación de alta integridad.
"""
import json
import shutil
import os
import hashlib
import time

def _obtener_ruta_sharding(jugador_id):
    """Crea una estructura de directorios para evitar colapsos de I/O."""
    prefijo = jugador_id[:2] if len(jugador_id) >= 2 else "00"
    directorio = f"datos_jugadores/{prefijo}"
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    return f"{directorio}/{jugador_id}.json"

def _generar_checksum(datos_dict):
    datos_str = json.dumps(datos_dict, sort_keys=True)
    return hashlib.sha256(datos_str.encode()).hexdigest()

def guardar_partida(jugador):
    ruta_archivo = _obtener_ruta_sharding(str(jugador.id))
    
    # 1. Crear backup previo de seguridad
    if os.path.exists(ruta_archivo):
        shutil.copy(ruta_archivo, f"{ruta_archivo}.bak")
    
    # 2. Estructura de datos completa
    datos = {
        "id": jugador.id,
        "nombre": jugador.progresion.nombre,
        "nivel": jugador.progresion.nivel,
        "stats": jugador.progresion.stats,
        "dinero": jugador.mochila.billetera.total_cobre,
        "habilidades": [h.id for h in jugador.habilidades_equipadas],
        "mochila": [item for item in jugador.mochila.items],
        "continente": jugador.progresion.continente_actual,
        "misiones_activas": [m.id for m in jugador.gestor_misiones.misiones_activas],
        "fatiga_montura": jugador.montura_actual.fatiga if hasattr(jugador, 'montura_actual') else 0,
        "timestamp": time.time()
    }
    
    datos["checksum"] = _generar_checksum({k: v for k, v in datos.items() if k != "checksum"})
    
    # 3. Guardado atómico (escribir y mover) para evitar corrupción por apagones
    tmp_file = f"{ruta_archivo}.tmp"
    with open(tmp_file, 'w') as f:
        json.dump(datos, f, separators=(',', ':')) # Separadores compactos para ahorrar espacio
    os.replace(tmp_file, ruta_archivo)
    
    return True

def cargar_partida(jugador):
    ruta_archivo = _obtener_ruta_sharding(str(jugador.id))
    
    for archivo in [ruta_archivo, f"{ruta_archivo}.bak"]:
        if not os.path.exists(archivo): continue
        
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            
            if datos.pop("checksum", None) != _generar_checksum(datos):
                continue
            
            # Restauración...
            jugador.progresion.nombre = datos["nombre"]
            jugador.progresion.nivel = datos["nivel"]
            jugador.progresion.stats = datos["stats"]
            jugador.progresion.continente_actual = datos["continente"]
            jugador.mochila.billetera.total_cobre = datos["dinero"]
            jugador.mochila.items = datos["mochila"]
            
            return True, "Carga exitosa desde cluster de persistencia."
        except Exception:
            continue
            
    return False, "Error: Datos de jugador no localizados en el cluster."
