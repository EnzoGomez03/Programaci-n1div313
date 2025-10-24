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

        ut.animar_texto("=== BIENVENIDO AL MENU ESTUDIANTES ===", Fore.MAGENTA)
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
        print(Fore.YELLOW +"6.Filtrar por condición de estudiantes")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.YELLOW +"7.Generar informe resumen")
        time.sleep(0.3)
        print("___"*20)
        time.sleep(0.3)
        print(Fore.RED +"8.Salir")
        time.sleep(0.3)




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
        writer = csv.DictWriter(archivo, fieldnames=["legajo","nombre","nota","condicion"])
        writer.writeheader()
        
        for alumno in alumnosList:
            writer.writerow(alumno)


def agregar_datos_alumnos(alumnosList):
    """
    Proposito: Agregar las reservas que el usuario ingreso, pero sin borrar las existentes.
    """
    with open("alumnos.csv","a",newline="") as archivo:
        writer = csv.DictWriter(archivo,fieldnames=["legajo","nombre","nota","condicion"])
        writer.writerows(alumnosList)



def crear_archivo(alumnosList):
    """
    PROPOSITO: Crear archivo en caso de que tal no exista, y cargarle los alumnos que ingreso.
    """
    with open("alumnos.csv", "w", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["legajo","nombre","nota","condicion"])
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
        legajoAlumno = int(input("Por favor ingrese el legajo del Alumno: "))
        condicionAlumno = vl.validar_condicion(notaAlumno)
        datosAlumno = {
            'legajo': legajoAlumno,
            'nombre': nombre,
            'nota' : notaAlumno,
            'condicion': condicionAlumno
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
            for dato in alumno:
                print (f"{dato}: {alumno[dato]} |" ,end = " " )
            # print(f"Nota de alumno:{alumno['nota']} ")
            print()  # salto de línea al final
            encontrado = True
            break
    
    if not encontrado:
        print(Fore.RED + "El alumno no se a encontrado!.")
        


#===================================Opcion Menu 4 =======================================================
def sub_menu():
    ut.animar_texto("=== Bienvenido al menu Estadisticas de Alumnos ===", Fore.MAGENTA)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.GREEN + "1.Promedio general del curso.")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW + "2.Porcentaje de promocionados, aprobados y desaprobados.")
    time.sleep(0.2)
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW +"3.Nombre de los alumnos con mejor y peor nota.")
    print("___"*20)
    time.sleep(0.2)
    print(Fore.YELLOW + "4.Promedio de los alumnos con condición de promoción.")
    print("___"*20)
    time.sleep(0.2)
    print(Fore.RED +"5.Salir del Submenu!.")


def calcular_estadisticas():
    archivo = "alumnos.csv"
    ut.limpiar()
    
    while True:
        sub_menu()
        opcion = input("Por favor ingrese una opcion: ")
        
        #En caso de que el usario no elija una opcion del menu.
        if opcion not in ["1","2","3","4","5"]:
            print(Fore.RED +"===" * 20)
            print(Fore.BLACK +"\n ⚠️  Ingresa una opcion correcta del SubMenu! \n")
            print(Fore.RED + "===" * 20)
            ut.esperar_limpiar()
            calcular_estadisticas()
        
        
        
        if opcion =="1":
            promedio_del_curso(archivo)
            ut.esperar_limpiar()
        elif opcion == "2":
            porcentaje_promocionados_aprobados_desaprobados(archivo)
            ut.esperar_limpiar()
        elif opcion =="3":
            alumnos_nota_baja_alta(archivo)
            ut.esperar_limpiar()
        elif opcion == "4":
            promedio_alumnos_promocion(archivo)
        elif opcion == "5":
            print(Fore.BLACK +"===" * 20)
            ut.animar_texto("Saliendo del submenu.👋 Hasta luego!",Fore.GREEN)
            print(Fore.BLACK +"===" * 20)
            ut.esperar_limpiar()
            break

#========================================Submenu Opcion 1=========================================================

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

#=============================================Submenu Opcion 2 ==============================================


def porcentaje_promocionados_aprobados_desaprobados(archivoALeer):
    archivoAlumnos = ut.leer_archivo(archivoALeer)
    alumnosPromocionados = 0
    alumnosAprobados = 0
    alumnosDesaprobados = 0
    notas = notas_del_curso(archivoAlumnos)
    totalAlumnos = len(notas)
    
    
    for notaAlumno in notas:
        if notaAlumno >= 6:
            alumnosPromocionados += 1
        elif notaAlumno >= 4:
            alumnosAprobados += 1
        else:
            alumnosDesaprobados += 1
    
    porcentaje_promocionados = (alumnosPromocionados / totalAlumnos) * 100
    porcentaje_aprobados = (alumnosAprobados / totalAlumnos) * 100
    porcentaje_desaprobados = (alumnosDesaprobados / totalAlumnos) * 100
    
    print(Fore.CYAN + f"🏅 Promocionados: {porcentaje_promocionados:.2f}%")
    print(Fore.GREEN + f"✅ Los alumnos aprobados son: {porcentaje_aprobados:.2f}%")
    print(Fore.RED + f"❌ Los alumnos desaprobados son: {porcentaje_desaprobados:.2f}%")

#=============================================Submenu Opcion 3 ==============================================
def alumnos_nota_baja_alta(archivoALeer):
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

    

#=============================================Submenu Opcion 4 ==============================================
def promedio_alumnos_promocion(archivoALeer):
    datosAlumnos = ut.leer_archivo(archivoALeer)
    notas = notas_del_curso(datosAlumnos)
    promocionadosNotas = []
    
    for nota in notas:
        if nota >= 6:
            promocionadosNotas.append(nota)
    
    totalNotasPromocion = sum(promocionadosNotas)
    alumnosTotalesPromocion = len(promocionadosNotas)
    promedioPromocionados = totalNotasPromocion / alumnosTotalesPromocion
    
    print(Fore.GREEN + f"✅  Promedio de alumnos promocionados: {promedioPromocionados:.2f}")
    
    
#=============================================Menu Opcion 5 ==============================================

def ordenar_mostrar():
    datosAlumnos = ut.leer_archivo("alumnos.csv")
    alumnos_copia = datosAlumnos.copy()
    criterioOrd = vl.pedir_criterio_ord()
    tipoOrdAscODesc = vl.pedir_tipo_Ord_Asc_Desc()

    # Convertir las notas a enteros solo si se ordena por nota
    if criterioOrd == "nota":
        for alumno in alumnos_copia:
            alumno["nota"] = int(alumno["nota"])


    # Ordenar usando sorted y reverse según el orden elegido
    alumnos_ordenados = sorted(
        alumnos_copia,
        key=lambda alumno: alumno[criterioOrd],
        reverse=(tipoOrdAscODesc == "DESC")
    )

    # Mostrar resultados
    mostrar_ordenado(alumnos_ordenados)

def mostrar_ordenado(alumnosOrdenados):
    for alumno in alumnosOrdenados:
        print("___" * 20)
        print(f"{alumno['nombre']} | {alumno['nota']}")
        print("___" * 20)
    ut.esperar_limpiar()
    
#=============================================Menu Opcion 6 ==============================================

def filtrar_por_condición_de_estudiantes():
    datosAlumnos = ut.leer_archivo("alumnos.csv")
    condicionFiltrado = input("Por favor ingrese la condicion de filtrado [promocionado,aprobado,desaprobado]: ").lower().strip()
    listaAlumnosFiltrado = []
    
    for alumno in datosAlumnos:
        if alumno["condicion"] == condicionFiltrado:
            listaAlumnosFiltrado.append(alumno)
            # print(f"legajo:"alumno[legajo])
    mostrar_filtrado(listaAlumnosFiltrado)
    guardar_archivo(listaAlumnosFiltrado)

def guardar_archivo(listaAlumnosFiltrado):
    guardar = input("¿Desea guardar el resultado en 'filtrados.csv'? [S/N]: ").strip().upper()
    if guardar == "S":
        guardar_filtrado_csv(listaAlumnosFiltrado)
        print("Archivo 'filtrados.csv' guardado correctamente.")
        
        
def guardar_filtrado_csv(lista):
    import csv
    with open("filtrados.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["legajo", "nombre", "nota", "condicion"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        for alumno in lista:
            writer.writerow(alumno)


def mostrar_filtrado(lista):
    for alumno in lista:
        print(f"legajo: {alumno['legajo']} | nombre {alumno['nombre']} | nota  {alumno['nota']} | condicion {alumno['condicion']}")



#===================================Opcion Menu 7========================================================

"""
INFORME FINAL DEL CURSO

------------------------------

Cantidad total de estudiantes: XX

Promedio general: XX.XX

Aprobados: XX (XX%)

Desaprobados: XX (XX%)

Mejor nota: X (Alumno: NOMBRE)

Peor nota: X (Alumno: NOMBRE)

Promedio de aprobados: XX.XX

------------------------------
"""
def generar_informe_resumen():
    datos = ut.leer_archivo("alumnos.csv")
    cantidadEstudiantes = len(datos)
    promedioGeneral = promedio_del_curso("alumnos.csv")
    aprobados = total_aprobados(datos)
    desaprobados = total_desaprobados(datos)
    mejorNota, peorNota = alumnos_nota_baja_alta_devuelve(datos)
    promedioDeAprobados = promedio_aprobados(datos)

    texto_informe = f"""INFORME FINAL DEL CURSO
{'___'*30}
Cantidad total de estudiantes: {cantidadEstudiantes}
Promedio General: {promedioGeneral}
Total Aprobados: {aprobados}
Total Desaprobados: {desaprobados}
Mejor nota: {mejorNota['nota']} (Alumno: {mejorNota['nombre']})
Peor nota: {peorNota['nota']} (Alumno: {peorNota['nombre']})
Promedio de aprobados: {promedioDeAprobados:.2f}
{'___'*30}
"""
    print(texto_informe)
    guardar_texto(texto_informe)


def guardar_texto(texto):
    with open("informe.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)


def promedio_aprobados(listaAlumnos):
    notasAprobadas = [int(alumno['nota']) for alumno in listaAlumnos if int(alumno['nota']) >= 4]
    if notasAprobadas:
        return sum(notasAprobadas) / len(notasAprobadas)
    return 0


def total_aprobados(datosAlumnos):
    notas = notas_del_curso(datosAlumnos)
    aprobados = 0
    for numero in notas:
        if numero >= 4:
            aprobados += 1
    return aprobados


def total_desaprobados(datosAlumnos):
    notas = notas_del_curso(datosAlumnos)
    desaprobados = 0
    for numero in notas:
        if numero < 4:
            desaprobados += 1
    return desaprobados


def alumnos_nota_baja_alta_devuelve(datos):
    notas = notas_del_curso(datos)
    notaMasAlta = max(notas)
    notaMasBaja = min(notas)
    alumnoNotaMasAlta = None
    alumnoNotaMasBaja = None
    for alumno in datos:
        if int(alumno['nota']) == notaMasAlta and alumnoNotaMasAlta is None:
            alumnoNotaMasAlta = alumno
        if int(alumno['nota']) == notaMasBaja and alumnoNotaMasBaja is None:
            alumnoNotaMasBaja = alumno
    return alumnoNotaMasAlta, alumnoNotaMasBaja

# def generar_informe_resumen():
#     datos = ut.leer_archivo("alumnos.csv")
#     cantidadEstudiantes = len(datos)
#     promedioGeneral = promedio_del_curso(datos)
#     aprobados = total_aprobados(datos)
#     desaprobados = total_desaprobados(datos)
#     mejorNota , peorNota = alumnos_nota_baja_alta_devuelve(datos)
#     promedioDeAprobados = promedio_aprobados(aprobados,datos)
    

#     texto_informe = f"""INFORME FINAL DEL CURSO
#     {'___'*30}
#     Cantidad total de estudiantes: {cantidadEstudiantes}
#     Promedio General: {promedioGeneral}
#     Total Aprobados: {aprobados}
#     Total Desaprobados: {desaprobados}
#     Mejor nota: {mejorNota['nota']} (Alumno: {mejorNota['nombre']})
#     Peor nota: {peorNota['nota']} (Alumno: {peorNota['nombre']})
#     {'___'*30}
#     """
    
#     print(texto_informe)
    
#     guardar_texto(texto_informe)


# def guardar_texto(texto):
#     with open("informe.txt", "w", encoding="utf-8") as archivo:
#         archivo.write(texto)


# def promedio_aprobados(alumnosAprobados,listaAlumnos):
#     notas = notas_del_curso(listaAlumnos)
#     notasAprobadas = 0

#     for nota in notas:
#         if nota >= 4:
#             notasAprobadas += 1
            
#     return alumnosAprobados / notasAprobadas

# def total_aprobados(datosAlumnos):
#     notas = notas_del_curso(datosAlumnos)
#     aprobados = 0
    
#     for numero in notas:
#         if numero >= 4:
#             aprobados += 1
#     return aprobados


# def total_desaprobados(datosAlumnos):
#     notas = notas_del_curso(datosAlumnos)
#     desaprobados = 0
    
#     for numero in notas:
#         if numero < 4:
#             desaprobados += 1
#     return desaprobados

# def alumnos_nota_baja_alta_devuelve(datos):
#     notas = notas_del_curso(datos)
#     notaMasAlta = max(notas)
#     notaMasBaja = min(notas)
#     alumnoNotaMasAlta = buscar_alumno_nota_mas_alta(datos,notaMasAlta)
#     alumnoNotaMasBaja = buscar_alumno_nota_mas_baja(datos, notaMasBaja)


#     return alumnoNotaMasAlta , alumnoNotaMasBaja


#=================================== Opcion Menu 8 ========================================================
def salir():
    print(Fore.BLACK +"===" * 20)
    ut.animar_texto("Saliendo del sistema.👋 Hasta luego!",Fore.GREEN)
    print(Fore.BLACK +"===" * 20)
    