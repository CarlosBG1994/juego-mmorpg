# --- CATÁLOGO DE HABILIDADES LEYENDA (TIER II) ---
# Límite: 10 portadores simultáneos por ID.
DETALLES_LEYENDA.update({
    "L012": {"Efecto": "Control de Gravedad", "Niv1": "Pulso Gravitatorio + 80% INT.", "Niv15": "Zona Cero: Inmoviliza área.", "Niv30": "Colapso: Daño 200% INT."},
    "L013": {"Efecto": "Alquimia de Sangre", "Niv1": "Daga Carmesí + 80% STR.", "Niv15": "Transfusión: Roba 15% vida.", "Niv30": "Festín de Sangre: Daño 200% STR."},
    "L014": {"Efecto": "Dominio de las Mareas", "Niv1": "Lanza de Agua + 80% DES.", "Niv15": "Corriente: Desvía proyectiles.", "Niv30": "Tsunami: Daño área 200% DES."},
    "L015": {"Efecto": "Bendición del Trueno", "Niv1": "Chispa Volt + 80% INT.", "Niv15": "Campo Estático: Aturde al golpear.", "Niv30": "Tormenta Final: Daño 200% INT."},
    "L016": {"Efecto": "Pacto del Vacío", "Niv1": "Toque Vacío + 80% AGI.", "Niv15": "Sustitución: Teletransporte al recibir daño.", "Niv30": "Explosión Vacía: 200% AGI + Silencio."},
    "L017": {"Efecto": "Canto de la Resistencia", "Niv1": "Melodía de Valor + 80% VIT.", "Niv15": "Aura de Hierro: +20% defensa equipo.", "Niv30": "Himno Final: Curación masiva 200% VIT."}
})

# --- CATÁLOGO DE HABILIDADES ÉPICAS (TIER 0) ---
# Límite: SOLO 1 JUGADOR por ID. Máximo poder del juego.
DETALLES_EPICAS = {
    "E001": { # El Trono del Nexo
        "Nombre": "Singularidad del Rey Antiguo",
        "Efecto": "El usuario manipula la realidad del campo de batalla.",
        "Niv1": "Onda de Realidad + 150% de todos los stats.",
        "Niv15": "Stasis: Detiene el tiempo para los enemigos por 4s.",
        "Niv30": "Borrado Existencial: Daño masivo 400% ATK + Ejecución directa."
    },
    "E002": { # El Último Aliento
        "Nombre": "Avatar del Dios Caído",
        "Efecto": "Transformación total en un ser de energía primigenia.",
        "Niv1": "Golpe Divino + 150% STR.",
        "Niv15": "Inmortalidad: Invulnerabilidad total 6s.",
        "Niv30": "Juicio del Cosmos: Daño global (mapa entero) 400% INT."
    }
}
