from colorama import init, Fore,Style 
#inicializar colorama
init(autoreset=True)

def validate_number():
    numeroAValidar = int(input("Por favor ingrese un numero[-1000 a 1000]: "))
    while not(-1000 <= numeroAValidar <= 1000):
        print("Estas elijiendo un numero fuera del rango!")
        return validate_number()
    return numeroAValidar

def validacion_max_impar(lista):   
    if len(lista) == 0:
        print("No agregaste ningun numero inpar!")
        pass
    else:
        numeroMaxImparVl = max(lista)
        return numeroMaxImparVl
    
    
def listar_pares(lista):
    listaParVl = []
    for numero in lista:
        if numero % 2 == 0:
            listaParVl.append(numero)
    return listaParVl


def convertir_lista_int_a_str(lista):
    resultado = ""
    for x in range(len(lista)):
        resultado += str(lista[x])
        if x != len(lista) - 1:
            resultado += ", "
    return resultado

def validar_lista_vacia(lista):
    """
    PROPOSITO: Indica que el usuario no agrego ningun dato.
    """
    if len(lista) == 0:
        print(Fore.RED+"Primero tenes que ingresar los datos!: " + " OPCION 1")
        return False
    else:
        return True

print(convertir_lista_int_a_str([1,2,3,4,5,6]))