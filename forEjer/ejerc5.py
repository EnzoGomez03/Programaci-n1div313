#Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
numerosASumar = 0
numerosIngresados = 0

for x in range(0,10):
    numero = int(input("ingrese un numero: "))
    numerosASumar += numero
    numerosIngresados += 1
    if numero == 0:
        break
    print(numero)

promedioTotalDeNumeros = numerosASumar / numerosIngresados
print(f"El total de los numeros sumados {numerosASumar}")
print(f"El promedio de todos los numeros sumados es de {promedioTotalDeNumeros}")