from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
Sky()

player = FirstPersonController()

Entity(
    model='plane',
    collider= 'mesh',
    texture= 'grass',
    scale= (100,1,100)
    
)

arma = Entity(
    model='plane',
    parent=camera.ui, #Esto es para que este en la camara del jugador
    texture = 'Ursina/pruebasPropias/assets/arma.png',
    scale=(0.10,0.55),
    rotation=(-90,-100,-100),
    position=(0.5,-0.3),
)


#De aca para arriba existe como un bucle que se va a hacer todo el tiempo
app.run() #Ejecuta la aplicacion


# Aca de bajo lo que se ponga, no se va a hacer porque esta fuera del bucle