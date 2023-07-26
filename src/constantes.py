import pygame

ANCHO, ALTO = 600, 600
FILAS, COLUMNAS = 8, 8
TAMANIO_CUADRADO = ANCHO // COLUMNAS

ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
GRIS = (128, 128, 128)

CORONA = pygame.transform.scale(pygame.image.load("assets\crown.png"), (44, 25))
