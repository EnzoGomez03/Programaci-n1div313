# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

numeroCliente = int(input("Ingrese un numero= "))

for numero in range(1,numeroCliente + 1 ):
    if (numeroCliente % numero) == 0:
        print(numero)