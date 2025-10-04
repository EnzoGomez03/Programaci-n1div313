import validacion as vl

def ingresar_datos(listaActual):
    """
    PROPOSITO:Permitir al usuario ingresar 10 numeros enteros.
    PRECONDICION:
    -Debe ser la primera vez que se ingresan datos!
    OBSERVACIONES:
    -El rango permitido es de -1000 a 1000.
    """
    vecesIngresado = 10
    if not(len(listaActual) == 0):
        print("Ya ingresaste los datos!.")
        pass
    else:
        while vecesIngresado != 0:
            numeroUsuario = vl.validate_number()
            listaActual.append(numeroUsuario)
            vecesIngresado -= 1
        print(f"\n\nSu lista de numeros es {listaActual}.\n\n" )
    
    return listaActual
    
def cantidad_positivos_negativos(listaNumeros):
    cantidadNegativos = 0
    cantidadPositivos = 0
    for numero in listaNumeros:
        if numero > 0:
            cantidadPositivos += 1
        else:
            cantidadNegativos += 1
    print(f"\n\nIngresaste {cantidadPositivos} numeros positivos y tambien ingresaste {cantidadNegativos} negativos.\n\n" )
    
    
def sumar_numeros_pares(listaNumeros):
    
    """
    PROPOSITO: Retorna la suma de todos los numeros pares de la lista
    """
    
    listaPar = []
    for numero in listaNumeros:
        if numero % 2 == 0:
            listaPar.append(numero)
    sumaTotalDePares = sum(listaPar)
    print(f"\n\n La suma de todos los pares ingresados son {sumaTotalDePares} pares\n\n")
    
    
def max_numero_impar(listaNumeros)->int:
    listaInpar = []
    
    for numero in listaNumeros:
        if numero % 2 == 1:
            listaInpar.append(numero)
            
    numeroMaxImpar = max(listaInpar)
    print(f"\n\n El maximo numero impar que ingresaste fue {numeroMaxImpar}\n\n")
    
    
def mostrar_orden_numeros(listaNumeros):
    pass