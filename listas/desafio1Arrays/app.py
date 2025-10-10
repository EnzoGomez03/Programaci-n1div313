import funciones as fn
import validacionDeRepaso as vl
from colorama import init, Fore,Style 
#inicializar colorama
init(autoreset=True)


def menu()->None:
    
    lista = []
    while True:
        
        print(Fore.BLUE + "BIENVENIDO AL MENU")
        print("___"*20)
        print(Fore.GREEN + "1.Ingresar datos")
        print("___"*20)
        print(Fore.YELLOW + "2.Cantidad Positivos y negativos")
        print("___"*20)
        print(Fore.YELLOW +"3.Suma de los numeros Pares")
        print("___"*20)
        print(Fore.YELLOW +"4.Mayor numero impar")
        print("___"*20)
        print(Fore.YELLOW +"5.Listar numeros ingresados")
        print("___"*20)
        print(Fore.YELLOW +"6.Listar los numeros pares")
        print("___"*20)
        print(Fore.YELLOW +"7.Listar los numeros en posiciones impares")
        print("___"*20)
        print(Fore.RED + "8.Salir")
        opcion = input("\nELIJA UNA OPCION: ")
        
        
        if opcion == "1":
            lista = fn.ingresar_datos(lista)
        elif opcion == "2":
            if vl.validar_lista_vacia(lista):
                fn.cantidad_positivos_negativos(lista)
        elif opcion == "3":
            if vl.validar_lista_vacia(lista):
                fn.sumar_numeros_pares(lista)
        elif opcion == "4":
            if vl.validar_lista_vacia(lista):
                fn.max_numero_impar(lista)
        elif opcion == "5":
            if vl.validar_lista_vacia(lista):
                fn.mostrar_orden_numeros(lista)
        elif opcion == "6":
            if vl.validar_lista_vacia(lista):
                fn.mostrar_pares(lista)
        elif opcion == "7":
            if vl.validar_lista_vacia(lista):
                fn.numeros_posiciones_impares(lista)
        elif opcion == "8":
            print(Fore.GREEN + "Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print(Fore.RED +"===" * 20)
            print(Fore.BLACK +"\nPor favor ingrese solo las opciones del menu!\n")
            print(Fore.RED + "===" * 20)