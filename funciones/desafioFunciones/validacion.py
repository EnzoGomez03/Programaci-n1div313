# Validate.py
# validate_number()
# validate_length()


def validate_number(numeroAValidar, numeroEsperado)-> bool:
    try:
        numero = float(numeroAValidar)
        return numero == float(numeroEsperado)
    except(ValueError, TypeError):
        print('No es un numero, por favor ingresa uno.')
        return False


def validate_length(datoAValidar:str,lengEsperado:int)-> bool:
    try:
        dato = len(datoAValidar)
        return dato == int(lengEsperado)
    except(AttributeError, TypeError):
        print('Dato invalido')
        return False
