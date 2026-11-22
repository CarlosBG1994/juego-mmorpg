import ast
import importlib.util
import re
import shutil
from pathlib import Path

BASE_DIR = Path("/workspaces/juego-mmorpg")
APP_FILE = BASE_DIR / "app.py"
MODULOS_DIR = BASE_DIR / "modulos"

START_MARKER = "# === AUTO-MODULOS START ==="
END_MARKER = "# === AUTO-MODULOS END ==="


def listar_modulos_validos() -> list[str]:
    if not MODULOS_DIR.exists():
        return []
    nombres = []
    for ruta in sorted(MODULOS_DIR.glob("*.py")):
        if ruta.name.startswith("__"):
            continue
        nombres.append(ruta.stem)
    return nombres


def probar_import_modulo(nombre: str) -> tuple[bool, str]:
    ruta = MODULOS_DIR / f"{nombre}.py""
            )
        else:
            lineas_imports.append(
                f"_mod_{m} = None  # Revisar error: {estados.get(m, ('', ''))[1]}"
            )

    diccionario_items = ",\n    ".join(f'"{m}": _mod_{m}' for m in modulos)
    cuerpo_imports = "\n".join(lineas_imports) if lineas_imports else "pass"

    return (
        f"{START_MARKER}\n"
        f"{cuerpo_imports}\n\n"
        f"MODULOS_CARGADOS = {{\n"
        f"    {diccionario_items}\n"
        f"}}\n"
        f"{END_MARKER}"
    )


def sincronizar_app():
    if not APP_FILE.exists():
        print(f"No existe {APP_FILE}")
        return

    modulos = listar_modulos_validos()
    estados = {m: probar_import_modulo(m) for m in modulos}

    for m in modulos:
        ok, info = estados[m]
        print(f"[MODULO] {m}.py -> {info}" if ok else f"[MODULO / AVISO] {m}.py -> {info}")

    shutil.copy2(APP_FILE, APP_FILE.with_suffix(".py.bak"))
    codigo_actual = APP_FILE.read_text(encoding="utf-8")
    bloque_nuevo = construir_bloque(modulos, estados)

    if START_MARKER in codigo_actual and END_MARKER in codigo_actual:
        patron = re.compile(
            rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
            re.DOTALL,
        )
        nuevo_codigo = patron.sub(bloque_nuevo, codigo_actual)
    else:
        nuevo_codigo = f"{codigo_actual.rstrip()}\n\n{bloque_nuevo}\n"

    APP_FILE.write_text(nuevo_codigo, encoding="utf-8")

    try:
        ast.parse(nuevo_codigo, filename=str(APP_FILE))
        print(f"[APP SYNC] {APP_FILE.name} actualizado correctamente ({len(modulos)} módulos).")
    except SyntaxError as exc:
        print(f"[APP SYNC / ERROR SINTAXIS] Línea {exc.lineno}: {exc.msg}")


if __name__ == "__main__":
    sincronizar_app()
