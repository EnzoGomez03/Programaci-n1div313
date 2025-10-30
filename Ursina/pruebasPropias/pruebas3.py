from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
import classPrueba2 as cl

app = Ursina()

# ------------------------------
#   CIELO Y COLOR AMBIENTAL
# ------------------------------
window.color = color.rgb(255, 210, 160)  # color base del fondo
Sky(texture='sky_sunset')  # probá también: 'sky_default', 'sky_night'

# ------------------------------
#   LUCES
# ------------------------------
DirectionalLight().look_at(Vec3(1, -1, -1))
AmbientLight(color=color.rgb(130, 130, 130))

# ------------------------------
#   TERRENO
# ------------------------------
ground = Entity(
    model='plane',
    texture='grass',
    collider='mesh',
    scale=(120, 1, 120)
)

# ------------------------------
#   ELEMENTOS DECORATIVOS
# ------------------------------



for i in range(10):
    cl.Arbol(modelo='assets/pino.glb',position=(random.uniform(-40, 40), 0.5, random.uniform(-40, 40)),scale=(2))
    cl.Arbol(modelo='assets/Tree.glb',position=(random.uniform(-40, 40), 0.5, random.uniform(-40, 40)),scale=(2))
    # Entity(
    #     model='sphere',
    #     color=color.rgb(100, 100, 100),
    #     scale=Vec3(2, 1, 2),
    #     position=(random.uniform(-40, 40), 0.5, random.uniform(-40, 40))
    # )

# for i in range(7):
#     Entity(
#         model='cube',
#         color=color.rgb(40, 180, 60),
#         position=(random.uniform(-40, 40), 1, random.uniform(-40, 40)),
#         scale=(1, 4, 1)
#     )

# ------------------------------
#   JUGADOR
# ------------------------------
player = FirstPersonController(
    position=(0, 3, 0),
    speed=5,
    jump_height=2
)

# ------------------------------
#   CICLO DE COLOR (efecto día/noche suave)
# ------------------------------
def update():
    t = time.time() * 0.2
    window.color = color.rgb(
        200 + 40 * math.sin(t),
        150 + 50 * math.sin(t + 1),
        160 + 60 * math.sin(t + 2)
    )

app.run()
