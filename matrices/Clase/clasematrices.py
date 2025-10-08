def inicializar_matriz(cantFilas:int,cantidadColumnas:int,valorInicial:any)->list:
    matriz = []
    for i in range(cantFilas):
        fila = [valorInicial] * cantidadColumnas
        matriz += [fila]
    return matriz

mi_matriz = inicializar_matriz(2,2,1)
print(mi_matriz)

# #=========================================================

# def cargar_matriz_secuencialmente(matriz:list):
#     """
#     PROPOSITO: Cargar una matriz completa por los datos del usuario secuencialmente.
#     """
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             matriz[i][j] = int(input(f"fila {i} columna {j}:"))
            
# cargar_matriz_secuencialmente(mi_matriz)
# print(mi_matriz,end="\n")
#==============================================================

def imprimir_matriz_con_end(matriz:list)->None:
    """
    Siempre tiene que estar antes de la que quiere imprimir!
    """
    for fila in matriz:
        for valor in fila:
            #IMPRIME CADA NUMERO SEGUIDO DE UN ESPACIO EN LA MISMA LINEA
            print(valor, end=" ")
        #AL TERMINAR LA FILA, HACEMOS UN SALTO DE LINEA.
        print()



#==============================================================

def cargar_matriz_aleatoriamente(matriz:list):
    """
    PROPOSITO: Cargar un dato ingresado por el usuario en la fila y columna especificada por el usuario.
    """
    seguir = "S"
    while seguir == "S":
        fila = int(input("Indice de fila: "))
        columna = int(input("Indice de columna: "))
        dato = int(input("Ingrese el numero a cargar: "))
        matriz[fila][columna] = dato
        seguir = input("Desea seguir cargando? S/N: ")
        imprimir_matriz_con_end(matriz)
        
cargar_matriz_aleatoriamente(mi_matriz)

#==============================================================

def buscar_valor_entero(matriz:list , valor:int):
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se encontro el numero en fila {i} columna {j}")
                # return -> Solo si quiere mostrar el primero!
                
buscar_valor_entero(mi_matriz,5)


#==============================================================
import random

def matriz_aleatoria(filas:int, columnas:int,minimo:int = 0,maximo:int =9):
    """
    CARGA UNA MATRIZ ALEATORIA, con filas x columnas con numeros enteros aleatorios entre minimo y maximo(inclusive)
    """
    matriz = []
    for _ in range(filas):
        fila=[random.randit(minimo,maximo)for _ in range(columnas)]
        matriz.append(fila)
    return 

#==============================================================
def sumar_matrices(A,B):
    """
    Suma dos matrices del mismo tamanio.
    """
    #Verificar que las dimensiones coincidan.
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        # raise ValueError("Las matrices deben de tener el mismo tamnio")  ESTO CORTA EL CODIGO Y TIRA EL ERROR!
        print("Las matrices deben de tener el mismo tamanio.")
        return #Esto tira el error y corta el codigo, lo mismo
        #pero con una linea de mas!
    
    resultado = []
    for i in range(len(A)):
        fila = []
        
        for j in range(len(B)):
            fila.append(A[i][j] + B[i][j])
            
        resultado.append(fila)
    return resultado

#==============================================================

def multiplicar_por_escalar(matriz,escalar):
    """
    Multiplica cada elemento de la matriz por un escalar
    """
    resultado = []
    for i in range(len(matriz)):
        nueva_fila = []
        for j in range(len(matriz[i])):
            nueva_fila.append(matriz[i][j] * escalar)
        resultado.append(nueva_fila)
    return resultado


#SUMA DE MATRICES POR COMPRENSION
# C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# ============================================================

def multiplicar_matrices(A, B):
    # Verificar si se puede multiplicar
    if len(A[0]) != len(B):
        # raise ValueError("La matriz A tiene que tener 2columnas y la matriz B tiene que tener 2 Filas.") 
        print("Número de columnas de A debe ser igual al número de filas de B")
        return

    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado