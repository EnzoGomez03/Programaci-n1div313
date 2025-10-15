import funciones as fn
import utilidades as ut
from colorama import init, Fore,Style 
import time
#inicializar colorama
init(autoreset=True)


def menu():
    vlOpcionUno = False
    
    while True:
        fn.opciones_menu()
        opcion = input("\n Elija una opcion: ").strip()
        
        #En caso de que el usario no elija una opcion del menu.
        if opcion not in ["1","2","3","4","5","6","7"]:
            fn.ingrese_opciones_correctas()
            continue
        
        
        if opcion == "1":
            fn.cargar_datos_estudiantes()
            vlOpcionUno = True
        elif opcion == "7":
            fn.salir()
            break
        elif vlOpcionUno:
            if opcion =="2":
                fn.mostrar_listado_estudiantes()
            elif opcion == "3":
                fn.buscar_estudiante()
                ut.esperar_limpiar()
            elif opcion == "4":
                fn.calcular_estadisticas()
            elif opcion == "5":
                fn.ordenar_mostrar()
            elif opcion == "6":
                fn.generar_informe_resumen()
        else:
            print(Fore.RED +"===" * 20)
            print(Fore.BLACK +"\n ⚠️  Primero tenes que ingresar los datos de los Alumnos!\n")
            print(Fore.RED + "===" * 20)
            ut.esperar_limpiar()
