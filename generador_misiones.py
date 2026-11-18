# --- GENERADOR AUTOMÁTICO DE MISIONES Y CONTROL DE PROGRESIÓN MULTICONTINENTE ---
import json
import random

CONTINENTES_MUNDO = {
    "Continente I: Reinos Fundacionales y Zonas Neutras": {
        "rango_niveles": (1, 100),
        "min_misiones_para_desbloquear": 0,
        "min_miticas_para_desbloquear": 0,
        "zonas": [
            "Reino Humano de Valoria", "Bosque Ancestral de Elfos", 
            "Baluarte Enano de Piedra", "Torre de los Arcanos", 
            "Puertas del Eón", "Archipiélago del Mar Abierto"
        ]
    },
    "Continente II: Tierras de Ceniza y Abismos Antiguos": {
        "rango_niveles": (101, 200),
        "min_misiones_para_desbloquear": 50,
        "min_miticas_para_desbloquear": 3,
        "zonas": [
            "Desierto de Obsidiana", "Cavernas del Dragón Ciego", 
            "Ciudadela del Rey Caído", "Fosas Abisales del Titán", 
            "Picos de los Vientos Eternos"
        ]
    },
    "Continente III: El Dominio Celestial y Grietas del Vacío": {
        "rango_niveles": (201, 300),
        "min_misiones_para_desbloquear": 120,
        "min_miticas_para_desbloquear": 10,
        "zonas": [
            "Santuario de las Estrellas Caídas", "Bastión Interdimensional", 
            "Jardines del Dios Olvidado", "Grieta Cuántica del Eón", 
            "Catedral del Creador"
        ]
    }
}

tipos_mision = ["Caza", "Recolección", "Exploración", "Cazarrecompensas de Normas", "Invasión de Grieta"]
adj_criaturas = ["Feroz", "Corrupto", "Salvaje", "Sombreado", "Ancestral", "Abisal", "Mutado", "Divino"]
criaturas = ["Goblin", "Lobo Huargo", "Slime Ácido", "Ent de la Sombra", "Espectro Errante", "Draco Menor", "Bandido Forajido", "Guardián del Vacío"]
materiales = ["Mineral de Hierro", "Esencia de Roble", "Cristal de Maná", "Escama de Fuego", "Pluma de Tormenta", "Esencia Estelar"]

def verificar_acceso_continente(nombre_continente, misiones_completadas, miticas_resueltas):
    datos = CONTINENTES_MUNDO.get(nombre_continente)
    if not datos:
        return False, "Continente desconocido."
    
    req_misiones = datos["min_misiones_para_desbloquear"]
    req_miticas = datos["min_miticas_para_desbloquear"]
    
    if misiones_completadas >= req_misiones and miticas_resueltas >= req_miticas:
        return True, "Acceso Autorizado"
    else:
        return False, f"🔒 Bloqueado: Requiere completar al menos {req_misiones} misiones generales y resolver {req_miticas} Misiones Míticas Ocultas del continente anterior."

def generar_mision_multicontinente(id_mision):
    nombre_continente = random.choice(list(CONTINENTES_MUNDO.keys()))
    datos_cont = CONTINENTES_MUNDO[nombre_continente]
    
    zona = random.choice(datos_cont["zonas"])
    min_nv, max_nv = datos_cont["rango_niveles"]
    nivel = random.randint(min_nv, max_nv)
    tipo = random.choice(tipos_mision)
    
    if tipo == "Caza":
        criatura = f"{random.choice(adj_criaturas)} {random.choice(criaturas)}"
        cantidad = random.randint(10, 30)
        titulo = f"Caza de Élite: {criaturas[0]} en {zona}"
        descripcion = f"Amenaza crítica en {zona} ({nombre_continente}). Elimina {cantidad} unidades de {criatura}."
        objetivo = f"Eliminar {criatura} (0/{cantidad})"
    elif tipo == "Recolección":
        material = random.choice(materiales)
        cantidad = random.randint(5, 20)
        titulo = f"Recursos Avanzados: {material}"
        descripcion = f"Se requieren suministros de {material} recolectados en las peligrosas tierras de {zona}."
        objetivo = f"Recolectar {material} (0/{cantidad})"
    elif tipo == "Cazarrecompensas de Normas":
        titulo = f"Orden de Arresto Global: Forajido Nv. {nivel}"
        descripcion = f"Un infractor de alto rango ha violado las leyes del servidor en {zona}. Neutralízalo."
        objetivo = "Neutralizar al Forajido Marcado"
    else:
        titulo = f"Exploración de Frontera: {zona}"
        descripcion = f"Cartografía las anomalías dimensionales y asegura las balizas en {zona}."
        objetivo = "Inspeccionar las 4 balizas de reconocimiento"

    oro = nivel * random.randint(50, 120)
    exp = nivel * random.randint(300, 700)

    return {
        "id": f"mc_proc_{id_mision:06d}",
        "continente": nombre_continente,
        "zona": zona,
        "titulo": titulo,
        "nivel_requerido": nivel,
        "tipo": tipo,
        "descripcion": descripcion,
        "objetivo": objetivo,
        "recompensa": {"exp": exp, "oro": oro}
    }

if __name__ == "__main__":
    misiones = [generar_mision_multicontinente(i) for i in range(1, 10001)]
    with open("misiones_multicontinente.json", "w", encoding="utf-8") as f:
        json.dump(misiones, f, ensure_ascii=False, indent=4)
    print("✅ 10,000 Misiones multicontinente generadas correctamente.")