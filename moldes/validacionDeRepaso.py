def validacion_input(clave):
    match clave:
        case "estado":
            eleccionUsuario = input("Ingrese un estado( 'funcional' , 'fuera de servicio'):").lower().strip()
            while eleccionUsuario not in ["funcional" , "fuera de servicio"]:
                print("=====================\n")
                print(" ⚠️Estado invalido!")
                print("\n=====================")
                eleccionUsuario = input("Ingrese uno válido : ")
            return (eleccionUsuario)
        case "categoria":
            eleccionUsuario = input("Categoria (router, pc, notebook, impresora): ").lower().strip()
            while eleccionUsuario not in ["router", "pc", "notebook", "impresora"]: 
                print("=================\n")
                print("⚠️ Categoria invalida!") 
                print("\n=================") 
                categoria = input(" Ingrese nuevamente: ")
            return(eleccionUsuario)
        case "valor":
                eleccionUsuario = float(input("Valor del equipo: ")).lower().strip()
                while not (eleccionUsuario > 0):
                    print("el valor debe ser un número positivo")
                    eleccionUsuario = float(input("Volve a ingresar el valor"))
                return eleccionUsuario



estado = validacion_input("estado")
categoria = validacion_input("categoria")
valor = validacion_input("valor")
print(estado)
print(categoria)
print(valor)