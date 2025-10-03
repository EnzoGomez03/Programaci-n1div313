#  Ejemplos Sencillos para Practicar
# Crear una lista con números del 1 al 5, agregar el 6, y luego eliminar el 2.

# listaNumeros = [1,2,3,4,5]
# print(listaNumeros)
# listaNumeros.append(6)
# print(listaNumeros)
# listaNumeros.remove(2)
# print(listaNumeros)
# print("---" * 20 )
# # # Crear una lista con nombres de tus amigos y ordenarla alfabéticamente.
# listaAmigos = ["Nacho","Naza","Enzito","Ariel","Mauro","Nico","Pabli"]
# print(listaAmigos)
# listaAmigos.sort()
# print(listaAmigos)
# print("---" * 20 )
# # Contar cuántas veces aparece el número 3 en una lista.

# listaNumero3 = [3,3,4,4]
# # aparicionesNumero3 = 0
# # for x in listaNumero3:
# #     if x == 3:
# #         aparicionesNumero3 +=1
# # print (aparicionesNumero3)

# print(listaNumero3.count(3))
        
# print("---" * 20 )

# # Invertir una lista de frutas.
# listaFrutas = ["banana","manzana","frutilla"]
# print("Lista original: ",listaFrutas)
# listaFrutas.sort(reverse= True)
# print("Lista invertida",listaFrutas)
# print("---" * 20 )
# # Hacer la suma de todos los números en una lista.

# lista2Numeros = [2,4,5,6,2,2,2,2,2]
# print(sum(lista2Numeros))

# Slicing



# 1 -Búsqueda lineal (el más simple)
mi_lista = [1, 3, 5, 7, 9, 11, 13, 39, 73,40]
buscar = 40

def buscar_Numero():
    encontrado = None
    for x in mi_lista:
        if x == buscar:
            encontrado = x
            return encontrado
    return encontrado

print(buscar_Numero())
print("---" * 20)

#  2 -Buscar el índice de un valor

def buscar_Indice(valorABuscar):
    indiceEncontrado = None
    for valor in mi_lista:
        if valor == valorABuscar:
            indiceEncontrado = mi_lista.index(valor)
            break
    return indiceEncontrado

print(buscar_Indice(3))

#  3 -Búsqueda binaria (requiere lista ordenada)
