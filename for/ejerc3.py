#Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero = int(input("Ingrese un numero entero valido: "))

for x in range(0,numero + 1):
    print(x)