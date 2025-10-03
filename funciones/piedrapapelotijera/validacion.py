def validate_number()-> int:
    numeroAValidar = int(input("Ingrese una jugada [1-3]: "))
    if not (1 <= numeroAValidar <=3):
        print("Tenes que elegir un numero del 1 al 3.")
        return validate_number()
    return numeroAValidar