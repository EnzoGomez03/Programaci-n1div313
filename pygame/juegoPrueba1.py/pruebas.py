import pygame

pygame.init() #Inicializar el juego
pantalla = pygame.display.set_mode((1280, 720)) #Tamanio de la pantalla
reloj = pygame.time.Clock()  # se inicializa la variable para controlar los FPS
corriendo = True

#                                  tipo  , tamanio
fuente_arial = pygame.font.SysFont("Arial", 20)

while corriendo:
    for event in pygame.event.get():  # El pygame.event.get captura los eventos que pasan en el juego.
        if event.type == pygame.QUIT:  # Para cerrar la ventana cuando se toca la X
            corriendo = False 
        if event.type == pygame.KEYDOWN:   # Aca pregunta si evento que esta ocurriendo es algun tipeo de algo!
            if event.key == pygame.K_w:    # Y aca pregunta si el evento que ocurrio al ser un tipeo, fue de la tecla w!
                print("Te moves para adelante!") # si fue la tecla w, imprime "Te moves para adelante!"
            elif event.key == pygame.K_s:
                print("Te moves para atras")
        
        
    pantalla.fill("purple")  
    
    #                                 (x,y,ancho,alto)
    #                                           get(es para obtener informacion) y el set(para setear algo)
    pygame.draw.rect(pantalla, "red", (pantalla.get_width()/2,pantalla.get_height()/2,100,100))#pygame.dibujo.rectangulo
    
    #                                     x  y  , tamanio
    pygame.draw.circle(pantalla, "green" , (100,100),100)
    
    
    texto = fuente_arial.render("Aca lo que pongas va a aparecer", True, "black")  # SE USA RENDER PARA MOSTRARLA
    pantalla.blit(texto, (0,500)) #BLIT es para imprimir texto e imagenes
    
    pygame.display.flip()
    reloj.tick(60)
    
pygame.quit()