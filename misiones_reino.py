# --- SISTEMA MAESTRO DE MISIONES, DIARIAS Y CADENAS MÍTICAS OCULTAS ---

SISTEMA_MISIONES = {
    "principales": [
        {
            "id": "mq_01",
            "titulo": "El Despertar en Valoria",
            "nivel_requerido": 1,
            "zona": "Reino Humano de Valoria",
            "descripcion": "La capital se encuentra sitiada. Presentate ante el General Aldric en Aurelia Capital.",
            "objetivo": "Hablar con el General Aldric y eliminar 5 Goblins de vanguardia.",
            "recompensa": {"exp": 500, "oro": 150, "item": "Espada de Bronce de Milicia"}
        },
        {
            "id": "mq_02",
            "titulo": "Las Sombras del Bosque Ancestral",
            "nivel_requerido": 16,
            "zona": "Bosque Ancestral de Elfos",
            "descripcion": "La corrupción se extiende por las raíces del gran árbol madre.",
            "objetivo": "Investigar el Santuario Silvestre y purificar los 3 altares élficos.",
            "recompensa": {"exp": 2200, "oro": 800, "item": "Arco de Madera de Luna"}
        }
    ],
    "diarias_y_secundarias": [
        {
            "id": "sq_diaria_01",
            "tipo": "Diaria - Recolección",
            "titulo": "Suministros para la Guardia",
            "nivel": "1+",
            "descripcion": "Reúne materiales básicos para el mantenimiento de las murallas.",
            "objetivo": "Recolectar Mineral de Hierro (0/10)",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 400, "oro": 100}
        },
        {
            "id": "sq_diaria_02",
            "tipo": "Diaria - Caza de Jefes",
            "titulo": "Bestia de la Cima: El Alfa de las Nieves",
            "nivel": "30+",
            "descripcion": "Un poderoso alfa desciende de las montañas para saquear las caravanas.",
            "objetivo": "Derrotar al Jefe de Zona en las Montañas Heladas",
            "reinicio": "1 vez al día por jugador",
            "recompensa": {"exp": 3500, "oro": 1500, "item": "Colmillo de Escarcha"}
        },
        {
            "id": "sq_diaria_03",
            "tipo": "Cazarrecompensas - Tribunal de Normas",
            "titulo": "Orden de Arresto: Forajidos y PKs",
            "nivel": "20+",
            "descripcion": "Caza a los jugadores o PNJs renegados que han violado las leyes del tratado de paz.",
            "objetivo": "Neutralizar al Forajido Marcado en los callejones oscuros",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 2000, "oro": 1200, "reputacion": "+50 Justicia"}
        }
    ],
    "ocultas_miticas": [
        {
            "id": "mitica_01",
            "titulo": "??? (Cadena Oculta: El Ecos del Sol Invictus)",
            "nivel_minimo": 50,
            "fases_totales": 5,
            "estado_conocido": "Desconocido (Requiere descubrir la pista en el mundo)",
            "pista_inicial": "Se dice que un mendigo ciego en los suburbios de Aurelia tararea una melodía sobre una espada que cortaba los cielos.",
            "pasos_ocultos": [
                "Fase 1: Encontrar al mendigo anónimo y darle 500 monedas de oro sin que lo vea la guardia.",
                "Fase 2: Descubrir la tumba olvidada detrás de la cascada secreta del Bosque Elfo a medianoche.",
                "Fase 3: Resolver el acertijo rúnico de las tres estatuas sin activar las trampas de fuego.",
                "Fase 4: Derrotar en combate solitario al Espectro del General Traidor dentro de la mazmorra de nivel 70.",
                "Fase 5: Forjar la hoja en el yunque místico durante un eclipse de servidor."
            ],
            "recompensa_oculta": "Objeto Mítico: Sol Invictus (Espada Legendaria de Fuego Estelar)"
        },
        {
            "id": "mitica_02",
            "titulo": "??? (Cadena Oculta: Las Lágrimas del Abismo Marino)",
            "nivel_minimo": 60,
            "fases_totales": 4,
            "estado_conocido": "Desconocido",
            "pista_inicial": "Un marinero borracho en el Puerto Comercial balbucea sobre burbujas que brillan con luz propia en el fondo del archipiélago.",
            "pasos_ocultos": [
                "Fase 1: Pescar un tiburón abisal en aguas profundas sin equipo de protección avanzado.",
                "Fase 2: Entregar la escama brillante al ermitaje de la isla desierta.",
                "Fase 3: Superar la prueba de oxígeno en la gruta sumergida.",
                "Fase 4: Extraer el núcleo de la marea."
            ],
            "recompensa_oculta": "Objeto Mítico: Armadura de Escamas del Leviatán Ancestral"
        },
        {
            "id": "mitica_03",
            "titulo": "??? (Cadena Oculta: El Grimorio de los Mil Eones)",
            "nivel_minimo": 75,
            "fases_totales": 6,
            "estado_conocido": "Desconocido",
            "pista_inicial": "En los estantes más altos de la Torre de los Arcanos hay libros que sangran letras de oro si se leen al revés.",
            "pasos_ocultos": [
                "Fase 1: Encontrar la página arrancada en la biblioteca prohibida.",
                "Fase 2: Traducir el idioma ancestral con ayuda del sabio ermitaño.",
                "Fase 3: Recolectar polvo de estrella caídas en las Puertas del Eón.",
                "Fase 4: Sellar el portal menor antes de que colapse.",
                "Fase 5: Derrotar al archimago corrompido.",
                "Fase 6: Vincular el grimorio al alma del invocador."
            ],
            "recompensa_oculta": "Objeto Mítico: Grimorio del Sol Eterno (Bastón Tier V)"
        },
        {
            "id": "mitica_04",
            "titulo": "??? (Cadena Oculta: La Sombra del Rey Caído)",
            "nivel_minimo": 85,
            "fases_totales": 5,
            "estado_conocido": "Desconocido",
            "pista_inicial": "Las murallas del Castillo de Hojacero vibran cuando la luna adopta un tono carmesí.",
            "pasos_ocultos": [
                "Fase 1: Infiltrarse en las catacumbas reales sin ser detectado por los guardias.",
                "Fase 2: Hallar la corona rota en el trono subterráneo.",
                "Fase 3: Soportar la maldición de la oscuridad durante 10 minutos reales.",
                "Fase 4: Vencer al Avatar del Rey en duelo cerrado.",
                "Fase 5: Reclamar el acero oscuro."
            ],
            "recompensa_oculta": "Objeto Mítico: Yermo del Monarca Absoluto (Set de Placas)"
        },
        {
            "id": "mitica_05",
            "titulo": "??? (Cadena Oculta: El Pulso del Titan de Piedra)",
            "nivel_minimo": 40,
            "fases_totales": 4,
            "estado_conocido": "Desconocido",
            "pista_inicial": "Los mineros del Baluarte Enano aseguran que las paredes de la mina inferior responden a los golpes con latidos.",
            "pasos_ocultos": [
                "Fase 1: Escuchar el eco en la veta más profunda de la mina.",
                "Fase 2: Ofrecer 100 lingotes de mithril al altar de piedra viva.",
                "Fase 3: Derrotar al Golem Guardián de Obsidiana.",
                "Fase 4: Extraer el corazón cristalino."
            ],
            "recompensa_oculta": "Objeto Mítico: Guanteletes del Coloso Inquebrantable"
        },
        {
            "id": "mitica_06",
            "titulo": "??? (Cadena Oculta: El Canto de las Sirenas del Viento)",
            "nivel_minimo": 65,
            "fases_totales": 5,
            "estado_conocido": "Desconocido",
            "pista_inicial": "En los acantilados del este, el viento sopla formando notas musicales exactas que enloquecen a los viajeros.",
            "pasos_ocultos": [
                "Fase 1: Tocar la flauta de hueso en el pico más alto del archipiélago.",
                "Fase 2: Atravesar la prueba de corrientes aéreas invisibles.",
                "Fase 3: Enfrentarse a la Arpía Reina en su nido flotante.",
                "Fase 4: Recoger la pluma de tormenta pura.",
                "Fase 5: Tejer la capa con hilos de nubes."
            ],
            "recompensa_oculta": "Objeto Mítico: Alas del Viento Celestial (Capa de Vuelo Definitiva)"
        },
        {
            "id": "mitica_07",
            "titulo": "??? (Cadena Oculta: El Ojo del Dragón Durmiente)",
            "nivel_minimo": 90,
            "fases_totales": 6,
            "estado_conocido": "Desconocido",
            "pista_inicial": "Un temblor constante sacude las Islas Brumas del Dragón cada vez que la marea baja.",
            "pasos_ocultos": [
                "Fase 1: Descifrar la escritura dracónica en las rocas volcánicas.",
                "Fase 2: Conseguir escamas de fuego sin quemarse vivo.",
                "Fase 3: Despertar al draco menor con ofrendas de carne de magma.",
                "Fase 4: Superar la prueba de fuego del sabio escamado.",
                "Fase 5: Entrar en la cámara del dragón primigenio.",
                "Fase 6: Reclamar el ojo primordial."
            ],
            "recompensa_oculta": "Objeto Mítico: Gema del Ojo de Dragón (Amuleto de Poder Absoluto)"
        },
        {
            "id": "mitica_08",
            "titulo": "??? (Cadena Oculta: Las Cenizas del Fénix Ciego)",
            "nivel_minimo": 70,
            "fases_totales": 4,
            "estado_conocido": "Desconocido",
            "pista_inicial": "Un rastro de plumas incandescentes cae desde el cielo nocturno sobre el desierto de ceniza.",
            "pasos_ocultos": [
                "Fase 1: Seguir el rastro lumínico hasta el nido calcinado.",
                "Fase 2: Recolectar las cenizas sagradas con un cáliz de plata.",
                "Fase 3: Apagar la llama maldita con lágrimas de manantial.",
                "Fase 4: Renacer junto al ave."
            ],
            "recompensa_oculta": "Objeto Mítico: Pluma de Resurrección Eterna (Anillo de Inmortalidad)"
        },
        {
            "id": "mitica_09",
            "titulo": "??? (Cadena Oculta: El Laberinto de Espejos del Tiempo)",
            "nivel_minimo": 80,
            "fases_totales": 5,
            "estado_conocido": "Desconocido",
            "pista_inicial": "En las ruinas del templo antiguo, los reflejos de los espejos muestran caminos que no existen en el mundo real.",
            "pasos_ocultos": [
                "Fase 1: Romper el espejo falso en la cámara principal.",
                "Fase 2: Encontrar tu propio reflejo corrompido y derrotarlo.",
                "Fase 3: Recorrer el laberinto sin mirar atrás.",
                "Fase 4: Sellar el portal temporal.",
                "Fase 5: Obtener el fragmento de crono."
            ],
            "recompensa_oculta": "Objeto Mítico: Reloj de Arena del Eón (Daga de Distorsión Temporal)"
        },
        {
            "id": "mitica_10",
            "titulo": "??? (Cadena Oculta: La Última Voluntad del Dios Olvidado)",
            "nivel_minimo": 95,
            "fases_totales": 7,
            "estado_conocido": "Desconocido",
            "pista_inicial": "Una runa titánica brilla en el suelo de la zona neutra de las Puertas del Eón solo cuando ningún jugador está cerca.",
            "pasos_ocultos": [
                "Fase 1: Activar la runa secreta con 4 fragmentos míticos anteriores.",
                "Fase 2: Soportar la prueba de los elementos supremos.",
                "Fase 3: Derrotar a los 3 avatares guardianes de los cielos.",
                "Fase 4: Cruzar el umbral hacia el vacío interdimensional.",
                "Fase 5: Responder al enigma del Dios Creador.",
                "Fase 6: Forjar la alianza definitiva del servidor.",
                "Fase 7: Reclamar el cetro de la creación."
            ],
            "recompensa_oculta": "Objeto Mítico Absoluto: Cetro del Creador de Mundos (Arma Definitiva)"
        }
    ]
}