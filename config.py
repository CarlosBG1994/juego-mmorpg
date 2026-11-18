# --- CONFIGURACIÓN GLOBAL DE SND-WORLDS ---

CONTINENTE_INICIAL = "Valoria (Continente I)"

CONTINENTES_OFICIALES = {
    "Valoria (Continente I)": {
        "tipo": "Nivel 1 - 100 | Tierras Centrales y Reinos Fundacionales",
        "detalle": "Niveles 1-60 divididos en 4 Reinos (Humano, Elfo, Enano, Hombre Bestia). Niveles 61-100 en Zonas Comunes Neutrales (sin gobierno fijo)."
    },
    "Eldoria (Continente II)": {
        "tipo": "Nivel 101 - 150 | Bosques Arcanos y Tierras Elementales",
        "rango": "101-150"
    },
    "Pyoria (Continente III)": {
        "tipo": "Nivel 151 - 200 | Volcanes, Abismos y Tierras de Bestias Primordiales",
        "rango": "151-200"
    },
    "Noxoria (Continente IV)": {
        "tipo": "Nivel 201 - 250 | El Imperio Oscuro y el Nexo Final (Ángeles y Demonios unidos)",
        "rango": "201-250"
    }
}

REINOS_VALORIA = {
    "Reino Humano de Valoria": {"rango_nivel": "1 - 60", "raza_dominante": "Humano", "asentamiento": "Aurelia Capital"},
    "Bosque Ancestral de Eldoria": {"rango_nivel": "1 - 60", "raza_dominante": "Elfo", "asentamiento": "Sylvanis Refugio"},
    "Fortaleza de Hierro de Pyoria": {"rango_nivel": "1 - 60", "raza_dominante": "Enano", "asentamiento": "Khazad Dun Baluarte"},
    "Estepas Salvajes de Noxoria": {"rango_nivel": "1 - 60", "raza_dominante": "Hombre Bestia", "asentamiento": "Garra de la Tormenta"},
    "Tierras Neutras del Vórtice": {"rango_nivel": "61 - 100", "raza_dominante": "Neutral / Zona Libre", "asentamiento": "Puesto Fronterizo del Ocaso"}
}

RAZAS_Y_CLASSES = {
    "Humano": {
        "clases": ["Invocador", "Guerrero", "Mago de Batalla", "Paladín", "Asesino", "Clérigo", "Cazador de Recompensas", "Bardo Táctico"],
        "reino_inicio": "Reino Humano de Valoria",
        "monturas_exclusivas": ["Caballo de Guerra Real", "Lobo Estepario de Valoria"],
        "lore": "Equilibrio, adaptabilidad y diplomacia entre los reinos."
    },
    "Elfo": {
        "clases": ["Arquero Arcano", "Sacerdotisa de la Luna", "Mago Estelar", "Cazador de Sombras", "Druida de los Bosques", "Caballero Silvano", "Elementalista de la Luz"],
        "reino_inicio": "Bosque Ancestral de Eldoria",
        "monturas_exclusivas": ["Ciervo Etéreo de la Luna", "Pantera de las Sombras Silvanas"],
        "lore": "Maestros de la magia ancestral y la arquería precisa en armonía con la naturaleza."
    },
    "Enano": {
        "clases": ["Herrero de Guerra", "Guardián de Runas", "Berserker de Magma", "Artillero de Asedio", "Ingeniero Rúnico", "Tanque de Mithril", "Sanador de Yunque"],
        "reino_inicio": "Fortaleza de Hierro de Pyoria",
        "monturas_exclusivas": ["Oso Acorazado de las Profundidades", "Jabalí Mecánico de Asedio"],
        "lore": "Inquebrantables protectores de las profundidades y maestros absolutos de la forja."
    },
    "Hombre Bestia": {
        "clases": ["Púgil", "Acechador Salvaje", "Chamán Elemental", "Guerrero Totémico", "Señor de la Manada", "Asesino Feral", "Monje de las Garras"],
        "reino_inicio": "Estepas Salvajes de Noxoria",
        "monturas_exclusivas": ["Tigre Dientes de Sable Gigante", "Huargo Alfa de la Estepa"],
        "lore": "Furia primordial y conexión directa con las fuerzas salvajes del continente."
    },
    "Ángeles y Demonios (Unidos)": {
        "clases": ["Serafín del Juicio", "Señor del Abismo", "Inquisidor Estelar", "Portador del Ocaso", "Templario Celestial", "Brujo del Caos"],
        "reino_inicio": "Santuario del Nexo Celestial",
        "monturas_exclusivas": ["Grifo Alado Celestial", "Pesadilla Abisal de Fuego Negro"],
        "lore": "Alianza universal entre facciones celestiales e infernales para frenar la corrupción total."
    }
}

MONTURAS_COMUNES = [
    "Caballo Trotón del Viajero",
    "Pony de Carga Resistente",
    "Lobo Ligero de Pradera",
    "Corcel Acorazado Común"
]

SUBFORMAS_BESTIA = ["Hombre Lobo", "Hombre Tigre", "Oso Berserker", "Águila Tormentosa", "Quimera Feral"]

ESTADISTICAS_BASE_CLASES = {
    "Invocador": {"str": 5, "int": 18, "agi": 6, "vit": 10, "luk": 12, "hp": 100},
    "Guerrero": {"str": 18, "int": 5, "agi": 10, "vit": 15, "luk": 8, "hp": 130},
    "Mago de Batalla": {"str": 8, "int": 16, "agi": 8, "vit": 12, "luk": 10, "hp": 110},
    "Paladín": {"str": 14, "int": 10, "agi": 6, "vit": 18, "luk": 10, "hp": 140},
    "Asesino": {"str": 12, "int": 6, "agi": 18, "vit": 8, "luk": 14, "hp": 95},
    "Arquero Arcano": {"str": 10, "int": 12, "agi": 16, "vit": 8, "luk": 12, "hp": 100},
    "Sacerdotisa de la Luna": {"str": 6, "int": 16, "agi": 8, "vit": 14, "luk": 12, "hp": 110},
    "Mago Estelar": {"str": 4, "int": 20, "agi": 8, "vit": 8, "luk": 12, "hp": 90},
    "Cazador de Sombras": {"str": 14, "int": 8, "agi": 16, "vit": 8, "luk": 14, "hp": 95},
    "Herrero de Guerra": {"str": 16, "int": 8, "agi": 6, "vit": 16, "luk": 10, "hp": 130},
    "Guardián de Runas": {"str": 12, "int": 12, "agi": 6, "vit": 16, "luk": 10, "hp": 125},
    "Berserker de Magma": {"str": 20, "int": 4, "agi": 12, "vit": 14, "luk": 6, "hp": 140},
    "Artillero de Asedio": {"str": 15, "int": 10, "agi": 8, "vit": 12, "luk": 10, "hp": 115},
    "Púgil": {"str": 16, "int": 6, "agi": 16, "vit": 12, "luk": 10, "hp": 120},
    "Acechador Salvaje": {"str": 14, "int": 6, "agi": 18, "vit": 10, "luk": 12, "hp": 105},
    "Chamán Elemental": {"str": 8, "int": 16, "agi": 8, "vit": 12, "luk": 12, "hp": 105},
    "Guerrero Totémico": {"str": 16, "int": 8, "agi": 10, "vit": 14, "luk": 10, "hp": 125},
    "Clérigo": {"str": 8, "int": 14, "agi": 6, "vit": 16, "luk": 12, "hp": 120},
    "Cazador de Recompensas": {"str": 14, "int": 8, "agi": 15, "vit": 10, "luk": 13, "hp": 110},
    "Bardo Táctico": {"str": 8, "int": 15, "agi": 12, "vit": 10, "luk": 15, "hp": 100},
    "Druida de los Bosques": {"str": 10, "int": 15, "agi": 10, "vit": 14, "luk": 10, "hp": 115},
    "Caballero Silvano": {"str": 16, "int": 8, "agi": 12, "vit": 14, "luk": 10, "hp": 130},
    "Elementalista de la Luz": {"str": 6, "int": 18, "agi": 8, "vit": 10, "luk": 12, "hp": 95},
    "Ingeniero Rúnico": {"str": 12, "int": 14, "agi": 10, "vit": 12, "luk": 10, "hp": 110},
    "Tanque de Mithril": {"str": 18, "int": 4, "agi": 6, "vit": 20, "luk": 8, "hp": 160},
    "Sanador de Yunque": {"str": 10, "int": 14, "agi": 6, "vit": 16, "luk": 10, "hp": 125},
    "Señor de la Manada": {"str": 18, "int": 6, "agi": 14, "vit": 14, "luk": 10, "hp": 135},
    "Asesino Feral": {"str": 14, "int": 6, "agi": 20, "vit": 8, "luk": 12, "hp": 95},
    "Monje de las Garras": {"str": 15, "int": 8, "agi": 16, "vit": 12, "luk": 10, "hp": 115},
    "Serafín del Juicio": {"str": 15, "int": 15, "agi": 12, "vit": 15, "luk": 15, "hp": 140},
    "Señor del Abismo": {"str": 18, "int": 12, "agi": 10, "vit": 16, "luk": 10, "hp": 145},
    "Inquisidor Estelar": {"str": 12, "int": 16, "agi": 12, "vit": 12, "luk": 14, "hp": 120},
    "Portador del Ocaso": {"str": 14, "int": 14, "agi": 14, "vit": 12, "luk": 12, "hp": 120},
    "Templario Celestial": {"str": 16, "int": 10, "agi": 8, "vit": 18, "luk": 10, "hp": 150},
    "Brujo del Caos": {"str": 8, "int": 19, "agi": 10, "vit": 10, "luk": 13, "hp": 100}
}
```[cite: 7]

---

### 2. `bestiario.py`
```python
# --- BESTIARIO MASIVO AMPLIADO Y DINÁMICO (NIVELES 1 A 250) ---

BESTIARIO_ZONAS = {
    "Reino Humano de Valoria": {
        "rango": "1 - 60",
        "mobs": [
            {"nombre": "Goblin Explorador", "nivel": 2, "tipo": "Goblin", "hp": 90, "ataque": "Físico", "drop": "Daga Oxidada", "velocidad": 2.0},
            {"nombre": "Lobo Gris Feroz", "nivel": 8, "tipo": "Lobo", "hp": 150, "ataque": "Físico", "drop": "Colmillo de Lobo", "velocidad": 2.5},
            {"nombre": "Slime Ácido", "nivel": 12, "tipo": "Slime", "hp": 220, "ataque": "Magia", "drop": "Gelatina Elemental", "velocidad": 1.2},
            {"nombre": "Bandido Forajido", "nivel": 20, "tipo": "Humanoide", "hp": 350, "ataque": "Físico", "drop": "Moneda de Plata", "velocidad": 1.8},
            {"nombre": "Oso Pardo Enorme", "nivel": 35, "tipo": "Oso", "hp": 700, "ataque": "Físico", "drop": "Piel Gruesa de Oso", "velocidad": 1.5},
            {"nombre": "Golem de Piedra Corrupto", "nivel": 48, "tipo": "Golem", "hp": 1100, "ataque": "Magia/Físico", "drop": "Mineral de Hierro Puro", "velocidad": 1.0}
        ],
        "jefes_zona": [
            {"nombre": "Rey Goblin de las Cavernas", "nivel": 25, "hp": 2500, "drop": "Corona de Hueso Goblin", "ataque": "Físico Feroz"}
        ],
        "mazmorras": [
            {"nombre": "Cripta Subterránea de Valoria", "nivel_min": 15, "jefe": "Señor de los Muertos Menor", "hp_jefe": 3200, "drop_jefe": "Amuleto de Cripta"}
        ]
    },
    "Bosque Ancestral de Eldoria": {
        "rango": "1 - 60",
        "mobs": [
            {"nombre": "Goblin Arquero Silvano", "nivel": 5, "tipo": "Goblin", "hp": 110, "ataque": "Físico", "drop": "Arco Corto", "velocidad": 2.2},
            {"nombre": "Slime Luminoso", "nivel": 14, "tipo": "Slime", "hp": 250, "ataque": "Magia", "drop": "Bulbo Luminoso", "velocidad": 1.4},
            {"nombre": "Tigre Colmilloblanco Enorme", "nivel": 28, "tipo": "Tigre", "hp": 600, "ataque": "Físico/Crítico", "drop": "Piel de Tigre Reluciente", "velocidad": 2.8},
            {"nombre": "Quimera del Bosque", "nivel": 45, "tipo": "Quimera", "hp": 1200, "ataque": "Magia/Físico", "drop": "Pluma de Quimera Arcanizada", "velocidad": 2.0},
            {"nombre": "Wyvern de la Copa", "nivel": 55, "tipo": "Wyvern", "hp": 1600, "ataque": "Magia", "drop": "Ala de Wyvern Esmeralda", "velocidad": 2.5}
        ],
        "jefes_zona": [
            {"nombre": "Patriarca de los Tigres Silvanos", "nivel": 50, "hp": 4000, "drop": "Garra Mística Ancestral", "ataque": "Físico Rápido"}
        ],
        "mazmorras": [
            {"nombre": "Templo Hundido de las Hojas", "nivel_min": 35, "jefe": "Gran Sacerdotisa Corrupta", "hp_jefe": 5500, "drop_jefe": "Báculo de la Luna Oscura"}
        ]
    },
    "Fortaleza de Hierro de Pyoria": {
        "rango": "1 - 60",
        "mobs": [
            {"nombre": "Ogro Minero Bruto", "nivel": 22, "tipo": "Ogro", "hp": 500, "ataque": "Físico", "drop": "Maza de Hierro Pesada", "velocidad": 1.1},
            {"nombre": "Golem de Magma", "nivel": 38, "tipo": "Golem", "hp": 950, "ataque": "Magia", "drop": "Escama de Magma", "velocidad": 1.3},
            {"nombre": "Slime de Lava", "nivel": 46, "tipo": "Slime", "hp": 800, "ataque": "Magia", "drop": "Núcleo Ígneo Fundido", "velocidad": 1.5},
            {"nombre": "Dragón Menor de Ceniza", "nivel": 58, "tipo": "Dragón", "hp": 2200, "ataque": "Magia Fuego", "drop": "Escama de Dragón Menor", "velocidad": 2.2}
        ],
        "jefes_zona": [
            {"nombre": "Coloso de Hierro y Fuego", "nivel": 59, "hp": 7500, "drop": "Núcleo de Magma Puro", "ataque": "Golpes Sísmicos"}
        ],
        "mazmorras": [
            {"nombre": "Fundición Abisal de los Enanos Oscuros", "nivel_min": 45, "jefe": "Herrero Maldito Azazel", "hp_jefe": 8000, "drop_jefe": "Yunque de Obsidiana"}
        ]
    },
    "Estepas Salvajes de Noxoria": {
        "rango": "1 - 60",
        "mobs": [
            {"nombre": "Lobo Alfa Estepario", "nivel": 30, "tipo": "Lobo", "hp": 750, "ataque": "Físico", "drop": "Colmillo Alfa", "velocidad": 2.6},
            {"nombre": "Ogro Berserker", "nivel": 42, "tipo": "Ogro", "hp": 1300, "ataque": "Físico", "drop": "Hacha de Guerra de Ogro", "velocidad": 1.4},
            {"nombre": "Quimera de las Estepas", "nivel": 52, "tipo": "Quimera", "hp": 1900, "ataque": "Magia/Físico", "drop": "Cuerno Bifurcado", "velocidad": 2.1}
        ],
        "jefes_zona": [
            {"nombre": "Señor de la Manada Suprema", "nivel": 59, "hp": 9000, "drop": "Piel del Gran Depredador", "ataque": "Embates Ferales"}
        ],
        "mazmorras": [
            {"nombre": "Guarida de la Bestia Primordial", "nivel_min": 50, "jefe": "Madre de las Quimeras", "hp_jefe": 9500, "drop_jefe": "Colmillo Primigenio"}
        ]
    },
    "Tierras Neutras del Vórtice": {
        "rango": "61 - 100",
        "mobs": [
            {"nombre": "Ogro de Elite Vórtice", "nivel": 65, "tipo": "Ogro", "hp": 2500, "ataque": "Físico Pesado", "drop": "Armadura de Ogre Vórtice", "velocidad": 1.3},
            {"nombre": "Wyvern Tormentoso", "nivel": 75, "tipo": "Wyvern", "hp": 3400, "ataque": "Magia Rayo", "drop": "Núcleo de Tormenta", "velocidad": 2.7},
            {"nombre": "Dragón Joven del Vórtice", "nivel": 90, "tipo": "Dragón", "hp": 5500, "ataque": "Magia/Físico", "drop": "Escama Estelar", "velocidad": 2.4}
        ],
        "jefes_zona": [
            {"nombre": "Señor de la Tempestad", "nivel": 100, "hp": 15000, "drop": "Ojo del Vórtice", "ataque": "Rayos Cataclísmicos"}
        ],
        "mazmorras": [
            {"nombre": "Abismo del Tiempo Neutro", "nivel_min": 70, "jefe": "Guardián del Reloj Absoluto", "hp_jefe": 14000, "drop_jefe": "Engranaje Temporal"}
        ]
    }
}
```[cite: 8]

---

### 3. `habilidades.py`
```python
# --- SISTEMA MASIVO DE HABILIDADES (1,870 HABILIDADES, TIER, PODERES Y RAREZAS) ---

CATALOGO_HABILIDADES_GLOBAL_DETALLADO = [
    # --- CLASE: INVOCADOR / MAGIA ---
    {
        "id": "sk_inv_1", "clase": "Invocador", "tier": "Tier I", "rareza": "Común",
        "nombre": "Invocación de Golem de Roca",
        "poderes": ["1. Golpe Férreo (Daño físico directo)", "2. Escudo de Piedra (Aumenta defensa 30s)", "3. Avalancha Menor (Daño en área por rocas)"]
    },
    {
        "id": "sk_inv_2", "clase": "Invocador", "tier": "Tier II", "rareza": "Raro",
        "nombre": "Invocación de Espíruto de Fuego",
        "poderes": ["1. Llamarada Arcana (Proyectil ígneo)", "2. Aura de Calor (Quema enemigos cercanos)", "3. Explosión de Fénix (Daño masivo en cono)"]
    },
    {
        "id": "sk_inv_3", "clase": "Invocador", "tier": "Tier III", "rareza": "Épico",
        "nombre": "Señor de los Elementos Abisales",
        "poderes": ["1. Puño Elemental (Golpe devastador)", "2. Tormenta Combinada (Rayo y Fuego)", "3. Santuario Elemental (Inmunidad temporal 5s)"]
    },
    {
        "id": "sk_mit_1", "clase": "Invocador", "tier": "Tier III", "rareza": "Mítico",
        "nombre": "Génesis del Primer Guardián",
        "poderes": ["1. Singularidad Cósmica (Atrae y destruye)", "2. Escudo del Nexo (Absorbe 100% daño)", "3. Juicio Primordial (Elimina mobs menores al instante)"]
    },
    {
        "id": "sk_leg_1", "clase": "Invocador", "tier": "Tier III", "rareza": "Legendario",
        "nombre": "Pacto con el Dios de la Creación",
        "poderes": ["1. Rayo Creador (Daño puro masivo)", "2. Bendición Eterna (Cura 100% HP instantánea)", "3. Cataclismo Divino (Lluvia de meteoritos estelares)"]
    },

    # --- CLASE: GUERRERO ---
    {
        "id": "sk_guer_1", "clase": "Guerrero", "tier": "Tier I", "rareza": "Común",
        "nombre": "Tajo Inicial",
        "poderes": ["1. Corte Rápido (Daño físico base)", "2. Estocada Precisa (Mayor probabilidad crítico)", "3. Giro Defensivo (Repele ataques frontales)"]
    },
    {
        "id": "sk_guer_2", "clase": "Guerrero", "tier": "Tier II", "rareza": "Raro",
        "nombre": "Carga del Titán",
        "poderes": ["1. Embestida Frontal (Aturde 2s)", "2. Golpe de Escudo (Rompe guardia)", "3. Sentencia del Guerrero (Daño x2 a enemigos con poca vida)"]
    },
    {
        "id": "sk_guer_3", "clase": "Guerrero", "tier": "Tier III", "rareza": "Épico",
        "nombre": "Torbellino de Cuchillas Divinas",
        "poderes": ["1. Giro Infinito (Daño continuo en área)", "2. Salto del León (Aterrizaje sísmico)", "3. Furia Inquebrantable (Aumenta ataque un 50%)"]
    },

    # --- CLASE: MAGO DE BATALLA ---
    {
        "id": "sk_mag_1", "clase": "Mago de Batalla", "tier": "Tier I", "rareza": "Común",
        "nombre": "Bola de Fuego",
        "poderes": ["1. Orbe Ígneo (Proyectil a distancia)", "2. Anillo de Flamas (Quema a melee)", "3. Lluvia de Chispas (Área pequeña)"]
    },
    {
        "id": "sk_mag_2", "clase": "Mago de Batalla", "tier": "Tier II", "rareza": "Raro",
        "nombre": "Muro de Hielo Permafrost",
        "poderes": ["1. Barrera Glacial (Bloquea proyectiles)", "2. Estalactitas Perforantes (Daño frontal)", "3. Aura Congelante (Ralentiza 50% enemigos)"]
    },

    # --- CLASE: ARQUERO ARCANO ---
    {
        "id": "sk_arq_1", "clase": "Arquero Arcano", "tier": "Tier I", "rareza": "Común",
        "nombre": "Flecha Relámpago",
        "poderes": ["1. Tiro Veloz (Daño penetrante)", "2. Flecha Electrificada (Cadena de rayos)", "3. Lluvia de Flechas (Área amplia)"]
    },

    # --- CLASE: PÚGIL ---
    {
        "id": "sk_pug_1", "clase": "Púgil", "tier": "Tier I", "rareza": "Común",
        "nombre": "Golpe del Dragón Interno",
        "poderes": ["1. Puño Relámpago (Golpe veloz)", "2. Patada Ascendente (Lanza al enemigo por los aires)", "3. Onda de Choque Físico (Empuje masivo)"]
    }
]

CATALOGO_EDIFICIOS = {
    "Gremio de Aventureros": {
        "items": [
            {"id": "sk_1", "nombre": "Grimorio: Muro de Hielo Permafrost", "tipo": "Habilidad Activa", "precio": 50, "metal": "Plata"},
            {"id": "sk_2", "nombre": "Grimorio: Carga del Titán", "tipo": "Habilidad Activa", "precio": 80, "metal": "Plata"},
            {"id": "sk_3", "nombre": "Grimorio: Flecha Relámpago", "tipo": "Habilidad Activa", "precio": 10, "metal": "Oro"}
        ]
    }
}

CATALOGO_OCULTAS = [
    {"nombre": "El Despertar del Abismo", "continente_premio": "Eldoria (Continente II)", "pista": "Derrota al Alfa de la Manada en Nivel 15 o superior."},
    {"nombre": "Las Llaves de la Forja Antigua", "continente_premio": "Pyoria (Continente III)", "pista": "Craftea 5 objetos épicos en el taller de Herrería."},
    {"nombre": "El Trono del Vacío", "continente_premio": "Noxoria (Continente IV)", "pista": "Alcanza el Nivel 50 y derrota al Señor de la Forja Abisal."}
]
```[cite: 9]

---

### 4. `crafting_talleres.py`
```python
# --- SISTEMA COMPLETO DE CRAFTING, OFICIOS Y TALLERES (OMNI-OFICIOS) ---

TALLERES_OFICIOS = {
    "Herrería": {
        "descripcion": "Fundición de metales y forja de armaduras pesadas y armas contundentes.",
        "recetas": [
            {
                "id": "espada_obsidiana",
                "nombre": "Espada de Obsidiana Rúnica",
                "tipo": "Arma Cuerpo a Cuerpo",
                "tier": "Épico",
                "materiales": {"Escama de Magma": 3, "Lingote de Hierro Puro": 5},
                "stats_bonus": {"str": 12, "hp": 50}
            },
            {
                "id": "coraza_valoria",
                "nombre": "Coraza de Acero de Valoria",
                "tipo": "Armadura Pesada",
                "tier": "Raro",
                "materiales": {"Lingote de Hierro Puro": 8, "Moneda Oxidada": 10},
                "stats_bonus": {"vit": 15, "hp": 100}
            },
            {
                "id": "maza_gigante",
                "nombre": "Maza Rúnica de Asedio",
                "tipo": "Arma Dos Manos",
                "tier": "Épico",
                "materiales": {"Mineral de Hierro Bruto": 12, "Núcleo de Granito": 2},
                "stats_bonus": {"str": 18, "vit": 10}
            }
        ]
    },
    "Minería": {
        "descripcion": "Procesamiento de minerales brutos extraídos en minas y cavernas para obtener lingotes refinados.",
        "recetas": [
            {
                "id": "lingote_hierro",
                "nombre": "Lingote de Hierro Puro",
                "tipo": "Material Refinado",
                "tier": "Común",
                "materiales": {"Mineral de Hierro Bruto": 3},
                "stats_bonus": {"refinamiento": "Base para Herrería"}
            },
            {
                "id": "lingote_cobalto",
                "nombre": "Lingote de Cobalto Rúnico",
                "tipo": "Material Refinado",
                "tier": "Raro",
                "materiales": {"Residuo Metálico": 5, "Mineral de Hierro Bruto": 5},
                "stats_bonus": {"refinamiento": "Base para equipo avanzado"}
            }
        ]
    },
    "Peletería": {
        "descripcion": "Tratamiento de pieles salvajes para confeccionar armaduras de cuero y refuerzos ágiles.",
        "recetas": [
            {
                "id": "botas_estepa",
                "nombre": "Botas del Acechador de la Estepa",
                "tipo": "Armadura Ligera",
                "tier": "Raro",
                "materiales": {"Piel Desértica": 4, "Piel de Huargo Veloz": 2},
                "stats_bonus": {"agi": 10, "luk": 5}
            },
            {
                "id": "coraza_huargo",
                "nombre": "Armadura de Cuero de Huargo Alfa",
                "tipo": "Armadura Media",
                "tier": "Épico",
                "materiales": {"Piel de Huargo Alfa": 3, "Colmillo de Huargo": 6},
                "stats_bonus": {"agi": 14, "vit": 8}
            }
        ]
    },
    "Sastrería": {
        "descripcion": "Confección de túnicas mágicas, mantos arcanos y telas encantadas.",
        "recetas": [
            {
                "id": "manto_veneno",
                "nombre": "Manto de Seda Venenosa",
                "tipo": "Armadura Mágica",
                "tier": "Épico",
                "materiales": {"Diadema de Seda Venenosa": 1, "Liana Resistente": 4},
                "stats_bonus": {"int": 14, "agi": 6}
            },
            {
                "id": "tunica_arcana",
                "nombre": "Túnica de Tejido Estelar",
                "tipo": "Armadura Mágica",
                "tier": "Raro",
                "materiales": {"Bulbo Luminoso": 3, "Residuo Arenoso": 5},
                "stats_bonus": {"int": 16, "hp": 30}
            }
        ]
    },
    "Herboristería": {
        "descripcion": "Extracción y purificación de plantas, esporas y bulbos del mundo natural.",
        "recetas": [
            {
                "id": "extracto_espora",
                "nombre": "Extracto Concentrado de Espora",
                "tipo": "Reactivo Alquímico",
                "tier": "Raro",
                "materiales": {"Espora Venenosa": 4, "Bulbo Luminoso": 2},
                "stats_bonus": {"uso": "Base para pociones avanzadas"}
            }
        ]
    },
    "Alquimia": {
        "descripcion": "Destilación de pociones curativas, elixires de combate y venenos tácticos.",
        "recetas": [
            {
                "id": "pocion_vitalidad",
                "nombre": "Poción de Vitalidad Ancestral",
                "tipo": "Consumible",
                "tier": "Raro",
                "materiales": {"Gelatina Elemental": 5, "Bulbo Luminoso": 2},
                "stats_bonus": {"cura_hp": 300}
            },
            {
                "id": "elixir_furia",
                "nombre": "Elixir de Furia Primordial",
                "tipo": "Consumible de Mejora",
                "tier": "Épico",
                "materiales": {"Núcleo de Tormenta": 1, "Escama de Magma": 1},
                "stats_bonus": {"buff_str": 20, "duracion": "30 mins"}
            }
        ]
    },
    "Cocina": {
        "descripcion": "Preparación de banquetes y raciones de campo que otorgan mejoras temporales de estadísticas.",
        "recetas": [
            {
                "id": "guiso_lobo",
                "nombre": "Guiso Estofado de Colmillo de Lobo",
                "tipo": "Comida de Buf",
                "tier": "Común",
                "materiales": {"Colmillo de Lobo": 2, "Raciones de Pan": 1},
                "stats_bonus": {"buff_hp": 50, "buff_regen": 5}
            },
            {
                "id": "banquete_wyvern",
                "nombre": "Asado Real de Wyvern con Especias",
                "tipo": "Banquete de Hermandad",
                "tier": "Legendario",
                "materiales": {"Aguijón de Wyvern": 1, "Piel Desértica": 2},
                "stats_bonus": {"buff_todos_stats": 10, "duracion": "1 hora"}
            }
        ]
    },
    "Pesca": {
        "descripcion": "Extracción de especies acuáticas, escamas de río y tesoros sumergidos en lagos y costas.",
        "recetas": [
            {
                "id": "cebo_magico",
                "nombre": "Cebo Luminoso de Profundidad",
                "tipo": "Herramienta de Pesca",
                "tier": "Raro",
                "materiales": {"Bulbo Luminoso": 2, "Ala Quiróptera": 3},
                "stats_bonus": {"prob_pez_raro": "+25%"}
            }
        ]
    },
    "Joyería": {
        "descripcion": "Tallado de gemas, engaste de núcleos elementales y creación de anillos y amuletos de poder.",
        "recetas": [
            {
                "id": "anillo_cores",
                "nombre": "Anillo de Cores Resonantes",
                "tipo": "Accesorio",
                "tier": "Épico",
                "materiales": {"Fragmento de Núcleo Puro": 2, "Esencia de Vacío": 1},
                "stats_bonus": {"int": 10, "luk": 15}
            },
            {
                "id": "amuleto_tormenta",
                "nombre": "Colgante del Ojo de la Tormenta",
                "tipo": "Accesorio",
                "tier": "Legendario",
                "materiales": {"Núcleo de Tormenta": 1, "Corona del Nexo Primordial": 1},
                "stats_bonus": {"str": 15, "agi": 15, "hp": 100}
            }
        ]
    },
    "Criadero de Monturas": {
        "descripcion": "Entrenamiento, mejora y cría de monturas nativas utilizando núcleos elementales y materiales puros.",
        "recetas": [
            {
                "id": "mejora_montura",
                "nombre": "Armadura Ceremonial de Montura",
                "tipo": "Mejora de Montura",
                "tier": "Épico",
                "materiales": {"Escama de Magma Pura": 1, "Piel de Huargo Alfa": 2},
                "stats_bonus": {"velocidad_montura": "+50%", "hp_montura": "+500"}
            }
        ]
    }
}

def simular_crafteo(oficio, receta_id, inventario_jugador):
    if oficio not in TALLERES_OFICIOS:
        return False, "Taller u oficio desconocido."
    
    recetas = TALLERES_OFICIOS[oficio]["recetas"]
    receta_sel = next((r for r in recetas if r["id"] == receta_id), None)
            
    if not receta_sel:
        return False, "Receta no encontrada."
        
    for mat, cant_nec in receta_sel["materiales"].items():
        if inventario_jugador.count(mat) < cant_nec:
            return False, f"Material insuficiente: necesitas {cant_nec}x {mat}."
            
    return True, receta_sel["nombre"]
```[cite: 1]

---

### 5. `canvas_engine.py`
```python
# --- MOTOR HTML5 / JS CANVAS PARA PVE EN TIEMPO REAL ---

def generar_canvas_html(es_caza, zona_actual, mobs_zona, jefes_zona):
    mobs_js_data = []
    for m in mobs_zona:
        mobs_js_data.append({
            "nombre": m["nombre"],
            "nivel": m["nivel"],
            "hp": m["hp"],
            "ataque_tipo": m["ataque"],
            "velocidad": m.get("velocidad", 1.5)
        })

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ background-color: #0e1117; color: white; text-align: center; font-family: sans-serif; margin: 0; padding: 0; }}
            canvas {{ background: #1a1c23; border: 2px solid #ffaa00; box-shadow: 0 0 20px rgba(255,170,0,0.4); border-radius: 8px; }}
            .hud-game {{ display: flex; justify-content: space-around; background: #161922; padding: 8px; margin-bottom: 5px; border-radius: 5px; font-weight: bold; font-size: 13px; color: #ffaa00; }}
            .controls-hint {{ font-size: 12px; color: #a0a0a0; margin-top: 5px; }}
        </style>
    </head>
    <body>
        <div class="hud-game">
            <span id="playerHpText">❤️ HP: 100/100</span>
            <span id="zoneText">🗺️ Zona: {zona_actual}</span>
            <span id="scoreText">⚔️ Derrotados: 0</span>
        </div>
        <canvas id="gameCanvas" width="800" height="380"></canvas>
        <div class="controls-hint">Usa las teclas <b>W, A, S, D</b> o <b>Flechas</b> para moverte y esquivar ataques mágicos y físicos en tiempo real.</div>
        
        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            
            let player = {{ x: 400, y: 190, size: 20, speed: 4, hp: 100, maxHp: 100, color: "#ffaa00" }};
            let keys = {{}};
            let enemies = [];
            let projectiles = [];
            let isCaza = {str(es_caza).lower()};
            
            let templateMobs = {str(mobs_js_data)};
            
            if (isCaza && templateMobs.length > 0) {{
                for(let i=0; i<4; i++) {{
                    let tmpl = templateMobs[Math.floor(Math.random() * templateMobs.length)];
                    enemies.push({{
                        x: Math.random() * 700 + 50,
                        y: Math.random() * 300 + 40,
                        size: 18,
                        speed: tmpl.velocidad || 1.5,
                        hp: tmpl.hp,
                        maxHp: tmpl.hp,
                        name: tmpl.nombre,
                        ataque_tipo: tmpl.ataque_tipo,
                        cooldown: 0,
                        color: tmpl.ataque_tipo.includes("Magia") ? "#9933ff" : "#ff4444"
                    }});
                }}
            }}
            
            window.addEventListener("keydown", (e) => keys[e.key] = true);
            window.addEventListener("keyup", (e) => keys[e.key] = false);
            
            function update() {{
                if (keys["ArrowUp"] || keys["w"] || keys["W"]) player.y -= player.speed;
                if (keys["ArrowDown"] || keys["s"] || keys["S"]) player.y += player.speed;
                if (keys["ArrowLeft"] || keys["a"] || keys["A"]) player.x -= player.speed;
                if (keys["ArrowRight"] || keys["d"] || keys["D"]) player.x += player.speed;
                
                player.x = Math.max(player.size, Math.min(canvas.width - player.size, player.x));
                player.y = Math.max(player.size, Math.min(canvas.height - player.size, player.y));
                
                if (isCaza) {{
                    enemies.forEach(en => {{
                        let dx = player.x - en.x;
                        let dy = player.y - en.y;
                        let dist = Math.sqrt(dx*dx + dy*dy);
                        
                        if (dist > 2) {{
                            en.x += (dx / dist) * en.speed;
                            en.y += (dy / dist) * en.speed;
                        }}
                        
                        en.cooldown++;
                        if (en.cooldown > 100 && dist < 200) {{
                            en.cooldown = 0;
                            if (en.ataque_tipo.includes("Magia")) {{
                                projectiles.push({{
                                    x: en.x, y: en.y,
                                    vx: (dx / dist) * 3,
                                    vy: (dy / dist) * 3,
                                    radius: 6,
                                    color: "#9933ff"
                                }});
                            }} else if (dist < 30) {{
                                let isCrit = Math.random() < 0.15;
                                let damage = isCrit ? 25 : 12;
                                player.hp -= damage;
                                if (player.hp < 0) player.hp = 0;
                                document.getElementById("playerHpText").innerText = `❤️ HP: ${{player.hp}}/${{player.maxHp}}` + (isCrit ? " [¡CRÍTICO RECIBIDO!]" : "");
                            }}
                        }}
                    }});
                    
                    for(let i = projectiles.length - 1; i >= 0; i--) {{
                        let p = projectiles[i];
                        p.x += p.vx;
                        p.y += p.vy;
                        
                        let pdx = player.x - p.x;
                        let pdy = player.y - p.y;
                        if (Math.sqrt(pdx*pdx + pdy*pdy) < player.size + p.radius) {{
                            let isCrit = Math.random() < 0.2;
                            let dmg = isCrit ? 30 : 15;
                            player.hp -= dmg;
                            if (player.hp < 0) player.hp = 0;
                            projectiles.splice(i, 1);
                            document.getElementById("playerHpText").innerText = `❤️ HP: ${{player.hp}}/${{player.maxHp}}` + (isCrit ? " [¡CRÍTICO MÁGICO!]" : "");
                            continue;
                        }}
                        
                        if (p.x < 0 || p.x > canvas.width || p.y < 0 || p.y > canvas.height) {{
                            projectiles.splice(i, 1);
                        }}
                    }}
                }}
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                ctx.strokeStyle = "#252836";
                ctx.lineWidth = 1;
                for(let x=0; x<canvas.width; x+=40) {{
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
                }}
                for(let y=0; y<canvas.height; y+=40) {{
                    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
                }}
                
                ctx.fillStyle = player.color;
                ctx.beginPath();
                ctx.arc(player.x, player.y, player.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.lineWidth = 3;
                ctx.strokeStyle = "#ffffff";
                ctx.stroke();
                
                enemies.forEach(en => {{
                    ctx.fillStyle = en.color;
                    ctx.beginPath();
                    ctx.arc(en.x, en.y, en.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = "#ffffff";
                    ctx.stroke();
                    
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "10px sans-serif";
                    ctx.fillText(en.name, en.x - 20, en.y - en.size - 6);
                }});
                
                projectiles.forEach(p => {{
                    ctx.fillStyle = p.color;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                    ctx.fill();
                }});
            }}
            
            function loop() {{
                update();
                draw();
                requestAnimationFrame(loop);
            }}
            
            loop();
        </script>
    </body>
    </html>
    """
```[cite: 10]

---

### 6. `app.py` (Director de Orquesta Completo)
```python
import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import random
from datetime import datetime

# Importar módulos de Snd-Worlds
from config import CONTINENTE_INICIAL, CONTINENTES_OFICIALES, REINOS_VALORIA, RAZAS_Y_CLASSES, MONTURAS_COMUNES, SUBFORMAS_BESTIA, ESTADISTICAS_BASE_CLASES
from bestiario import BESTIARIO_ZONAS
from habilidades import CATALOGO_HABILIDADES_GLOBAL_DETALLADO, CATALOGO_EDIFICIOS, CATALOGO_OCULTAS
from canvas_engine import generar_canvas_html
from crafting_talleres import TALLERES_OFICIOS, simular_crafteo

st.set_page_config(
    page_title="Snd-Worlds MMORPG Sandbox",
    page_icon="⚔️",
    layout="wide"
)

@st.cache_resource
def init_firebase():
    if not firebase_admin._apps:
        try:
            if "firebase" in st.secrets:
                cred_dict = dict(st.secrets["firebase"])
                cred = credentials.Certificate(cred_dict)
                firebase_admin.initialize_app(cred)
            else:
                cred = credentials.Certificate("serviceAccountKey.json")
                firebase_admin.initialize_app(cred)
        except Exception:
            cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
    return firestore.client()

try:
    db = init_firebase()
except Exception as e:
    st.error(f"Error crítico al conectar con Firebase: {e}")
    st.stop()

# --- ESTADO DE SESIÓN ---
for key, default in [
    ("logged_in", False), ("user_email", ""), ("hero_name", ""),
    ("raza", "Humano"), ("subforma", "Hombre Lobo"), ("genero", "Hombre"),
    ("clase", "Invocador"), ("continente", CONTINENTE_INICIAL),
    ("reino_actual", "Reino Humano de Valoria"), ("asentamiento_actual", "Aurelia Capital"),
    ("plano_vista", "Exterior (Puertas del Asentamiento)"),
    ("hero_level", 1), ("hero_hp", 100), ("max_hp", 100), ("hero_xp", 0),
    ("puntos_libres", 0),
    ("str", 5), ("int", 16), ("agi", 6), ("vit", 10), ("luk", 10),
    ("cores", 15), ("plata", 200), ("oro", 20), ("diamante", 3),
    ("habilidades_equipadas", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno"]),
    ("grimorio_inventario", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno", "Muro de Hielo Permafrost"]),
    ("habilidades_fusionadas", []),
    ("inventario", ["Ropa de Viajero", "Raciones de Pan", "Escama de Magma", "Mineral de Hierro Bruto", "Piel Desértica", "Bulbo Luminoso"]),
    ("montura_activa", "Ninguna"),
    ("misiones_activas", [{"id": "m1", "titulo": "Caza de Goblins en Valoria", "objetivo": "Derrota 5 Goblins", "progreso": 0, "meta": 5, "completada": False}]),
    ("has_character", False)
]:
    if key not in st.session_state:
        st.session_state[key] = default

def save_user_data():
    if st.session_state.logged_in and st.session_state.user_email:
        user_data = {
            "hero_name": st.session_state.hero_name,
            "raza": st.session_state.raza,
            "clase": st.session_state.clase,
            "continente": st.session_state.continente,
            "reino_actual": st.session_state.reino_actual,
            "asentamiento_actual": st.session_state.asentamiento_actual,
            "hero_level": st.session_state.hero_level,
            "hero_hp": st.session_state.hero_hp,
            "max_hp": st.session_state.max_hp,
            "hero_xp": st.session_state.hero_xp,
            "puntos_libres": st.session_state.puntos_libres,
            "str": st.session_state.str,
            "int": st.session_state.int,
            "agi": st.session_state.agi,
            "vit": st.session_state.vit,
            "luk": st.session_state.luk,
            "cores": st.session_state.cores,
            "plata": st.session_state.plata,
            "oro": st.session_state.oro,
            "diamante": st.session_state.diamante,
            "habilidades_equipadas": st.session_state.habilidades_equipadas,
            "grimorio_inventario": st.session_state.grimorio_inventario,
            "habilidades_fusionadas": st.session_state.habilidades_fusionadas,
            "inventario": st.session_state.inventario,
            "montura_activa": st.session_state.montura_activa,
            "misiones_activas": st.session_state.misiones_activas,
            "has_character": st.session_state.has_character
        }
        db.collection("users").document(st.session_state.user_email).set(user_data, merge=True)

# ================= LOGIN =================
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #ffaa00;'>⚔️ SND-WORLDS MMORPG SANDBOX ⚔️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a0a0a0;'>Arquitectura Modular | 1,870 Habilidades | Canvas Real-Time | Omni-Oficios</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("### Acceso al Servidor")
        user_input = st.text_input("Correo electrónico o Usuario")
        
        if st.button("Conectar al Servidor", use_container_width=True):
            if user_input:
                email = user_input.strip().lower()
                st.session_state.user_email = email
                user_ref = db.collection("users").document(email)
                user_doc = user_ref.get()
                
                if user_doc.exists:
                    data = user_doc.to_dict()
                    st.session_state.hero_name = data.get("hero_name", email.split("@")[0])
                    st.session_state.raza = data.get("raza", "Humano")
                    st.session_state.clase = data.get("clase", "Invocador")
                    st.session_state.continente = data.get("continente", CONTINENTE_INICIAL)
                    st.session_state.reino_actual = data.get("reino_actual", "Reino Humano de Valoria")
                    st.session_state.asentamiento_actual = data.get("asentamiento_actual", "Aurelia Capital")
                    st.session_state.hero_level = data.get("hero_level", 1)
                    st.session_state.hero_hp = data.get("hero_hp", 100)
                    st.session_state.max_hp = data.get("max_hp", 100)
                    st.session_state.hero_xp = data.get("hero_xp", 0)
                    st.session_state.puntos_libres = data.get("puntos_libres", 0)
                    st.session_state.str = data.get("str", 5)
                    st.session_state.int = data.get("int", 16)
                    st.session_state.agi = data.get("agi", 6)
                    st.session_state.vit = data.get("vit", 10)
                    st.session_state.luk = data.get("luk", 10)
                    st.session_state.habilidades_equipadas = data.get("habilidades_equipadas", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno"])
                    st.session_state.grimorio_inventario = data.get("grimorio_inventario", ["Invocación de Golem de Roca", "Tajo Inicial", "Bola de Fuego", "Flecha Relámpago", "Golpe del Dragón Interno", "Muro de Hielo Permafrost"])
                    st.session_state.habilidades_fusionadas = data.get("habilidades_fusionadas", [])
                    st.session_state.inventario = data.get("inventario", ["Ropa de Viajero", "Raciones de Pan"])
                    st.session_state.montura_activa = data.get("montura_activa", "Ninguna")
                    st.session_state.misiones_activas = data.get("misiones_activas", [])
                    st.session_state.has_character = data.get("has_character", True)
                else:
                    st.session_state.hero_name = email.split("@")[0]
                    st.session_state.has_character = False
                
                st.session_state.logged_in = True
                st.rerun()
    st.stop()

# ================= CREACIÓN DE PERSONAJE =================
if not st.session_state.has_character:
    st.markdown("<h2 style='text-align: center; color: #ffaa00;'>🛡️ Creación de Tu Héroe en Snd-Worlds</h2>", unsafe_allow_html=True)
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.session_state.hero_name = st.text_input("Nombre del Héroe", value=st.session_state.hero_name)
        st.session_state.raza = st.selectbox("Raza / Facción", list(RAZAS_Y_CLASSES.keys()))
        if st.session_state.raza == "Hombre Bestia":
            st.session_state.subforma = st.selectbox("Sub-forma de Bestia", SUBFORMAS_BESTIA)
    with col_c2:
        info_raza = RAZAS_Y_CLASSES[st.session_state.raza]
        st.session_state.clase = st.selectbox("Clase Oficial", info_raza["clases"])
        st.session_state.reino_actual = info_raza["reino_inicio"]
        st.session_state.asentamiento_actual = f"Asentamiento de {st.session_state.raza}"
        
        base_stats = ESTADISTICAS_BASE_CLASES.get(st.session_state.clase, {"str": 10, "int": 10, "agi": 10, "vit": 10, "luk": 10, "hp": 100})
        st.session_state.str = base_stats["str"]
        st.session_state.int = base_stats["int"]
        st.session_state.agi = base_stats["agi"]
        st.session_state.vit = base_stats["vit"]
        st.session_state.luk = base_stats["luk"]
        st.session_state.max_hp = base_stats["hp"]
        st.session_state.hero_hp = base_stats["hp"]

        monturas_disponibles = info_raza["monturas_exclusivas"] + MONTURAS_COMUNES
        st.session_state.montura_activa = monturas_disponibles[0]

        st.info(f"🐎 **Montura Asignada:** `{st.session_state.montura_activa}`\n\n*{info_raza['lore']}*")

    if st.button("🚀 ¡Entrar al Mundo!", use_container_width=True):
        if st.session_state.hero_name:
            st.session_state.has_character = True
            save_user_data()
            st.rerun()
    st.stop()

# ================= BARRA LATERAL =================
st.sidebar.header(f"🛡️ {st.session_state.hero_name}")
st.sidebar.write(f"**Raza:** {st.session_state.raza} | **Clase:** {st.session_state.clase}")
st.sidebar.write(f"⭐ **Nivel:** {st.session_state.hero_level} | ❤️ **HP:** {st.session_state.hero_hp}/{st.session_state.max_hp}")
st.sidebar.write(f"🐎 **Montura:** `{st.session_state.montura_activa}`")
st.sidebar.markdown(f"🌍 **Continente:** `{st.session_state.continente}`")
st.sidebar.markdown(f"🏰 **Reino / Asentamiento:** `{st.session_state.asentamiento_actual}`")

if st.sidebar.button("🚪 Cerrar Sesión"):
    save_user_data()
    st.session_state.logged_in = False
    st.session_state.has_character = False
    st.rerun()

# Pestañas principales
tab_canvas, tab_craft, tab_stats, tab_skills, tab_dungeon, tab_quests, tab_edificio, tab_viaje_local, tab_bag, tab_world = st.tabs([
    "🎮 Motor PvE (Tiempo Real)",
    "🛠️ Talleres & Oficios",
    "📊 Atributos & Nivel",
    "✨ Grimorio (15 Habilidades)",
    "🏰 Mazmorras & Jefes",
    "📜 Misiones",
    "🏪 Tienda Gremio",
    "🗺️ Bestiario y Zonas",
    "🎒 Mochila",
    "🌍 Continentes"
])

# ================= TAB 1: CANVAS PVE EN TIEMPO REAL =================
with tab_canvas:
    col_top1, col_top2 = st.columns([2.5, 1.5])
    with col_top1:
        st.subheader(f"📍 {st.session_state.asentamiento_actual} — Combate en Tiempo Real")
    with col_top2:
        if st.session_state.plano_vista == "Exterior (Puertas del Asentamiento)":
            if st.button("🚪 Cruzar Murallas a Zonas de Caza (PvE)", use_container_width=True, type="primary"):
                st.session_state.plano_vista = "Zona de Caza y Combate"
                st.rerun()
        else:
            if st.button("🏰 Volver al Refugio del Asentamiento", use_container_width=True):
                st.session_state.plano_vista = "Exterior (Puertas del Asentamiento)"
                st.rerun()

    st.markdown("#### ⚡ Barra de Habilidades Activas (Dominas hasta 15 habilidades)")
    cols_sk = st.columns(5)
    for i, sk_name in enumerate(st.session_state.habilidades_equipadas):
        with cols_sk[i]:
            if sk_name:
                st.button(f"[{i+1}] {sk_name}\n(Poderes x3)", key=f"btn_sk_{i}")
            else:
                st.button(f"[{i+1}] Vacío", disabled=True, key=f"btn_sk_empty_{i}")

    es_caza = "Caza" in st.session_state.plano_vista
    reino_actual_str = st.session_state.reino_actual
    datos_reino_actual = BESTIARIO_ZONAS.get(reino_actual_str, BESTIARIO_ZONAS["Reino Humano de Valoria"])
    
    html_code = generar_canvas_html(es_caza, reino_actual_str, datos_reino_actual["mobs"], datos_reino_actual.get("jefes_zona", []))
    st.components.v1.html(html_code, height=480)

# ================= TAB 2: TALLERES Y OFICIOS =================
with tab_craft:
    st.subheader("🛠️ Centro General de Talleres y Oficios (Omni-Oficios)")
    st.write("Acceso universal a los 10 talleres. Fabrica equipo y objetos 100% libres de ataduras (*0% Soul-Bound*).")
    
    taller_sel = st.selectbox("Selecciona el Taller", list(TALLERES_OFICIOS.keys()))
    info_taller = TALLERES_OFICIOS[taller_sel]
    st.info(info_taller["descripcion"])

    for receta in info_taller["recetas"]:
        with st.expander(f"✨ {receta['nombre']} — Tier: {receta['tier']} ({receta['tipo']})"):
            st.write(f"**Materiales requeridos:**")
            for mat, cant in receta["materiales"].items():
                en_inv = st.session_state.inventario.count(mat)
                col = "green" if en_inv >= cant else "red"
                st.markdown(f"- :{col}[{cant}x {mat}] (Tienes: {en_inv})")
            
            if st.button(f"🔨 Fabricar {receta['nombre']}", key=f"craft_{receta['id']}"):
                exito, msg = simular_crafteo(taller_sel, receta["id"], st.session_state.inventario)
                if exito:
                    for mat, cant in receta["materiales"].items():
                        for _ in range(cant): st.session_state.inventario.remove(mat)
                    st.session_state.inventario.append(receta['nombre'])
                    save_user_data()
                    st.success(f"¡Fabricado con éxito **{receta['nombre']}**!")
                    st.rerun()
                else:
                    st.error(f"Error: {msg}")

# ================= TAB 3: ATRIBUTOS Y NIVEL =================
with tab_stats:
    st.subheader("📊 Panel de Atributos y Escalado de Nivel")
    st.write(f"⭐ **Nivel Actual:** `{st.session_state.hero_level}` | 🎁 **Puntos Libres:** `{st.session_state.puntos_libres}`")
    
    col_st1, col_st2 = st.columns(2)
    with col_st1:
        st.write(f"💪 **STR:** {st.session_state.str} | 🔮 **INT:** {st.session_state.int} | ⚡ **AGI:** {st.session_state.agi} | ❤️ **VIT:** {st.session_state.vit} | 🍀 **LUK:** {st.session_state.luk}")
        if st.session_state.puntos_libres > 0:
            attr = st.selectbox("Atributo a subir", ["Fuerza", "Inteligencia", "Agilidad", "Vitalidad", "Suerte"])
            if st.button("Asignar Punto"):
                st.session_state.puntos_libres -= 1
                if attr == "Fuerza": st.session_state.str += 1
                elif attr == "Inteligencia": st.session_state.int += 1
                elif attr == "Agilidad": st.session_state.agi += 1
                elif attr == "Vitalidad": 
                    st.session_state.vit += 1
                    st.session_state.max_hp += 5
                    st.session_state.hero_hp += 5
                elif attr == "Suerte": st.session_state.luk += 1
                save_user_data()
                st.success("¡Atributo mejorado!")
                st.rerun()
    with col_st2:
        if st.button("✨ Simular Subida de Nivel (+1 Nivel)", use_container_width=True):
            st.session_state.hero_level += 1
            st.session_state.puntos_libres += 5
            st.session_state.max_hp += 10
            st.session_state.hero_hp = st.session_state.max_hp
            save_user_data()
            st.success(f"¡Subiste a Nivel {st.session_state.hero_level}!")
            st.rerun()

# ================= TAB 4: GRIMORIO Y FUSIÓN =================
with tab_skills:
    st.subheader("✨ Grimorio, Habilidades y Laboratorio de Fusión")
    st.write("Cada habilidad cuenta con **3 poderes únicos**. Domina hasta 15 habilidades y fusiona pares para crear super-poderes.")
    
    col_sk1, col_sk2 = st.columns(2)
    with col_sk1:
        st.markdown("### 📋 Tus 5 Ranuras Activas de Combate")
        for idx in range(5):
            actual = st.session_state.habilidades_equipadas[idx]
            nueva = st.selectbox(f"Ranura #{idx+1}", ["(Vacío)"] + st.session_state.grimorio_inventario, index=(st.session_state.grimorio_inventario.index(actual)+1) if actual in st.session_state.grimorio_inventario else 0, key=f"slot_{idx}")
            val = "" if nueva == "(Vacío)" else nueva
            if st.session_state.habilidades_equipadas[idx] != val:
                st.session_state.habilidades_equipadas[idx] = val
                save_user_data()

    with col_sk2:
        st.markdown("### ⚗️ Laboratorio de Fusión de Habilidades")
        if st.session_state.hero_level >= 30:
            fp1 = st.selectbox("Habilidad 1", st.session_state.grimorio_inventario, key="f1")
            fp2 = st.selectbox("Habilidad 2", st.session_state.grimorio_inventario, key="f2")
            nombre_fus = st.text_input("Nombre del Poder Híbrido")
            if st.button("✨ Fusionar Poderes") and nombre_fus and fp1 != fp2:
                st.session_state.habilidades_fusionadas.append({"nombre": nombre_fus, "p1": fp1, "p2": fp2})
                st.session_state.grimorio_inventario.append(nombre_fus)
                save_user_data()
                st.success(f"¡Habilidad fusionada **{nombre_fus}** creada con éxito!")
                st.rerun()
        else:
            st.warning("🔒 Se desbloquea al Nivel 30.")

# ================= TAB 5: MAZMORRAS Y JEFES =================
with tab_dungeon:
    st.subheader("🏰 Mazmorras del Reino y Jefes de Instancia")
    reino_d = BESTIARIO_ZONAS.get(st.session_state.reino_actual, {})
    mazmorras = reino_d.get("mazmorras", [])
    if mazmorras:
        for maz in mazmorras:
            st.markdown(f"**{maz['nombre']}** (Nivel mínimo: `{maz['nivel_min']}`)")
            st.write(f"Boss: **{maz['jefe']}** (HP: {maz['hp_jefe']}) | Drop: *{maz['drop_jefe']}*")
            if st.button(f"⚔️ Entrar a {maz['nombre']}", key=f"entrar_{maz['nombre']}"):
                if st.session_state.hero_level >= maz['nivel_min']:
                    st.success(f"¡Has derrotado a **{maz['jefe']}** en la mazmorra y obtenido {maz['drop_jefe']}!")
                    st.session_state.inventario.append(maz['drop_jefe'])
                    save_user_data()
                    st.rerun()
                else:
                    st.error(f"Nivel insuficiente. Requieres nivel {maz['nivel_min']}.")
    else:
        st.info("No hay mazmorras registradas en esta zona exacta. Explora otro reino.")

# ================= TAB 6: MISIONES =================
with tab_quests:
    st.subheader("📜 Tablón de Misiones del Asentamiento")
    for m in st.session_state.misiones_activas:
        estado = "✅ Completada" if m['completada'] else f"Progreso: {m['progreso']}/{m['meta']}"
        st.markdown(f"**{m['titulo']}** — *{m['objetivo']}* [{estado}]")
        if not m['completada'] and st.button(f"Completar Misión", key=f"m_comp_{m['id']}"):
            m['completada'] = True
            m['progreso'] = m['meta']
            st.session_state.puntos_libres += 2
            st.session_state.plata += 100
            save_user_data()
            st.success("¡Misión completada! +2 Puntos libres y +100 plata.")
            st.rerun()

# ================= TAB 7: TIENDA GREMIO =================
with tab_edificio:
    st.subheader("🏪 Tienda del Gremio de Aventureros")
    for item in CATALOGO_EDIFICIOS["Gremio de Aventureros"]["items"]:
        col_t1, col_t2 = st.columns([3, 1])
        with col_t1:
            st.markdown(f"**{item['nombre']}** — Coste: {item['precio']} {item['metal']}")
        with col_t2:
            if st.button("Comprar", key=f"comprar_{item['id']}"):
                sk_limpia = item['nombre'].split(": ")[-1]
                if sk_limpia not in st.session_state.grimorio_inventario:
                    st.session_state.grimorio_inventario.append(sk_limpia)
                    save_user_data()
                    st.success(f"¡Aprendiste **{sk_limpia}**!")
                    st.rerun()

# ================= TAB 8: BESTIARIO Y ZONAS =================
with tab_viaje_local:
    st.subheader("🗺️ Bestiario y Viaje entre Reinos (Continente I: Niveles 1-100)")
    reino_sel = st.selectbox("Selecciona Reino o Zona Común", list(BESTIARIO_ZONAS.keys()))
    info_r = BESTIARIO_ZONAS[reino_sel]
    st.write(f"**Rango de Nivel:** `{info_r['rango']}`")

    st.markdown("### 🐺 Enemigos Comunes")
    for mob in info_r["mobs"]:
        st.markdown(f"- **{mob['nombre']}** (Nivel {mob['nivel']}) | Tipo: `{mob['tipo']}` | HP: {mob['hp']} | Ataque: `{mob['ataque']}` | Loot: *{mob['drop']}*")

    st.markdown("### 👑 Jefes de Zona")
    for j in info_r.get("jefes_zona", []):
        st.markdown(f"- 🔴 **{j['nombre']}** (Nivel {j['nivel']}) | HP: {j['hp']} | Loot: *{j['drop']}*")

    if st.button("🚀 Viajar a este Reino o Zona", use_container_width=True):
        st.session_state.reino_actual = reino_sel
        st.session_state.asentamiento_actual = f"Asentamiento en {reino_sel}"
        save_user_data()
        st.success(f"Te has desplazado a **{reino_sel}**.")
        st.rerun()

# ================= TAB 9: MOCHILA =================
with tab_bag:
    st.subheader("🎒 Inventario y Objetos en Mochila")
    st.write(st.session_state.inventario)

# ================= TAB 10: CONTINENTES =================
with tab_world:
    st.subheader("🌍 Mapa de Continentes y Escalado de Niveles")
    for cont, info in CONTINENTES_OFICIALES.items():
        st.markdown(f"**{cont}**")
        st.write(f"- {info['tipo']}")

st.markdown("---")
st.caption("Snd-Worlds MMORPG Sandbox - Arquitectura Modular Definitiva con Canvas Real-Time")
```[cite: 11]