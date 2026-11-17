import os
import json

os.makedirs("www", exist_ok=True)

# Estructura oficial de Razas y sus Clases personalizadas
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
            for i in range(1, 12): # Genera un volumen masivo por clase/tier
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
    "descripcion_proyecto": "Snd-Worlds MMORPG Sandbox - Base de Datos Oficial con Clases por Raza y Miasma Humano",
    "total_habilidades_registradas": id_counter - 1,
    "lore_especial": {
        "continente_miasma": "Pertenece al Continente Humano. Se desbloquea mediante misiones ocultas y requiere comprar el objeto de supervivencia en tienda."
    },
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

print(f"¡Base de datos definitiva generada con éxito! Total de habilidades creadas: {id_counter - 1}")