# import json #se importa libreria de JSON

# #se crea conexión al Drive
# # from google.colab import drive
# # drive.mount("/drive/")
# # Direccion = "/drive/MyDrive/Clases_47765_python/Entrega_Proyecto_1"


# # se crea el diccionario como base de datos
# Usuarios = {}

# #función de registro de usuario donde se captura los datos de usuario y se almacenan en el diccionario : Usuarios[nombres]=contraseña
# def registro_usuarios():
#     print("REGISTAR USUARIO\n")
#     nombres = input("Ingrese nombre del usuario: ")
#     contraseña = input("Ingrese una contraseña: ")
#     Usuarios[nombres]=contraseña
#     print ("Usuario Creado Correctamente.:\n")
#     input('Para volver al menu Principal oprima Enter...')

# #función de consulta de usuario donde va y verifica los datos almacenados en el diccionario.
# def consulta_usuarios():
#     print("Usuarios Registrados\n")
#     print("-"*10)
#     for key, value in Usuarios.items():
#         print("RESULTADOS\n")
#         print(f"USUARIO: {key}\n")
#         print(f"CONTRASEÑA: {value}\n")
#     print("-"*10)
#     input('Presione Enter para continuar...')

# #función de login donde va y retorna los usuarios almacenados en el diccionario, y en caso de no estar registrodo el programa le dira que no existe.
# def loguin_usuario():
#     print("Iniciar sesion\n")
#     codigo1 = input("Ingrese su usuario de red asignado: ")
#     contraseña1 = input("Ingrese  Contraseña: ")
#     if (codigo1) in Usuarios:
#         print('El usuario ya se encuentra registrado en el sistema')
#         if Usuarios[codigo1] == contraseña1:
#             print("Bienvenid@ ha iniciado correctamente\n")
#         else:
#             print("Contraseña incorrecta, Vuelva a validar")
#     else:
#         print('No existe usuario no no se encuentra en nuestra base')

#     input('Para volver al menu Principal oprima Enter...')

# # #función de guardar en el Drive con archivo tipo JSON, asi hace la conversion a diccionario
# # def Guardar():
# #     with open(Direccion + "/proyectoPreentrega1.json" , "w") as file:
# #         json.dump(Usuarios,file, indent=4)

# def opciones_menu():
#     print("1. Registrar nuevo usuario")
#     print("2. Ver Usuarios registrados")
#     print("3. Iniciar Sesion")
#     print("4. Guardar")
#     print("5. Cerrar Programa")

# def menu():
#     # se crea un menú de apertura
#     print("BIENVENIDOS AL PROGRAMA DE REGISTRO DE no-CODERHOUSE.\n")
#     print("Por favor, seleccione una opción del menú:")
#     opciones_menu()


# #función del Menu principal donde se almacena las variables a ejecutar
# def my_Programa(opcion):

#     menu()
#     # opcion = input("Ingrese el número de la opción deseada: ")

# #se creara un bucle para las condiciones del programa
#     while True:
#     # registrar usuarios
#         if opcion == "1":
#             registro_usuarios()
#     # Ver los usuarios registrados
#         elif opcion == "2":
#             consulta_usuarios()
#     # Iniciar sesion con usuarios
#         elif opcion == "3":
#             loguin_usuario()
#     #guardar
#         elif opcion == "4":
#             Guardar()
#             print("Se guardo Exitosamente\n")
#     #cerrar programa
#         elif opcion == "5":
#             break
#         else:
#             print("Opción inválida. Por favor, seleccione una opción válida del menú.")
#             opciones_menu()
            
# opcion = input("Ingrese el número de la opción deseada: ")
# my_Programa(opcion)