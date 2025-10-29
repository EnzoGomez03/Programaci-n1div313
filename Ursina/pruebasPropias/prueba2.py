from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
Sky()

Entity(
    #Esto es para el escenario.
    model='plane',
    collider= 'mesh',
    texture= '../pruebas/assets/Terrain004_1K_Color.png',
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

arbol= Entity(
    model='assets/pino.glb',
    position= (10,0,20),
    scale=(4),
    collider='mesh' #Esta colicion "mesh" hace el contorno del objeto
)

otroArbol = Entity(
    model='assets/Tree.glb',
    position=(18,0,30),
    scale=(4),
    collider='mesh'
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