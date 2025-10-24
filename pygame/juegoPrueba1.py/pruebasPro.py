import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú Principal")

# Colores
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
GRIS = (128, 128, 128)
AMARILLO = (255, 255, 0)
CELESTE = ( 0, 0,128)
AZUL = ( 0, 0, 255)

# Fuente
fuente = pygame.font.Font(None, 60)


# Botones
boton_jugar = pygame.Rect(ANCHO // 2 - 100, 250, 200, 60)
boton_salir = pygame.Rect(ANCHO // 2 - 100, 350, 200, 60)


# Bucle principal
def menu_principal():
    while True:
        pantalla.fill(GRIS)

        # Obtener posición del mouse
        mouse = pygame.mouse.get_pos()

        # Dibujar botones
        pygame.draw.rect(pantalla, AZUL if boton_jugar.collidepoint(mouse) else VERDE, boton_jugar)
        pygame.draw.rect(pantalla, AZUL if boton_salir.collidepoint(mouse) else ROJO, boton_salir)

        # Texto
        texto_jugar = fuente.render("JUGAR", True, BLANCO)
        texto_salir = fuente.render("SALIR", True, BLANCO)

        pantalla.blit(texto_jugar, (boton_jugar.x + 40, boton_jugar.y + 10))
        pantalla.blit(texto_salir, (boton_salir.x + 55, boton_salir.y + 10))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    print("Iniciar juego...")
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

# Ejecutar menú
menu_principal()
