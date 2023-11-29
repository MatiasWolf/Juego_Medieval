import pygame
from Constantes import *
from Ingreso_nombre import *
from ranking import *
from menus import *
#pygame.init()

#ventana
#ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
#pygame.display.set_caption('UTN')



def Nivel_tres(ventana,cancion):
    from niveles import Nivel
    from config import data_nivel_3
    from funciones import cambiar_escala_imagenes
    from personaje import Personaje
    from enemigos import Monstruo
    from item import Item
    import puntaje
    
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    cancion.set_volume(0.2)
    
    #reloj
    reloj = pygame.time.Clock()
    fps = 60
    tiempo_inicial = pygame.time.get_ticks()

    #fondo e interfaz
    fondo = pygame.image.load('fondo_nivel_3.png')
    alto_fondo = fondo.get_height()
    ancho_fondo = fondo.get_width()
    fondo = pygame.transform.scale(fondo,(ancho_fondo * 4.5,alto_fondo * 3.6))
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

    juego_finalizado = 'Juego Finalizado'
    score_final = 'Tu score final es:'
    texto_juego_finalizado = fuente_grande.render(str(juego_finalizado),True,COLOR_NEGRO)
    texto_score_final = fuente_grande.render(str(score_final),True,COLOR_NEGRO)
    game_over = 'GAME OVER'
    texto_game_over = fuente_grande.render(str(game_over),True,COLOR_NEGRO)
    
    finish = False
    
    juego_pausado  = False
    
    nivel_3 = Nivel(data_nivel_3)

    personaje = Personaje(100,500)

    enemigo_1 = Monstruo(400,272,2,500)
    enemigo_2 = Monstruo(200,152,2,500)
    enemigo_3 = Monstruo(900,152,2,500)
    enemigo_4 = Monstruo(500,480,2,500)

    lista_enemigos = [enemigo_1,enemigo_2,enemigo_3,enemigo_4]

    obstaculo_1 = pygame.Rect(380,320,20,40)
    obstaculo_2 = pygame.Rect(800,320,20,40)
    obstaculo_3 = pygame.Rect(360,200,20,40)
    obstaculo_4 = pygame.Rect(20,200,20,40)
    obstaculo_5 = pygame.Rect(820,200,20,40)
    obstaculo_6 = pygame.Rect(1160,200,20,40)
    obstaculo_7 = pygame.Rect(300,460,20,40)
    obstaculo_8 = pygame.Rect(880,460,20,40)

    item_1 = Item(600,410)
    item_2 = Item(460,80)
    item_3 = Item(700,80)

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
        nivel_3.dibujar(ventana)
        
        personaje.actualizar(ventana)
        
        enemigo_1.actualizar()
        enemigo_2.actualizar()
        enemigo_3.actualizar()
        enemigo_4.actualizar()
        enemigo_1.animar_sprites(ventana,personaje)
        enemigo_2.animar_sprites(ventana,personaje)
        enemigo_3.animar_sprites(ventana,personaje)
        enemigo_4.animar_sprites(ventana,personaje)
        
        item_1.actualizar(ventana,personaje)
        item_2.actualizar(ventana,personaje)
        item_3.actualizar(ventana,personaje)
        
        for enemigo in lista_enemigos:
            if enemigo.muerto:
                lista_enemigos.remove(enemigo)
                if personaje.vida >= 75:
                    nivel_puntaje += 100
                else:
                    nivel_puntaje += 50
        
        for cuadricula in nivel_3.lista_cuadriculas:
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
        
        if mostrar_rectangulos:
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_1,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_2,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_3,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_4,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_5,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_6,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_7,2)
            pygame.draw.rect(ventana,COLOR_ROSA,obstaculo_8,2)
        
        enemigo_1.manejar_colision_obstaculo(obstaculo_1)
        enemigo_1.manejar_colision_obstaculo(obstaculo_2)
        enemigo_2.manejar_colision_obstaculo(obstaculo_3)
        enemigo_2.manejar_colision_obstaculo(obstaculo_4)
        enemigo_3.manejar_colision_obstaculo(obstaculo_5)
        enemigo_3.manejar_colision_obstaculo(obstaculo_6)
        enemigo_4.manejar_colision_obstaculo(obstaculo_7)
        enemigo_4.manejar_colision_obstaculo(obstaculo_8)
        enemigo_1.manejar_colision_espada(personaje.espada_rect)
        enemigo_2.manejar_colision_espada(personaje.espada_rect)
        enemigo_3.manejar_colision_espada(personaje.espada_rect)
        enemigo_4.manejar_colision_espada(personaje.espada_rect)
        
        #texto y barra de vida
        if personaje.vida == 100:
            ventana.blit(barra_vida_completa,(10,10))
        elif personaje.vida == 75:
            ventana.blit(barra_vida_75,(10,10))
        elif personaje.vida == 50:
            ventana.blit(barra_vida_50,(10,10))
        elif personaje.vida == 25:
            ventana.blit(barra_vida_25,(10,10))
        elif personaje.vida <= 0:
            ventana.blit(barra_sin_vida,(10,10))
        ventana.blit(texto_puntuacion,(980,570))
        ventana.blit(texto_cantidad_puntuacion,(1100,570))
        
        if len(lista_enemigos) == 0:
            puntaje.guardar_puntaje(nivel_puntaje)
            finish = True
        
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
        
        if finish:
            ventana.fill(COLOR_BLANCO)
            ventana.blit(texto_juego_finalizado,(150,100))
            ventana.blit(texto_score_final,(150,200))
            puntaje_final = puntaje.cargar_puntaje()
            nombre = ingresar_nombre(ventana)
            agregar_puntaje(nombre,puntaje_final)
            run = False
        pygame.display.flip()
    pygame.quit