from colorama import init, Fore,Style 
import utilidades as ut
import time
import csv
import os
import validaciones as vl
#inicializar colorama
init(autoreset=True)

#=======================================MENU======================================================

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

#======================================= MENU OPCION 1 ========================================
# def cargar_reservas(reservasList):
#     """
#     Cada reserva se representa con un diccionario con las claves:
#     "id" (entero autoincremental),
#     "docente",
#     "materia",
#     "fecha" (validar formato DD/MM/AAAA),
#     "horas_reservadas" (entero mayor que 0).
#     "aula" (texto, por ejemplo: Lab1, Lab2, Lab3)
#     Los datos se guardan en una lista y también en el archivo reservas.csv.
#     Si el archivo ya existe, preguntar:
#     “¿Desea reemplazar los datos existentes o agregar nuevos equipos?”
#     """
    
#     cantReservas = vl.validar_cant_reservas()
#     listaReservas = reservasList.copy()

#     # vl.validar_archivo(listaReservas)
    
#     for x in range(cantReservas):
#         id = len(listaReservas) + 1
#         docente = input("Ingresar nombre docente: ")
#         materia = input("Ingresar materia: ")
#         fecha =  vl.validar_reservas("fecha")
#         horasReservadas = vl.validar_reservas("hora")
#         aula = vl.validar_reservas("aula")
#         reserva = {
#             'id': id,
#             'docente':docente,
#             'materia':materia,
#             'fecha':fecha,
#             'horas_reservadas':horasReservadas,
#             'aula':aula
#         }
#         listaReservas.append(reserva)
    
#     vl.validar_archivo(listaReservas)
    
#     print("===" *20)
#     print(Fore.GREEN + "Reservas cargadas!")
#     print("===" *20)
    
#     ut.esperar_limpiar()
#     return listaReservas


def cargar_reserva():
    
    if os.path.exists("reservas.csv"): #Verifica si el archivo existe.
        print("El archivo ya existe!")
        eleccionUsuario = input("¿Desea reemplazar los datos existentes o agregar nuevos equipos? [R] o [A]: ")
        match eleccionUsuario:
            case "r":
                remplazar_archivo()
            case "a":
                agregar_reserva()
    else:
        crear_archivo()
    
    print("===" *20)
    print(Fore.GREEN + "Reservas cargadas!")
    print("===" *20)
    ut.esperar_limpiar()


def crear_archivo():
    reservasList = crear_reserva()
    with open("reservas.csv", "w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["id", "docente", "materia", "fecha","horas_reservadas", "aula"])
        writer.writeheader()
        for reserva in reservasList:
            writer.writerow(reserva)

def agregar_reserva():
    reservasList = crear_reserva()
    with open("reservas.csv","a",newline="") as archivo:
        writer = csv.DictWriter(archivo,fieldnames=["id", "docente", "materia", "fecha","horas_reservadas", "aula"])
        writer.writerows(reservasList)


def remplazar_archivo():
    #Llamo a la funcion crear_reserva que crea todas las reservas que el usario quiera.
    reservasList = crear_reserva()
    
    #Reemplazo el archivo existente, por el nuevo creado por las reservas del usuario.
    with open("reservas.csv", "w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["id", "docente", "materia", "fecha","horas_reservadas", "aula"])
        writer.writeheader()
        for reserva in reservasList:
            writer.writerow(reserva)
    
    


def crear_reserva():
    listaReservas = []
    cantReservas = vl.validar_cant_reservas()
    
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
    return listaReservas
    

#======================================= MENU OPCION 2 ========================================
def mostrar_reservas():
    
    """
    PROPOSITO: Mostrarle al usuario los datos cargados de las reservas que ingreso.
    """
    datos = leer_archivo("reservas.csv")
    
    for reserva in datos:
        print(Fore.BLACK +"===" * 40)
        print(f"Equipo: {datos.index(reserva) + 1} ")
        for dato in reserva:
            print(f"{dato}: {reserva[dato]} | "  , end=" ")
        print()
    ut.esperar_limpiar()


#======================================= MENU OPCION 3 ========================================
def buscar_por_docente():
    """
    PROPOSITO: Buscar al docente ingresado por el usuario, y mostrar las reservas que tiene dicho docente
    """
    
    datos = leer_archivo("reservas.csv")
    docenteABuscar = input("Por favor ingrese el nombre del docente: ").lower().strip()
    reservasDocente = []
    for reserva in datos:
        if docenteABuscar == reserva["docente"].lower():
            print(f"ID: {reserva["id"]} | materia: {reserva["materia"]} | fecha: {reserva["fecha"]} | horas_reservadas: {reserva["horas_reservadas"]} | aula: {reserva["aula"]}")


#======================================= MENU OPCION 8 ========================================
def salir():
    print(Fore.BLACK +"===" * 20)
    ut.animar_texto("Saliendo del sistema.👋 Hasta luego!",Fore.GREEN)
    print(Fore.BLACK +"===" * 20)

#======================================= MENU OPCION ERROR ========================================
def ingrese_opciones_correctas():
    print(Fore.RED +"===" * 20)
    print(Fore.BLACK +"\n ⚠️  Por favor ingrese solo las opciones del menu!\n")
    print(Fore.RED + "===" * 20)
    ut.esperar_tecla()
    ut.limpiar()


#============================================MENU OPCION: 4 ======================================
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
            ut.esperar_limpiar()
        elif opcion == "2":
            total_horas_reservadas()
            ut.esperar_limpiar()
        elif opcion =="3":
            promedio_total_horas_por_reserva()
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

#============================SubMenu Opcion: 1=============================================
def total_reservas_registradas():
    """
    PROPOSITO: Indica al usuario el total de reservas que hay en el archivo actualmente.
    """
    reservasContadas = reservas_registradas()
    print(f"El total de reservas actualmente son de: {reservasContadas}")


def reservas_registradas():
    """
    PROPOSITO: Determina la cantidad de reservas que hay en el archivo.
    """
    datos = leer_archivo("reservas.csv")
    reservasContadas = 0
    for reserva in datos:
        reservasContadas += 1
    return reservasContadas

#============================SubMenu Opcion: 2=============================================

def total_horas_reservadas():
    """
    PROPOSITO: Indica al usuario las horas entre todas las reservas del archivo.
    """
    
    minutosTotales = minutos_reservados()
    horasTotales = minutosTotales // 60
    totalMinutos = minutosTotales % 60
    
    if totalMinutos >= 10:
        print(f"El total de horas entre todas las reservas juntas es de {horasTotales}:{totalMinutos} HS")
    else:
        print(f"El total de horas entre todas las reservas juntas es de {horasTotales}:0{totalMinutos} HS")
    # print(f"El total de horas entre todas las reservas juntas es de {horasTotales}") #Esto esta mal porque reservas["horas_reservadas"] basicamente tenemos ejemplo 2:30hs
    


def minutos_reservados():
    """
    PROPOSITO: Determina la suma de la cantidad de horas pero lo devuelve en minutos totales.
    """
    minutosTotales = 0
    datos = leer_archivo("reservas.csv")
    for reservas in datos:
        horas,minutos = map( int,reservas["horas_reservadas"].split(":") ) #Convierte 2:30 a 2 , 30
        minutosTotales += horas * 60 + minutos
    return minutosTotales



#============================ FUNCION LEER ARCHIVO ===========================================
def leer_archivo(archivo):
    """
    PROPOSITO: Devuelve una lista de dic, con toda la informacion del archivo
    OBSERVACIONES:
    Muy util la verdad, pero solo lee, tal vez pueda probar despues que haga mas cosas dependiendo de que quiero hacer.
    """
    
    with open(archivo,"r", newline="",encoding="utf-8") as e:
        lector = csv.DictReader(e)
        return list(lector)




#============================SubMenu Opcion: 3 =============================================

def promedio_total_horas_por_reserva():
    """
    PROPOSITO: Indica el promedio de horas entre todas las reservas hechas.
    """
    #Cargo los datos para hacer el calculo del promedio
    datos = leer_archivo("reservas.csv")
    minutosTotales = minutos_reservados()
    reservasTotales = reservas_registradas()
    
    #Aca se hace el calculo del promedio de las horas
    promedioHoras = minutosTotales // reservasTotales
    horasTotales = promedioHoras // 60
    totalMinutos = promedioHoras %  60
    
    #Verifico si el total de minutos, es mayor de 10 no le agrego 0, si es menor a 10, le agrego 0 adelante 
    if totalMinutos >= 10:
        print(f"El promedio de horas totales por reserva es de: {horasTotales}:{totalMinutos}HS.")
    else:
        print(f"El promedio de horas entre todas las reservas juntas es de {horasTotales}:0{totalMinutos} HS.")
    
    ut.esperar_limpiar()


#============================SubMenu Opcion: 4 =============================================

def docente_mas_horas_reservadas():
    pass