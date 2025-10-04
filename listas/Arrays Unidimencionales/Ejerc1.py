# Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def array_numeros(num):
    listaNumeros = []
    for numero in range(num):
        numeroAdd = int(input("Por favor ingrese un numero: "))
        listaNumeros.append(numeroAdd)
    return listaNumeros

print(array_numeros(5))