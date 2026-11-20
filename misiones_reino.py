# --- SISTEMA MAESTRO DE MISIONES, CADENAS ENCADENADAS, MÍTICAS Y LLAVES DE CONTINENTE (misiones_reino.py) ---

SISTEMA_MISIONES = {
    "principales": [
        {
            "id": "mq_01",
            "titulo": "El Despertar en Valoria",
            "nivel_requerido": 1,
            "continente": "Continente I: Reinos Fundacionales y Zonas Neutras",
            "zona": "Reino Humano de Valoria",
            "descripcion": (
                "La guerra de los Eones vuelve a agitar las fronteras. Aurelia Capital refuerza "
                "sus defensas mientras criaturas errantes asedian las rutas iniciales."
            ),
            "objetivo": "Reportarte en Aurelia Capital y repeler 5 amenazas de vanguardia en Valoria.",
            "prerequisito_id": None,
            "recompensa": {"exp": 600, "oro": 200, "item": "Emblema de Vanguardia de Valoria"},
        },
        {
            "id": "mq_02",
            "titulo": "Las Raíces Corruptas del Bosque Ancestral",
            "nivel_requerido": 16,
            "continente": "Continente I: Reinos Fundacionales y Zonas Neutras",
            "zona": "Bosque Ancestral de Elfos",
            "descripcion": (
                "Una sombra antinatural se filtra bajo el dosel élfico, alterando a las criaturas "
                "del bosque y corrompiendo los antiguos santuarios."
            ),
            "objetivo": "Rastrear el foco de corrupción en el Bosque Ancestral y purificar los altares.",
            "prerequisito_id": "mq_01",
            "recompensa": {"exp": 2400, "oro": 850, "item": "Sello del Guardián Silvestre"},
        },
        {
            "id": "mq_03",
            "titulo": "El Eco de Hierro en las Profundidades",
            "nivel_requerido": 31,
            "continente": "Continente I: Reinos Fundacionales y Zonas Neutras",
            "zona": "Baluarte Enano de Piedra",
            "descripcion": (
                "Desde las galerías inferiores del Baluarte Enano llegan vibraciones rítmicas que "
                "no pertenecen a ningún derrumbe natural."
            ),
            "objetivo": "Descender a los niveles profundos y asegurar la forja principal.",
            "prerequisito_id": "mq_02",
            "recompensa": {"exp": 5200, "oro": 1800, "item": "Martillo de Runas de Piedra"},
        },
        {
            "id": "mq_04",
            "titulo": "Fractura en la Torre de los Arcanos",
            "nivel_requerido": 46,
            "continente": "Continente I: Reinos Fundacionales y Zonas Neutras",
            "zona": "Dominio de los Magos",
            "descripcion": (
                "Los archivos arcanos registran interferencias dimensionales cerca de las Puertas del Eón, "
                "señal de que el equilibrio entre continentes está tensándose."
            ),
            "objetivo": "Estabilizar los cristales de contención y presentar el informe a los arcanos.",
            "prerequisito_id": "mq_03",
            "recompensa": {"exp": 9500, "oro": 3500, "item": "Tomo de las Líneas del Eón"},
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
            "zona": "Reino Humano de Valoria",
            "titulo": "Mapas Rasgados del Camino Real",
            "descripcion": (
                "Un viejo cartógrafo perdió la mitad de sus planos de ruta cerca de los lindes "
                "del reino. Solo se puede completar una vez."
            ),
            "objetivo": "Recuperar los 3 fragmentos de mapa extraviados (0/3).",
            "recompensa": {"exp": 800, "oro": 300, "item": "Fragmento de Mapa I"},
        },
        {
            "id": "sec_cad_01b",
            "cadena": "La Deuda del Cartógrafo",
            "paso": 2,
            "unica_vez": True,
            "prerequisito_mision_id": "sec_cad_01a",
            "desbloquea_mision_id": "sec_cad_01c",
            "nivel_requerido": 12,
            "zona": "Bosque Ancestral de Elfos",
            "titulo": "El Sendero que No Figura en las Cartas",
            "descripcion": (
                "Con el primer mapa recompuesto, aparece una anotación en tinta invisible que apunta "
                "hacia un cruce olvidado del bosque. Requiere haber completado 'Mapas Rasgados del Camino Real'."
            ),
            "objetivo": "Localizar el hito oculto del sendero y verificar las marcas antiguas.",
            "recompensa": {"exp": 1900, "oro": 700, "item": "Brújula de Tinta Oculta"},
        },
        {
            "id": "sec_cad_01c",
            "cadena": "La Deuda del Cartógrafo",
            "paso": 3,
            "unica_vez": True,
            "prerequisito_mision_id": "sec_cad_01b",
            "desbloquea_mision_id": None,
            "nivel_requerido": 22,
            "zona": "Archipiélago y Mazmorras del Mar Abierto",
            "titulo": "El Cofre del Vigía Costero",
            "descripcion": (
                "Cierre definitivo de la cadena del cartógrafo (única vez). Solo accesible tras completar "
                "'El Sendero que No Figura en las Cartas'."
            ),
            "objetivo": "Abrir el alijo sellado en el islote del vigía y entregar el registro.",
            "recompensa": {"exp": 4200, "oro": 1600, "item": "Anillo del Explorador Olvidado"},
        },
        {
            "id": "sec_cad_02a",
            "cadena": "Juramento de los Vigilantes",
            "paso": 1,
            "unica_vez": True,
            "prerequisito_mision_id": None,
            "desbloquea_mision_id": "sec_cad_02b",
            "nivel_requerido": 18,
            "zona": "Baluarte Enano de Piedra",
            "titulo": "Herramientas de la Vieja Guardia",
            "descripcion": (
                "Una misión de una sola ejecución para rearmar a los centinelas de vanguardia."
            ),
            "objetivo": "Reunir 12 lingotes y piezas de forja (0/12).",
            "recompensa": {"exp": 2300, "oro": 900, "item": "Vale de la Guardia"},
        },
        {
            "id": "sec_cad_02b",
            "cadena": "Juramento de los Vigilantes",
            "paso": 2,
            "unica_vez": True,
            "prerequisito_mision_id": "sec_cad_02a",
            "desbloquea_mision_id": None,
            "nivel_requerido": 28,
            "zona": "Puertas del Eón",
            "titulo": "Puesto Avanzado en la Frontera",
            "descripcion": (
                "Solo disponible tras completar 'Herramientas de la Vieja Guardia'. De una única realización."
            ),
            "objetivo": "Asegurar el perímetro del puesto fronterizo sin que caigan las balizas.",
            "recompensa": {"exp": 4800, "oro": 2100, "item": "Capa del Centinela del Eón"},
        },
    ],
    "diarias_y_caza": [
        {
            "id": "sq_diaria_01",
            "tipo": "Diaria - Recolección",
            "titulo": "Suministros para la Guardia",
            "nivel": "1+",
            "descripcion": "Reúne materiales básicos para el mantenimiento de murallas y puestos.",
            "objetivo": "Recolectar Mineral de Hierro (0/10)",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 450, "oro": 120},
        },
        {
            "id": "sq_diaria_02",
            "tipo": "Diaria - Caza de Jefes",
            "titulo": "Bestia de la Cima: El Alfa de las Nieves",
            "nivel": "30+",
            "descripcion": "Un depredador dominante merodea cerca de las rutas elevadas.",
            "objetivo": "Derrotar al Jefe de Zona marcado",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 3600, "oro": 1500, "item": "Colmillo de Escarcha"},
        },
        {
            "id": "sq_diaria_03",
            "tipo": "Cazarrecompensas - Tribunal de Normas",
            "titulo": "Orden de Arresto: Forajidos y PKs",
            "nivel": "20+",
            "descripcion": "Da caza a infractores marcados que quebrantan el orden en zonas vigiladas.",
            "objetivo": "Neutralizar al Forajido Marcado",
            "reinicio": "1 vez al día",
            "recompensa": {"exp": 2200, "oro": 1300, "reputacion": "+50 Justicia"},
        },
    ],
    "ocultas_miticas": [
        {
            "id": "mitica_01",
            "titulo": "??? (Mítica Oculta: El Eco del Sol Invictus)",
            "nivel_minimo": 50,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Dicen que un ciego junto a las fuentes de Aurelia responde solo a quien llega sin armas desenvainadas y con una ofrenda específica.",
            "condicion_activacion_oculta": (
                "Hablar con el PNJ anónimo en los suburbios tras completar 'El Despertar en Valoria', "
                "llevar 500 de oro y activar el diálogo oculto en horario nocturno."
            ),
            "fases_totales": 5,
            "recompensa_mitica": "Sol Invictus (Espada Mítica de Fuego Estelar)",
        },
        {
            "id": "mitica_02",
            "titulo": "??? (Mítica Oculta: Las Lágrimas del Abismo Marino)",
            "nivel_minimo": 60,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "En la costa del archipiélago, ciertos reflejos bajo el agua solo aparecen cuando la marea está baja y llevas equipo de exploración.",
            "condicion_activacion_oculta": (
                "Inspeccionar el pecio sumergido del archipiélago portando la Brújula de Tinta Oculta "
                "y derrotar al guardián de las profundidades."
            ),
            "fases_totales": 4,
            "recompensa_mitica": "Coraza de Escamas del Leviatán Ancestral",
        },
        {
            "id": "mitica_03",
            "titulo": "??? (Mítica Oculta: El Grimorio de los Mil Eones)",
            "nivel_minimo": 75,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "En el Dominio de los Magos, un estante sellado reacciona al orden exacto en que se tocan cuatro tomos apagados.",
            "condicion_activacion_oculta": (
                "Completar 'Fractura en la Torre de los Arcanos' e interactuar con los cuatro tomos "
                "siguiendo la secuencia rúnica de los elementos."
            ),
            "fases_totales": 6,
            "recompensa_mitica": "Grimorio del Sol Eterno",
        },
        {
            "id": "mitica_04",
            "titulo": "??? (Mítica Oculta: La Sombra del Rey Caído)",
            "nivel_minimo": 85,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Las murallas antiguas susurran nombres de generales olvidados cuando cae la noche sobre la fortaleza.",
            "condicion_activacion_oculta": (
                "Cruzar el patio interior sin activar alertas y examinar el altar de piedra agrietado."
            ),
            "fases_totales": 5,
            "recompensa_mitica": "Yelmo del Monarca Absoluto",
        },
        {
            "id": "mitica_05",
            "titulo": "??? (Mítica Oculta: El Pulso del Titán de Piedra)",
            "nivel_minimo": 40,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Bajo el Baluarte Enano, los golpes de pico en una veta estéril devuelven un eco metálico distinto al resto.",
            "condicion_activacion_oculta": (
                "Golpear la veta resonante tras haber completado 'Juramento de los Vigilantes' y ofrecer mineral puro."
            ),
            "fases_totales": 4,
            "recompensa_mitica": "Guanteletes del Coloso Inquebrantable",
        },
        {
            "id": "mitica_06",
            "titulo": "??? (Mítica Oculta: El Canto de las Sirenas del Viento)",
            "nivel_minimo": 65,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "En los acantilados expuestos al viento, la brisa forma acordes que abren una grieta en la roca.",
            "condicion_activacion_oculta": (
                "Alcanzar el mirador del acantilado con montura rápida y responder al eco de las corrientes."
            ),
            "fases_totales": 5,
            "recompensa_mitica": "Alas del Viento Celestial",
        },
        {
            "id": "mitica_07",
            "titulo": "??? (Mítica Oculta: El Ojo del Dragón Durmiente)",
            "nivel_minimo": 90,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Solo quienes han superado pruebas de fuego y abismos logran percibir el calor latente bajo la ceniza.",
            "condicion_activacion_oculta": (
                "Reunir 3 fragmentos dracónicos y despertar el sello ígneo en la zona más profunda."
            ),
            "fases_totales": 6,
            "recompensa_mitica": "Gema del Ojo de Dragón",
        },
        {
            "id": "mitica_08",
            "titulo": "??? (Mítica Oculta: Las Cenizas del Fénix Ciego)",
            "nivel_minimo": 70,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Un rastro de brasas que no quema aparece únicamente tras derrotar élites sin recibir daño letal.",
            "condicion_activacion_oculta": (
                "Localizar el nido de ceniza y purificar el brasero con agua de manantial."
            ),
            "fases_totales": 4,
            "recompensa_mitica": "Anillo de Resurrección Eterna",
        },
        {
            "id": "mitica_09",
            "titulo": "??? (Mítica Oculta: El Laberinto de Espejos del Tiempo)",
            "nivel_minimo": 80,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "Los espejos antiguos muestran un pasillo que no existe cuando miras de frente, pero sí de reojo.",
            "condicion_activacion_oculta": (
                "Encontrar el espejo verdadero entre las ilusiones y romper el reflejo anómalo."
            ),
            "fases_totales": 5,
            "recompensa_mitica": "Reloj de Arena del Eón",
        },
        {
            "id": "mitica_10",
            "titulo": "??? (Mítica Oculta: La Última Voluntad del Dios Olvidado)",
            "nivel_minimo": 95,
            "estado": "Oculta — Activación secreta no revelada",
            "pista_rumor": "En las Puertas del Eón, una inscripción apenas visible aguarda a quienes dominan los secretos de los reinos.",
            "condicion_activacion_oculta": (
                "Haber resuelto múltiples cadenas míticas previas e invocar el glifo en el umbral del Eón."
            ),
            "fases_totales": 7,
            "recompensa_mitica": "Cetro del Creador de Mundos",
        },
    ],
    "llaves_continente": [
        {
            "id": "llave_cont_02",
            "continente_objetivo": "Continente II: Tierras de Ceniza y Abismos Antiguos",
            "titulo": "??? (Misión Oculta de Paso: El Umbral de Ceniza)",
            "nivel_minimo": 90,
            "estado": "Oculta — Requiere descubrir y activar el ritual de paso",
            "pista_rumor": (
                "Las Puertas del Eón permanecen cerradas a la fuerza bruta. Quienes logran cruzar hacia "
                "las Tierras de Ceniza hablan de un sello antiguo que exige demostrar dominio sobre "
                "las pruebas de los Reinos Fundacionales y despertar al menos 3 Míticas Ocultas."
            ),
            "condicion_activacion_oculta": (
                "Completar el arco principal del Continente I, alcanzar el umbral de misiones requerido, "
                "activar la baliza oculta de las Puertas del Eón y superar la prueba del guardián del umbral."
            ),
            "recompensa": {
                "exp": 25000,
                "oro": 10000,
                "desbloquea": "Continente II: Tierras de Ceniza y Abismos Antiguos",
            },
        },
        {
            "id": "llave_cont_03",
            "continente_objetivo": "Continente III: El Dominio Celestial y Grietas del Vacío",
            "titulo": "??? (Misión Oculta de Paso: La Ascensión del Vacío)",
            "nivel_minimo": 190,
            "estado": "Oculta — Requiere descubrir y activar el ritual celestial",
            "pista_rumor": (
                "El Dominio Celestial no se abre con mapas ordinarios. Solo quienes han domado las "
                "Tierras de Ceniza, reunido los ecos míticos ocultos y descifrado las grietas "
                "encontrarán el conducto hacia las alturas."
            ),
            "condicion_activacion_oculta": (
                "Completar el progreso exigido en el Continente II, resolver la totalidad de las 10 Míticas Ocultas "
                "y armonizar los tres núcleos de la grieta."
            ),
            "recompensa": {
                "exp": 75000,
                "oro": 30000,
                "desbloquea": "Continente III: El Dominio Celestial y Grietas del Vacío",
            },
        },
    ],
}


def obtener_secundarias_disponibles(misiones_completadas_ids):
    """
    Devuelve solo las misiones secundarias de única vez que:
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