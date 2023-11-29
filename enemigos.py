import pygame
import random
from carga_sprites_enemigo import *

class Enemigo:
    def __init__(self,x,y,velocidad,vida) -> None:
        
        #variables generales de enemigos
        self.x = x
        self.y = y
        self.direccion = True #True-Derecha/False-Izquierda
        self.velocidad = velocidad
        self.posicion_actual = self.x
        self.cuenta_pasos = 0
        self.indice_muerte = 0
        self.indice_ataque = 0
        self.daño = random.randrange(10,20)
        self.vida = vida
        self.muerto = False
        
    def actualizar(self):
        if not self.muerto:
            if self.direccion:
                self.x += self.velocidad
            else:
                self.x -= self.velocidad
            
            if self.vida <= 0:
                self.muerto = True

class Rata(Enemigo):
    def __init__(self,x,y,velocidad,vida) -> None:
        super().__init__(x,y,velocidad,vida)
        
        self.ancho_enemigo = rata_imagen_correr_d.get_width()
        self.alto_enemigo = rata_imagen_correr_d.get_height()
        
        self.sprites_correr_derecha = rata_correr_derecha
        self.sprites_correr_izquierda = rata_correr_izquierda
        self.sprites_atacar_derecha = rata_atacar_derecha
        self.sprites_atacar_izquierda = rata_atacar_izquierda
        self.sprites_muerte_derecha = rata_muerto_derecha
        self.sprites_muerte_izquierda = rata_muerto_izquierda
        
        self.rect = pygame.Rect(self.x, self.y, self.ancho_enemigo, self.alto_enemigo)
        self.rect_left = pygame.Rect(0, 0, 0, 0)
        self.rect_right = pygame.Rect(0, 0, 0, 0)
        
        self.cuenta_pasos = 0
        self.indice_muerte = 0
        self.indice_ataque = 0
        
    def actualizar(self):
        super().actualizar()
        if not self.muerto:
            if self.direccion:
                self.rect_left = pygame.Rect(0, 0, 0, 0)
                self.rect_right = pygame.Rect((self.x + self.ancho_enemigo), self.y, 10, self.alto_enemigo // 2)
            else:
                self.rect_left = pygame.Rect(self.x - 10,self.y,10,self.alto_enemigo // 2)
                self.rect_right = pygame.Rect(0, 0, 0, 0)
            
            self.rect.x = self.x
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)
            self.rect_left = pygame.Rect(0, 0, 0, 0)
            self.rect_right = pygame.Rect(0, 0, 0, 0)
    
    def animar_sprites(self,ventana, personaje):
        if (not self.rect_left.colliderect(personaje.rect) and not self.rect_right.colliderect(personaje.rect)) or personaje.muerto:
            self.velocidad = 2
            if not self.muerto:
                if self.cuenta_pasos + 1 >= 8:
                    self.cuenta_pasos = 0
                
                if self.direccion:
                    ventana.blit(self.sprites_correr_derecha[int(self.cuenta_pasos) // 1], (int(self.x), int(self.y)))
                    self.cuenta_pasos += 1
                else:
                    ventana.blit(self.sprites_correr_izquierda[int(self.cuenta_pasos) // 1], (int(self.x), int(self.y)))
                    self.cuenta_pasos += 1
            else:
                if self.direccion:
                    if self.indice_muerte < 3:
                        ventana.blit(self.sprites_muerte_derecha[self.indice_muerte], (int(self.x), int(self.y)))
                        self.indice_muerte += 1
                    else:
                        ventana.blit(self.sprites_muerte_derecha[self.indice_muerte], (int(self.x), int(self.y + 30)))
                else:
                    if self.indice_muerte < 3:
                        ventana.blit(self.sprites_muerte_izquierda[self.indice_muerte], (int(self.x), int(self.y)))
                        self.indice_muerte += 1
                    else:
                        ventana.blit(self.sprites_muerte_izquierda[self.indice_muerte], (int(self.x), int(self.y + 30)))
        else:
            self.velocidad = 0
            if self.rect_left.colliderect(personaje.rect):
                if self.indice_ataque + 1 >= 8:
                    self.indice_ataque = 0
                    personaje.vida -= 25
                ventana.blit(self.sprites_atacar_izquierda[int(self.indice_ataque) // 1], (int(self.x),int(self.y)))
                self.indice_ataque += 0.4
            elif self.rect_right.colliderect(personaje.rect):
                if self.indice_ataque + 1 >= 8:
                    self.indice_ataque = 0
                    personaje.vida -= 25
                
                ventana.blit(self.sprites_atacar_derecha[int(self.indice_ataque) // 1], (int(self.x),int(self.y)))
                self.indice_ataque += 0.4
    
    def manejar_colision_espada(self, espada_jugador):
        if self.rect.colliderect(espada_jugador):
            self.vida -= self.daño
            self.atacado = True
    
    def manejar_colision_obstaculo(self,obstaculo):
        if self.rect.colliderect(obstaculo):
            self.direccion = not self.direccion

class Esqueleto(Enemigo):
    def __init__(self,x,y,velocidad,vida) -> None:
        super().__init__(x,y,velocidad,vida)
        
        self.ancho_enemigo = esqueleto_imagen_correr_d.get_width()
        self.alto_enemigo = esqueleto_imagen_correr_d.get_height()
        
        self.sprites_correr_derecha = esqueleto_correr_derecha
        self.sprites_correr_izquierda = esqueleto_correr_izquierda
        self.sprites_atacar_derecha = esqueleto_ataque_derecha
        self.sprites_atacar_izquierda = esqueleto_ataque_izquierda
        self.sprites_muerte_derecha = esqueleto_muerte_derecha
        self.sprites_muerte_izquierda = esqueleto_muerte_izquierda
        
        self.rect = pygame.Rect(self.x, self.y, self.ancho_enemigo, self.alto_enemigo)
        self.rect_left = pygame.Rect(0, 0, 0, 0)
        self.rect_right = pygame.Rect(0, 0, 0, 0)

        self.cuenta_pasos = 0
        self.indice_muerte = 0
        self.indice_ataque = 0
    
    def actualizar(self):
        super().actualizar()
        
        if not self.muerto:
            if self.direccion:
                self.rect_left = pygame.Rect(0, 0, 0, 0)
                self.rect_right = pygame.Rect((self.x + self.ancho_enemigo), self.y, 10, self.alto_enemigo // 2)
            else:
                self.rect_left = pygame.Rect(self.x - 10,self.y,10,self.alto_enemigo // 2)
                self.rect_right = pygame.Rect(0, 0, 0, 0)
            
            self.rect.x = self.x
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)
            self.rect_left = pygame.Rect(0, 0, 0, 0)
            self.rect_right = pygame.Rect(0, 0, 0, 0)
    
    def animar_sprites(self,ventana,personaje):
        if (not self.rect_left.colliderect(personaje.rect) and not self.rect_right.colliderect(personaje.rect)) or personaje.muerto:
            self.velocidad = 2
            if not self.muerto:
                if self.cuenta_pasos + 1 >= 9:
                    self.cuenta_pasos = 0
                
                if self.direccion:
                    ventana.blit(self.sprites_correr_derecha[int(self.cuenta_pasos) // 1], (int(self.x), int(self.y)))
                    self.cuenta_pasos += 0.5
                else:
                    ventana.blit(self.sprites_correr_izquierda[int(self.cuenta_pasos) // 1], (int(self.x), int(self.y)))
                    self.cuenta_pasos += 0.5
            else:
                if self.direccion:
                    if self.indice_muerte < 8:
                        ventana.blit(self.sprites_muerte_derecha[self.indice_muerte], (int(self.x), int(self.y)))
                        self.indice_muerte += 1
                    else:
                        ventana.blit(self.sprites_muerte_derecha[self.indice_muerte], (int(self.x), int(self.y)))
                else:
                    if self.indice_muerte < 8:
                        ventana.blit(self.sprites_muerte_izquierda[self.indice_muerte], (int(self.x), int(self.y)))
                        self.indice_muerte += 1
                    else:
                        ventana.blit(self.sprites_muerte_izquierda[self.indice_muerte], (int(self.x), int(self.y)))
        else:
            self.velocidad = 0
            if self.rect_left.colliderect(personaje.rect):
                if self.indice_ataque + 1 >= 6:
                    self.indice_ataque = 0
                    personaje.vida -= 25
                ventana.blit(self.sprites_atacar_izquierda[int(self.indice_ataque) // 1], (int(self.x),int(self.y)))
                self.indice_ataque += 0.2
            elif self.rect_right.colliderect(personaje.rect):
                if self.indice_ataque + 1 >= 6:
                    self.indice_ataque = 0
                    personaje.vida -= 25
                
                ventana.blit(self.sprites_atacar_derecha[int(self.indice_ataque) // 1], (int(self.x),int(self.y)))
                self.indice_ataque += 0.2
        
    def manejar_colision_espada(self, espada_jugador):
        if self.rect.colliderect(espada_jugador):
            self.vida -= self.daño
            self.atacado = True
    
    def manejar_colision_obstaculo(self,obstaculo):
        if self.rect.colliderect(obstaculo):
            self.direccion = not self.direccion

class Monstruo(Enemigo):
    def __init__(self, x, y, velocidad, vida) -> None:
        super().__init__(x, y, velocidad, vida)
        
        self.ancho_enemigo = monstruo_imagen_correr_d.get_width()
        self.alto_enemigo = monstruo_imagen_correr_d.get_height()
        
        self.sprites_correr_derecha = monstruo_correr_derecha
        self.sprites_correr_izquierda = monstruo_correr_izquierda
        self.sprites_atacar_derecha = monstruo_ataque_derecha
        self.sprites_atacar_izquierda = monstruo_ataque_izquierda
        self.sprites_muerte_derecha = monstruo_muerte_derecha
        self.sprites_muerte_izquierda = monstruo_muerte_izquierda
        
        self.rect = pygame.Rect(self.x, self.y, self.ancho_enemigo, self.alto_enemigo)
        self.rect_left = pygame.Rect(0, 0, 0, 0)
        self.rect_right = pygame.Rect(0, 0, 0, 0)
        
        self.cuenta_pasos = 0
        self.indice_muerte = 0
        self.indice_ataque = 0
    
    def actualizar(self):
        super().actualizar()
        
        if not self.muerto:
            if self.direccion:
                self.rect_left = pygame.Rect(0, 0, 0, 0)
                self.rect_right = pygame.Rect((self.x + self.ancho_enemigo), self.y, 10, self.alto_enemigo // 2)
            else:
                self.rect_left = pygame.Rect(self.x - 10,self.y,10,self.alto_enemigo // 2)
                self.rect_right = pygame.Rect(0, 0, 0, 0)
            
            self.rect.x = self.x
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)
            self.rect_left = pygame.Rect(0, 0, 0, 0)
            self.rect_right = pygame.Rect(0, 0, 0, 0)
    
    def animar_sprites(self,ventana,personaje):
        if (not self.rect_left.colliderect(personaje.rect) and not self.rect_right.colliderect(personaje.rect)) or personaje.muerto:
            self.velocidad = 2
            self.indice_ataque = 0
            if not self.muerto:
                if self.cuenta_pasos + 1 >= 8:
                    self.cuenta_pasos = 0
                
                if self.direccion:
                    ventana.blit(self.sprites_correr_derecha[int(self.cuenta_pasos) // 1], (int(self.x), int(self.y)))
                    self.cuenta_pasos += 0.5
                else:
                    ventana.blit(self.sprites_correr_izquierda[int(self.cuenta_pasos) // 1], (int(self.x), int(self.y)))
                    self.cuenta_pasos += 0.5
            else:
                if self.direccion:
                    if self.indice_muerte < 9:
                        ventana.blit(self.sprites_muerte_derecha[self.indice_muerte], (int(self.x), int(self.y)))
                        self.indice_muerte += 1
                    else:
                        ventana.blit(self.sprites_muerte_derecha[self.indice_muerte], (int(self.x), int(self.y)))
                else:
                    if self.indice_muerte < 9:
                        ventana.blit(self.sprites_muerte_izquierda[self.indice_muerte], (int(self.x), int(self.y)))
                        self.indice_muerte += 1
                    else:
                        ventana.blit(self.sprites_muerte_izquierda[self.indice_muerte], (int(self.x), int(self.y)))
        else:
            self.velocidad = 0
            if self.rect_left.colliderect(personaje.rect):
                if self.indice_ataque + 1 >= 8:
                    self.indice_ataque = 0
                    personaje.vida -= 75
                ventana.blit(self.sprites_atacar_izquierda[int(self.indice_ataque) // 1], (int(self.x),int(self.y)))
                self.indice_ataque += 0.2
            elif self.rect_right.colliderect(personaje.rect):
                if self.indice_ataque + 1 >= 8:
                    self.indice_ataque = 0
                    personaje.vida -= 75
                
                ventana.blit(self.sprites_atacar_derecha[int(self.indice_ataque) // 1], (int(self.x),int(self.y)))
                self.indice_ataque += 0.2
        
    def manejar_colision_espada(self, espada_jugador):
        if self.rect.colliderect(espada_jugador):
            self.vida -= self.daño
            self.atacado = True
    
    def manejar_colision_obstaculo(self,obstaculo):
        if self.rect.colliderect(obstaculo):
            self.direccion = not self.direccion