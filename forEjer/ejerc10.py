#Ingresar un número. Determinar si el número es primo o no

numeroUsuario = int(input("Ingrese un numero entero: "))
numerosDivisibles = 0

#Determina cuantos numeros son divisibles por el numero que ingreso el usuario
for numeroDivisor in range(1,numeroUsuario + 1):
    if (numeroUsuario % numeroDivisor) == 0:
        numerosDivisibles += 1
        
#Determina si el numero es primo o no, y imprime una respuesta
if numerosDivisibles == 2:
    print(f"El numero que ingresaste, es un numero primo")
else:
    print(f"El numero que ingresas, no es un numero primo")