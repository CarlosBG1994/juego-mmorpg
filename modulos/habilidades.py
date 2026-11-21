# --- TIER I (Mitica) - Limitado a 5 jugadores por habilidad ---
# Estas habilidades requieren una maestría extrema y solo pueden ser usadas por clases de alto rango.

registrar_habilidad("M001", "Ira del Cataclismo", "I", ["Humano", "Enano"], ["Paladin", "Campeon Runico"])
registrar_habilidad("M002", "Corazón de los Ancestros", "I", ["Elfo"], ["Druida", "Alcaide"])
registrar_habilidad("M003", "Rugido del Totem Primordial", "I", ["Hombre Bestia"], ["Chaman Primordial", "Campeon"])
registrar_habilidad("M004", "Velo de la Oscuridad Eterna", "I", ["Humano", "Elfo", "Hombre Bestia"], ["Asesino", "Acechador Nocturno"])
registrar_habilidad("M005", "Sentencia de la Forja Solar", "I", ["Enano", "Humano"], ["Clerigo", "Paladin"])

# --- NOTA DE CONTROL DE SISTEMA ---
# Para asegurar que solo 5 jugadores tengan estas habilidades, 
# se debe validar el contador global en el modulo de persistencia o integrador.
