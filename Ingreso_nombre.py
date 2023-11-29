import pygame
import sys
import sqlite3
from Constantes import *
#ventana = pygame.display.set_mode((600,600))



def ingresar_nombre(ventana):
    fuente = pygame.font.Font('8-bit Arcade In.ttf',60)
    nombre = ""
    ingresar = True
    
    while ingresar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ingresar = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ingresar = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode
        ventana.fill(COLOR_BLANCO)
        texto_ingreso = fuente.render("Ingresa tu nombre: " + nombre,True,COLOR_NEGRO)
        rect = texto_ingreso.get_rect(center=(ANCHO_VENTANA // 2,ALTO_VENTANA // 2))
        ventana.blit(texto_ingreso,rect)
        
        pygame.display.flip()
    
    return nombre

