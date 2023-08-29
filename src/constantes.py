import pygame
import os

#Ruta del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# DIMENSIONES
ANCHO, ALTO = 600, 600
FILAS, COLUMNAS = 8, 8
TAMANIO_CUADRADO = ANCHO // COLUMNAS

# COLORES RGB
ROJO = (160, 0, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 11, 142)
GRIS = (128, 128, 128)
VERDE = (19, 156, 0)
COLOR_RESALTADO = BLANCO
COLOR_NORMAL = NEGRO

# IMAGENES
CORONA = pygame.transform.scale(pygame.image.load(os.path.join(script_dir, "assets", "crown.png")), (34, 25))
FONDO = pygame.image.load(os.path.join(script_dir, "assets", "fondo.jpg"))
