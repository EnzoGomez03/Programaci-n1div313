from colorama import init, Fore,Style 
import utilidades as ut
import time
import csv
import os
import validaciones as vl
#inicializar colorama
init(autoreset=True)


#==============================Opciones Menu==================
def opciones_menu():

        ut.animar_texto("=== BIENVENIDO AL MENU ===", Fore.MAGENTA)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.GREEN + "1.Cargar datos de estudiantes")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW + "2.Mostrar listado de estudiantes")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"3.Buscar estudiante")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"4.Calcular estadísticas")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"5. Ordenar y mostrar")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"6.Generar informe resumen")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.RED +"7.Salir")
        time.sleep(0.3)
        print("___"*20)

#==============================Opcion 1 menu==================

def cargar_datos_estudiantes(opcionUsuarioArchivo):
    datosEstudiantes = crear_datos_estudiantes() #Cargo los datos de los estudiantes!
    
    match opcionUsuarioArchivo:
        case "r":
            remplazar_archivo_de_alumnos(datosEstudiantes)
        case "a":
            agregar_datos_alumnos(datosEstudiantes)
        case "c":
            crear_archivo(datosEstudiantes)


    print("===" *20)
    print(Fore.GREEN + "\n Datos de los alumnos cargados!\n")
    print("===" *20)
    ut.esperar_limpiar()

def remplazar_archivo_de_alumnos(alumnosList):
    with open("alumnos.csv", "w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre","nota"])
        writer.writeheader()
        
        for alumno in alumnosList:
            writer.writerow(alumno)

def agregar_datos_alumnos(alumnosList):
    """
    Proposito: Agregar las reservas que el usuario ingreso, pero sin borrar las existentes.
    """
    with open("alumnos.csv","a",newline="") as archivo:
        writer = csv.DictWriter(archivo,fieldnames=["nombre","nota"])
        writer.writerows(alumnosList)


def crear_archivo(alumnosList):
    """
    PROPOSITO: Crear archivo en caso de que tal no exista, y cargarle los alumnos que ingreso.
    """
    with open("alumnos.csv", "w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre","nota"])
        writer.writeheader()
        for alumno in alumnosList:
            writer.writerow(alumno)


def crear_datos_estudiantes():
    """
    PROPOSITO: Cargar los datos de los estudiantes, tantos como el usuario desee.
    """
    listaAlumnos = []
    cantAlumnosCargar = vl.validar_cant_alumnos()
    
    for x in range(cantAlumnosCargar):
        nombre = input("Por favor ingrese el nombre del Alumno: ").lower().strip()
        notaAlumno = vl.validar_nota()
        datosAlumno = {
            'nombre': nombre,
            'nota' : notaAlumno
        }
        listaAlumnos.append(datosAlumno)
    
    return listaAlumnos


#============================Opcion 2 Menu======================
def mostrar_listado_estudiantes():
    
    """
    PROPOSITO: Mostrarle al usuario los datos de los alumnos cargados hasta el momento.
    """
    datosAlumnos = ut.leer_archivo("alumnos.csv")
    for alumno in datosAlumnos:
        print(Fore.BLACK +"===" * 40)
        print(f"Alumno: {datosAlumnos.index(alumno) + 1} ")
        for dato in alumno:
            print(f"{dato}: {alumno[dato]} | "  , end=" ")
        print()
    ut.esperar_limpiar()



#==========================Opcion 3 Menu========================

def buscar_estudiante():
    datos = ut.leer_archivo("alumnos.csv")
    alumnoABuscar = input("Por favor ingrese el nombre del alumno: ").lower().strip()
    encontrado = False
    
    for alumno in datos:
        if alumnoABuscar == alumno["nombre"]:
            print(Fore.GREEN + "Alumno Encontrado!.")
            print(f"Nota de alumno:{alumno['nota']} ")
            encontrado = True
            break
    
    if not encontrado:
        print(Fore.RED + "El alumno no se a encontrado!.")
        


#===========================Opcion Menu 4============================
def sub_menu():
    ut.animar_texto("=== Bienvenido al menu Estadisticas===", Fore.MAGENTA)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.GREEN + "1.Promedio general del curso.")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW + "2.Cantidad de aprobados y desaprobados.")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW +"3.Nota mas alta y mas baja.")
    print("___"*20)
    time.sleep(0.2)
    print(Fore.RED + "4.Salir del submenu")


def calcular_estadisticas():
    archivo = "alumnos.csv"
    ut.limpiar()
    
    while True:
        sub_menu()
        opcion = input("Por favor ingrese una opcion: ")
        
        if opcion =="1":
            promedio_del_curso(archivo)
            ut.esperar_limpiar()
        elif opcion == "2":
            total_aprobados_desaprobados(archivo)
            ut.esperar_limpiar()
        elif opcion =="3":
            nota_mas_alta_y_mas_baja(archivo)
        elif opcion == "4":
            print(Fore.BLACK +"===" * 20)
            ut.animar_texto("Saliendo del submenu.👋 Hasta luego!",Fore.GREEN)
            print(Fore.BLACK +"===" * 20)
            ut.esperar_limpiar()
            break


#=======================Opcion SubMenu 1 ====================================
def notas_del_curso(listaAlumnos):
    notasCurso = []
    for alumno in listaAlumnos:
        nota = int(alumno["nota"])
        notasCurso.append(nota)
    
    return notasCurso

def promedio_del_curso(archivoALeer):
    """
    PROPOSITO: Indicar el promedio total de nota entre todo el curso.
    """
    datosAlumnos = ut.leer_archivo(archivoALeer)
    sumaNotas = 0
    notasTotalesCurso = sum(notas_del_curso(datosAlumnos))
    cantidadAlumnos = len(datosAlumnos)
    promedio = notasTotalesCurso // cantidadAlumnos
    
    print(f"El promedio del curso es de: {promedio}")


#======================Opcion Submenu 2 =====================================

def total_aprobados_desaprobados(archivoALeer):
    archivoAlumnos = ut.leer_archivo(archivoALeer)
    alumnosAprobados = 0
    alumnosDesaprobados = 0
    notas = notas_del_curso(archivoAlumnos)
        
    for notaAlumno in notas:
        if notaAlumno >= 6:
            alumnosAprobados += 1
        else:
            alumnosDesaprobados += 1
    print(Fore.GREEN + f"✅ Los alumnos aprobados son: {alumnosAprobados}")
    print(Fore.RED + f"❌ Los alumnos desaprobados son: {alumnosDesaprobados}")


#======================= Opcion Submenu 3 ===================================
def nota_mas_alta_y_mas_baja(archivoALeer):
    datosAlumnos = ut.leer_archivo(archivoALeer)
    notas = notas_del_curso(datosAlumnos)
    notaMasAlta = max(notas)
    notaMasBaja = min(notas)
    alumnoNotaMasAlta = buscar_alumno_nota_mas_alta(datosAlumnos,notaMasAlta)
    alumnoNotaMasBaja = buscar_alumno_nota_mas_baja(datosAlumnos, notaMasBaja)
    
    print(Fore.CYAN + f"🏆 Alumno con mejor nota ({notaMasAlta}): {alumnoNotaMasAlta}")
    print(Fore.RED + f"⚠️ Alumno con peor nota ({notaMasBaja}): {alumnoNotaMasBaja}")


def buscar_alumno_nota_mas_alta(datos,notaAlta):

# Buscar el primer alumno con la nota más alta
    for alumno in datos:
        if int(alumno["nota"]) == notaAlta:
            alumnoMejor = alumno["nombre"]
            return alumnoMejor

def buscar_alumno_nota_mas_baja(datos,notaBaja):
    for alumno in datos:
        if int(alumno["nota"]) == notaBaja:
            alumnoPeor = alumno["nombre"]
            return alumnoPeor
        

#=======================Opcion MENU 5========================================
# 5) Ordenar y mostrar

# Solicitar al usuario el criterio de ordenamiento (ASC o DESC) y mostrar la lista ordenada por nota según esa elección.

# La lista original no debe modificarse (usar una copia).
# Validar que el texto ingresado sea correcto, sin importar mayúsculas/minúsculas.


def notas_alumnos(listaAlumnos):
    lista = []
    for alumno in listaAlumnos:
        alumno['nota'] = int(alumno['nota'])
        lista.append(alumno)
    return lista

def ordenar_mostrar():
    datosAlumnos = ut.leer_archivo("alumnos.csv")
    notasDeAlumnos = notas_alumnos(datosAlumnos)
    
    while True:
        criterioUsuario = input("Por favor ingrese el criterio de ordenamiento que desea [ASC] o [DESC]: ").strip().upper()
        if criterioUsuario in ["ASC","DESC"]:
            break
    
    alumnos_ordenados_notas = sorted(notasDeAlumnos, key=lambda alumno:alumno['nota'], reverse = (criterioUsuario == "DESC") )

    mostrar_ordenado(alumnos_ordenados_notas)
    
def mostrar_ordenado(alumnosOrdenados):
    
    for alumno in alumnosOrdenados:
        print("___"*20)
        print(f"{alumno['nombre']} | {alumno['nota']}")
        print("___"*20)
    ut.esperar_limpiar()



#===================================Opcion Menu 6 =======================================================
# 6) Generar informe resumen

# Generar un informe final con el siguiente formato:

# INFORME FINAL DEL CURSO

# -------------------------

# Cantidad total de estudiantes: XX

# Promedio general: XX.XX

# Aprobados: XX

# Desaprobados: XX

# Mejor nota: X (Alumno: NOMBRE)

# Peor nota: X (Alumno: NOMBRE)

# -------------------------

# Mostrarlo por pantalla y también guardar el texto en un archivo llamado "informe.txt".


def generar_informe_resumen():
    """
    PROPOSITO: Informa al usuario el informe general de todo el curso.
    """
    datosAlumnos = ut.leer_archivo("alumnos.csv")   
    cantidadTotalEstudiantes = len(datosAlumnos)
    promedioGeneral = promedio_del_curso("alumnos.csv")
    totalAprobados,totalDesaprobados = total_aprobados_desaprobados_sin_print()
    mejorNota = max(datosAlumnos, key=lambda alumno: int(alumno['nota']))
    peorNota = min(datosAlumnos, key=lambda alumno: int(alumno['nota']))
    
    texto_informe = f"""INFORME FINAL DEL CURSO
    {'___'*30}
    Cantidad total de estudiantes: {cantidadTotalEstudiantes}
    Promedio General: {promedioGeneral}
    Total Aprobados: {totalAprobados}
    Total Desaprobados: {totalDesaprobados}
    Mejor nota: {mejorNota['nota']} (Alumno: {mejorNota['nombre']})
    Peor nota: {peorNota['nota']} (Alumno: {peorNota['nombre']})
    {'___'*30}
    """
    print(texto_informe)
    
    guardar_texto(texto_informe)


def guardar_texto(texto):
    with open("informe.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)

def total_aprobados_desaprobados_sin_print():
    archivoAlumnos = ut.leer_archivo("alumnos.csv")
    alumnosAprobados = 0
    alumnosDesaprobados = 0
    notas = notas_del_curso(archivoAlumnos)
        
    for notaAlumno in notas:
        if notaAlumno >= 6:
            alumnosAprobados += 1
        else:
            alumnosDesaprobados += 1
            
    return alumnosAprobados, alumnosDesaprobados

#===================================Opcion Menu 7========================================================
def salir():
    print(Fore.BLACK +"===" * 20)
    ut.animar_texto("Saliendo del sistema.👋 Hasta luego!",Fore.GREEN)
    print(Fore.BLACK +"===" * 20)
    
