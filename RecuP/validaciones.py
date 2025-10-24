import os
import utilidades as ut
from colorama import init, Fore,Style 
#inicializar colorama
init(autoreset=True)


def validar_archivo_existe():
    if os.path.exists("alumnos.csv"): #Verifica si el archivo existe.
        ut.mensaje_deteccion_archivo()
        eleccionUsuario = validar_opcion_usuario_R_A()
        return eleccionUsuario
    else:
        return "c"


def validar_opcion_usuario_R_A():
    """
    Proposito: Validar que el usuario ingrese una opcion correcta.
    """
    eleccionUsuario = input("¿Desea reemplazar los datos existentes o agregar nuevos registros? [R] o [A]: ").lower().strip()
    
    if eleccionUsuario == "a":
        return "a"
    elif eleccionUsuario == "r":
        return "r"
    else:
        print("Ingrese solo una de las dos opciones! [R] o [A]")
        validar_opcion_usuario_R_A()


def validar_cant_alumnos():
    """
    PROPOSITO: Validar que el usuario ingrese un numero y no otro caracter.
    """
    
    try:
        cantAlumnos = int(input("Por favor ingrese la cantidad de datos de alumnos que quiere ingresar! : "))
        return cantAlumnos
    except:
        print("=====================\n")
        print(" ⚠️  Dato invalido!")
        print("\n=====================")
        return validar_cant_alumnos()
    
def validar_nota():
    """
    Proposito: Validar que el usuario ingrese una nota entera y que sea una entre 0 - 10 inclusives.
    """
    
    try:
        notaValidar = int(input("Por favor ingrese la nota de dicho alumno: "))
        if 0 <= notaValidar <= 10:
            return notaValidar
        else:
            print("=====================\n")
            print(" ⚠️  La nota debe de ser un entero entre(0-10 inclusives!)")
            print("\n=====================")
            return validar_nota()
    except:
        
        print("=====================\n")
        print(" ⚠️  Dato invalido!")
        print("\n=====================")
        return validar_nota()


def validar_condicion(nota):
    condicion = "desaprobado"
    
    if nota >= 6:
        condicion = "promocionado"
    elif nota >= 4:
        condicion = "aprobado"
    else:
        condicion = "desaprobado"
    return condicion




def pedir_criterio_ord():
# Pedir criterio de ordenamiento: nombre o nota

    try:
        criterio = input("Ingrese el criterio de ordenamiento ('nombre' o 'nota'): ").strip().lower()
        if criterio not in ["nombre", "nota"]:
            print(Fore.RED + "Criterio inválido. Debe ser 'nombre' o 'nota'.")
            pedir_criterio_ord()
        else:
            return criterio
    except:
        print("=====================\n")
        print(" ⚠️  Dato invalido!")
        print("\n=====================")
        pedir_criterio_ord()
        
        
        
def pedir_tipo_Ord_Asc_Desc():
    # Pedir orden: ascendente o descendente
    try:
        orden = input("Ingrese el orden [ASC] o [DESC]: ").strip().upper()
        if orden not in ["ASC", "DESC"]:
            print(Fore.RED + "Orden inválido. Debe ser 'ASC' o 'DESC'.")
            pedir_tipo_Ord_Asc_Desc()
        else:
            return orden
    except:
        print("=====================\n")
        print(" ⚠️  Dato invalido!")
        print("\n=====================")
        pedir_tipo_Ord_Asc_Desc()