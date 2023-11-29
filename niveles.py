import pygame
from Constantes import *

#tamaño cuadricula
tamaño_cuadricula = 40


class Nivel():
    def __init__(self,data) -> None:
        self.lista_cuadriculas = []
        
        imagen_suelo = pygame.image.load('imagenes_obstaculos/pasto_arriba.png')
        imagen_tierra = pygame.image.load('imagenes_obstaculos/tierra.png')
        imagen_pasto_izquierda = pygame.image.load('imagenes_obstaculos/pasto_izquierda.png')
        imagen_pasto_derecha = pygame.image.load('imagenes_obstaculos/pasto_derecha.png')
        
        contador_filas = 0
        for fila in data:
            contador_columnas = 0
            for cuadricula in fila:
                if cuadricula == 1:
                    imagen = pygame.transform.scale(imagen_tierra, (tamaño_cuadricula,tamaño_cuadricula))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = contador_columnas * tamaño_cuadricula
                    imagen_rect.y = contador_filas * tamaño_cuadricula
                    cuadricula = (imagen, imagen_rect)
                    self.lista_cuadriculas.append(cuadricula)
                if cuadricula == 2:
                    imagen = pygame.transform.scale(imagen_suelo, (tamaño_cuadricula,tamaño_cuadricula))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = contador_columnas * tamaño_cuadricula
                    imagen_rect.y = contador_filas * tamaño_cuadricula
                    cuadricula = (imagen, imagen_rect)
                    self.lista_cuadriculas.append(cuadricula)
                if cuadricula == 3:
                    imagen = pygame.transform.scale(imagen_pasto_izquierda, (tamaño_cuadricula,tamaño_cuadricula))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = contador_columnas * tamaño_cuadricula
                    imagen_rect.y = contador_filas * tamaño_cuadricula
                    cuadricula = (imagen, imagen_rect)
                    self.lista_cuadriculas.append(cuadricula)
                if cuadricula == 4:
                    imagen = pygame.transform.scale(imagen_pasto_derecha, (tamaño_cuadricula,tamaño_cuadricula))
                    imagen_rect = imagen.get_rect()
                    imagen_rect.x = contador_columnas * tamaño_cuadricula
                    imagen_rect.y = contador_filas * tamaño_cuadricula
                    cuadricula = (imagen, imagen_rect)
                    self.lista_cuadriculas.append(cuadricula)
                contador_columnas += 1
            contador_filas += 1
    
    def dibujar(self,ventana):
        for cuadricula in self.lista_cuadriculas:
            ventana.blit(cuadricula[0], cuadricula[1])
            #pygame.draw.rect(ventana,COLOR_BLANCO, cuadricula[1], 2)
    
    