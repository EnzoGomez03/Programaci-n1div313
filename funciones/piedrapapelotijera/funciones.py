import random
import validacion as vl

def verificar_ganador_ronda(eleccionJugador, eleccionMaquina)->str:
    """
    PROPOSITO: Indica quien gano la ronda, si la maquina o el jugador.
    PRECONDICION:
    -El jugador debe de haber elegido 1(piedra) o 2(papel) o 3(tijera)
    -La maquina debe de haber elegido 1(piedra) o 2(papel) o 3(tijera)
    PARAMETROS:
    eleccionJugador: Indica el valor elegido por el jugador
    eleccionMaquina: Indica el valor elegido por la maquina
    """
    ganadorRonda = ""
    if eleccionMaquina == eleccionJugador:
        ganadorRonda = "Empate"
    elif (eleccionMaquina == 1 and eleccionJugador == 3) or\
        (eleccionMaquina == 2 and eleccionJugador == 1) or\
        (eleccionMaquina == 3 and eleccionJugador == 2):
        ganadorRonda = "Maquina"
    else:
        ganadorRonda = "Jugador"
    
    return ganadorRonda

def verifcar_estado_partida(aciertosJugador,aciertosMaquina,rondaActual)->bool:
    """
    PROPOSITO:Determinar si la partida sigue en curso o finalizo.
    PRECONDICION:
    -NINGUNA
    PARAMETROS:
    aciertosJugador: Indica las rondas ganadas del jugador
    aciertosMaquina: Indica las rondas ganas de la maquina
    rondaActual: Indica el numero de la ronda actual
    """
    
    partida = None
    if rondaActual < 3:
        if aciertosJugador <= 2:
            partida = True
        elif aciertosJugador == 3:
            partida = False
        elif aciertosMaquina <= 2:
            partida = True
        elif aciertosMaquina == 3:
            partida = False
    else:
        partida = False
    
    return partida

def verificar_ganador_partida(aciertos_jugador:int,aciertos_maquina:int)-> str:
    """
    PROPOSITO: Indica quien es el ganador de la partida.
    PRECONDICION:
    -Se deben de haber jugado las 3 rondas.
    PARAMETROS:
    aciertos_jugador : Indica las rondas ganas del jugador.
    aciertos_maquinaL: Indica las rondas ganadas de la maquina.
    """
    
    ganadorPartida = "No hay ganador todavia"
    if aciertos_jugador == 3:
        ganadorPartida = "Jugador"
    elif aciertos_maquina == 3:
        ganadorPartida = "Maquina"
        
    return ganadorPartida

def mostrar_elemento(eleccion:int)-> str:
    """
    PROPOSITO: Convierte la eleccion numerica por un string.
    PRECONDICION:
    -La eleccion debe de ser uno de los numeros permitidos 1,2,3
    """
    
    eleccionConvertida = eleccion
    match eleccionConvertida:
        case 1: 
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"
