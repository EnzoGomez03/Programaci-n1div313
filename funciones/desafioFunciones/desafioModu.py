# En donde:
# mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
# mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
# mínimo: valor mínimo admitido (inclusive)
# máximo: valor máximo admitido (inclusive)
# reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.


def get_int(mensaje: str, mensaje_error:str, minimo:int , maximo: int, reintentos: int) ->int|None:
    
    reintentosActuales = reintentos
    while reintentosActuales != 0:
        datoUsuario = int(mensaje)
        if minimo <= datoUsuario <= maximo:
            print("Numero Valido!")
            return datoUsuario
        else:
            print(mensaje_error)
            reintentosActuales -= 1
    return None
    

def get_float(mensaje: str, mensaje_error:str,minimo:float, maximo:float,reintentos:int) -> float|None:
    reintentosActuales = reintentos
    while reintentosActuales != 0:
        datoUsuario = float(input(mensaje))
        if minimo <= datoUsuario <= maximo:
            print("Numero Valido!")
            return datoUsuario
        else:
            print(mensaje_error)
            reintentosActuales -= 1
    return None
    
# Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):

def get_string(longitud: int, mensaje:str,mensaje_error:str,intentos:int) -> str|None:
    reintentosActuales = intentos
    while reintentosActuales != 0:
        datoUsuario = input(mensaje)
        if len(datoUsuario) <= longitud:
            print("Dato Valido!")
            return datoUsuario
        else:
            print(mensaje_error)
            reintentosActuales -= 1
    return None
