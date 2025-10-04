# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 

def calcular_promedio(listaEnteros):
    cantidadNumeros = len(listaEnteros)
    totalDeLaLista = sum(listaEnteros)
    return totalDeLaLista / cantidadNumeros

print(calcular_promedio([2,2,2,2]))