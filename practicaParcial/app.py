import funciones as fn
import utilidades as ut
from colorama import init, Fore,Style 
import time
#inicializar colorama
init(autoreset=True)


def menu():
    vlOpcionUno = False
    # lista = []
    
    while True:
        #Opciones del Menu
        fn.opciones_menu()
        opcion = input("\n Elija una opcion: ").strip()
        
        #En caso de que el usario no elija una opcion del menu.
        if opcion not in ["1","2","3","4","5","6","7","8"]:
            fn.ingrese_opciones_correctas()
            continue
        
        #Opciones que pudo elegir el usuario
        
        if opcion == "1":
            # lista = fn.cargar_reservas(lista)
            fn.cargar_reserva()
            vlOpcionUno = True
        elif opcion == "8":
            fn.salir()
            break
        elif vlOpcionUno:
            if opcion =="2":
                fn.mostrar_reservas()
            elif opcion == "3":
                fn.buscar_por_docente()
            elif opcion == "4":
                fn.calcular_estadisticas_generales()
            elif opcion == "5":
                pass
            elif opcion == "6":
                pass
            elif opcion == "7":
                pass
        else:
            print(Fore.RED +"===" * 20)
            print(Fore.BLACK +"\n ⚠️  Primero tenes que ingresar los datos!\n")
            print(Fore.RED + "===" * 20)
            ut.esperar_limpiar()



