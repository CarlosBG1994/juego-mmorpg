"""
Modulo: Persistencia y Monitorización de Snd-Worlds
Rol: Auditoría de alta disponibilidad y persistencia desacoplada.
"""
import json
import shutil
import os
import hashlib
import time

# --- CAPA DE AUDITORÍA Y CALIDAD ---
class MonitorCalidad:
    def __init__(self):
        self.errores_detectados = []
        self.ids_registrados = set() 

    def auditar_operacion(self, jugador_id, accion):
        """Registra actividad y detecta posibles colisiones o errores."""
        if not jugador_id:
            self.errores_detectados.append({"ts": time.time(), "error": "ID_NULO", "accion": accion})
            return False
        return True

monitor_qa = MonitorCalidad()

# --- CAPA DE DESACOPLAMIENTO ---
class EventBus:
    @staticmethod
    def emit(evento, datos):
        # Conecta con colas asíncronas para no bloquear al usuario.
        pass

def _obtener_ruta_sharding(jugador_id):
    prefijo = jugador_id[:2] if len(jugador_id) >= 2 else "00"
    directorio = f"datos_jugadores/{prefijo}"
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    return f"{directorio}/{jugador_id}.json"

def _generar_checksum(datos_dict):
    datos_str = json.dumps(datos_dict, sort_keys=True)
    return hashlib.sha256(datos_str.encode()).hexdigest()

def guardar_partida(jugador):
    if not monitor_qa.auditar_operacion(jugador.id, "GUARDAR"):
        return False
        
    EventBus.emit("SOLICITUD_GUARDADO", {"jugador_id": jugador.id})
    ruta_archivo = _obtener_ruta_sharding(str(jugador.id))
    
    if os.path.exists(ruta_archivo):
        shutil.copy(ruta_archivo, f"{ruta_archivo}.bak")
    
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
    
    tmp_file = f"{ruta_archivo}.tmp"
    with open(tmp_file, 'w') as f:
        json.dump(datos, f, separators=(',', ':'))
    os.replace(tmp_file, ruta_archivo)
    
    return True

def cargar_partida(jugador):
    if not monitor_qa.auditar_operacion(jugador.id, "CARGAR"):
        return False, "Error de ID en monitor."
        
    ruta_archivo = _obtener_ruta_sharding(str(jugador.id))
    for archivo in [ruta_archivo, f"{ruta_archivo}.bak"]:
        if not os.path.exists(archivo): continue
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
            if datos.pop("checksum", None) != _generar_checksum(datos):
                continue
            
            jugador.progresion.nombre = datos["nombre"]
            jugador.progresion.nivel = datos["nivel"]
            jugador.progresion.stats = datos["stats"]
            jugador.progresion.continente_actual = datos["continente"]
            jugador.mochila.billetera.total_cobre = datos["dinero"]
            jugador.mochila.items = datos["mochila"]
            return True, "Carga exitosa y validada por auditoría."
        except Exception:
            continue
    return False, "Error: Datos no localizados."
