import pygame

def cambiar_escala_imagenes(imagen, multiplicador_x, multiplicador_y):
    
    ancho_imagen = imagen.get_width()
    alto_imagen = imagen.get_height()
    
    imagen = pygame.transform.scale(imagen,(ancho_imagen * multiplicador_x, alto_imagen * multiplicador_y))
    
    return imagen


