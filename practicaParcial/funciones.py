from colorama import init, Fore,Style 
import utilidades as ut
import time
import validaciones as vl
#inicializar colorama
init(autoreset=True)


def opciones_menu():
        ut.animar_texto("=== BIENVENIDO AL MENU ===", Fore.MAGENTA)
        # print(Fore.MAGENTA + "BIENVENIDO AL MENU")
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
        docente = input("Por favor ingrese el docente: ")
        materia = input("Por favor ingrese la materia: ")
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
    print("===" *20)
    print(Fore.GREEN + "Reservas cargadas!")
    print("===" *20)
    ut.esperar_tecla()
    ut.limpiar()
    return listaReservas

def mostrar_reservas(reservasUsuario):
    for reserva in reservasUsuario:
        for dato in reserva:
            print(reserva[dato])


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