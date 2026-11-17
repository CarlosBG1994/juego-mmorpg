import json
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase con tu clave de servicio
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Cargar el archivo game_data.json generado
with open("www/game_data.json", "r", encoding="utf-8") as f:
    game_data = json.load(f)

print("Subiendo configuración maestra de Snd-Worlds a Firestore...")

# 1. Guardar metadata global y escala del mundo
db.collection("snd_worlds_config").document("mundo").set({
    "descripcion": game_data["descripcion_proyecto"],
    "escala_mundo": game_data["escala_mundo"],
    "lore_especial": game_data["lore_especial"],
    "metales_economicos": game_data["metales_economicos"]
})

# 2. Guardar los 7 continentes
for cont in game_data["continentes"]:
    db.collection("snd_worlds_continentes").document(cont["id"]).set(cont)

# 3. Guardar catálogo de clases por raza
db.collection("snd_worlds_config").document("razas_y_clases").set(game_data["estructura_razas_clases"])

print("¡Sincronización con Firebase completada con éxito!")