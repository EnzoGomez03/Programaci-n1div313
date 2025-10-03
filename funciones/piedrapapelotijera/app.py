import funciones as fn
import random
import validacion as vl

def jugar_piedra_papel_tijera()->str:
    """
    PROPOSITO:Jugar piedra, papel o tijera, contra la maquina
    PRECONDICION:
    -NINGUNA
    OBSERVACIONES:
    El usuario/jugador va a elegir un numero entre el 1 y el 3.
    """
    
    rondasGanadasJugador = 0
    rondasGanadasMaquina = 0
    rondasJugadas = 0
    print("BIENVENIDO A PIEDRA, PAPEL O TIJERA")
    
    while fn.verifcar_estado_partida(rondasGanadasJugador,rondasGanadasMaquina,rondasJugadas):
        maquina = random.randint(1,3)
        print(f"Perfecto elegiste {fn.mostrar_elemento(vl.validate_number())}")
        print(f"La maquina eligio {fn.mostrar_elemento(maquina)}")

