import pygame

class Item:
    def __init__(self,x,y) -> None:
        
        imagen = pygame.image.load('imagenes_obstaculos/corazon_item.png')
        self.alto = imagen.get_height()
        self.ancho = imagen.get_width()
        self.x = x
        self.y = y
        self.imagen = pygame.transform.scale(imagen,(self.ancho * 0.2,self.alto * 0.2))
        self.rect = self.imagen.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.item_agarrado = False
    
    def animar(self,ventana):
        ventana.blit(self.imagen,(self.x,self.y))
    
    def actualizar(self,ventana,personaje):
        if not self.item_agarrado:
            self.animar(ventana)
            self.dar_vida(personaje)
    
    def dar_vida(self,personaje):
        if self.rect.colliderect(personaje.rect):
            if personaje.vida < 100:
                personaje.vida = 100
                self.item_agarrado = True
    