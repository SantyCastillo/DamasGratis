from constantes import *
import pygame

class Pieza:
    RELLENO = 15
    CONTORNO = 2

    def __init__(self, fila, columna, color):
        self.fila = fila
        self.columna = columna
        self.color = color
        self.rey = False
        self.x = 0
        self.y = 0
        self.calcular_posicion()

    def calcular_posicion(self):
        self.x = TAMANIO_CUADRADO * self.columna + TAMANIO_CUADRADO // 2
        self.y = TAMANIO_CUADRADO * self.fila + TAMANIO_CUADRADO // 2

    def crear_rey(self):
        self.rey = True
    
    def dibujar(self, win):
        radio = TAMANIO_CUADRADO // 2 - self.RELLENO 
        pygame.draw.circle(win, GRIS, (self.x, self.y), radio + self.CONTORNO)
        pygame.draw.circle(win, self.color, (self.x, self.y), radio)
        if self.rey:
           win.blit(CORONA, (self.x - CORONA.get_width() // 2, self.y - CORONA.get_height() // 2))

    def mover(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.calcular_posicion()
        
    def __repr__(self):
        return str(self.color)