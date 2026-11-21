from modulos.integrador import Jugador
from modulos.historia_lore import obtener_prologo_jugador
from modulos.misiones import GestorMisiones

def ejecutar_juego():
    print("\n--- BIENVENIDO A SND-WORLDS ---")
    nombre = input("Nombre de tu aventurero: ")
    raza = input("Raza (Humano, Elfo, Enano, Hombre Bestia): ")
    clase = input("Clase: ")
    
    try:
        pj = Jugador(nombre, raza, clase)
        gestor = GestorMisiones()
        
        print("\n--- CARGANDO MUNDO ---")
        print(obtener_prologo_jugador(raza))
        
        while True:
            cmd = input(f"\n[{pj.progresion.nombre} Nv.{pj.progresion.nivel}] > ").lower()
            if cmd == "stats": print(f"Stats: {pj.progresion.stats}")
            elif cmd == "mochila": print(f"Items: {pj.mochila.items}")
            elif cmd == "dinero": print(f"Billetera: {pj.mochila.billetera.desglose()}")
            elif cmd == "misiones": print(f"Misiones: {[m.titulo for m in gestor.misiones_disponibles]}")
            elif cmd == "salir": break
            else: print("Comandos: stats, mochila, dinero, misiones, salir.")
    except Exception as e:
        print(f"Error de sistema: {e}")

if __name__ == "__main__":
    ejecutar_juego()
