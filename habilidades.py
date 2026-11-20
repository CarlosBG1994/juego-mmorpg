# --- BANCO MAESTRO DE 1.870 HABILIDADES CONFIGURADAS (habilidades.py) ---

PREFIJOS_ELEMENTO = [
    ("Ígneo", "🔥", "fire", "#f97316"),
    ("Glacial", "❄️", "pulse", "#38bdf8"),
    ("Voltaico", "⚡", "lightning", "#facc15"),
    ("Marcial", "⚔️", "slash", "#e2e8f0"),
    ("Sísmico", "💥", "pulse", "#d97706"),
    ("Arcano", "🌀", "pulse", "#a855f7"),
    ("Umbrío", "🌑", "slash", "#64748b"),
    ("Sagrado", "✨", "shield", "#fde047"),
    ("Dracónico", "🐉", "fire", "#ef4444"),
    ("Tempestuoso", "🌪️", "lightning", "#22d3ee"),
    ("Espectral", "👻", "pulse", "#94a3b8"),
    ("Titánico", "🛡️", "shield", "#3b82f6"),
]

FORMAS_TECNICA = [
    "Impacto", "Onda", "Ráfaga", "Estallido", "Pulso", "Tajo", "Lanza",
    "Torbellino", "Égida", "Sello", "Furia", "Rugido", "Cascada", "Choque",
    "Destello", "Vórtice", "Golpe", "Descarga", "Muralla", "Juicio",
    "Eco", "Fulgor", "Garra", "Espiral", "Colisión", "Ascensión",
    "Devastación", "Prisión", "Aliento", "Cuchilla"
]

TIERS = [
    ("Tier I", 1.0, 30),
    ("Tier II", 1.35, 40),
    ("Tier III", 1.75, 55),
    ("Tier IV", 2.25, 75),
    ("Tier V", 3.0, 95),
]

MITICAS_BASE = [
    "Sol Invictus", "Aliento del Leviatán", "Juicio del Eón", "Rugido del Dragón Primigenio",
    "Égida del Monarca Caído", "Pulso del Coloso", "Canto de las Sirenas", "Fénix Inmortal",
    "Distorsión Temporal", "Voluntad del Creador"
]


def generar_catalogo_1870_habilidades():
    """
    Genera exactamente 1.870 habilidades configuradas y deterministas:
    - 1.800 habilidades estándar (12 elementos x 30 técnicas x 5 Tiers)
    - 70 habilidades míticas (10 arquetipos míticos x 7 rangos de maestría)
    """
    catalogo = {}

    # 1. 1.800 habilidades de Tier I a Tier V
    contador = 1
    for tier_nombre, mult_dano, cd_base in TIERS:
        for elem_nombre, icono, efecto_visual, color in PREFIJOS_ELEMENTO:
            for forma in FORMAS_TECNICA:
                skill_id = f"skill_{contador:04d}"
                es_escudo = forma in ("Égida", "Muralla", "Sello")
                dano = 0 if es_escudo else int(45 * mult_dano)
                radio = 40 if es_escudo else int(85 + (mult_dano * 25))
                catalogo[skill_id] = {
                    "id": skill_id,
                    "numero": contador,
                    "nombre": f"[{tier_nombre}] {forma} {elem_nombre}",
                    "categoria": tier_nombre,
                    "elemento": elem_nombre,
                    "icono": "🛡️" if es_escudo else icono,
                    "tipo": "defensa" if es_escudo else "ofensiva",
                    "dano": dano,
                    "radio": radio,
                    "cooldown": cd_base,
                    "duracion_escudo": int(80 * mult_dano) if es_escudo else 0,
                    "efecto_visual": "shield" if es_escudo else efecto_visual,
                    "color": color,
                }
                contador += 1

    # 2. 70 habilidades Míticas (1801 a 1870)
    for m_base in MITICAS_BASE:
        for grado in range(1, 8):
            skill_id = f"skill_{contador:04d}"
            catalogo[skill_id] = {
                "id": skill_id,
                "numero": contador,
                "nombre": f"[MÍTICA - Grado {grado}] {m_base}",
                "categoria": "Mítica",
                "elemento": "Primordial",
                "icono": "👑",
                "tipo": "mitica",
                "dano": 180 + (grado * 45),
                "radio": 160 + (grado * 15),
                "cooldown": 110,
                "duracion_escudo": 0,
                "efecto_visual": "pulse",
                "color": "#facc15",
            }
            contador += 1

    return catalogo


CATALOGO_HABILIDADES = generar_catalogo_1870_habilidades()

BARRA_HABILIDADES_DEFECTO = {
    "1": "skill_0091",  # [Tier I] Impacto Marcial
    "2": "skill_0001",  # [Tier I] Impacto Ígneo
    "3": "skill_0219",  # [Tier I] Égida Sagrada
    "4": "skill_0078",  # [Tier I] Descarga Voltaica
    "q": "skill_1801",  # [MÍTICA - Grado 1] Sol Invictus
}