import validacion as vl
import utilidades as ut

def esperar_limpiar():
    """
    PROPOSITO: Indica al usuario si desea continuar.
    """
    ut.esperar_tecla()
    ut.limpiar()
    
    
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
        esperar_limpiar()
        pass
    else:
        while vecesIngresado != 0:
            numeroUsuario = vl.validate_number()
            listaActual.append(numeroUsuario)
            vecesIngresado -= 1
        print(f"\n\nSu lista de numeros es {listaActual}.\n\n" )
        esperar_limpiar()
    
    return listaActual
    
def cantidad_positivos_negativos(listaNumeros):
    """
    PROPOSITO:Determina la cantidad de numeros positivos y negativos que ingreso el usuario.
    """
    cantidadNegativos = 0
    cantidadPositivos = 0
    for numero in listaNumeros:
        if numero > 0:
            cantidadPositivos += 1
        else:
            cantidadNegativos += 1
    print(f"\n\nIngresaste {cantidadPositivos} numeros positivos y tambien ingresaste {cantidadNegativos} negativos.\n\n" )
    esperar_limpiar()
    
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
    esperar_limpiar()
    
def max_numero_impar(listaNumeros)->int:
    """
    PROPOSITO: Indica el numero maximo impar  ingresado por el usuario.
    """
    #Arreglar que cuando no hay inpares se pone NONE!
    listaInpar = []
    numeroMaxImpar = 0
    
    for numero in listaNumeros:
        if numero % 2 == 1:
            listaInpar.append(numero)
            
    numeroMaxImpar = vl.validacion_max_impar(listaInpar)
    print(f"\n\n El maximo numero impar que ingresaste fue {numeroMaxImpar}\n\n")
    esperar_limpiar()
    
def mostrar_orden_numeros(listaNumeros):
    """
    PROPOSITO: Mostrar al usuario el orden en el que ingreso los numeros.
    """
    listaIngresados = listaNumeros.copy()
    numeroIngreso = 0
    for numero in listaIngresados:
        numeroIngreso += 1
        print(f"El {numeroIngreso + 1}.º numero que ingresaste fue {numero} ")
    esperar_limpiar()
        
def mostrar_pares(listaNumeros):
    """
    PROPOSITO: Mostrarle al usuario los numeros pares que ingreso.
    """
    listaPar = [vl.listar_pares(listaNumeros)]
    for numeroPar in listaPar:
        print(f"Los numeros pares son:{numeroPar}")
    esperar_limpiar()
    
def numeros_posiciones_impares(listaNumeros):
    """
    PROPOSITO: Mostrarle al usuario los numeros que se encuentran en posiciones
    impares.
    OBSERVACION:
    -Cuando se menciona la posicion seria el indice.
    """
    numerosEnPosicionesImpares = []
    for indexNum in range(len(listaNumeros)):
        if indexNum % 2 == 1:
            numerosEnPosicionesImpares.append(listaNumeros[indexNum])
            
    print(f"Los numeros que se encuentran en posiciones impares son: {vl.convertir_lista_int_a_str(numerosEnPosicionesImpares)}")
    esperar_limpiar()