# numeros = int(input("Numero: "))

# for x in range(numeros):
#     numero = x
#     print(f"El numero es: {numero + 1}")


import csv
import os


# with open("equipos.csv","w",newline="") as archivo:
#     writer = csv.DictWriter(archivo, fieldnames=["id","nombre","categoria","estado","valor"])#Para escribir
    
#     writer.writeheader()
#     writer.writerow({"id":1,"nombre":"compu","categoria":"notebook","estado":"funcional","valor":1000})


import csv

# lista_equipos = [
#     { "id": 1, "nombre": "super compu",  "categoria": "notebook", "estado": "funcional", "valor": 500 },
#     { "id": 2, "nombre": "super computadora", "categoria": "notebook", "estado": "funcional", "valor": 700 }
# ]

# with open("equipos.csv", "w", newline="") as archivo:
#     writer = csv.DictWriter(archivo, fieldnames=["id", "nombre", "categoria", "estado", "valor"])
#     writer.writeheader()
#     for equipo in lista_equipos:
#         writer.writerow(equipo)
        
        
        
with open("equipos.csv", "r")as archivo:
    reader = csv.DictReader(archivo)
    for linea in reader:
        print(linea)
        

        
# if os.path.exists("equipos.csv"):
    print(os.path.exists("equipos.csv"))