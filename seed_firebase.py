import json
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase con tu clave de servicio
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Cargar el archivo game_data.json generado
with open("www/game_data.json", "r", encoding="utf-8") as f:
    game_data = json.load(f)

print("Subiendo configuración maestra de Snd-Worlds a Firestore...")

# 1. Guardar metadata global y escala del mundo de forma segura
db.collection("snd_worlds_config").document("mundo").set({
    "descripcion": game_data.get("descripcion_proyecto", "Snd-Worlds MMORPG"),
    "escala_mundo": game_data.get("escala_mundo", {}),
    "lore_especial": game_data.get("lore_especial", {}),
    "metales_economicos": game_data.get("metales_economicos", [])
})

# 2. Guardar los 7 continentes (si existen en el JSON)
continentes = game_data.get("continentes", [])
for cont in continentes:
    db.collection("snd_worlds_continentes").document(cont["id"]).set(cont)

# 3. Guardar catálogo de clases por raza
razas_clases = game_data.get("estructura_razas_clases", {})
db.collection("snd_worlds_config").document("razas_y_clases").set(razas_clases)

print("¡Sincronización con Firebase completada con éxito!")