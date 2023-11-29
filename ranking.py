import sqlite3
import pygame
from Constantes import *
import boton

ventana = pygame.display.set_mode((600,600))

def crear_SQLite():
    # Conectar a la base de datos (esto creará el archivo si no existe)
    conn = sqlite3.connect('ranking.db')

    # Crear un objeto cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Crear la nueva estructura de la tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ranking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            puntaje INTEGER
        )
    ''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def agregar_puntaje(nombre, puntaje):
    conn = sqlite3.connect('ranking.db')
    cursor = conn.cursor()

    # Insertar el nombre y el puntaje en la tabla
    cursor.execute('INSERT INTO ranking (nombre, puntaje) VALUES (?, ?)', (nombre, puntaje))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def obtener_ranking():
    conn = sqlite3.connect('ranking.db')
    cursor = conn.cursor()

    # Obtener los datos del ranking ordenados por puntaje descendente
    cursor.execute('SELECT nombre, puntaje FROM ranking ORDER BY puntaje DESC')
    ranking = cursor.fetchall()

    # Cerrar la conexión
    conn.close()

    return ranking

def mostrar_ranking():
    fuente_ranking = pygame.font.Font('upheavtt.ttf',80) 
    
    ranking = obtener_ranking()
    
    estado_menu = 'ranking'
    
    ventana.fill(COLOR_BLANCO)

    # Mostrar el ranking en pantalla
    y_pos = 100
    for i, (nombre, puntaje) in enumerate(ranking, start=1):
        texto_ranking = fuente_ranking.render(f"{i}. {nombre}: {puntaje}", True, COLOR_NEGRO)
        ventana.blit(texto_ranking, (600 // 2 - 200, y_pos))
        y_pos += 80
    
    imagen_exit = pygame.image.load('imagenes_interfaz/boton_exit.png')
    boton_back = boton.Boton(700,450,imagen_exit,6)
    
    if boton_back.dibujar(ventana):
        estado_menu = 'main'
    pygame.display.flip()
    return estado_menu