import os
import csv


# def validar_nombre():
#     docente = input("Ingrese nombre del docente: ")
#     while docente in []

def validar_cant_reservas():
    try:
        reserva = int(input("Ingrese la cantidad de reservas!: "))
        return reserva
    except:
        print("=====================\n")
        print(" ⚠️  Dato invalido!")
        print("\n=====================")
        return validar_cant_reservas()

def validar_reservas(claveReserva):
    match claveReserva:
        case "fecha":
                dia = validar_dia()
                mes = validar_mes()
                anio = validar_anio()
                return(f"{dia}/{mes}/{anio}")
        case "hora":
            horaVl = validar_hora()
            minutosVl = validar_minutos()
            return (f"{horaVl}:{minutosVl}")
        case "aula":
            aulaVl = validar_aula()
            return aulaVl
            
            
def validar_dia():
    try:
        diaVl = int(input("Ingrese dia valido(1 - 31): "))
        if 1 <= diaVl <= 31:
            return diaVl
        else:
            print("=====================\n")
            print(" ⚠️  Dia invalido!")
            print("\n=====================")
            return validar_dia()
    except:
        print("=====================\n")
        print(" ⚠️Dato invalido!")
        print("\n=====================")
        return validar_dia()
        
        
        
def validar_mes():
    try:
        mesVl = int(input("Ingrese mes valido(1 - 12): "))
        if mesVl <= 12:
            return mesVl
        else:
            print("=====================\n")
            print(" ⚠️  Mes invalido!")
            print("\n=====================")
            return validar_mes()
    except:
        print("=====================\n")
        print(" ⚠️Dato invalido!")
        print("\n=====================")
        return validar_mes()
    
    
def validar_anio():
    try:
        anioVl = int(input("Ingrese anio valido(2000 - 2025): "))
        if 2000 <= anioVl <= 2025:
            return anioVl
        else:
            print("=====================\n")
            print(" ⚠️  Anio invalido!")
            print("\n=====================")
            return validar_anio()
    except:
        print("=====================\n")
        print(" ⚠️Dato invalido!")
        print("\n=====================")
        return validar_anio()
    
    

def validar_hora():
    """
    Proposito: Validar que el usuario ingrese bien la Hora.
    Observaciones:
    Se tiene en cuenta que el laboratorio abre a las 06.
    Se tiene en cuenta que el laboratorio cierra a las 21.
    """
    try:
        horaVl = int(input("Ingrese las horas reservadas: "))
        if horaVl > 0:
            return horaVl
        else:
            print("=====================\n")
            print(" ⚠️  Hora invalida!")
            print("\n=====================")
            return validar_hora()
    except:
        print("=====================\n")
        print(" ⚠️Dato invalido!")
        print("\n=====================")
        return validar_hora()
    
def validar_minutos():
    try:
        minutoVl = int(input("Ingrese los minutos reservados(0 - 60): "))
        if 0 <= minutoVl <= 60:
            return minutoVl
        else:
            print("=====================\n")
            print(" ⚠️  Minuto invalido!")
            print("\n=====================")
            return validar_minutos()
    except:
        print("=====================\n")
        print(" ⚠️Dato invalido!")
        print("\n=====================")
        return validar_minutos()
    
    
def validar_aula():
    try:
        aulaVl = input("Por favor ingrese el aula(lab1,lab2,lab3)").lower().strip()
        
        while aulaVl not in ["lab1","lab2","lab3"]:
            print("=====================\n")
            print(" ⚠️  Aula invalida!")
            print("\n=====================")
            aulaVl = input("Ingrese una valida: ")
        return aulaVl
    except:
        print("=====================\n")
        print(" ⚠️Dato invalido!")
        print("\n=====================")
        return validar_aula()
    
    
    
def validar_archivo(listaReservas):
    """
    PROPOSITO: Valida si reservas.csv existe, si existe ve la eleccion del usuario, si no, crea el archivo.
    
    """
    if os.path.exists("reservas.csv"): #Verifica si el archivo existe.
        print("El archivo ya existe!")
        eleccionUsuario = input("¿Desea reemplazar los datos existentes o agregar nuevos equipos? [R] o [A]: ")
        match eleccionUsuario:
            case "r":
                crear_archivo_o_remplazar(listaReservas)
            case "a":
                agregar_nuevos_equipos(listaReservas)
    else:
        crear_archivo_o_remplazar(listaReservas)


def crear_archivo_o_remplazar(listaReservas):
    
    """
    PROPOSITO: Crea el archivo, y si en caso de que el usuario seleccion reemplazar, reemplaza el archivo existente por el del usuario.
    """
    
    with open("reservas.csv", "w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["id", "docente", "materia", "fecha","horas_reservadas", "aula"])
        writer.writeheader()
        for reserva in listaReservas:
            writer.writerow(reserva)


def agregar_nuevos_equipos(lista):
    """
    PROPOSITO: Agrega al archivo un nuevo equipo.
    """
    with open("reservas.csv","a",newline="") as archivo:
        writer = csv.DictWriter(archivo,fieldnames=["id", "docente", "materia", "fecha","horas_reservadas", "aula"])
        writer.writerows(lista)