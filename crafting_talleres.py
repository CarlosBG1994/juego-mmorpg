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