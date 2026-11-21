import datetime
import http.server
import json
import os
import re
import shutil
import socketserver
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

    contents = []
    for m in mensajes:
        rol = "user" if m["role"] == "user" else "model"
        contents.append({"role": rol, "parts": [{"text": m["content"]}]})

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": contents,
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    partes = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    texto = "".join(p.get("text", "") for p in partes if "text" in p).strip()
    return texto or "No se recibio respuesta de texto."


def extraer_bloques_archivo(respuesta: str) -> list[tuple[str, str]]:
    """
    Permite que el Agente 0 cree varios archivos de modulo a la vez si se le pide:
    ```archivo:modulos/ejemplo.py
    ...codigo...
    ```
    """
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
        return f"""
Eres {info.get('nombre')} para el juego Snd-Worlds.
Habla en espanol claro, cercano y sin jerga innecesaria. El usuario no quiere revisar codigo a mano ni perder cosas que ya existen.

{REGLAS_SND_WORLDS}

AGENTES Y MODULOS REGISTRADOS ACTUALMENTE:
{modulos_resumen}

LECTURA COMPLETA DE LO QUE HAY AHORA MISMO:
{panoramica}

TU MISION:
1. Analiza todo lo que ya existe en el proyecto y en juego_explicado.txt.
2. Cuando el usuario pida crear modulos o generar agentes (o que crees lo que ya existe para ir haciendo modificaciones):
   - Por cada agente/modulo nuevo que debas activar, incluye un bloque:
```nuevo_modulo
{{
  "id": "nombre_en_minusculas_sin_espacios",
  "nombre": "Agente · Nombre del Modulo",
  "rol": "Que hace este modulo y que modifica",
  "archivo": "modulos/nombre_en_minusculas_sin_espacios.py"
}}