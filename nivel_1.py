import pygame
from Constantes import *
from menus import *

#pygame.init()


#ventana
#ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
#pygame.display.set_caption('UTN')



def Nivel_uno(ventana,cancion):
    from niveles import Nivel
    from config import data_nivel_1
    from funciones import cambiar_escala_imagenes
    from personaje import Personaje
    from enemigos import Rata
    from item import Item
    import puntaje
    
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    cancion.set_volume(0.2)
    
    #fondo e interfaz
    fondo = pygame.image.load('fondo_nivel_1.png')
    alto_fondo = fondo.get_height()
    ancho_fondo = fondo.get_width()
    fondo = pygame.transform.scale(fondo,(ancho_fondo * 0.55,alto_fondo * 0.55))
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
    
    #reloj
    reloj = pygame.time.Clock()
    fps = 60

    tiempo_inicial = pygame.time.get_ticks()
    

    #variable de puntuacion
    nivel_puntaje = 0

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
    
    siguiente_nivel_desbloqueado = False
    
    nivel_1 = Nivel(data_nivel_1)
    personaje = Personaje(100, ALTO_VENTANA - 120)
    
    rata_1 = Rata(446,ALTO_VENTANA-80,2,150)
    rata_2 = Rata(760,ALTO_VENTANA-160,2,150)
    rata_3 = Rata(480,ALTO_VENTANA-240,2,150)
    rata_4 = Rata(200,ALTO_VENTANA-240,2,150)
    rata_5 = Rata(160,ALTO_VENTANA-520,2,150)
    rata_6 = Rata(540,ALTO_VENTANA-400,2,150)
    
    lista_enemigos = [rata_1,rata_2,rata_3,rata_4,rata_5,rata_6]
    
    obstaculo_1 = pygame.Rect(720,500,20,60)
    obstaculo_2 = pygame.Rect(420,500,20,60)
    obstaculo_3 = pygame.Rect(740,420,20,60)
    obstaculo_4 = pygame.Rect(1160,420,20,60)
    obstaculo_5 = pygame.Rect(680,340,20,60)
    obstaculo_6 = pygame.Rect(460,340,20,60)
    obstaculo_7 = pygame.Rect(320,340,20,60)
    obstaculo_8 = pygame.Rect(20,340,20,60)
    obstaculo_9 = pygame.Rect(140,60,20,60)
    obstaculo_10 = pygame.Rect(440,60,20,60)    
    obstaculo_11 = pygame.Rect(460,180,20,60)
    obstaculo_12 = pygame.Rect(680,180,20,60)
    
    lista_obstaculos = [obstaculo_1,obstaculo_2,obstaculo_3,obstaculo_4,obstaculo_5,obstaculo_6,obstaculo_7,
    obstaculo_8,obstaculo_9,obstaculo_10,obstaculo_11,obstaculo_12]
    
    item_1 = Item(45,370)
    item_2 = Item(1125,330)
    mostrar_rectangulos = False
    
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
        nivel_1.dibujar(ventana)
        
        personaje.actualizar(ventana)
        
        if len(lista_enemigos) > 0:
            imagen_puerta = pygame.image.load('imagenes_obstaculos/puerta_cerrada.png')
            alto_puerta = imagen_puerta.get_height()
            ancho_puerta = imagen_puerta.get_width()
            imagen_puerta = pygame.transform.scale(imagen_puerta,(ancho_puerta * 0.2, alto_puerta * 0.2))
            puerta_rect = imagen_puerta.get_rect()
            ventana.blit(imagen_puerta,(1100,50))
        else:
            imagen_puerta = pygame.image.load('imagenes_obstaculos/puerta_abierta.png')
            alto_puerta = imagen_puerta.get_height()
            ancho_puerta = imagen_puerta.get_width()
            imagen_puerta = pygame.transform.scale(imagen_puerta,(ancho_puerta * 0.2, alto_puerta * 0.2))
            puerta_rect = imagen_puerta.get_rect()
            puerta_rect.x = 1100
            puerta_rect.y = 50
            ventana.blit(imagen_puerta,(1100,50))
            if puerta_rect.colliderect(personaje.rect):
                puntaje.guardar_puntaje(nivel_puntaje)
                siguiente_nivel_desbloqueado = True
                run = False
        
        
        
        item_1.actualizar(ventana,personaje)
        item_2.actualizar(ventana,personaje)
        rata_1.actualizar()
        rata_2.actualizar()
        rata_3.actualizar()
        rata_4.actualizar()
        rata_5.actualizar()
        rata_6.actualizar()
        rata_1.animar_sprites(ventana,personaje)
        rata_2.animar_sprites(ventana,personaje)
        rata_3.animar_sprites(ventana,personaje)
        rata_4.animar_sprites(ventana,personaje)
        rata_5.animar_sprites(ventana,personaje)
        rata_6.animar_sprites(ventana,personaje)
        
        for enemigo in lista_enemigos:
            if enemigo.muerto:
                lista_enemigos.remove(enemigo)
                if personaje.vida >= 75:
                    nivel_puntaje += 50
                else:
                    nivel_puntaje += 25
        
        #mostrar los rects
        if mostrar_rectangulos:
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect,2)
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect_derecha,2)
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect_izquierda,2)
            pygame.draw.rect(ventana,COLOR_BLANCO,personaje.rect_arriba,2)
            pygame.draw.rect(ventana,COLOR_ROJO,personaje.espada_rect,2)
            pygame.draw.rect(ventana,COLOR_AZUL,rata_1.rect,2)
            pygame.draw.rect(ventana,COLOR_AZUL,rata_2.rect,2)
            pygame.draw.rect(ventana,COLOR_AZUL,rata_1.rect_left,2)
            pygame.draw.rect(ventana,COLOR_AZUL,rata_2.rect_left,2)
            pygame.draw.rect(ventana,COLOR_AZUL,rata_1.rect_right,2)
            pygame.draw.rect(ventana,COLOR_AZUL,rata_2.rect_right,2)
            for i in lista_obstaculos:
                pygame.draw.rect(ventana,COLOR_ROSA,i,2)
            pygame.draw.rect(ventana,COLOR_VERDE,item_1.rect,2)
            pygame.draw.rect(ventana,COLOR_GRIS,puerta_rect,2)
            
        
        #colisiones del personaje
        for cuadricula in nivel_1.lista_cuadriculas:
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
        
        #colision de los enemigos
        rata_1.manejar_colision_obstaculo(obstaculo_1)
        rata_1.manejar_colision_obstaculo(obstaculo_2)
        rata_2.manejar_colision_obstaculo(obstaculo_3)
        rata_2.manejar_colision_obstaculo(obstaculo_4)
        rata_3.manejar_colision_obstaculo(obstaculo_5)
        rata_3.manejar_colision_obstaculo(obstaculo_6)
        rata_4.manejar_colision_obstaculo(obstaculo_7)
        rata_4.manejar_colision_obstaculo(obstaculo_8)
        rata_5.manejar_colision_obstaculo(obstaculo_9)
        rata_5.manejar_colision_obstaculo(obstaculo_10)
        rata_6.manejar_colision_obstaculo(obstaculo_11)
        rata_6.manejar_colision_obstaculo(obstaculo_12)
        rata_1.manejar_colision_espada(personaje.espada_rect)
        rata_2.manejar_colision_espada(personaje.espada_rect)
        rata_3.manejar_colision_espada(personaje.espada_rect)
        rata_4.manejar_colision_espada(personaje.espada_rect)
        rata_5.manejar_colision_espada(personaje.espada_rect)
        rata_6.manejar_colision_espada(personaje.espada_rect)
        
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
        
        
        if personaje.muerto:
            imagen_exit = pygame.image.load('imagenes_interfaz/boton_exit.png')
            boton_back = boton.Boton(500,450,imagen_exit,6)
            ventana.blit(texto_game_over,(350,250))
            if boton_back.dibujar(ventana):
                run = False
        
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
        pygame.display.update()
    
    return siguiente_nivel_desbloqueado

