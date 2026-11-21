"""
Modulo: Habilidades de Snd-Worlds (Actualizado: Catalogo Maestro)
Estructura de catalogacion: 1.870 habilidades organizadas por Tier y requisitos.
"""

# ... (Se mantiene todo lo anterior: TIERS, PORTADORES_MAXIMOS, class Habilidad) ...

# Catalogo Maestro categorizado
# Estructura: CATALOGO_HABILIDADES = { "ID": Habilidad(objeto) }
CATALOGO_HABILIDADES = {}

def registrar_habilidad(id_hab, nombre, tier, razas, clases):
    CATALOGO_HABILIDADES[id_hab] = Habilidad(id_hab, nombre, tier, razas, clases)

# --- INICIO DEL REGISTRO DE CATALOGO BASE (MUESTRA) ---

# TIER I (Mitica) - Limitado a 5 jugadores
registrar_habilidad("M001", "Ira del Cataclismo", "I", ["Humano", "Enano"], ["Paladin", "Campeon Runico"])

# TIER II (Leyenda) - Limitado a 10 jugadores
registrar_habilidad("L001", "Susurro del Viento Silvano", "II", ["Elfo"], ["Guardabosques", "Druida"])

# TIER III (Ultra Raro)
registrar_habilidad("UR001", "Golpe de Puno de Hierro", "III", ["Enano", "Hombre Bestia"], ["Pugil", "Luchador de Puno de Hierro"])

# TIER IV (Raro)
registrar_habilidad("R001", "Llamarada Arcana", "IV", ["Humano", "Elfo"], ["Mago de Batalla", "Invocador"])

# TIER V (Poco Comun)
registrar_habilidad("PC001", "Sigilo de las Sombras", "V", ["Humano", "Elfo", "Enano", "Hombre Bestia"], ["Asesino", "Acechador Nocturno"])

# TIER VI (Comun)
registrar_habilidad("C001", "Corte Basico", "VI", ["Humano", "Elfo", "Enano", "Hombre Bestia"], ["Caballero", "Espadachin Silvano", "Campeon"])

# --- FIN DEL REGISTRO MUESTRA ---

def obtener_habilidades_por_clase(clase_buscada):
    """Filtra el catalogo para mostrar qué habilidades puede usar una clase especifica."""
    return [hab for hab in CATALOGO_HABILIDADES.values() if clase_buscada in hab.clase_req]

# ... (El resto de funciones como fusionar_habilidades se mantienen intactas) ...
