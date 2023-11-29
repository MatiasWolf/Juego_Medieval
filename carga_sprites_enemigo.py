import pygame
from funciones import cambiar_escala_imagenes

rata_correr_derecha = []
rata_correr_izquierda = []
rata_atacar_derecha = []
rata_atacar_izquierda = []
rata_muerto_derecha = []
rata_muerto_izquierda = []

for i in range(1,9):
    rata_imagen_correr_d = pygame.image.load(f"sprites_enemigo/rata/correr_d/sprites_correr_d_{str(i)}.png")
    rata_imagen_correr_i = pygame.image.load(f"sprites_enemigo/rata/correr_i/sprites_correr_i_{str(i)}.png")
    rata_imagen_atacar_d = pygame.image.load(f"sprites_enemigo/rata/atacar_d/sprites_atacar_d_{str(i)}.png")
    rata_imagen_atacar_i = pygame.image.load(f"sprites_enemigo/rata/atacar_i/sprites_atacar_i_{str(i)}.png")
    
    rata_imagen_correr_d = cambiar_escala_imagenes(rata_imagen_correr_d,2.5,2.5)
    rata_imagen_correr_i = cambiar_escala_imagenes(rata_imagen_correr_i,2.5,2.5)
    rata_imagen_atacar_d = cambiar_escala_imagenes(rata_imagen_atacar_d,2.5,2.5)
    rata_imagen_atacar_i = cambiar_escala_imagenes(rata_imagen_atacar_i,2.5,2.5)
    
    rata_correr_derecha.append(rata_imagen_correr_d)
    rata_correr_izquierda.append(rata_imagen_correr_i)
    rata_atacar_derecha.append(rata_imagen_atacar_d)
    rata_atacar_izquierda.append(rata_imagen_atacar_i)

for i in range(1,5):
    rata_imagen_muerto_d = pygame.image.load(f"sprites_enemigo/rata/muerto_d/sprites_muerto_d_{str(i)}.png")
    rata_imagen_muerto_i = pygame.image.load(f"sprites_enemigo/rata/muerto_i/sprites_muerto_i_{str(i)}.png")
    
    rata_imagen_muerto_d = cambiar_escala_imagenes(rata_imagen_muerto_d,2.5,2.5)
    rata_imagen_muerto_i = cambiar_escala_imagenes(rata_imagen_muerto_i,2.5,2.5)
    
    rata_muerto_derecha.append(rata_imagen_muerto_d)
    rata_muerto_izquierda.append(rata_imagen_muerto_i)

#-----------------------------------------------------------------------------------------------------------------------------

esqueleto_correr_derecha = []
esqueleto_correr_izquierda = []
esqueleto_ataque_derecha = []
esqueleto_ataque_izquierda = []
esqueleto_muerte_derecha = []
esqueleto_muerte_izquierda = []

for i in range(1,10):
    esqueleto_imagen_correr_d = pygame.image.load(f"sprites_enemigo/esqueleto/sprites_correr_d/correr_d_{str(i)}.png")
    esqueleto_imagen_correr_i = pygame.image.load(f"sprites_enemigo/esqueleto/sprites_correr_i/correr_i_{str(i)}.png")
    esqueleto_imagen_muerte_d = pygame.image.load(f"sprites_enemigo/esqueleto/sprites_muerte_d/muerte_d_{str(i)}.png")
    esqueleto_imagen_muerte_i = pygame.image.load(f"sprites_enemigo/esqueleto/sprites_muerte_i/muerte_i_{str(i)}.png")
    
    esqueleto_imagen_correr_d = cambiar_escala_imagenes(esqueleto_imagen_correr_d,2,2)
    esqueleto_imagen_correr_i = cambiar_escala_imagenes(esqueleto_imagen_correr_i,2,2)
    esqueleto_imagen_muerte_d = cambiar_escala_imagenes(esqueleto_imagen_muerte_d,2,2)
    esqueleto_imagen_muerte_i = cambiar_escala_imagenes(esqueleto_imagen_muerte_i,2,2)
    
    esqueleto_correr_derecha.append(esqueleto_imagen_correr_d)
    esqueleto_correr_izquierda.append(esqueleto_imagen_correr_i)
    esqueleto_muerte_derecha.append(esqueleto_imagen_muerte_d)
    esqueleto_muerte_izquierda.append(esqueleto_imagen_muerte_i)

for i in range(1,7):
    esqueleto_imagen_ataque_d = pygame.image.load(f"sprites_enemigo/esqueleto/sprites_atacar_d/ataque_d_{str(i)}.png")
    esqueleto_imagen_ataque_i = pygame.image.load(f"sprites_enemigo/esqueleto/sprites_atacar_i/ataque_i_{str(i)}.png")
    
    esqueleto_imagen_ataque_d = cambiar_escala_imagenes(esqueleto_imagen_ataque_d,2,2)
    esqueleto_imagen_ataque_i = cambiar_escala_imagenes(esqueleto_imagen_ataque_i,2,2)
    
    esqueleto_ataque_derecha.append(esqueleto_imagen_ataque_d)
    esqueleto_ataque_izquierda.append(esqueleto_imagen_ataque_i)

#-----------------------------------------------------------------------------------------------------------------------

monstruo_correr_derecha = []
monstruo_correr_izquierda = []
monstruo_ataque_derecha = []
monstruo_ataque_izquierda = []
monstruo_muerte_derecha = []
monstruo_muerte_izquierda = []

for i in range(1,9):
    monstruo_imagen_correr_d = pygame.image.load(f"sprites_enemigo/monstruo/correr_d/correr_d_{str(i)}.png")
    monstruo_imagen_correr_i = pygame.image.load(f"sprites_enemigo/monstruo/correr_i/correr_i_{str(i)}.png")
    monstruo_imagen_ataque_d = pygame.image.load(f"sprites_enemigo/monstruo/ataque_d/ataque_d_{str(i)}.png")
    monstruo_imagen_ataque_i = pygame.image.load(f"sprites_enemigo/monstruo/ataque_i/ataque_i_{str(i)}.png")
    
    monstruo_imagen_correr_d = cambiar_escala_imagenes(monstruo_imagen_correr_d,1.6,1.6)
    monstruo_imagen_correr_i = cambiar_escala_imagenes(monstruo_imagen_correr_i,1.6,1.6)
    monstruo_imagen_ataque_d = cambiar_escala_imagenes(monstruo_imagen_ataque_d,1.6,1.6)
    monstruo_imagen_ataque_i = cambiar_escala_imagenes(monstruo_imagen_ataque_i,1.6,1.6)
    
    monstruo_correr_derecha.append(monstruo_imagen_correr_d)
    monstruo_correr_izquierda.append(monstruo_imagen_correr_i)
    monstruo_ataque_derecha.append(monstruo_imagen_ataque_d)
    monstruo_ataque_izquierda.append(monstruo_imagen_ataque_i)

for i in range(1,11):
    monstruo_imagen_muerte_d = pygame.image.load(f"sprites_enemigo/monstruo/muerte_d/muerte_d_{str(i)}.png")
    monstruo_imagen_muerte_i = pygame.image.load(f"sprites_enemigo/monstruo/muerte_i/muerte_i_{str(i)}.png")
    
    monstruo_imagen_muerte_d = cambiar_escala_imagenes(monstruo_imagen_muerte_d,1.6,1.6)
    monstruo_imagen_muerte_i = cambiar_escala_imagenes(monstruo_imagen_muerte_i,2,2)
    
    monstruo_muerte_derecha.append(monstruo_imagen_muerte_d)
    monstruo_muerte_izquierda.append(monstruo_imagen_muerte_i)