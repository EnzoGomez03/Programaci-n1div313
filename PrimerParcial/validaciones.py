def validar_opcion_usuario_R_A():
    """
    Proposito: Validar que el usuario ingrese una opcion correcta.
    """
    eleccionUsuario = input("¿Desea reemplazar los datos existentes o agregar nuevos registros? [R] o [A]").lower().strip()
    
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