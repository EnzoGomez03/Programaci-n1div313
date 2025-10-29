from ursina import *

#Arbol herado todo de Entity
class Arbol(Entity):
    
    def __init__(self, modelo, position=(0,0,0), scale=1, collider='mesh'):
        #super basicamente es el Entity
        super().__init__(
            model=modelo,
            position=position,
            scale=scale,
            collider=collider,
        )
        
