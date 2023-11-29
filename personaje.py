import pygame
from Constantes import *
from carga_sprites import *

class Personaje:
    def __init__(self,x,y) -> None:
        
        #imagenes e indice
        self.correr_derecha = correr_derecha
        self.correr_izquierda = correr_izquierda
        self.quieto_derecha = quieto_derecha
        self.quieto_izquierda = quieto_izquierda
        self.ataque_derecha = ataque_derecha
        self.ataque_izquierda = ataque_izquierda
        self.salto_derecha = salto_derecha
        self.salto_izquierda = salto_izquierda
        self.muerto_derecha = muerte_derecha
        self.muerto_izquierda = muerte_izquierda
        self.indice = 0
        
        #imagen, rect y variables del personaje
        self.imagen = self.quieto_derecha[self.indice]
        self.ancho = self.imagen.get_width()    
        self.alto = self.imagen.get_height()
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.px = self.rect.x
        self.py = self.rect.y
        self.vida = 100
        self.muerto = False
        self.dy = 0
        self.dx = 0
        self.rect_derecha = pygame.Rect(self.rect.right,self.rect.top + 5,10,self.rect.height - 10)
        self.rect_izquierda = pygame.Rect(self.rect.left - 10,self.rect.top + 5,10,self.rect.height - 10)
        self.rect_arriba = pygame.Rect(self.rect.left + 4,self.rect.top - 10,self.rect.width - 7,7)
        self.velocidad_y = 0
        self.saltando = False
        self.atacando = False
        self.salto_terminado = False
        self.ataque_terminado = False
        self.indice_ataque = 0
        self.direccion = 'derecha'
        self.espada_rect = pygame.Rect(0,0,0,0)
        
        self.puntaje = 0
        
        #estado de las teclas
        self.estado_teclas = {
        'derecha': False,
        'izquierda': False,
        'ataque': False,
        'salto': False
        }
    
    def actualizar(self,ventana):
        #manejo movimiento
        self.dx = 0
        self.dy = 0
        
        self.px = self.rect.x
        self.py = self.rect.y
        if self.vida <= 0:
            self.muerto = True
            
        teclas = pygame.key.get_pressed()
        if not self.muerto:
            if teclas[pygame.K_SPACE] and not self.salto_terminado:
                self.estado_teclas['salto'] = True
                self.velocidad_y = -15
                self.salto_terminado = True
                self.saltando = True
            elif teclas[pygame.K_SPACE] == False:
                self.estado_teclas['salto'] = False
            if teclas[pygame.K_f] and not self.ataque_terminado:
                self.estado_teclas['ataque'] = True
            elif teclas[pygame.K_f] == False:
                self.estado_teclas['ataque'] = False
                self.atacando = False
                self.indice_ataque = 0
                self.espada_rect = pygame.Rect(0,0,0,0)
            if teclas[pygame.K_d]:
                self.estado_teclas['derecha'] = True
                self.direccion = 'derecha'
                self.dx += 4
            elif teclas[pygame.K_d] == False:
                self.estado_teclas['derecha'] = False
            if teclas[pygame.K_a]:
                self.estado_teclas['izquierda'] = True
                self.direccion = 'izquierda'
                self.dx -= 4
            elif teclas[pygame.K_a] == False:
                self.estado_teclas['izquierda'] = False
            
            
            self.dy += self.velocidad_y
            
            self.rect.x += self.dx
            self.rect.y += self.dy
            self.rect_derecha.x += self.dx
            self.rect_derecha.y += self.dy
            self.rect_izquierda.x += self.dx
            self.rect_izquierda.y += self.dy
            self.rect_arriba.x += self.dx
            self.rect_arriba.y += self.dy
            
            #manejo sprites
            self.indice += 0.3
            if not self.saltando:
                if self.direccion == 'derecha':
                    if self.estado_teclas['derecha']:
                        if self.indice >= len(self.correr_derecha):
                            self.indice = 0
                        self.imagen = self.correr_derecha[int(self.indice)]
                    elif self.estado_teclas['ataque']:
                        if not self.atacando:
                            if self.indice_ataque + 1 < len(self.ataque_derecha):
                                self.indice_ataque += 0.3
                            else:
                                self.indice_ataque = 0
                                self.atacando = True
                            if int(self.indice_ataque) == 2:
                                self.espada_rect = pygame.Rect(self.rect.x + self.rect.width,self.rect.y + self.rect.height // 2,50,15)
                            else:
                                self.espada_rect = pygame.Rect(0,0,0,0)
                            self.imagen = self.ataque_derecha[int(self.indice_ataque)]
                            
                                
                        else:
                            if self.indice >= len(self.quieto_derecha):
                                self.indice = 0
                            self.imagen = self.quieto_derecha[int(self.indice)]
                    else:
                        if self.indice >= len(self.quieto_derecha):
                            self.indice = 0
                        self.imagen = self.quieto_derecha[int(self.indice)]
                else:
                    if self.estado_teclas['izquierda']:
                        if self.indice >= len(self.correr_izquierda):
                            self.indice = 0
                        self.imagen = self.correr_izquierda[int(self.indice)]
                    elif self.estado_teclas['ataque']:
                        if not self.atacando:
                            if self.indice_ataque + 1 < len(self.ataque_izquierda):
                                self.indice_ataque += 0.3
                            else:
                                self.indice_ataque = 0
                                self.atacando = True
                            if int(self.indice_ataque) == 2:
                                self.espada_rect = pygame.Rect(self.rect.x - self.rect.width,self.rect.y + self.rect.height // 2, 50,15)
                            else:
                                self.espada_rect = pygame.Rect(0,0,0,0)
                            self.imagen = self.ataque_izquierda[int(self.indice_ataque)]
                        else:
                            if self.indice >= len(self.quieto_derecha):
                                self.indice = 0
                            self.imagen = self.quieto_izquierda[int(self.indice)]
                    else:
                        if self.indice >= len(self.quieto_izquierda):
                            self.indice = 0
                        self.imagen = self.quieto_izquierda[int(self.indice)]
            else:
                if self.direccion == 'derecha':
                    if self.indice >= len(self.salto_derecha):
                        self.indice = 0
                    self.imagen = self.salto_derecha[int(self.indice)]
                else:
                    if self.indice >= len(self.salto_izquierda):
                        self.indice = 0
                    self.imagen = self.salto_izquierda[int(self.indice)]
        
        self.aplicar_gravedad()
        if not self.muerto:
            ventana.blit(self.imagen, self.rect)
        else:
            if self.direccion == 'derecha':
                if int(self.indice) < 9:
                    ventana.blit(self.muerto_derecha[int(self.indice)],(int(self.px),int(self.py + 50)))
                    self.indice += 0.5
                else:
                    ventana.blit(self.muerto_derecha[int(self.indice)],(int(self.px),int(self.py + 50)))
            elif self.direccion == 'izquierda':
                if int(self.indice) < 9:
                    ventana.blit(self.muerto_izquierda[int(self.indice)],(int(self.px),int(self.py + 50)))
                    self.indice += 0.5
                else:
                    ventana.blit(self.muerto_izquierda[int(self.indice)],(int(self.px),int(self.py + 50)))
    
    def aplicar_gravedad(self):
        self.velocidad_y += 1
        if self.velocidad_y > 10:
            self.velocidad_y = 10
    