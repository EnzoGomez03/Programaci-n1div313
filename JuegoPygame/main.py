import pygame
import constantes
import colores as col
import funciones as fn
from personaje import Personaje
#Iniciamos pygame
pygame.init()

#Config de la ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

#Nombre de la pagina
pygame.display.set_caption("Proyecto")

#Aca va el pj principal
animaciones = []
for numeroImagen in range(7):
    img = pygame.image.load(f"JuegoPygame//assets//imagenes//characters//player//mov{numeroImagen}.png")
    # Recortamos solo el área visible
    rect_recorte = img.get_bounding_rect()
    player_image = img.subsurface(rect_recorte).copy()
    img = fn.escalar_img(img,constantes.SCALA_PERSONAJE)
    animaciones.append(img)



#                   x , y, listaDeImagenesaa
jugador = Personaje(10,10, animaciones)

#controlar los fps
reloj = pygame.time.Clock()

run = True
while run:

    #va a 60fps
    reloj.tick(constantes.FPS)
    #LIMPIAR PANTALLA CADA FRAME
    ventana.fill(col.VERDE)  # o cualquier color de fondo

    
    listaEventos = pygame.event.get()
    for event in listaEventos : #entrega todos los eventos.
        #Cerrar juego al apretar la X de la ventana
        if event.type == pygame.QUIT:
            run = False
        
    teclas = pygame.key.get_pressed()
    jugador.mover(teclas) #Mueve al jugador.
    jugador.update()
    jugador.dibujar(ventana)
    pygame.display.flip()

pygame.quit()