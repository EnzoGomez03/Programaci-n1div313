from ursina import *
import math

app = Ursina()
window.color = color.rgb(215,235,255)
window.fps_counter.enabled = True

# Mundo
ground = Entity(model='cube', color=color.lime.tint(-.2), scale=(80,1,80), y=-2, collider='box')
plat1  = Entity(model='cube', color=color.gray,  position=(6,0,6),  scale=(4,1,4), collider='box')
plat2  = Entity(model='cube', color=color.azure, position=(12,2,2), scale=(3,1,3), collider='box')
Sky()

# Personaje
player = Entity(
    model='assets/personaje.glb',
    color=color.white,
    scale=1.0,
    position=(0, 1.2, 2.5),    # arranque alto para evitar interpenetración inicial
    rotation_y=0
)
# BoxCollider ajustado; pon size.y a tu altura real
player.collider = BoxCollider(player, center=Vec3(0,1.0,0), size=Vec3(0.8,2.0,0.8))  # [web:56]

# Cámara con pivote (tercera persona)
pivot = Entity(position=player.position + Vec3(0,1.3,0))
camera.parent     = pivot
camera.position   = (0, 0.8, -4.2)
camera.rotation_x = 12

# Parámetros del controlador
move_speed       = 6.0
accel            = 16.0
manual_turn_deg  = 110.0      # giro con A/D
gravity          = 30.0
jump_force       = 9.5
max_fall_step    = 0.5        # límite caída por frame [web:220]
skin             = 0.07       # separación anti-penetración
probe_h          = 1.05       # altura del raycast de grounding
snap_dist        = 3.8
step_height      = 0.35       # “escalón” máximo que puede subir [web:261]

min_zoom, max_zoom = 2.3, 9.0
orbit_speed      = 120.0
pitch_min, pitch_max = 6, 58

vel_y  = 0.0
vel_2d = Vec2(0,0)

def clamp(v,a,b): return max(a,min(b,v))

def ground_snap_and_step():
    """Devuelve (grounded, floor_y) y hace step-up simple si hay borde bajo."""
    origin = player.world_position + Vec3(0, probe_h, 0)

    # Ray hacia abajo (centro)
    hit_c = raycast(origin, Vec3(0,-1,0), distance=snap_dist, ignore=[player], debug=False)

    # Ray ligeramente adelantado en dirección de marcha para detectar escalón
    yaw = math.radians(player.rotation_y)
    fwd = Vec3(math.sin(yaw), 0, math.cos(yaw))
    ahead = origin + fwd * 0.4
    hit_f = raycast(ahead, Vec3(0,-1,0), distance=snap_dist, ignore=[player], debug=False)

    # Decide altura de piso a partir de los hits
    hits = [h for h in (hit_c, hit_f) if h.hit]
    if not hits:
        return False, None

    floor_y = max(h.world_point.y for h in hits)  # preferí el más alto para evitar “baches”
    # Intento de step-up: si el piso adelantado está un poco más alto, y dentro del rango step_height, sube
    if hit_f.hit and hit_c.hit:
        delta = hit_f.world_point.y - hit_c.world_point.y
        if 0 < delta <= step_height:
            # Subir suavemente
            player.y += min(delta, step_height)

    return True, floor_y

def input(key):
    # Zoom
    if key == 'scroll up':
        camera.z += 0.25 * abs(camera.z)
    if key == 'scroll down':
        camera.z -= 0.25 * abs(camera.z)
    camera.z = -clamp(abs(camera.z), min_zoom, max_zoom)

def update():
    global vel_y, vel_2d

    # Pivote sigue al jugador para órbita
    pivot.position = player.position + Vec3(0,1.3,0)

    # Órbita con botón derecho
    if held_keys['right mouse']:
        pivot.rotation_y += mouse.velocity[0] * orbit_speed
        camera.rotation_x = clamp(camera.rotation_x - mouse.velocity[1] * orbit_speed * 0.5, pitch_min, pitch_max)

    # Giro manual con A/D (limitado)
    player.rotation_y += (held_keys['d'] - held_keys['a']) * manual_turn_deg * time.dt

    # Entrada W/S para avanzar/retro
    inp = Vec2(0, held_keys['w']-held_keys['s'])
    if inp.length() > 0: inp = inp.normalized()
    vel_2d += (inp - vel_2d) * accel * time.dt

    # Dirección según yaw del personaje
    moved = False
    if abs(vel_2d.y) > 0.001:
        yaw = math.radians(player.rotation_y)
        fwd = Vec3(math.sin(yaw), 0, math.cos(yaw))
        move_dir = fwd * vel_2d.y
        move_vec = move_dir.normalized() * move_speed * time.dt

        # Antipared
        head = player.world_position + Vec3(0, probe_h, 0)
        if not raycast(head, move_dir.normalized(), distance=0.6, ignore=[player]).hit:
            player.position += move_vec
            moved = True

    # Cámara mira a donde mira el personaje
    camera.look_at(player.world_position + player.forward*10 + Vec3(0,1.5,0))

    # Física vertical con tope
    vel_y -= gravity * time.dt
    dy = clamp(vel_y * time.dt, -max_fall_step, max_fall_step)
    player.y += dy

    grounded, floor_y = ground_snap_and_step()
    if grounded:
        feet_offset = player.collider.center.y - player.collider.size.y/2
        desired_y = floor_y - feet_offset + skin
        if player.y <= desired_y + 0.02 and vel_y <= 0:
            player.y = desired_y
            vel_y = 0
            if held_keys['space']:
                vel_y = jump_force

app.run()
