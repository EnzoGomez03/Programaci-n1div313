
# # Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
# def numero_Retornado(numero):
#     return (f"El numero que ingreso es {numero}")

# pedirNumero = int(input("Por favor ingrese un numero entero: "))

# print(numero_Retornado(pedirNumero))
# # Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# def numero_Retornado_Flotante(numero):
#     return (f"El numero que ingreso es {numero}")

# pedirNumeroFlotante = float(input("Por favor ingrese un numero flotante: "))

# print(numero_Retornado_Flotante(pedirNumeroFlotante))

# # Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

# def cadena_(cadena):
#     return (f"La cadena de texto ingresa es: {cadena}")

# cadenaTexto = input("Por favor ingrese una cadena de texto: ")
# print(cadena_(cadenaTexto))

# # Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

# def calcular_area_rectangulo(base, altura):
#     return base * altura

# areaRectangulo = int(input("Por favor ingrese el area del rectangulo: "))
# baseRectangulo = int(input("Por favor ingrese la base del rectangulo: "))

# print(f"El area del rectangulo es de {calcular_area_rectangulo(areaRectangulo,baseRectangulo)}")


# # Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# import math
# def calcular_area_circulo(radioCirculo):
#     return(math.pi * radioCirculo * radioCirculo)

# radio = int(input("Por favor ingrese el radio del circulo: "))

# print(f"El area del circulo es de: {calcular_area_circulo(radio)}")

# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

# def verificar_Par_o_Impar(numero):
#     if (numero % 2) == 0:
#         return("par")
#     else:
#         return("impar")
    
# numeroElegido = int(input("Ingrese un numero: "))

# print(f"El numero ingresado es {verificar_Par_o_Impar(numeroElegido)}")

# # Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

# def verificar_Par_o_Impar(numero):
#     if (numero % 2) == 0:
#         return(True)
#     else:
#         return(False)
    
# numeroElegido = int(input("Ingrese un numero: "))

# print(verificar_Par_o_Impar(numeroElegido))

# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

# def encontrar_Maximo_Numero(num1,num2,num3):
#     if num1 > num2 and num1 > num3:
#         return (num1)
#     elif num2 > num1 and num2 > num3:
#         return (num2)
#     else:
#         return(num3)
    
# numero1 = int(input("Por favor ingrese un numero: "))
# numero2 = int(input("Por favor ingrese un numero: "))
# numero3 = int(input("Por favor ingrese un numero: "))

# print(f"El numero mas alto entre los numeros que ingreso es: {encontrar_Maximo_Numero(numero1, numero2, numero3)}")

# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

# def calcular_Potencia(base,exponente):
#     return base ** exponente

# numeroBase = int(input("Por favor ingrese el numero que quiere potenciar: "))
# numeroExpo = int(input("Por favor ingrese el exponente: "))
# print(f"La potencia del numero {numeroBase} por potencia {numeroExpo} es de: {calcular_Potencia(numeroBase,numeroExpo)}")

# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

# def verificar_Si_Es_Primo(numeroVeri):
#     contador = 0
    
#     if numeroVeri < 2:
#         return False
#     else: 
#         for x in range(2, numeroVeri):
#             if numeroVeri % x == 0:
#                 contador += 1
    
#         if contador == 0:
#             return True
#         else:
#             return False

# numero = int(input("Ingrese un numero para confirmar si es primo o no: "))

# print(verificar_Si_Es_Primo(numero))

# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
from forEjer import ejerc11 as ejercicio11

def numeros_Comprendidos(numero):
    return ejercicio11.mostrar_cuantos_primos_hay(numero)


numeroPrimo = int(input("Ingrese el numero primo: "))
numerosPrimosStr , cantidadDeNumerosPrimos = numeros_Comprendidos(numeroPrimo)

print(f"Los numeros primos son {numerosPrimosStr} , y la cantidad de numeros primos son {numerosPrimosStr}")
# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

