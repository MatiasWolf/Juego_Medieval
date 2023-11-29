import pygame
from funciones import *


correr_derecha = []
correr_izquierda = []
quieto_derecha = []
quieto_izquierda = []
ataque_derecha = []
ataque_izquierda = []
salto_derecha = []
salto_izquierda = []
caida_derecha = []
caida_izquierda = []
muerte_derecha = []
muerte_izquierda = []

for i in range(1,11):
    imagen_correr_d = pygame.image.load(f"sprites_personaje/sprites_correr_d/correr_d_{str(i)}.png")
    imagen_correr_i = pygame.image.load(f"sprites_personaje/sprites_correr_i/correr_i_{str(i)}.png")
    imagen_quieto_d = pygame.image.load(f"sprites_personaje/sprites_quieto_d/quieto_d_{str(i)}.png")
    imagen_quieto_i = pygame.image.load(f"sprites_personaje/sprites_quieto_i/quieto_i_{str(i)}.png")
    imagen_muerto_d = pygame.image.load(f"sprites_personaje/sprites_muerte_d/muerte_d_{str(i)}.png")
    imagen_muerto_i = pygame.image.load(f"sprites_personaje/sprites_muerte_i/muerte_i_{str(i)}.png")
    
    imagen_correr_d = cambiar_escala_imagenes(imagen_correr_d, 1.5, 1.5)
    imagen_correr_i = cambiar_escala_imagenes(imagen_correr_i, 1.5, 1.5)
    imagen_quieto_d = cambiar_escala_imagenes(imagen_quieto_d, 1.5, 1.5)
    imagen_quieto_i = cambiar_escala_imagenes(imagen_quieto_i, 1.5, 1.5)
    imagen_muerto_d = cambiar_escala_imagenes(imagen_muerto_d, 1.5, 1.5)
    imagen_muerto_i = cambiar_escala_imagenes(imagen_muerto_i, 1.5, 1.5)
    
    correr_derecha.append(imagen_correr_d)
    correr_izquierda.append(imagen_correr_i)
    quieto_derecha.append(imagen_quieto_d)
    quieto_izquierda.append(imagen_quieto_i)
    muerte_derecha.append(imagen_muerto_d)
    muerte_izquierda.append(imagen_muerto_i)

for i in range(1,6):
    imagen_ataque_d = pygame.image.load(f"sprites_personaje/sprites_atacar_d/ataque_d_{str(i)}.png")
    imagen_ataque_i = pygame.image.load(f"sprites_personaje/sprites_atacar_i/ataque_i_{str(i)}.png")
    
    imagen_ataque_d = cambiar_escala_imagenes(imagen_ataque_d, 1.45, 1.45)
    imagen_ataque_i = cambiar_escala_imagenes(imagen_ataque_i, 1.5, 1.5)
    
    ataque_derecha.append(imagen_ataque_d)
    ataque_izquierda.append(imagen_ataque_i)

for i in range(1,4):
    imagen_salto_d = pygame.image.load(f"sprites_personaje/sprites_salto_d/salto_d_{str(i)}.png")
    imagen_salto_i = pygame.image.load(f"sprites_personaje/sprites_salto_i/salto_i_{str(i)}.png")
    imagen_caida_d = pygame.image.load(f"sprites_personaje/sprites_caida_d/caida_d_{str(i)}.png")
    imagen_caida_i = pygame.image.load(f"sprites_personaje/sprites_caida_i/caida_i_{str(i)}.png")
    
    imagen_salto_d = cambiar_escala_imagenes(imagen_salto_d, 1.5, 1.5)
    imagen_salto_i = cambiar_escala_imagenes(imagen_salto_i, 1.5, 1.5)
    imagen_caida_d = cambiar_escala_imagenes(imagen_caida_d, 1.5, 1.5)
    imagen_caida_i = cambiar_escala_imagenes(imagen_caida_i, 1.5, 1.5)
    
    salto_derecha.append(imagen_salto_d)
    salto_izquierda.append(imagen_salto_i)
    caida_derecha.append(imagen_caida_d)
    caida_izquierda.append(imagen_caida_i)



