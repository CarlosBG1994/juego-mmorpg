import datetime
import http.server
import json
import os
import re
import shutil
import socketserver
import urllib.error
import urllib.request
from pathlib import Path

from especificacion_base import REGLAS_SND_WORLDS

BASE_DIR = Path(__file__).resolve().parent
MODULOS_DIR = BASE_DIR / "modulos"
BACKUPS_DIR = BASE_DIR / "backups_agentes"
REGISTRO_PATH = BASE_DIR / "registro_agentes.json"
HISTORIALES_DIR = BASE_DIR / "historiales_chats"
TXT_GUIA_PATH = BASE_DIR / "juego_explicado.txt"

MODULOS_DIR.mkdir(exist_ok=True)
BACKUPS_DIR.mkdir(exist_ok=True)
HISTORIALES_DIR.mkdir(exist_ok=True)

REGISTRO_INICIAL = {
    "explorador": {
        "nombre": "Agente 0 · Explorador y Creador",
        "rol": "Lee todo lo que existe en el proyecto y en juego_explicado.txt, crea modulos base/nuevos y genera agentes con su chat.",
        "archivo": None,
        "es_creador_modulos": True,
    },
    "razas_y_clases": {
        "nombre": "Agente · Razas y Clases",
        "rol": "Crea y modifica el modulo de las 4 razas, clases, sub-formas de Hombre Bestia, Pugil y compatibilidad de uso.",
        "archivo": "modulos/razas_y_clases.py",
        "es_creador_modulos": False,
    },
    "habilidades": {
        "nombre": "Agente · Habilidades (1.870)",
        "rol": "Crea y modifica el catalogo de 1.870 habilidades, tiers 15/30, fusion nivel 40 y uso restringido vs. obtencion libre.",
        "archivo": "modulos/habilidades.py",
        "es_creador_modulos": False,
    },
    "economia_y_comercio": {
        "nombre": "Agente · Mochila, Subasta, Gremio e Intercambio",
        "rol": "Crea y modifica inventario, habilidades no equipables obtenidas y comercio por Subasta, Gremio e Intercambio directo.",
        "archivo": "modulos/economia_y_comercio.py",
        "es_creador_modulos": False,
    },
    "progresion_y_stats": {
        "nombre": "Agente · Niveles y Estadisticas",
        "rol": "Crea y modifica niveles 1-100 iniciales, +5 puntos libres, +10 HP por nivel y +50 niveles por continente hasta nivel 300.",
        "archivo": "modulos/progresion_y_stats.py",
        "es_creador_modulos": False,
    },
    "mundo_y_pve": {
        "nombre": "Agente · Reinos, Monstruos y Jefes",
        "rol": "Crea y modifica reinos, zonas de caza, bestiario, drops, jefes de zona, misiones y continentes ocultos.",
        "archivo": "modulos/mundo_y_pve.py",
        "es_creador_modulos": False,
    },
    "integrador": {
        "nombre": "Agente · Integrador General",
        "rol": "Revisa todos los modulos creados, los conecta sin borrar nada y verifica que todo encaje.",
        "archivo": "modulos/integrador.py",
        "es_creador_modulos": False,
    },
}


def cargar_registro() -> dict:
    if not REGISTRO_PATH.exists():
        guardar_registro(REGISTRO_INICIAL)
        return dict(REGISTRO_INICIAL)
    data = json.loads(REGISTRO_PATH.read_text(encoding="utf-8"))
    for k, v in REGISTRO_INICIAL.items():
        if k not in data:
            data[k] = v
    return data


def guardar_registro(data: dict) -> None:
    REGISTRO_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def slug_modulo(texto: str) -> str:
    limpio = re.sub(r"[^a-zA-Z0-9_]+", "_", texto.lower().strip()).strip("_")
    return limpio or "nuevo_modulo"


def cargar_historial(agente_id: str) -> list:
    ruta = HISTORIALES_DIR / f"{agente_id}.json"
    if not ruta.exists():
        return []
    return json.loads(ruta.read_text(encoding="utf-8"))


def guardar_historial(agente_id: str, historial: list) -> None:
    ruta = HISTORIALES_DIR / f"{agente_id}.json"
    ruta.write_text(json.dumps(historial, indent=2, ensure_ascii=False), encoding="utf-8")


def hacer_backup(archivo_rel: str) -> str | None:
    origen = BASE_DIR / archivo_rel
    if not origen.exists():
        return None
    marca = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_seguro = archivo_rel.replace("/", "_").replace("\\", "_")
    destino = BACKUPS_DIR / f"{marca}_{nombre_seguro}"
    shutil.copy2(origen, destino)
    return str(destino.relative_to(BASE_DIR))


def leer_todo_el_proyecto() -> str:
    partes = []
    if TXT_GUIA_PATH.exists():
        contenido_txt = TXT_GUIA_PATH.read_text(encoding="utf-8").strip()
        partes.append(f"--- juego_explicado.txt ---\n{contenido_txt or '(Vacio)'}")
    else:
        partes.append("--- juego_explicado.txt ---\n(No creado aun)")

    archivos_py = sorted(MODULOS_DIR.glob("*.py"))
    if not archivos_py:
        partes.append("--- modulos/ ---\n(Aun no hay archivos en modulos/)")
    else:
        for p in archivos_py:
            texto = p.read_text(encoding="utf-8")
            if len(texto) > 6000:
                texto = texto[:6000] + "\n# ... (truncado por longitud en lectura rapida) ..."
            partes.append(f"--- modulos/{p.name} ---\n{texto}")
    return "\n\n".join(partes)


def llamar_gemini(system_prompt: str, mensajes: list) -> str:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        return (
            "Falta configurar GEMINI_API_KEY en la terminal del Codespace.\n"
            "Ejecuta: export GEMINI_API_KEY='tu_clave_aqui' y vuelve a arrancar."
        )

    modelo_env = os.environ.get("GEMINI_MODEL", "").strip()
    modelos_a_probar = [modelo_env] if modelo_env else [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
    ]

    contents = []
    for m in mensajes:
        rol = "user" if m["role"] == "user" else "model"
        contents.append({"role": rol, "parts": [{"text": m["content"]}]})

    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": contents,
    }

    ultimo_error = ""
    for modelo in modelos_a_probar:
        if not modelo:
            continue
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            partes = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
            texto = "".join(p.get("text", "") for p in partes if "text" in p).strip()
            return texto or "No se recibio respuesta de texto."
        except urllib.error.HTTPError as e:
            detalle = ""
            try:
                detalle = e.read().decode("utf-8", errors="ignore")
            except Exception:
                detalle = str(e)
            ultimo_error = f"Error HTTP {e.code} con el modelo '{modelo}': {detalle[:300]}"
            print(f"[AVISO] {ultimo_error}")
            if e.code == 404:
                continue
            return ultimo_error
        except Exception as e:
            ultimo_error = f"Error de conexion al llamar a Gemini: {e}"
            print(f"[AVISO] {ultimo_error}")
            return ultimo_error

    return (
        "No se pudo conectar con ningun modelo de Gemini (404 Not Found).\n"
        f"Ultimo detalle: {ultimo_error}\n"
        "Puedes probar indicando un modelo concreto en la terminal con:\n"
        "export GEMINI_MODEL='gemini-2.0-flash'"
    )


def extraer_bloques_archivo(respuesta: str) -> list[tuple[str, str]]:
    patron = re.compile(r"```archivo:([^\n`]+)\n(.*?)```", re.DOTALL | re.IGNORECASE)
    resultados = []
    for ruta_raw, codigo in patron.findall(respuesta):
        ruta_limpia = ruta_raw.strip().lstrip("./")
        if not ruta_limpia.startswith("modulos/"):
            ruta_limpia = f"modulos/{Path(ruta_limpia).name}"
        resultados.append((ruta_limpia, codigo.strip() + "\n"))
    return resultados


def extraer_bloque_python(respuesta: str) -> str | None:
    patron = re.compile(r"```python\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
    coincidencias = patron.findall(respuesta)
    if not coincidencias:
        return None
    return coincidencias[-1].strip() + "\n"


def extraer_nuevos_modulos(respuesta: str) -> list[dict]:
    patron = re.compile(r"```nuevo_modulo\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
    creados = []
    for bloque in patron.findall(respuesta):
        try:
            obj = json.loads(bloque.strip())
            if isinstance(obj, dict):
                creados.append(obj)
        except json.JSONDecodeError:
            continue
    return creados


def construir_prompt_agente(agente_id: str, info: dict, registro: dict) -> str:
    panoramica = leer_todo_el_proyecto()

    if info.get("es_creador_modulos"):
        modulos_resumen = "\n".join(
            f"- {k}: {v.get('nombre')} -> archivo: {v.get('archivo') or 'sin archivo'} | rol: {v.get('rol')}"
            for k, v in registro.items()
        )
        return (
            f"Eres {info.get('nombre')} para el juego Snd-Worlds.\n"
            "Habla en espanol claro, cercano y sin jerga innecesaria. "
            "El usuario no quiere revisar codigo a mano ni perder cosas que ya existen.\n\n"
            f"{REGLAS_SND_WORLDS}\n\n"
            "AGENTES Y MODULOS REGISTRADOS ACTUALMENTE:\n"
            f"{modulos_resumen}\n\n"
            "LECTURA COMPLETA DE LO QUE HAY AHORA MISMO:\n"
            f"{panoramica}\n\n"
            "TU MISION:\n"
            "1. Analiza todo lo que ya existe en el proyecto y en juego_explicado.txt.\n"
            "2. Cuando el usuario pida crear modulos o generar agentes "
            "(o que crees lo que ya existe para ir haciendo modificaciones):\n"
            "   - Por cada agente/modulo nuevo que debas activar, incluye un bloque:\n"
            "```nuevo_modulo\n"
            "{\n"
            '  "id": "nombre_en_minusculas_sin_espacios",\n'
            '  "nombre": "Agente · Nombre del Modulo",\n'
            '  "rol": "Que hace este modulo y que modifica",\n'
            '  "archivo": "modulos/nombre_en_minusculas_sin_espacios.py"\n'
            "}\n"
            "```\n"
            "   - Si el usuario pide que tu mismo crees o generes el codigo inicial "
            "de uno o varios archivos de modulo en modulos/, incluye por cada archivo un bloque:\n"
            "```archivo:modulos/nombre_modulo.py\n"
            "# codigo python inicial conservando las reglas de Snd-Worlds\n"
            "```\n"
            "3. Explica al usuario en lenguaje sencillo que se ha creado, "
            "que agentes nuevos han aparecido en la lista y que no se ha borrado nada previo.\n"
        )

    archivo_rel = info.get("archivo") or f"modulos/{agente_id}.py"
    ruta_abs = BASE_DIR / archivo_rel
    contenido_actual = ruta_abs.read_text(encoding="utf-8") if ruta_abs.exists() else "# Modulo aun vacio\n"

    return (
        f"Eres {info.get('nombre')} para el juego Snd-Worlds.\n"
        f"Tu rol es: {info.get('rol')}\n"
        "Habla en espanol claro y directo. El usuario no quiere tocar codigo ni que se borre lo que ya existe.\n\n"
        f"{REGLAS_SND_WORLDS}\n\n"
        "CONTEXTO GENERAL DEL PROYECTO Y juego_explicado.txt:\n"
        f"{panoramica}\n\n"
        f"TU ARCHIVO ASIGNADO ES: {archivo_rel}\n"
        f"CONTENIDO ACTUAL DE {archivo_rel}:\n"
        "```python\n"
        f"{contenido_actual}\n"
        "```\n\n"
        "TU MISION:\n"
        f"- Cuando el usuario pida crear, ampliar o modificar algo de tu modulo, "
        f"entrega el codigo completo actualizado de {archivo_rel} dentro de un unico bloque ```python ... ``` "
        "conservando todo lo anterior que siga siendo valido y anadiendo o ajustando lo pedido sin borrar lo previo.\n"
        "- Al final, resume en palabras sencillas que se ha guardado y que no se ha borrado nada anterior.\n"
    )


HTML_PAGE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Snd-Worlds · Centro de Agentes (Puerto 9567)</title>
  <style>
    body { font-family: system-ui, -apple-system, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; display: flex; flex-direction: column; height: 100vh; }
    header { background: #1e293b; padding: 12px 18px; border-bottom: 1px solid #334155; display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; }
    header h1 { font-size: 16px; margin: 0; color: #38bdf8; }
    .quick-btn { background: #0f766e; color: #fff; border: none; border-radius: 6px; padding: 7px 12px; font-size: 12px; font-weight: 600; cursor: pointer; }
    .quick-btn:hover { background: #0d9488; }
    .main { display: flex; flex: 1; min-height: 0; }
    .sidebar { width: 280px; background: #1e293b; border-right: 1px solid #334155; overflow-y: auto; padding: 10px; display: flex; flex-direction: column; gap: 6px; }
    .tab-btn { text-align: left; background: transparent; color: #cbd5e1; border: 1px solid transparent; padding: 10px 12px; border-radius: 8px; cursor: pointer; font-size: 13px; }
    .tab-btn:hover { background: #334155; }
    .tab-btn.active { background: #0284c7; color: #fff; font-weight: 600; }
    .chat-area { flex: 1; display: flex; flex-direction: column; min-width: 0; }
    .chat-header { padding: 12px 18px; background: #162032; border-bottom: 1px solid #334155; font-size: 13px; color: #94a3b8; }
    .chat-header strong { color: #f8fafc; font-size: 15px; display: block; margin-bottom: 2px; }
    .messages { flex: 1; overflow-y: auto; padding: 18px; display: flex; flex-direction: column; gap: 12px; }
    .msg { max-width: 84%; padding: 12px 14px; border-radius: 10px; white-space: pre-wrap; line-height: 1.45; font-size: 14px; }
    .msg.user { align-self: flex-end; background: #0369a1; color: #fff; }
    .msg.assistant { align-self: flex-start; background: #1e293b; border: 1px solid #334155; color: #e2e8f0; }
    .aviso { font-size: 12px; color: #4ade80; margin-top: 8px; font-weight: 600; }
    .composer { display: flex; gap: 10px; padding: 14px 18px; background: #1e293b; border-top: 1px solid #334155; }
    textarea { flex: 1; resize: none; height: 54px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #f8fafc; padding: 10px; font-family: inherit; font-size: 14px; }
    button.send { background: #0284c7; color: #fff; border: none; border-radius: 8px; padding: 0 20px; font-weight: 600; cursor: pointer; }
    button.send:hover { background: #0369a1; }
  </style>
</head>
<body>
  <header>