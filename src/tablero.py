import pygame
from constantes import *

class Tablero:
    def __init__(self):
        self.tablero = []
        self.pieza_seleccionada = None
        self.piezas_rojas = self.blancas = 12
        self.rey_roja = self.rey_blanca = 0

    def dibujar_casillas(self, win):
        win.fill(NEGRO)
        
        for fila in range(FILAS):
            for columna in range(fila % 2, FILAS, 2):
                pygame.draw.rect(win, ROJO, (columna * TAMANIO_CUADRADO, 
                                             fila * TAMANIO_CUADRADO, 
                                             TAMANIO_CUADRADO, TAMANIO_CUADRADO))

    def crear_tablero(self):
        pass