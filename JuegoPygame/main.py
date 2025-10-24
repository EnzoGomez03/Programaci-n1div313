import pygame
import constantes
import colores as col
from personaje import Personaje
#Iniciamos pygame
pygame.init()

#Config de la ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

#Nombre de la pagina
pygame.display.set_caption("Proyecto")

#Aca va el pj principal
player_image = pygame.image.load("JuegoPygame//assets//imagenes//characters//player//mov11.png") 
player_image = pygame.transform.scale(player_image, (player_image.get_width() * constantes.SCALA_PERSONAJE,player_image.get_height()* constantes.SCALA_PERSONAJE))

#                   x , y
jugador = Personaje(30,30, player_image)

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
    jugador.dibujar(ventana)
    pygame.display.flip()

pygame.quit()