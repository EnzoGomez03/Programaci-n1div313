import pygame
import constantes as cs
import colores as col

class Personaje():
    
    def __init__(self, x ,y , image): #x , y donde aparece el pj
        #Forma Pj
        self.flip = False
        self.imagen = image.convert_alpha()
        self.forma = self.imagen.get_rect(center = (x,y))
        self.velocidad = 3
        
        
    #dibujamos Al pj
    def dibujar(self,interfaz):
        imagenFlip = pygame.transform.flip(self.imagen,self.flip,False)
        interfaz.blit(imagenFlip,self.forma)
        
    

    def mover(self,teclas):
        if self.forma.x <0:
            self.flip = True
        if self.forma.x > 0:
            self.flip = False
        
        if teclas[pygame.K_w]:
            self.forma.y -= self.velocidad
        if teclas[pygame.K_s]:
            self.forma.y += self.velocidad
        if teclas[pygame.K_a]:
            self.forma.x -= self.velocidad
        if teclas[pygame.K_d]:
            self.forma.x += self.velocidad

        
        
        #Limitar al tamanio de la ventana!
        if self.forma.left < 0:
            self.forma.left = 0
        if self.forma.right > cs.ANCHO_VENTANA:
            self.forma.right = cs.ANCHO_VENTANA
        if self.forma.top < 0:
            self.forma.top = 0
        if self.forma.bottom > cs.ALTO_VENTANA:
            self.forma.bottom = cs.ALTO_VENTANA