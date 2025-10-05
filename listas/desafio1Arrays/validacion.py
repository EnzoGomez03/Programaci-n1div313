from colorama import init, Fore,Style 
#inicializar colorama
init(autoreset=True)

def validate_number():
    try:
        numeroAValidar = int(input("Por favor ingrese un numero[-1000 a 1000]: "))
        while not(-1000 <= numeroAValidar <= 1000):
            print(Fore.RED +"===" * 20)
            print("⚠️  Estas elijiendo un numero fuera del rango!")
            print(Fore.RED +"===" * 20)
            return validate_number()
        return numeroAValidar
    except:
        print(Fore.RED +"===" * 20)
        print(Fore.RED + "\n ⚠️  Por favor ingresa un numero entero valido y que este dentro del rango!\n")
        print(Fore.RED +"===" * 20)

def validacion_max_impar(lista):   
    if len(lista) == 0:
        print(Fore.RED +"===" * 20)
        print("⚠️ No agregaste ningun numero inpar!")
        print(Fore.RED +"===" * 20)
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
        print(Fore.RED +"===" * 20)
        print(Fore.RED+"\n ⚠️ Primero tenes que ingresar los datos!: " + " OPCION 1\n")
        print(Fore.RED +"===" * 20)
        return False
    else:
        return True
