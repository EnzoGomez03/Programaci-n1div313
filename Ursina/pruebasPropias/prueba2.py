from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import classPrueba2  as cl

app = Ursina()
Sky()

terreno = '../pruebas/assets/Terrain004_1K_Color.png'
arbolPino = 'assets/pino.glb'
arbolNormal = 'assets/Tree.glb'
muro = 'assets/muro.glb'

Entity(
    #Esto es para el escenario.
    model='plane',
    collider= 'mesh',
    texture= terreno,
    scale= (100,1,100)
    
)


#Puedo literalmente hacer cosas arriba de otras jugar con las posiciones etc
plat1 = Entity(
    model='cube', 
    color=color.gray,  
    position=(6,2,6),  
    scale=(4,1,4), 
    collider='box')

plat2 = Entity(
    model='cube', 
    color=color.red,  
    position=(4,1,6),  
    scale=(4,1,4), 
    collider='box')

#Arboles con Clases
arbol_pino = cl.Arbol(modelo=arbolPino,position=(1,0,1),scale=(2))
arbol_normal = cl.Arbol(modelo=arbolNormal,position=(10,1,10),scale=(4))

#Arboles Sin clases
# arbol_pino= Entity(
#     model= arbolPino,
#     position= (1,0,1),
#     scale=(2),
#     collider='mesh' #Esta colicion "mesh" hace el contorno del objeto
# )

# arbol_normal = Entity(
#     model= arbolNormal,
#     position=(5,1,5),
#     scale=(4),
#     collider='mesh'
# )
castillo = Entity(
    model = 'assets/castillo.glb',
    position= (20,0,30),
    scale= (20),
    collider='mesh'
)


# for i in range(10):
#     Entity(
#         model= muro,
#         position= (i * 2, 0 , 0 ),
#         scale= (2),
#         collider= 'box'
#     )

for i in range(10):
    Entity(
        model= 'assets/madera.glb',
        position= (i * 8, 0 , 0 ),
        scale= (2),
        collider= 'box'
    )


Entity(
    #           x,y,z(profundidad)
    scale= Vec3(3,6,10),
    model= 'cube',
    collider='box'
)

#crea una entidad que representa al jugador (con cámara y movimiento incluidos)
#FirstPersonController(
#     position = (0, 0, 0),     # Posición inicial
#     speed = 5,                # Velocidad de movimiento
#     gravity = 1,              # Intensidad de la gravedad
#     jump_height = 2,          # Altura del salto
#     mouse_sensitivity = Vec2(40, 40), # Sensibilidad del mouse
#     origin_y = -0.5,          # Ajuste vertical del modelo del jugador
#     collider = 'box',         # Tipo de colisión
#     model = None,             # Modelo 3D (por defecto invisible)
#     color = color.white,      # Color si usás un modelo visible
# )


player = FirstPersonController(
    position = (5, 2, 5),
    speed = 3,
    model = '../pruebas/assets/personaje.glb',
    collider = 'box'
)


app.run()