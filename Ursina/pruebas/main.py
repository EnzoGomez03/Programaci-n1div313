from ursina import *
import math

app = Ursina()
window.color = color.rgb(215,235,255)
window.fps_counter.enabled = True

# ------------------------------
# Mundo / Escenario
# ------------------------------
ground = Entity(model='cube', color=color.lime.tint(-.2), scale=(80,1,80), y=-2, collider='box')
plat1 = Entity(model='cube', color=color.gray,  position=(6,0,6),  scale=(4,1,4), collider='box')
plat2 = Entity(model='cube', color=color.azure, position=(12,2,2), scale=(3,1,3), collider='box')
Sky()

# ------------------------------
# Jugador (primera persona)
# ------------------------------
player = Entity(
    model=None,
    position=(0, 1.5, 0),
    collider='box'
)

# --- Modelo visible de los brazos (o cuerpo parcial) ---
# ⚠️ Reemplazá por tu modelo real, por ejemplo 'assets/personaje.glb'
arms = Entity(
    parent=camera,
    model='assets/personaje.glb',                  # poné tu modelo acá (por ej. 'assets/personaje.glb')
    scale=(0.4, 0.4, 0.4),
    color=color.azure,
    position=(0.4, -0.3, 0.6),
    rotation=Vec3(10, -20, 0)
)

# ------------------------------
# Parámetros de movimiento / físicas
# ------------------------------
move_speed = 6.0
jump_force = 9.0
gravity = 30.0
vel_y = 0.0

camera.parent = player
camera.position = (0, 1.5, 0)
camera.rotation = (0, 0, 0)

mouse_sensitivity = 80
rotation_x = 0

# ------------------------------
# Input
# ------------------------------
def update():
    global vel_y, rotation_x

    # Rotación con el mouse
    rotation_x -= mouse.velocity[1] * mouse_sensitivity
    rotation_x = clamp(rotation_x, -80, 80)
    camera.rotation_x = rotation_x
    player.rotation_y += mouse.velocity[0] * mouse_sensitivity

    # Movimiento
    direction = Vec3(
        math.sin(math.radians(player.rotation_y)),
        0,
        math.cos(math.radians(player.rotation_y))
    )
    right = Vec3(
        math.sin(math.radians(player.rotation_y + 90)),
        0,
        math.cos(math.radians(player.rotation_y + 90))
    )

    move = Vec3(0, 0, 0)
    if held_keys['w']:
        move += direction
    if held_keys['s']:
        move -= direction
    if held_keys['a']:
        move -= right
    if held_keys['d']:
        move += right

    move = move.normalized() * move_speed * time.dt
    player.position += move

    # Gravedad
    vel_y -= gravity * time.dt
    player.y += vel_y * time.dt

    # Detección de piso
    ray = raycast(player.world_position + Vec3(0, 0.5, 0), Vec3(0, -1, 0), distance=0.6, ignore=[player])
    if ray.hit:
        vel_y = 0
        player.y = ray.world_point.y + 1
        if held_keys['space']:
            vel_y = jump_force

    # Movimiento de brazos
    if held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']:
        arms.y = -0.3 + math.sin(time.time() * 6) * 0.02
    else:
        arms.y = -0.3


# Bloquear el cursor dentro de la ventana
mouse.locked = True

app.run()
