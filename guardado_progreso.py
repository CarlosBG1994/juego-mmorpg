import json
from pathlib import Path
from typing import Any

RUTA_GUARDADOS = Path(__file__).resolve().parent.parent / "datos_jugadores"


class GestorProgresoJugador:
    """Guarda y carga el estado completo de cada jugador en formato JSON."""

    def __init__(self, carpeta_guardados: Path = RUTA_GUARDADOS):
        self.carpeta_guardados = Path(carpeta_guardados)
        self.carpeta_guardados.mkdir(parents=True, exist_ok=True)

    def _ruta_jugador(self, jugador_id: str) -> Path:
        limpio = "".join(c if c.isalnum() or c in ("_", "-") else "_" for c in jugador_id.strip())
        return self.carpeta_guardados / f"{limpio or 'jugador'}.json"

    def guardar_progreso(self, jugador_id: str, datos: dict[str, Any]) -> Path:
        ruta = self._ruta_jugador(jugador_id)
        payload = {
            "jugador_id": jugador_id,
            "progreso": datos,
        }
        ruta.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return ruta

    def cargar_progreso(self, jugador_id: str) -> dict[str, Any] | None:
        ruta = self._ruta_jugador(jugador_id)
        if not ruta.exists():
            return None
        contenido = json.loads(ruta.read_text(encoding="utf-8"))
        return contenido.get("progreso")