def validate_number():
    numeroAValidar = int(input("Por favor ingrese un numero[-1000 a 1000]: "))
    while not(-1000 <= numeroAValidar <= 1000):
        print("Estas elijiendo un numero fuera del rango!")
        return validate_number()
    return numeroAValidar