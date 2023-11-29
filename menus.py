import pygame
import sys
from Constantes import ANCHO_VENTANA,ALTO_VENTANA,COLOR_NEGRO
from funciones import cambiar_escala_imagenes
import boton

def alternar_volumen(cancion):
    volumen_actual = cancion.get_volume()
    if volumen_actual > 0:
        cancion.set_volume(0)
    else:
        cancion.set_volume(0.2)

#def dibujar_texto(texto,fuente,texto_color,x,y,ventana):
#    imagen = fuente.render(texto,True,texto_color)
#    ventana.blit(imagen,(x,y))

def pausa(ventana,cancion):

    juego_pausado = True
    estado_menu = 'pausa'

    menu_pausa_grande = pygame.image.load('imagenes_interfaz/pantallita_menu.png').convert_alpha()
    menu_pausa_grande = cambiar_escala_imagenes(menu_pausa_grande,4,4)
    menu_pausa = pygame.image.load('imagenes_interfaz/marco_menu.png').convert_alpha()
    menu_pausa = cambiar_escala_imagenes(menu_pausa,6,6)
    imagen_start = pygame.image.load('imagenes_interfaz/boton_start.png').convert_alpha()
    imagen_options = pygame.image.load('imagenes_interfaz/boton_options.png').convert_alpha()
    imagen_exit = pygame.image.load('imagenes_interfaz/boton_exit.png').convert_alpha()
    imagen_musica = pygame.image.load('imagenes_interfaz/boton_musica.png').convert_alpha()
    imagen_back = pygame.image.load('imagenes_interfaz/boton_back.png').convert_alpha()

    boton_start = boton.Boton(530,200,imagen_start,4)
    boton_options = boton.Boton(530,270,imagen_options,4)
    boton_exit = boton.Boton(530,340,imagen_exit,4)
    boton_musica = boton.Boton(520,281,imagen_musica,5)
    boton_back = boton.Boton(620,281,imagen_back,5)
    
    running = True
    while running:
        cancion.play()
        
        if juego_pausado:
            if estado_menu == 'pausa':
                ventana.fill(COLOR_NEGRO)
                ventana.blit(menu_pausa_grande,(503,140))
                if boton_start.dibujar(ventana):
                    estado = 'juego'
                    running = False
                if boton_options.dibujar(ventana):
                    estado_menu = 'options'
                if boton_exit.dibujar(ventana):
                    estado = 'niveles'
                    running = False
            elif estado_menu == 'options':
                ventana.fill(COLOR_NEGRO)
                ventana.blit(menu_pausa,(480,180))
                if boton_musica.dibujar(ventana):
                    alternar_volumen(cancion)
                if boton_back.dibujar(ventana):
                    estado_menu = 'pausa'
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    estado = 'juego'
                    running = False
        
        
        pygame.display.flip()
    
    return estado
