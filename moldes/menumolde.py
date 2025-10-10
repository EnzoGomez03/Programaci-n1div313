from colorama import init, Fore,Style 
import time
#inicializar colorama
init(autoreset=True)
import utlidades as ut


def opciones_menu():
        ut.animar_texto("=== BIENVENIDO AL MENU ===", Fore.MAGENTA)
        # print(Fore.MAGENTA + "BIENVENIDO AL MENU")
        print("___"*20)
        time.sleep(0.3)
        print(Fore.GREEN + "1.")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW + "2.")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"3.")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"4.")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"5.")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"6.")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"7.")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.RED + "8.Salir")
        time.sleep(0.3)

def menu():
    
    while True:
        opciones_menu()
        opcion = input("\n Elija una opcion: ").strip()
        
        if opcion == "1":
            pass
        elif opcion =="2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        elif opcion == "8":
            salir()
            # print(Fore.GREEN + "Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            ingrese_opciones_correctas()


def salir():
    print(Fore.BLACK +"===" * 20)
    ut.animar_texto("Saliendo del sistema.👋 Hasta luego!",Fore.GREEN)
    print(Fore.BLACK +"===" * 20)
    
def ingrese_opciones_correctas():
    print(Fore.RED +"===" * 20)
    print(Fore.BLACK +"\n ⚠️  Por favor ingrese solo las opciones del menu!\n")
    print(Fore.RED + "===" * 20)

menu()
