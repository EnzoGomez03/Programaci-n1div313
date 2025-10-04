# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def calcular_producto(listaProducto):
    copiaDeLista = listaProducto.copy()
    resultadoDeProducto = copiaDeLista.pop(0)
    for numero in copiaDeLista:
        resultadoDeProducto *= numero
    return resultadoDeProducto

print(calcular_producto([2,4,5,2]))