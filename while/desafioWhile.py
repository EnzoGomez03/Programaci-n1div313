# CANTIDAD DE ENTREVISTADOS
cantIngresos = 0

#VOTOS DE LOS ENTREVISTADOS
votosPorIA = 0
votosPorIOT = 0
votosPorRV = 0
notVotosIA = 0

#PERSONA CON MAYOR EDAD
edadMayor = 0 
nombreMayor = "El nombre de la persona con mayor edad"
tecnologíaMayor = "Tecnologia elegida del mayor de edad"

while not (cantIngresos == 10) :
    
    #INPUTS PARA LOS DATOS DEL EMPLEADO
    nombre = input("Por favor ingrese su nombre: ")
    edad = int(input("Ingrese su edad(debe ser 18 años o más): ")) #(debe ser 18 años o más)
    genero = input("Por favor ingrese su genero: ").lower() #(Masculino, Femenino, Otro)
    tecnologíaElegida = input('Ingrese la tecnologia elegida ("IA", "RV/RA", "IOT"): ') #(IA, RV/RA, IOT)
    
    #MATCH PARA CASO DE GENERO
    match genero :
        case "masculino":
            #MASCULINOS QUE VOTARON POR IA O IOT
            if tecnologíaElegida != "RV/RA" and 25 <= edad <= 50: 
                match tecnologíaElegida:
                    case "IA":
                        votosPorIA += 1
                    case "IOT":
                        votosPorIOT += 1
            elif 33 <= edad <= 40:    #MASCULINOS QUE NO VOTARON POR IA
                notVotosIA += 1 
                if tecnologíaElegida == "IOT":
                    votosPorIOT += 1
                elif tecnologíaElegida == "RV/RA":
                    votosPorRV +=1
    if edad > edadMayor:
        edadMayor = edad
        nombreMayor = nombre
        tecnologíaMayor = tecnologíaElegida
        
    cantIngresos += 1

#PORCENTAJES DE VOTOS
porcentajeVotosPorIA = (votosPorIA / cantIngresos) * 100
porcentajeVotosPorIOT = (votosPorIOT / cantIngresos) * 100
porcentajeVotosPorRVRA = (votosPorRV / cantIngresos) * 100
porcentajeVotosQueNoFueronParaIA = (notVotosIA / cantIngresos) * 100

#PRINTS DE VOTOS Y LA PERSONA DE MAYOR EDAD
print(f"El porcentaje de votos por IA es de {porcentajeVotosPorIA}")
print("======================================")
print(f"El porcentaje de votos por IOT es de {porcentajeVotosPorIOT}")
print("======================================")
print(f"El porcentaje de votos por RV/RA es de {porcentajeVotosPorRVRA}")
print("======================================")
print(f"El porcentaje de empleados masculinos, con edad entre 33 y 40 años que no votaron por IA es de {porcentajeVotosQueNoFueronParaIA}")
print("======================================")
print(f"El nombre de la persona con mas edad es {nombreMayor}, su edad es de {edadMayor} y voto por la tecnologia de {tecnologíaMayor}")