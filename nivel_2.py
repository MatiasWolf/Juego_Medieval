import pygame
from Constantes import *
from menus import *
#pygame.init()

#ventana
#ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
#pygame.display.set_caption('UTN')


def Nivel_dos(ventana,cancion):
    from niveles import Nivel
    from config import data_nivel_2
    from funciones import cambiar_escala_imagenes
    from personaje import Personaje
    from enemigos import Esqueleto
    from item import Item
    import puntaje
    
    #reloj
    reloj = pygame.time.Clock()
    fps = 60
    tiempo_inicial = pygame.time.get_ticks()
    
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    cancion.set_volume(0.2)
    
    #fondo e interfaz
    fondo = pygame.image.load('fondo_nivel_2.png')
    alto_fondo = fondo.get_height()
    ancho_fondo = fondo.get_width()
    fondo = pygame.transform.scale(fondo,(ancho_fondo * 2,alto_fondo * 1.2))
    barra_vida_completa = pygame.image.load('imagenes_interfaz/barra_vida_completa.png')
    barra_vida_completa = cambiar_escala_imagenes(barra_vida_completa, 3, 3)
    barra_vida_75 = pygame.image.load('imagenes_interfaz/barra_vida_75.png')
    barra_vida_75 = cambiar_escala_imagenes(barra_vida_75, 3, 3)
    barra_vida_50 = pygame.image.load('imagenes_interfaz/barra_vida_50.png')
    barra_vida_50 = cambiar_escala_imagenes(barra_vida_50, 3, 3)
    barra_vida_25 = pygame.image.load('imagenes_interfaz/barra_vida_25.png')
    barra_vida_25 = cambiar_escala_imagenes(barra_vida_25, 3, 3)
    barra_sin_vida = pygame.image.load('imagenes_interfaz/barra_sin_vida.png')
    barra_sin_vida = cambiar_escala_imagenes(barra_sin_vida, 3, 3)
    
    juego_pausado = False
    
    #variable de puntuacion
    nivel_puntaje = puntaje.cargar_puntaje()
    
    #fuente
    ruta_fuente = 'upheavtt.ttf'
    tamaño_fuente_1 = 36
    tamaño_fuente_2 = 100
    fuente_chica = pygame.font.Font(ruta_fuente,tamaño_fuente_1)
    fuente_grande = pygame.font.Font(ruta_fuente,tamaño_fuente_2)
    puntuacion = 'SCORE:'
    texto_puntuacion = fuente_chica.render(str(puntuacion),True,COLOR_NEGRO)
    texto_cantidad_puntuacion = fuente_chica.render(str(nivel_puntaje),True,COLOR_NEGRO)
    game_over = 'GAME OVER'
    texto_game_over = fuente_grande.render(str(game_over),True,COLOR_NEGRO)
    
    nivel_2 = Nivel(data_nivel_2)
    
    personaje = Personaje(50,300)
    esqueleto_1 = Esqueleto(160,460,2,250)
    esqueleto_2 = Esqueleto(500,500,2,250)
    esqueleto_3 = Esqueleto(880,380,2,250)
    esqueleto_4 = Esqueleto(880,100,2,250)
    esqueleto_5 = Esqueleto(1080,100,2,250)
    esqueleto_6 = Esqueleto(50,140,2,250)
    esqueleto_7 = Esqueleto(280,140,2,250)
    
    lista_enemigos = [esqueleto_1,esqueleto_2,esqueleto_3,esqueleto_4,esqueleto_5,esqueleto_6,esqueleto_7]
    
    obstaculo_1 = pygame.Rect(140,480,20,40)
    obstaculo_2 = pygame.Rect(440,480,20,40)
    obstaculo_3 = pygame.Rect(420,520,20,40)
    obstaculo_4 = pygame.Rect(720,520,20,40)
    obstaculo_5 = pygame.Rect(780,400,20,40)
    obstaculo_6 = pygame.Rect(1080,400,20,40)
    obstaculo_7 = pygame.Rect(780,120,20,40)
    obstaculo_8 = pygame.Rect(1160,120,20,40)
    obstaculo_9 = pygame.Rect(360,160,20,40)
    obstaculo_10 = pygame.Rect(20,160,20,40)
    
    item_1 = Item(520,290)
    item_2 = Item(925,210)
    item_3 = Item(50,50)
    
    mostrar_rectangulos = False
    
    siguiente_nivel_desbloqueado = False
    
    run = True
    while run:
        cancion.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    mostrar_rectangulos = not mostrar_rectangulos
                elif event.key == pygame.K_ESCAPE:
                    juego_pausado = True 
        
        texto_cantidad_puntuacion = fuente_chica.render(str(nivel_puntaje),True,COLOR_NEGRO)
        
        #logica y sprites
        reloj.tick(fps)
        ventana.blit(fondo,(0,0))
        nivel_2.dibujar(ventana)
        personaje.actualizar(ventana)
        
        if len(lista_enemigos) > 0:
            imagen_puerta = pygame.image.load('imagenes_obstaculos/puerta_cerrada.png')
            alto_puerta = imagen_puerta.get_height()
            ancho_puerta = imagen_puerta.get_width()
            imagen_puerta = pygame.transform.scale(imagen_puerta,(ancho_puerta * 0.2, alto_puerta * 0.2))
            ventana.blit(imagen_puerta,(1095,290))
        else:
            imagen_puerta = pygame.image.load('imagenes_obstaculos/puerta_abierta.png')
            alto_puerta = imagen_puerta.get_height()
            ancho_puerta = imagen_puerta.get_width()
            imagen_puerta = pygame.transform.scale(imagen_puerta,(ancho_puerta * 0.2, alto_puerta * 0.2))
            puerta_rect = pygame.Rect(1095,290,ancho_puerta,alto_puerta)
            ventana.blit(imagen_puerta,(1095,290))
            if puerta_rect.colliderect(personaje.rect):
                puntaje.guardar_puntaje(nivel_puntaje)
                siguiente_nivel_desbloqueado = True
                run = False
        
        item_1.actualizar(ventana,personaje)
        item_2.actualizar(ventana,personaje)
        item_3.actualizar(ventana,personaje)
        
        esqueleto_1.actualizar()
        esqueleto_2.actualizar()
        esqueleto_3.actualizar()
        esqueleto_4.actualizar()
        esqueleto_5.actualizar()
        esqueleto_6.actualizar()
        esqueleto_7.actualizar()
        
        esqueleto_1.animar_sprites(ventana,personaje)
        esqueleto_2.animar_sprites(ventana,personaje)
        esqueleto_3.animar_sprites(ventana,personaje)
        esqueleto_4.animar_sprites(ventana,personaje)
        esqueleto_5.animar_sprites(ventana,personaje)
        esqueleto_6.animar_sprites(ventana,personaje)
        esqueleto_7.animar_sprites(ventana,personaje)
        
        for enemigo in lista_enemigos:
            if enemigo.muerto:
                lista_enemigos.remove(enemigo)
                if personaje.vida >= 75:
                    nivel_puntaje += 50
                else:
                    nivel_puntaje += 25
        
        if mostrar_rectangulos:
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect,2)
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect_arriba,2)
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect_derecha,2)
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect_izquierda,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_1.rect,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_1.rect_left,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_1.rect_right,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_2.rect,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_2.rect_left,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_2.rect_right,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_3.rect,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_3.rect_left,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_3.rect_right,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_4.rect,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_4.rect_left,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_4.rect_right,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_5.rect,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_5.rect_left,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_5.rect_right,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_6.rect,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_6.rect_left,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_6.rect_right,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_7.rect,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_7.rect_left,2)
            pygame.draw.rect(ventana,COLOR_ROJO,esqueleto_7.rect_right,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_1,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_2,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_3,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_4,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_5,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_6,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_7,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_8,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_9,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_10,2)
            
        
        for cuadricula in nivel_2.lista_cuadriculas:
            if personaje.rect.colliderect(cuadricula[1]):
                personaje.rect.bottom = cuadricula[1].top - 7
                personaje.rect_derecha.bottom = cuadricula[1].top - 15
                personaje.rect_izquierda.bottom = cuadricula[1].top - 15
                personaje.rect_arriba.bottom = personaje.rect.top
                personaje.salto_terminado = False
                personaje.saltando = False
            if personaje.rect_derecha.colliderect(cuadricula[1]):
                personaje.rect_izquierda.right = personaje.rect.left
                personaje.rect.right = personaje.rect_derecha.left
                personaje.rect_derecha.right = cuadricula[1].left
                personaje.rect_arriba.right = personaje.rect.right - 4
            if personaje.rect_izquierda.colliderect(cuadricula[1]):
                personaje.rect_derecha.left = personaje.rect.right
                personaje.rect.left = personaje.rect_izquierda.right
                personaje.rect_izquierda.left = cuadricula[1].right
                personaje.rect_arriba.left = personaje.rect.left + 4
            if personaje.rect_arriba.colliderect(cuadricula[1]):
                personaje.velocidad_y = 1
        
        esqueleto_1.manejar_colision_obstaculo(obstaculo_1)
        esqueleto_1.manejar_colision_obstaculo(obstaculo_2)
        esqueleto_2.manejar_colision_obstaculo(obstaculo_3)
        esqueleto_2.manejar_colision_obstaculo(obstaculo_4)
        esqueleto_3.manejar_colision_obstaculo(obstaculo_5)
        esqueleto_3.manejar_colision_obstaculo(obstaculo_6)
        esqueleto_4.manejar_colision_obstaculo(obstaculo_7)
        esqueleto_4.manejar_colision_obstaculo(obstaculo_8)
        esqueleto_5.manejar_colision_obstaculo(obstaculo_7)
        esqueleto_5.manejar_colision_obstaculo(obstaculo_8)
        esqueleto_6.manejar_colision_obstaculo(obstaculo_9)
        esqueleto_6.manejar_colision_obstaculo(obstaculo_10)
        esqueleto_7.manejar_colision_obstaculo(obstaculo_9)
        esqueleto_7.manejar_colision_obstaculo(obstaculo_10)
        esqueleto_1.manejar_colision_espada(personaje.espada_rect)
        esqueleto_2.manejar_colision_espada(personaje.espada_rect)
        esqueleto_3.manejar_colision_espada(personaje.espada_rect)
        esqueleto_4.manejar_colision_espada(personaje.espada_rect)
        esqueleto_5.manejar_colision_espada(personaje.espada_rect)
        esqueleto_6.manejar_colision_espada(personaje.espada_rect)
        esqueleto_7.manejar_colision_espada(personaje.espada_rect)
        
        #texto y barra de vida
        if personaje.vida == 100:
            ventana.blit(barra_vida_completa,(10,10))
        elif personaje.vida == 75:
            ventana.blit(barra_vida_75,(10,10))
        elif personaje.vida == 50:
            ventana.blit(barra_vida_50,(10,10))
        elif personaje.vida == 25:
            ventana.blit(barra_vida_25,(10,10))
        elif personaje.vida == 0:
            ventana.blit(barra_sin_vida,(10,10))
        ventana.blit(texto_puntuacion,(1000,570))
        ventana.blit(texto_cantidad_puntuacion,(1130,570))
        
        if juego_pausado:
            estado = pausa(ventana,cancion)
            if estado == 'juego':
                juego_pausado = False
            elif estado == 'niveles':
                run = False
        else:
            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = (tiempo_actual - tiempo_inicial) / 1000
            texto_tiempo = fuente_chica.render(f"Tiempo: {tiempo_transcurrido}",True,COLOR_NEGRO)
            ventana.blit(texto_tiempo,(500,10))
        
        if personaje.muerto:
            imagen_exit = pygame.image.load('imagenes_interfaz/boton_exit.png')
            boton_back = boton.Boton(500,450,imagen_exit,6)
            ventana.blit(texto_game_over,(350,250))
            if boton_back.dibujar(ventana):
                run = False
        pygame.display.flip()

    return siguiente_nivel_desbloqueado