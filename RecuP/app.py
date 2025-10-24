import funciones as fn
import utilidades as ut
import validaciones as vl
import os
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
        if opcion not in ["1","2","3","4","5","6","7","8"]:
            print(Fore.RED +"===" * 20)
            print(Fore.BLACK +"\n ⚠️  Ingresa una opcion correcta del menu! \n")
            print(Fore.RED + "===" * 20)
            ut.esperar_limpiar()
            menu()
        
        
        if opcion == "1":
            vlOpcionArchivo = vl.validar_archivo_existe() #Valido al principio si el archivo existe o no
            fn.cargar_datos_estudiantes(vlOpcionArchivo)
            vlOpcionUno = True
        elif opcion == "8":
            fn.salir()
            ut.esperar_limpiar()
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
                fn.filtrar_por_condición_de_estudiantes()
                ut.esperar_limpiar()
            elif opcion == "7":
                fn.generar_informe_resumen()
                ut.esperar_limpiar()
        else:
            print(Fore.RED +"===" * 20)
            print(Fore.BLACK +"\n ⚠️  Primero tenes que ingresar los datos de los Alumnos!\n")
            print(Fore.RED + "===" * 20)
            ut.esperar_limpiar()
