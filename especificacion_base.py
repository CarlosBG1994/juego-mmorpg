REGLAS_SND_WORLDS = """
REGLAS BASE DE SND-WORLDS (NO ROMPER NI CONTRADECIR):
1. Razas y Clases:
   - Humano: Caballero, Paladin, Mago de Batalla, Pugil, Asesino, Explorador, Invocador, Clerigo.
   - Elfo (sin Clerigo; el Druida asume sanacion y soporte): Guardabosques, Alcaide, Druida, Espadachin Silvano, Monje del Viento (Pugil), Acechador Nocturno (Asesino), Mago de Batalla, Invocador.
   - Enano: Guerrero Pesado, Defensor Runico de Asedio, Campeon Runico, Luchador de Puno de Hierro (Pugil), Ballestero (Explorador), Asesino, Mago de Batalla, Invocador, Clerigo.
   - Hombre Bestia (7 sub-formas: Hombre Lobo, Hombre Pantera, Hombre Tigre, Hombre Leon, Hombre Mono, Hombre Tortuga y Hombre Panda): Campeon, Acechador Salvaje, Chaman Primordial, Pugil (incluye variantes/estado frenetico tipo Berserker), Asesino, Explorador, Mago de Batalla, Invocador, Clerigo.
   - Cada raza y clase tiene sus propios atributos.
   - Estadisticas: Fuerza (STR), Inteligencia (INT), Agildiad (AGI), Vitalidad (VIT), Suerte (LUK) y Destreza (DES).
2. Habilidades (1,870 en catalogo):
   - Cualquier personaje puede obtener o encontrar habilidades ya sea por el mapa en cofres, en mazmorra al derrotar a un jefe o en misiones.
   - Solo se pueden EQUIPAR y USAR si cumplen compatibilidad de RAZA y CLASE. Es decir, las habilidades tendran sus caracteristicas y se podran equipar segun la clase que elijan  los jugadores.
   - Evolucion de habilidades (tiers: común (tier VI), poco común ( tier V), raro (tier IV), ultra raro (tier III), leyenda (tier II), mitica (tier I)), cada habilidad tendra su subida propia de niveles (subira a medida que vayan practicando o matando enemigos) del 1 al 50. Una vez llegue al nivel 15 se desbloqueara un nuevo ataque dentro de la habilidad y al nivel 30 un tercer ataque, generando que cada habilidad tenga 3 ataques propios con sus caracteristicas. Ademas, se podran fusionar las habilidades al instante generando una super habilidad con un unico ataque que mezcla las 2 habilidades. De esta manera, cada jugador tendra 15 ataques diferentes y 10 super ataques.
   - Las habilidades tipo leyenda habran pocas y solo 10 jugadores pueden llevar a la vez esas habilidades y las miticas solo la podran llevar 5 jugadores. El resto de habilidades las podran llevar cualqueir jugadores que tenga la clase para llevarla.
3. Economia y Comercio:
   - Las habilidades obtenidas (incluidas las que el personaje no pueda equipar/usar por raza o clase) y objetos pueden venderse mediante Subasta, Gremio o Intercambio directo.
   - La economia propia del juego estara distribuido entre cobre, plata, oro, diamante y platino. La equivalencia es cada 100 de cobre = 1 de plata, cada 100 de plata = 1 de oro, cada 100 de oro = 1 diamante y cada 100 de diamante = 1 platino.
   - El mundo se rige por esta economia, las cosas basicas costara poco, pero a medida que uno va subiendo de nivel todo lo que necesite (equipo, habilidades, etc) ira costando mas.
   - La manera de conseguir dinero son con misiones, matando enemigos, en cofres o vendiendo en los gremios, tallers o en subastas.
4. Progresion y Mundos:
   - Nivel inicial 1 a 100 en el Continente Primordial. Con 1 reino para cada raza (4 reinos) con sus caracteristicas propias.
   - +5 puntos de estadisticas libres por nivel y +10 HP maximo automatico por nivel.
   - Expansion de +50 niveles por cada continente oculto hasta Nivel 300:
     * Continente Primordial (Limite 100)
     * Archipielago de los Vientos (Limite 150)
     * Continente Abisal de los Demonios (Limite 200)
     * Continente Celestial de los Angeles (Limite 250)
     * Nucleo Central de Comercio y Nexo Global (Limite 300)
    - Jefes de zona: Cada reino tendra zonas con variedad de enemigos que se moveran en cada zona, excepto para eventos que los enemigos podran viajar de zona. Las zonas iran del 1-15 / 16-25 / 26-35 / 36-45 / 46-60 y tendran varios jefes que seran elites de esa zona. Después, habra zonas unida a los reinos que iran desde el 61-75 / 76-85 / 86-100 que seran zonas que no pertenecen a nigun reino tambien con sus jefes elite.
    - Habra mazmorras esparcidas que tendran zonas secretas con cofres que daran objetos o habilidades. El nivel de esa mazmorra dependera de la zona donde este. Cada mazmorra tendra un jefe final. Las mazmorras una vez completadas no desaparecen, se podra volver a entrar, lo que el jefe final tarda entre 15-20 minutos a volver a aparecer para todos los jugadores.
5. Regla de seguridad de codigo:
   - Nunca borres ni elimines funciones, clases o datos previos validados en el archivo del modulo salvo que el usuario lo pida de forma expresa; amplia, completa o anade encima conservando lo existente y dejando copia de seguridad.
"""