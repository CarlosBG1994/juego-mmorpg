import os
import json

os.makedirs("www", exist_ok=True)

# Las 4 razas y sus clases personalizadas
razas_y_clases = {
    "Humano": [
        "Caballero", 
        "Paladín", 
        "Mago de Batalla", 
        "Púgil", 
        "Asesino", 
        "Explorador", 
        "Invocador", 
        "Clérigo"
    ],
    "Elfo": [
        "Guardabosques", 
        "Alcaide", 
        "Druida", 
        "Espadachín Silvano", 
        "Monje del Viento", 
        "Acechador Nocturno", 
        "Mago de Batalla", 
        "Invocador"
    ],
    "Enano": [
        "Guerrero Pesado", 
        "Defensor Rúnico de Asedio", 
        "Berserker Rúnico", 
        "Luchador de Puño de Hierro", 
        "Ballestero", 
        "Asesino", 
        "Mago de Batalla", 
        "Invocador", 
        "Clérigo"
    ],
    "Hombre Bestia": [
        "Campeón", 
        "Acechador Salvaje", 
        "Chamán Primordial", 
        "Púgil", 
        "Asesino", 
        "Explorador", 
        "Mago de Batalla", 
        "Invocador", 
        "Clérigo"
    ]
}

# Los 7 continentes del mundo abierto masivo (Snd-Worlds)
continentes_mundo = [
    {"id": "cont_1", "nombre": "Continente Humano (Región del Miasma)", "descripcion": "Territorio principal de los humanos, albergando las zonas de Miasma tóxico accesibles mediante misiones ocultas y objetos de supervivencia."},
    {"id": "cont_2", "nombre": "Dominio Silvano de los Elfos", "descripcion": "Vastas extensiones de bosques ancestrales, arcanos y fronteras naturales."},
    {"id": "cont_3", "nombre": "Cordillera e Imperios Enanos", "descripcion": "Fortalezas de piedra, montañas de asedio y minas de extracción de metales."},
    {"id": "cont_4", "nombre": "Tierras Salvajes de los Hombres Bestia", "descripcion": "Ecosistemas hostiles y salvajes adaptados a las 7 sub-formas de bestia."},
    {"id": "cont_5", "nombre": "Archipiélago de los Cielos Abiertos", "descripcion": "Islas flotantes y rutas comerciales de alta mar y aire."},
    {"id": "cont_6", "nombre": "Las Fronteras del Olvido", "descripcion": "Territorios inexplorados de incursión y mazmorras de gremio reclamables."},
    {"id": "cont_7", "nombre": "El Núcleo Central de Comercio", "descripcion": "Zona neutral de libre comercio basada en los 4 metales económicos (Cores, Plata, Oro, Diamante)."}
]

tiers = ["Común", "Raro", "Épico", "Legendario", "Místico"]

metodos_obtencion = [
    "Compra en Tienda de Facción", 
    "Recompensa de Misión", 
    "Cofre de Incursión / Mazmorra de Gremio", 
    "Misión Oculta (Secreta)", 
    "Habilidad Prohibida / Hallazgo Raro en Mundo Abierto"
]

habilidades_por_raza_clase = {}
id_counter = 1

for raza, lista_clases in razas_y_clases.items():
    habilidades_por_raza_clase[raza] = {}
    for clase in lista_clases:
        habilidades_por_raza_clase[raza][clase] = []
        for tier in tiers:
            for i in range(1, 12):
                metodo_idx = (i + tiers.index(tier)) % len(metodos_obtencion)
                metodo_actual = metodos_obtencion[metodo_idx]
                
                if tier in ["Legendario", "Místico"] and i > 9:
                    metodo_actual = "Habilidad Prohibida / Hallazgo Raro en Mundo Abierto"

                habilidades_por_raza_clase[raza][clase].append({
                    "id": id_counter,
                    "nombre": f"Técnica [{raza}] {clase} {tier} #{i}",
                    "raza": raza,
                    "clase": clase,
                    "tier": tier,
                    "metodo_obtencion": metodo_actual,
                    "daño_o_efecto": i * 15 + (tiers.index(tier) + 1) * 55,
                    "descripcion": f"Habilidad de {clase} para la raza {raza} (Tier: {tier}). Obtención: {metodo_actual}."
                })
                id_counter += 1

data = {
    "descripcion_proyecto": "Snd-Worlds MMORPG Sandbox - Base de Datos Completa con 7 Continentes y 4 Razas",
    "total_habilidades_registradas": id_counter - 1,
    "escala_mundo": {
        "tierra_km2": "8.5 Millones",
        "oceanos_km2": "1.55 Millones",
        "total_continentes": 7
    },
    "continentes": continentes_mundo,
    "estructura_razas_clases": razas_y_clases,
    "habilidades": habilidades_por_raza_clase,
    "metales_economicos": [
        {"id": "met_1", "nombre": "Cores", "tipo": "Metal Económico Principal"},
        {"id": "met_2", "nombre": "Plata", "tipo": "Metal Económico Estándar"},
        {"id": "met_3", "nombre": "Oro", "tipo": "Metal Económico Avanzado"},
        {"id": "met_4", "nombre": "Diamante", "tipo": "Metal Económico Máximo"}
    ]
}

with open("www/game_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"¡Base de datos con los 7 continentes generada con éxito! Total de habilidades creadas: {id_counter - 1}")