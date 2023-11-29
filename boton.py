import pygame

class Boton():
    def __init__(self,x,y,imagen,escala) -> None:
        ancho = imagen.get_width()
        alto = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen,(int(ancho * escala),int(alto * escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x,y)
        self.presionado = False
    
    def dibujar(self,fondo):
        accion = False
        
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.presionado == False:
                self.presionado = True
                accion = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.presionado = False
        
        fondo.blit(self.imagen,(self.rect.x,self.rect.y))
        
        return accion