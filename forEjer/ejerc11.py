#Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.


def mostrar_cuantos_primos_hay(numeroIngresado):
    cantidadNumeroPrimos = 0
    numerosPrimosStr = ""

    for numero in range(1,numeroIngresado + 1):
        numerosDivisibles = 0

        #Determina si el "numero" al ser dividido por "numeroDivisor" 
        # es igual a 0, suma + 1 a los divisibles.

        for numeroDivisor in range(1,numero + 1):
            if (numero % numeroDivisor) ==0:
                numerosDivisibles += 1

        #Determina si numerosDivisibles es igual a 2, significa que 
        #es un numero primo, por lo tanto lo suma a la cantidad de primos.        
        if numerosDivisibles == 2:
            cantidadNumeroPrimos += 1
            numerosPrimosStr += str(numero) + ","
            #print(numero, end= "," )
            
    return numerosPrimosStr , cantidadNumeroPrimos


#Imprime los numeros primos encontrados.
numeroIngresadoUsuario = int(input("Por favor ingrese un numero: "))
num , cant = mostrar_cuantos_primos_hay(numeroIngresadoUsuario)

print(f"Los numeros primos son: {num}")

#Imprime la cantidad de numeros primos encontrados.
print(f"La cantidad de numeros primos que se encontrar son {cant}")

#2,3,5,7