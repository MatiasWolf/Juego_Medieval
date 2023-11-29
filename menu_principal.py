import pygame
import sys
from Constantes import *
import boton
from nivel_1 import *
from nivel_2 import *
from nivel_3 import *
from Ingreso_nombre import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

cancion = pygame.mixer.Sound('cancion_juego.mp3')
cancion.set_volume(0.2)

ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption('UTN')

fondo = pygame.image.load('fondo_menu_principal.png')
ruta_fuente = '8-bit Arcade In.ttf'
tamaño_fuente = 120
fuente =  pygame.font.Font(ruta_fuente,tamaño_fuente)
titulo = 'Knight Adventure'
texto_titulo = fuente.render(str(titulo),True,COLOR_NEGRO)
niveles = 'Niveles'
texto_niveles = fuente.render(str(niveles),True,COLOR_NEGRO)
estado_menu = 'main'

imagen_play = pygame.image.load('imagenes_interfaz/boton_start.png')
imagen_ranking = pygame.image.load('imagenes_interfaz/boton_ranking.png')
imagen_exit = pygame.image.load('imagenes_interfaz/boton_exit.png')
imagen_nivel_1 = pygame.image.load('imagenes_interfaz/boton_nivel_1.png')
imagen_nivel_2 = pygame.image.load('imagenes_interfaz/boton_nivel_2.png')
imagen_nivel_3 = pygame.image.load('imagenes_interfaz/boton_nivel_3.png')
imagen_back = pygame.image.load('imagenes_interfaz/boton_back.png')

boton_play = boton.Boton(290,400,imagen_play,4)
boton_ranking = boton.Boton(500,400,imagen_ranking,4)
boton_exit_1 = boton.Boton(790,400,imagen_exit,4)
boton_nivel_1 = boton.Boton(100,250,imagen_nivel_1,6)
boton_nivel_2 = boton.Boton(450,250,imagen_nivel_2,6)
boton_nivel_3 = boton.Boton(800,250,imagen_nivel_3,6)
boton_exit_2 = boton.Boton(500,450,imagen_exit,6)

crear_SQLite()

nivel_2_desbloqueado = False
nivel_3_desbloqueado = False

temporizador_global = 0
menu = True
while menu:
    cancion.play()
    ventana.blit(fondo,(0,0))
    
    if estado_menu == 'main':
        ventana.blit(texto_titulo,(160,100))
        if boton_play.dibujar(ventana):
            estado_menu = 'niveles'
        if boton_ranking.dibujar(ventana):
            estado_menu = 'ranking'
        if boton_exit_1.dibujar(ventana):
            menu = False
    elif estado_menu == 'niveles':
        ventana.blit(texto_niveles,(400,50))
        if boton_nivel_1.dibujar(ventana):
            nivel_2_desbloqueado = Nivel_uno(ventana,cancion)
            estado_menu = 'niveles'
        if boton_nivel_2.dibujar(ventana) and nivel_2_desbloqueado:
            nivel_3_desbloqueado = Nivel_dos(ventana,cancion)
            estado_menu = 'niveles'
        if boton_nivel_3.dibujar(ventana) and nivel_3_desbloqueado:
            Nivel_tres(ventana,cancion)
        if boton_exit_2.dibujar(ventana):
            estado_menu = 'main'
    elif estado_menu == 'ranking':
        estado_menu = mostrar_ranking()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            sys.exit()
    
    pygame.display.flip()
pygame.quit()