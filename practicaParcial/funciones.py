from colorama import init, Fore,Style 
import utilidades as ut
import time
import csv
import os
import validaciones as vl
#inicializar colorama
init(autoreset=True)


def opciones_menu():
        ut.animar_texto("=== BIENVENIDO AL MENU ===", Fore.MAGENTA)
        print("___"*20)
        time.sleep(0.2)
        print(Fore.GREEN + "1.Cargar reservas")
        time.sleep(0.2)
        print("___"*20)     
        time.sleep(0.2)
        print(Fore.YELLOW + "2.Mostrar reservas")
        time.sleep(0.2)
        print("___"*20)
        time.sleep(0.2)
        print(Fore.YELLOW +"3.Buscar por docente")
        time.sleep(0.2)
        print("___"*20)
        time.sleep(0.2)
        print(Fore.YELLOW +"4.Estadisticas generales")
        time.sleep(0.2)
        print("___"*20)
        time.sleep(0.2)
        print(Fore.YELLOW +"5.Filtrar por aula")
        time.sleep(0.2)
        print("___"*20)
        time.sleep(0.2)
        print(Fore.YELLOW +"6.Ordenar por horas")
        time.sleep(0.2)
        print("___"*20)
        time.sleep(0.2)
        print(Fore.YELLOW +"7.Generar informe")
        time.sleep(0.2)
        print("___"*20)
        time.sleep(0.2)
        print(Fore.RED + "8.Salir")
        time.sleep(0.2)

def cargar_reservas(reservasList):
    """
    Cada reserva se representa con un diccionario con las claves:
    "id" (entero autoincremental),
    "docente",
    "materia",
    "fecha" (validar formato DD/MM/AAAA),
    "horas_reservadas" (entero mayor que 0).
    "aula" (texto, por ejemplo: Lab1, Lab2, Lab3)
    Los datos se guardan en una lista y también en el archivo reservas.csv.
    Si el archivo ya existe, preguntar:
    “¿Desea reemplazar los datos existentes o agregar nuevos equipos?”
    """
    
    cantReservas = vl.validar_cant_reservas()
    listaReservas = reservasList.copy()
    
    
    for x in range(cantReservas):
        id = len(listaReservas) + 1
        docente = input("Ingresar nombre docente: ")
        materia = input("Ingresar materia: ")
        fecha =  vl.validar_reservas("fecha")
        horasReservadas = vl.validar_reservas("hora")
        aula = vl.validar_reservas("aula")
        reserva = {
            'id': id,
            'docente':docente,
            'materia':materia,
            'fecha':fecha,
            'horas_reservadas':horasReservadas,
            'aula':aula
        }
        listaReservas.append(reserva)
    
    vl.validar_archivo(listaReservas)
    
    print("===" *20)
    print(Fore.GREEN + "Reservas cargadas!")
    print("===" *20)
    
    ut.esperar_limpiar()
    return listaReservas

def mostrar_reservas(reservasUsuario):
    
    """
    PROPOSITO: Mostrarle al usuario los datos cargados de las reservas que ingreso.
    """
    
    for reserva in reservasUsuario:
        print(Fore.BLACK +"===" * 40)
        print(f"Equipo: {reservasUsuario.index(reserva) + 1} ")
        for dato in reserva:
            print(f"{dato}: {reserva[dato]} | "  , end=" ")
        print()
    ut.esperar_limpiar()

def buscar_por_docente():
    """
    PROPOSITO: Buscar al docente ingresado por el usuario, y mostrar las reservas que tiene dicho docente
    """
    
    archivo = "reservas.csv"
    docenteABuscar = input("Por favor ingrese el nombre del docente: ").lower().strip()
    
    with open(archivo,"r",newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        reservasDocente = []
        for reserva in lector:
            if docenteABuscar == reserva["docente"].lower():
                print(f"ID: {reserva["id"]} | materia: {reserva["materia"]} | fecha: {reserva["fecha"]} | horas_reservadas: {reserva["horas_reservadas"]} | aula: {reserva["aula"]}")
            else:
                print("El docente no tiene ninguna reserva hecha!")


def sub_menu():
    
    ut.animar_texto("=== Bienvenido al menu Estadisticas===", Fore.MAGENTA)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.GREEN + "1.Total de reservas registradas.")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW + "2.Total de horas reservadas.")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW +"3.Promedio de horas por reserva.")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW +"4.Docente con más horas reservadas")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW +"5.Día con más reservas.")
    print("___"*20)
    time.sleep(0.2)
    print(Fore.RED + "6.Salir del submenu")
    

def calcular_estadisticas_generales():
    archivo = "reservas.csv"
    ut.limpiar()
    
    while True:
        sub_menu()
        opcion = input("Por favor ingrese una opcion: ")
        
        if opcion =="1":
            total_reservas_registradas()
        elif opcion == "2":
            total_horas_reservadas()
        elif opcion =="3":
            pass
        elif opcion == "4":
            pass
        elif opcion =="5":
            pass
        if opcion == "6":
            print(Fore.BLACK +"===" * 20)
            ut.animar_texto("Saliendo del submenu.👋 Hasta luego!",Fore.GREEN)
            print(Fore.BLACK +"===" * 20)
            ut.esperar_limpiar()
            break
    
    
def total_reservas_registradas():
    archivo = "reservas.csv"
    reservasContadas = 0
    with open(archivo,"r",newline="",encoding="utf-8") as e:
        lector = csv.DictReader(e)
        for reserva in lector:
            reservasContadas += 1
            
    print(f"El total de reservas actualmente son de: {reservasContadas}")
    ut.esperar_limpiar()
    
    
def total_horas_reservadas():
    archivo = "reservas.csv"
    horasTotales = 0
    with open(archivo,"r", newline="",encoding="utf-8") as e:
        lector = csv.DictReader(e)
        for reservas in lector:
            horasTotales += reservas["horas_reservadas"]
    print(f"El total de horas entre todas las reservas juntas es de {horasTotales}") #Esto esta mal porque reservas["horas_reservadas"] basicamente tenemos ejemplo 2:30hs
    
def salir():
    print(Fore.BLACK +"===" * 20)
    ut.animar_texto("Saliendo del sistema.👋 Hasta luego!",Fore.GREEN)
    print(Fore.BLACK +"===" * 20)
    
    
def ingrese_opciones_correctas():
    print(Fore.RED +"===" * 20)
    print(Fore.BLACK +"\n ⚠️  Por favor ingrese solo las opciones del menu!\n")
    print(Fore.RED + "===" * 20)
    ut.esperar_tecla()
    ut.limpiar()