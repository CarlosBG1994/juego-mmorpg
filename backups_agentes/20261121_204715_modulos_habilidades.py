# --- TIER I (Mitica) - Limitado a 5 jugadores por habilidad ---
# Cada clase tiene acceso a al menos una habilidad definitiva de nivel Mitico.

# --- HUMANOS ---
registrar_habilidad("M001", "Ira del Cataclismo", "I", ["Humano"], ["Paladin", "Caballero"])
registrar_habilidad("M006", "Dominio del Nexo Arcano", "I", ["Humano"], ["Mago de Batalla", "Invocador"])
registrar_habilidad("M007", "Sentencia de la Forja Solar", "I", ["Humano", "Enano"], ["Clerigo"])
registrar_habilidad("M008", "Danza de la Muerte Blanca", "I", ["Humano"], ["Pugil", "Asesino"])
registrar_habilidad("M009", "Ojo del Explorador Eterno", "I", ["Humano"], ["Explorador"])

# --- ELFOS ---
registrar_habilidad("M002", "Corazon de los Ancestros", "I", ["Elfo"], ["Druida", "Alcaide"])
registrar_habilidad("M010", "Flecha del Eclipse Lunar", "I", ["Elfo"], ["Guardabosques"])
registrar_habilidad("M011", "Filo del Viento Silvano", "I", ["Elfo"], ["Espadachin Silvano"])
registrar_habilidad("M012", "Sombra de la Noche Eterna", "I", ["Elfo"], ["Acechador Nocturno"])
registrar_habilidad("M013", "Invocar al Guardian de Sylva", "I", ["Elfo"], ["Invocador", "Mago de Batalla"])
registrar_habilidad("M014", "Meditacion del Monje del Aire", "I", ["Elfo"], ["Monje del Viento (Pugil)"])

# --- ENANOS ---
registrar_habilidad("M015", "Impacto de la Forja Profunda", "I", ["Enano"], ["Guerrero Pesado", "Campeon Runico"])
registrar_habilidad("M016", "Muralla de los Mil Reinos", "I", ["Enano"], ["Defensor Runico de Asedio"])
registrar_habilidad("M017", "Disparo del Baluarte Rúnico", "I", ["Enano"], ["Ballestero (Explorador)"])
registrar_habilidad("M018", "Golpe de Hierro Ancestral", "I", ["Enano"], ["Luchador de Puno de Hierro (Pugil)"])

# --- HOMBRE BESTIA ---
registrar_habilidad("M003", "Rugido del Totem Primordial", "I", ["Hombre Bestia"], ["Chaman Primordial", "Campeon"])
registrar_habilidad("M019", "Frenesi del Depredador Alfa", "I", ["Hombre Bestia"], ["Acechador Salvaje", "Pugil"])
registrar_habilidad("M020", "Vision del Acechador Nocturno", "I", ["Hombre Bestia"], ["Asesino", "Explorador"])
registrar_habilidad("M021", "Llamada del Nexo Bestial", "I", ["Hombre Bestia"], ["Invocador", "Mago de Batalla"])
registrar_habilidad("M022", "Bendicion del Espiritu Vital", "I", ["Hombre Bestia"], ["Clerigo"])

# --- NOTA DE CONTROL DE SISTEMA ---
# Cada clase tiene ahora su propia habilidad Mítica única (o compartida entre clases de rol similar).
# Se mantienen las restricciones de cupo (Max 5 jugadores por ID).
