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
```[cite: 6]

Avísame cuando quieras que te pase el siguiente (`habilidades.py`).