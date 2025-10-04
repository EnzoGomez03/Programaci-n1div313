# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def valor_maximo_encontrado(listaEnteros):
    posicionMaximoActual = 0
    listaCopiada = listaEnteros.copy()
    maximoActual = listaCopiada.pop(0)
    
    for numero in listaCopiada:
        if numero > maximoActual:
            maximoActual = numero
            posicionMaximoActual = listaEnteros.index(maximoActual)
    return posicionMaximoActual
