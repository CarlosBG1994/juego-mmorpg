# --- SISTEMA MAESTRO DE MISIONES (misiones_reino.py) ---

SISTEMA_MISIONES = {
    "principales": [
        {
            "id": "mq_inicial_01",
            "titulo": "El Despertar en las Tierras del Origen",
            "nivel_requerido": 1,
            "continente": "Continente Inicial: Tierras del Origen (Niveles 1–100)",
            "zona": "Valoria Inicial",
            "descripcion": (
                "Los aventureros despiertan en el Continente Inicial mientras las grietas del Eón "
                "comienzan a resonar a lo largo de los niveles 1–100."
            ),
            "objetivo": "Establecer tu base en Valoria Inicial y superar las pruebas iniciales del territorio.",
            "prerequisito_id": None,
            "recompensa": {"exp": 800, "oro": 250, "item": "Emblema del Viajero del Origen"},
        },
        {
            "id": "mq_inicial_02",
            "titulo": "El Llamado de las Cuatro Fronteras",
            "nivel_requerido": 65,
            "continente": "Continente Inicial: Tierras del Origen (Niveles 1–100)",
            "zona": "Puertas del Eón",
            "descripcion": (
                "Las rutas hacia los cuatro continentes raciales aguardan ser abiertas; el orden "
                "en que se despierten marcará la escalada de niveles (101–150, 151–200, 201–250 y 251–300)."
            ),
            "objetivo": "Investigar las cuatro sendas en las Puertas del Eón y reunir los registros de frontera.",
            "prerequisito_id": "mq_inicial_01",
            "recompensa": {"exp": 4500, "oro": 1500, "item": "Compás de los Cuatro Caminos"},
        },
        {
            "id": "mq_racial_humano",
            "titulo": "Corona de Hierro de Aurelia",
            "nivel_requerido": 101,
            "continente": "Continente Racial Humano",
            "zona": "Aurelia Capital",
            "descripcion": "Restaura el orden en el bastión humano cuando su umbral de niveles esté activo.",
            "objetivo": "Asegurar Aurelia Capital y repeler la ofensiva de las murallas.",
            "prerequisito_id": "mq_inicial_02",
            "recompensa": {"exp": 12000, "oro": 4000, "item": "Estandarte de Aurelia"},
        },
        {
            "id": "mq_racial_elfico",
            "titulo": "El Canto del Árbol Madre",
            "nivel_requerido": 101,
            "continente": "Continente Racial Élfico",
            "zona": "Santuario Silvestre",
            "descripcion": "Purifica los santuarios élficos y protege el equilibrio natural del continente.",
            "objetivo": "Sellar las raíces corruptas en el Santuario Silvestre.",
            "prerequisito_id": "mq_inicial_02",
            "recompensa": {"exp": 12000, "oro": 4000, "item": "Reliquia Silvestre"},
        },
        {
            "id": "mq_racial_enano",
            "titulo": "El Corazón de la Gran Forja",
            "nivel_requerido": 101,
            "continente": "Continente Racial Enano",
            "zona": "Baluarte de Piedra",
            "descripcion": "Reaviva los hornos ancestrales en las profundidades del reino enano.",
            "objetivo": "Defender las galerías de fundición y restaurar el núcleo rúnico.",
            "prerequisito_id": "mq_inicial_02",
            "recompensa": {"exp": 12000, "oro": 4000, "item": "Yunque de Piedra Viva"},
        },
        {
            "id": "mq_racial_draconico",
            "titulo": "El Pacto de los Cielos Escamados",
            "nivel_requerido": 101,
            "continente": "Continente Racial Dracónico",
            "zona": "Cumbre de Escamas",
            "descripcion": "Demuestra valía ante los guardianes dracónicos en las cumbres volcánicas.",
            "objetivo": "Superar la prueba de las cumbres y encender el altar dracónico.",
            "prerequisito_id": "mq_inicial_02",
            "recompensa": {"exp": 12000, "oro": 4000, "item": "Blasón de Escamas"},
        },
        {
            "id": "mq_demoniaco_01",
            "titulo": "Las Fauces del Abismo (301–350)",
            "nivel_requerido": 301,
            "continente": "Continente Demoníaco: Abismo Ígneo (Niveles 301–350)",
            "zona": "Fosas del Abismo",
            "descripcion": (
                "Con los continentes previos abiertos y las principales superadas, el frente demoníaco "
                "exige enfrentar horrores de nivel 301 a 350."
            ),
            "objetivo": "Avanzar por las Fosas del Abismo y quebrar la vanguardia demoníaca.",
            "prerequisito_id": None,
            "recompensa": {"exp": 45000, "oro": 18000, "item": "Fragmento del Abismo"},
        },
        {
            "id": "mq_angelical_01",
            "titulo": "El Ascenso a la Ciudadela Celestial",
            "nivel_requerido": 350,
            "continente": "Continente Angelical: Ciudadela Celestial (Final)",
            "zona": "Pináculo de Luz",
            "descripcion": (
                "Misión culminante tras abrir todos los continentes anteriores, completar sus "
                "principales y resolver las misiones ocultas de apertura angelical."
            ),
            "objetivo": "Alcanzar el Pináculo de Luz y completar el juicio celestial.",
            "prerequisito_id": "mq_demoniaco_01",
            "recompensa": {"exp": 120000, "oro": 50000, "item": "Corona del Alba Eterna"},
        },
    ],
    "secundarias_encadenadas": [
        {
            "id": "sec_cad_01a",
            "cadena": "La Deuda del Cartógrafo",
            "paso": 1,
            "unica_vez": True,
            "prerequisito_mision_id": None,
            "desbloquea_mision_id": "sec_cad_01b",
            "nivel_requerido": 5,
            "zona": "Valoria Inicial",
            "titulo": "Mapas Rasgados del Camino Real",
            "descripcion": "Secundaria de única vez. Al completarla se abre el segundo encargo del cartógrafo.",
            "objetivo": "Recuperar los 3 fragmentos de mapa extraviados (0/3).",
            "recompensa": {"exp": 900, "oro": 350, "item": "Fragmento de Mapa I"},
        },
        {
            "id": "sec_cad_01b",
            "cadena": "La Deuda del Cartógrafo",
            "paso": 2,
            "unica_vez": True,
            "prerequisito_mision_id": "sec_cad_01a",
            "desbloquea_mision_id": "sec_cad_01c",
            "nivel_requerido": 15,
            "zona": "Bosque de Bruma",
            "titulo": "El Sendero que No Figura en las Cartas",
            "descripcion": "Solo disponible tras completar 'Mapas Rasgados del Camino Real'. De única vez.",
            "objetivo": "Encontrar el hito oculto entre la bruma y verificar sus marcas.",
            "recompensa": {"exp": 2100, "oro": 750, "item": "Brújula de Tinta Oculta"},
        },
        {
            "id": "sec_cad_01c",
            "cadena": "La Deuda del Cartógrafo",
            "paso": 3,
            "unica_vez": True,
            "prerequisito_mision_id": "sec_cad_01b",
            "desbloquea_mision_id": None,
            "nivel_requerido": 28,
            "zona": "Puertas del Eón",
            "titulo": "El Alijo del Vigía Olvidado",
            "descripcion": "Cierre de única vez de la cadena; exige haber completado 'El Sendero que No Figura en las Cartas'.",
            "objetivo": "Abrir el cofre sellado del vigía y entregar su bitácora.",
            "recompensa": {"exp": 4800, "oro": 1800, "item": "Anillo del Rastreador"},
        },
        {
            "id": "sec_cad_02a",
            "cadena": "Juramento de los Vigilantes",
            "paso": 1,
            "unica_vez": True,
            "prerequisito_mision_id": None,
            "desbloquea_mision_id": "sec_cad_02b",
            "nivel_requerido": 20,
            "zona": "Llanuras del Comienzo",
            "titulo": "Acero para los Puestos Avanzados",
            "descripcion": "Misión secundaria de una sola realización que abre la siguiente fase de la guardia.",
            "objetivo": "Entregar 12 lotes de hierro forjado (0/12).",
            "recompensa": {"exp": 2500, "oro": 950, "item": "Vale del Centinela"},
        },
        {
            "id": "sec_cad_02b",
            "cadena": "Juramento de los Vigilantes",
            "paso": 2,
            "unica_vez": True,
            "prerequisito_mision_id": "sec_cad_02a",
            "desbloquea_mision_id": None,
            "nivel_requerido": 35,
            "zona": "Puertas del Eón",
            "titulo": "Guardia Nocturna en el Umbral",
            "descripcion": "Requiere completar 'Acero para los Puestos Avanzados'. Solo se puede hacer una vez.",
            "objetivo": "Mantener segura la baliza fronteriza durante la incursión.",
            "recompensa": {"exp": 5400, "oro": 2200, "item": "Capa del Guardián Fronterizo"},
        },
    ],
    "diarias_y_caza": [
        {
            "id": "sq_diaria_01",
            "tipo": "Diaria - Recolección",
            "titulo": "Suministros para la Guardia",
            "nivel": "1+",
            "descripcion": "Recolecta materiales básicos para mantener operativas las rutas.",
            "objetivo": "Recolectar Mineral de Hierro (0/10)",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 450, "oro": 120},
        },
        {
            "id": "sq_diaria_02",
            "tipo": "Diaria - Caza de Jefes",
            "titulo": "Bestia de la Cima: El Alfa de las Nieves",
            "nivel": "40+",
            "descripcion": "Elimina al jefe de zona que amenaza las rutas de suministros.",
            "objetivo": "Derrotar al Jefe de Zona marcado",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 4200, "oro": 1600, "item": "Colmillo de Escarcha"},
        },
        {
            "id": "sq_diaria_03",
            "tipo": "Cazarrecompensas - Tribunal de Normas",
            "titulo": "Orden de Arresto: Forajidos y PKs",
            "nivel": "25+",
            "descripcion": "Neutraliza a infractores marcados que rompan las normas en zonas vigiladas.",
            "objetivo": "Neutralizar al Forajido Marcado",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 2600, "oro": 1400, "reputacion": "+50 Justicia"},
        },
    ],
    "ocultas_miticas": [
        {
            "id": "mitica_01",
            "titulo": "??? (Mítica Oculta: El Eco del Sol Invictus)",
            "nivel_minimo": 50,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Un anciano ciego junto a las fuentes responde solo a quien llega con una ofrenda precisa y sin provocar disturbios.",
            "condicion_activacion_oculta": "Completar la cadena del cartógrafo, portar 500 de oro y activar el diálogo oculto en el punto exacto.",
            "fases_totales": 5,
            "recompensa_mitica": "Sol Invictus (Espada Mítica de Fuego Estelar)",
        },
        {
            "id": "mitica_02",
            "titulo": "??? (Mítica Oculta: Las Lágrimas del Abismo Marino)",
            "nivel_minimo": 70,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Ciertos reflejos bajo el agua solo se revelan al inspeccionar el pecio con la Brújula de Tinta Oculta.",
            "condicion_activacion_oculta": "Poseer la Brújula de Tinta Oculta e inspeccionar el altar sumergido.",
            "fases_totales": 4,
            "recompensa_mitica": "Coraza de Escamas del Leviatán Ancestral",
        },
        {
            "id": "mitica_03",
            "titulo": "??? (Mítica Oculta: El Grimorio de los Mil Eones)",
            "nivel_minimo": 110,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Cuatro tomos apagados en un santuario antiguo responden a una secuencia rúnica concreta.",
            "condicion_activacion_oculta": "Activar los cuatro glifos en orden inverso a la lectura habitual.",
            "fases_totales": 6,
            "recompensa_mitica": "Grimorio del Sol Eterno",
        },
        {
            "id": "mitica_04",
            "titulo": "??? (Mítica Oculta: La Sombra del Rey Caído)",
            "nivel_minimo": 140,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Las murallas antiguas vibran cuando examinas el altar agrietado sin activar alertas.",
            "condicion_activacion_oculta": "Cruzar el patio sin ser detectado e interactuar con el sello del trono.",
            "fases_totales": 5,
            "recompensa_mitica": "Yelmo del Monarca Absoluto",
        },
        {
            "id": "mitica_05",
            "titulo": "??? (Mítica Oculta: El Pulso del Titán de Piedra)",
            "nivel_minimo": 120,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Una veta aparentemente estéril devuelve un eco metálico al golpearla con precisión.",
            "condicion_activacion_oculta": "Completar 'Juramento de los Vigilantes' y ofrendar mineral puro en la veta resonante.",
            "fases_totales": 4,
            "recompensa_mitica": "Guanteletes del Coloso Inquebrantable",
        },
    ],
    "ocultas_apertura_continentes": [
        {
            "id": "oculta_abrir_racial",
            "objetivo_tipo": "Continentes Raciales (101–150 / 151–200 / 201–250 / 251–300)",
            "titulo": "??? (Misión Oculta: El Sello de los Cuatro Umbrales)",
            "estado": "Oculta — Requiere descubrir el detonante de cada frontera racial",
            "pista_rumor": (
                "Cada continente racial (Humano, Élfico, Enano o Dracónico) guarda un ritual de apertura "
                "oculto. El primero en abrirse toma el tramo 101–150, el segundo 151–200, el tercero 201–250 "
                "y el cuarto 251–300."
            ),
            "condicion_activacion_oculta": (
                "Reunir los indicios de frontera en las Puertas del Eón, superar la prueba del sello racial "
                "y activar el portal correspondiente."
            ),
        },
        {
            "id": "oculta_abrir_demoniaco",
            "objetivo_tipo": "Continente Demoníaco (301–350)",
            "titulo": "??? (Misión Oculta: La Llave de Ceniza y Sangre)",
            "estado": "Oculta — Requiere continentes previos abiertos y principales completadas",
            "pista_rumor": (
                "El paso al Continente Demoníaco (301–350) permanece sellado hasta que estén abiertos "
                "los continentes anteriores y al menos un jugador haya completado todas las misiones "
                "principales abiertas."
            ),
            "condicion_activacion_oculta": (
                "Tener abiertos el Continente Inicial y los 4 Raciales, contar con al menos 1 jugador que "
                "haya completado todas las misiones principales abiertas y encender el brasero abisal."
            ),
        },
        {
            "id": "oculta_abrir_angelical",
            "objetivo_tipo": "Continente Angelical (Final)",
            "titulo": "??? (Misión Oculta: El Juicio de las Estrellas Caídas)",
            "estado": "Oculta — Requiere todos los continentes abiertos, principales hechas y ocultas previas",
            "pista_rumor": (
                "Solo quienes han abierto todos los continentes anteriores, completado sus misiones "
                "principales y descifrado las misiones ocultas específicas pueden despertar el ascenso "
                "al Continente Angelical."
            ),
            "condicion_activacion_oculta": (
                "Tener abiertos todos los continentes previos (incluyendo el Demoníaco), completar todas "
                "las misiones principales y resolver las misiones ocultas específicas de apertura."
            ),
        },
    ],
}


def obtener_secundarias_disponibles(misiones_completadas_ids):
    """
    Devuelve únicamente las misiones secundarias de única vez que:
    1) No han sido completadas aún (`unica_vez=True`).
    2) Cumplen su `prerequisito_mision_id` (si tienen uno).
    """
    completadas = set(misiones_completadas_ids)
    disponibles = []
    for mision in SISTEMA_MISIONES["secundarias_encadenadas"]:
        if mision.get("unica_vez") and mision["id"] in completadas:
            continue
        prereq = mision.get("prerequisito_mision_id")
        if prereq is not None and prereq not in completadas:
            continue
        disponibles.append(mision)
    return disponibles