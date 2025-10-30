from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random, math
import classPrueba2 as cl  # tu clase Arbol

app = Ursina()
Sky()

# ------------------------------
#   CONFIGURACIÓN
# ------------------------------
cantidad_bosques = 3        # cuántas zonas densas querés
arboles_por_bosque = 10     # árboles en cada zona
radio_bosque = 15           # tamaño de cada zona
espacio_minimo = 5           # distancia mínima entre árboles
area_total = 80             # tamaño del mapa (-area_total a +area_total)

# Lista global para guardar posiciones ya usadas
posiciones_usadas = []


def posicion_valida(nueva_pos, distancia_minima=5):
    """Verifica si la nueva posición no está demasiado cerca de otra."""
    for pos in posiciones_usadas:
        dx = nueva_pos[0] - pos[0]
        dz = nueva_pos[2] - pos[2]
        distancia = math.sqrt(dx**2 + dz**2)
        if distancia < distancia_minima:
            return False
    return True


# ------------------------------
#   GENERACIÓN DE BOSQUES
# ------------------------------
for i in range(cantidad_bosques):
    # Centro de cada bosque
    centro_x = random.uniform(-area_total, area_total)
    centro_z = random.uniform(-area_total, area_total)

    for j in range(arboles_por_bosque):
        for intento in range(100):
            # Posición cerca del centro del bosque
            angulo = random.uniform(0, 2 * math.pi)
            distancia = random.uniform(0, radio_bosque)
            x = centro_x + math.cos(angulo) * distancia
            z = centro_z + math.sin(angulo) * distancia
            pos = (x, 0.5, z)

            if posicion_valida(pos, espacio_minimo):
                posiciones_usadas.append(pos)
                # Alterna entre tipos de árboles
                modelo = random.choice(['assets/pino.glb', 'assets/Tree.glb'])
                escala = random.uniform(1.5, 2.5)
                cl.Arbol(modelo=modelo, position=pos, scale=escala)
                break

# ------------------------------
#   ESCENARIO
# ------------------------------
Entity(
    model='plane',
    texture='../pruebas/assets/Terrain004_1K_Color.png',
    collider='mesh',
    scale=(100,1,100)
)

player = FirstPersonController(position=(0, 3, 0))
app.run()
