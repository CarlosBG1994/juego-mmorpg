# --- MÓDULO: HABILIDADES (CATÁLOGO MAESTRO) ---

# TIER 0: ÉPICAS (1 Portador por ID)
DETALLES_EPICAS = {
    f"E{i:03}": datos for i, datos in enumerate([
        {"Clase": "Caballero", "Nombre": "Excalibur del Nexo", "Niv30": "Daño 400% STR + Ejecución."},
        {"Clase": "Paladín", "Nombre": "Aura del Juicio Final", "Niv30": "Daño 400% INT + Purga Global."},
        {"Clase": "Mago de Batalla", "Nombre": "Singularidad Arcano", "Niv30": "Daño 400% INT + Stasis."},
        {"Clase": "Púgil", "Nombre": "Golpe del Dios del Rayo", "Niv30": "Daño 400% STR + Aturdimiento masivo."},
        {"Clase": "Asesino", "Nombre": "Muerte Silenciosa", "Niv30": "Daño 400% AGI + Invisible permanente."},
        {"Clase": "Explorador", "Nombre": "Ojo del Halcón Cósmico", "Niv30": "Daño 400% DES + Visión Real."},
        {"Clase": "Invocador", "Nombre": "Pacto del Rey Demoníaco", "Niv30": "Daño 400% INT + Invoca jefe Tier I."},
        {"Clase": "Clérigo", "Nombre": "Resurrección del Cosmos", "Niv30": "Revive todo el grupo + Inmortalidad."},
        {"Clase": "Guardabosques", "Nombre": "Flecha del Destino", "Niv30": "Daño 400% DES + Perfora todo."},
        {"Clase": "Alcaide", "Nombre": "Custodio del Árbol Mundo", "Niv30": "Escudo invencible 10s + Regeneración HP total."},
        {"Clase": "Druida", "Nombre": "Avatar de la Madre Naturaleza", "Niv30": "Transmutación en Coloso + 400% INT."},
        {"Clase": "Espadachín Silvano", "Nombre": "Filo del Infinito", "Niv30": "Daño 400% AGI + Velocidad x10."},
        {"Clase": "Guerrero Pesado", "Nombre": "Coloso de Hierro", "Niv30": "Daño 400% VIT + Inmune a CC."},
        {"Clase": "Defensor Rúnico", "Nombre": "Baluarte de los 4 Reinos", "Niv30": "Daño 400% VIT + Reflejo de daño 100%."},
        {"Clase": "Campeón Rúnico", "Nombre": "Furia de Ymir", "Niv30": "Daño 400% STR + Terremoto global."},
        {"Clase": "Campeón (Bestia)", "Nombre": "Aliento del Dragón Ancestral", "Niv30": "Daño 400% STR + Fuego azul."},
        {"Clase": "Chamán Primordial", "Nombre": "Espirítu del Nexo", "Niv30": "Daño 400% INT + Invocación de Avatar."}
    ], start=1)
}

# TIER II: LEYENDA (10 Portadores por ID)
# Catálogo estandarizado para las 30 habilidades
DETALLES_LEYENDA = {
    f"L{i:03}": {
        "Efecto": f"Poder Leyenda {i}", 
        "Niv1": "80% Stat base", 
        "Niv15": "Efecto Utility", 
        "Niv30": "200% Stat base"
    } for i in range(1, 31)
}
