import funciones as fn
import random
import validacion as vl
from colorama import init, Fore, Style


def jugar_piedra_papel_tijera()->str:
    """
    PROPOSITO:Jugar piedra, papel o tijera, contra la maquina.
    PRECONDICION:
    -NINGUNA
    OBSERVACIONES:
    El usuario/jugador va a elegir un numero entre el 1 y el 3.
    """
    #VARIABLES PARA EL INICIO DEL JUEGO
    rondasGanadasJugador = 0
    rondasGanadasMaquina = 0
    rondasJugadas = 0
    #PRINT DE VISUALES PARA EL JUEGO!
    print(Fore.GREEN + "- " * 100)
    print(" " * 80  +"BIENVENIDO A PIEDRA, PAPEL O TIJERA")
    print(Fore.GREEN + "- " * 100 + Style.RESET_ALL)
    
    print(Fore.RED + "=====" * 10)
    print("REGLAS DEL JUEGO")
    print("1 PIEDRA, 2 PAPEL, 3 TIJERA")
    print(Fore.RED + "=====" * 10 + Style.RESET_ALL)
    
    #While juego
    while fn.verifcar_estado_partida(rondasGanadasJugador,rondasGanadasMaquina,rondasJugadas):
        
        maquina = random.randint(1,3)
        jugador = vl.validate_number()
        
        if fn.verificar_ganador_ronda(jugador,maquina) == "Empate":
            print("Oh tenemos un empate, siguiente ronda!")
        elif fn.verificar_ganador_ronda(jugador,maquina) == "Maquina":
            print(Fore.BLUE + "Punto Para la Maquina!" + Style.RESET_ALL)
            rondasGanadasMaquina += 1
            rondasJugadas += 1
        else:
            print(Fore.YELLOW + "Punto Para El Jugador!" + Style.RESET_ALL)
            rondasGanadasJugador += 1
            rondasJugadas += 1
        print(f"El jugador eligio {fn.mostrar_elemento(jugador)}")
        print(f"La maquina eligio {fn.mostrar_elemento(maquina)}")
    
    return print(f"El GANADOR DE LA PARTIDA ES {fn.verificar_ganador_partida(rondasGanadasJugador,rondasGanadasMaquina)}") 
