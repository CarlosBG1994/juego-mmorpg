"""
Modulo: Persistencia de Snd-Worlds
Gestiona el guardado y carga de los datos del jugador (JSON).
Incluye: Backup automático, validación SHA-256, recuperación de desastres,
metadatos de zona y persistencia de estados temporales.
"""
import json
import shutil
import os
import hashlib
import time

def _generar_checksum(datos_dict):
    """Crea una firma única para validar que el archivo no ha sido alterado."""
    datos_str = json.dumps(datos_dict, sort_keys=True)
    return hashlib.sha256(datos_str.encode()).hexdigest()

def guardar_partida(jugador, nombre_archivo="partida_jugador.json"):
    # 1. Crear backup previo de seguridad
    if os.path.exists(nombre_archivo):
        shutil.copy(nombre_archivo, f"{nombre_archivo}.bak")
    
    # 2. Estructura de datos completa (Incluye estados temporales y metadatos)
    datos = {
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
    
    # 3. Añadir checksum para validación de integridad
    datos["checksum"] = _generar_checksum({k: v for k, v in datos.items() if k != "checksum"})
    
    with open(nombre_archivo, 'w') as f:
        json.dump(datos, f, indent=4)
    return True

def cargar_partida(jugador, nombre_archivo="partida_jugador.json"):
    # Intentar cargar archivo principal, si falla, intentar con el .bak
    archivos_a_probar = [nombre_archivo, f"{nombre_archivo}.bak"]
    
    for archivo in archivos_a_probar:
        if not os.path.exists(archivo): continue
        
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            
            # Validación de integridad
            checksum_almacenado = datos.pop("checksum", None)
            if checksum_almacenado != _generar_checksum(datos):
                continue # Saltar al backup si el principal está corrupto
            
            # Restauración de datos base
            jugador.progresion.nombre = datos["nombre"]
            jugador.progresion.nivel = datos["nivel"]
            jugador.progresion.stats = datos["stats"]
            jugador.progresion.continente_actual = datos["continente"]
            jugador.mochila.billetera.total_cobre = datos["dinero"]
            jugador.mochila.items = datos["mochila"]
            
            # Restauración de estados temporales
            if hasattr(jugador, 'montura_actual'):
                jugador.montura_actual.fatiga = datos.get("fatiga_montura", 0)
            
            return True, f"Progreso cargado exitosamente desde {archivo}."
            
        except Exception:
            continue # Intentar con el siguiente archivo si hay error crítico
            
    return False, "Error crítico: No se pudo recuperar ningún archivo de guardado válido."
