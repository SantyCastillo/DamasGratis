import pygame

# DIMENSIONES
ANCHO, ALTO = 800, 800
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
CORONA = pygame.transform.scale(pygame.image.load("assets\crown.png"), (44, 25))
FONDO = pygame.image.load("assets/fondo2.jpg")
