# --- SISTEMA MASIVO DE HABILIDADES (1,870 HABILIDADES, TIER, PODERES Y RAREZAS) ---

CATALOGO_HABILIDADES_GLOBAL_DETALLADO = [
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
    {
        "id": "sk_arq_1", "clase": "Arquero Arcano", "tier": "Tier I", "rareza": "Común",
        "nombre": "Flecha Relámpago",
        "poderes": ["1. Tiro Veloz (Daño penetrante)", "2. Flecha Electrificada (Cadena de rayos)", "3. Lluvia de Flechas (Área amplia)"]
    },
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