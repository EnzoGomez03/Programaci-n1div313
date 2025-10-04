# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

def calcular_promedio_positivos(listaPositivos):
    totalNumerosPromedio = 0
    totalSumaPositivos = 0
    for posit in listaPositivos:
        if posit >= 0:
            totalNumerosPromedio += 1
            totalSumaPositivos += posit
    return totalSumaPositivos / totalNumerosPromedio

print(calcular_promedio_positivos([-1,2,-20,2,-10,2]))