import pygame
import constantes as cs
import colores as col

class Personaje():
    
    def __init__(self, x ,y , animaciones): #x , y donde aparece el pj, animaciones es una lista de imagenes
        #Forma Pj
        self.flip = False
        #le cargo a self.animacion el parametro animaciones
        self.animacion = animaciones
        #imagen de la animacion que se esta mostrando!
        self.frame_index = 0
        #Almacena la hora actual(en milisegundos desde que se inicio pygame)
        self.update_time = pygame.time.get_ticks()
        self.imagen = animaciones[self.frame_index]
        self.forma = self.imagen.get_rect(topleft=(x, y))
        self.velocidad = 3

    def update(self):
        cooldown_animacion = 100
        self.imagen = self.animacion[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animacion):
            self.frame_index = 0
        
        
    #dibujamos Al pj
    def dibujar(self,interfaz):
        imagenFlip = pygame.transform.flip(self.imagen,self.flip,False)
        interfaz.blit(imagenFlip,self.forma)
        
    
    def mover(self, teclas):
        # Movimiento
        if teclas[pygame.K_w]:
            self.forma.y -= self.velocidad
        if teclas[pygame.K_s]:
            self.forma.y += self.velocidad
        if teclas[pygame.K_a]:
            self.forma.x -= self.velocidad
            self.flip = True #Si toca la a entonces se gira a la izquierda
        elif teclas[pygame.K_d]:
            self.forma.x += self.velocidad
            self.flip = False #Si toca d se gira para la derecha

        # Limitar al tamaño de la ventana
        if self.forma.left < 0:
            self.forma.left = 0
        if self.forma.right > cs.ANCHO_VENTANA:
            self.forma.right = cs.ANCHO_VENTANA
        if self.forma.top < 0:
            self.forma.top = 0
        if self.forma.bottom > cs.ALTO_VENTANA:
            self.forma.bottom = cs.ALTO_VENTANA
        
        #print(self.forma.x, self.forma.left, self.forma.right)

    
    
    
    # def mover(self,teclas):
    #     if self.forma.x <0:
    #         self.flip = True
    #     if self.forma.x > 0:
    #         self.flip = False
        
    #     if teclas[pygame.K_w]:
    #         self.forma.y -= self.velocidad
    #     if teclas[pygame.K_s]:
    #         self.forma.y += self.velocidad
    #     if teclas[pygame.K_a]:
    #         self.forma.x -= self.velocidad
    #     if teclas[pygame.K_d]:
    #         self.forma.x += self.velocidad

        
        
    #     #Limitar al tamanio de la ventana!
    #     if self.forma.left < 0:
    #         self.forma.left = 0
    #     if self.forma.right > cs.ANCHO_VENTANA:
    #         self.forma.right = cs.ANCHO_VENTANA
    #     if self.forma.top < 0:
    #         self.forma.top = 0
    #     if self.forma.bottom > cs.ALTO_VENTANA:
    #         self.forma.bottom = cs.ALTO_VENTANA