#Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

numeroLimite = int(input("Porfavor ingrese un numero: "))


for fila in range(1,numeroLimite + 1):
    for numero in range(1, fila + 1):
        print(numero, end = "")  # end define cuando termina la linea
    print("")

# 1
# 12
# 123
# 1234
# 12345