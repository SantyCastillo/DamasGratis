from constantes import *
import pygame

class Pieza:
    RELLENO = 20
    CONTORNO = 2

    def __init__(self, fila, columna, color):
        self.fila = fila
        self.columna = columna
        self.color = color
        self.rey = False
        self.x = 0
        self.y = 0

        if self.color == ROJO:
            self.direccion = -1
        else:
            self.direccion = 1

    def calcular_posicion(self):
        self.x = self.columna * TAMANIO_CUADRADO + TAMANIO_CUADRADO // 2
        self.y = self.fila * TAMANIO_CUADRADO + TAMANIO_CUADRADO // 2

    def crear_rey(self):
        self.rey = True
    
    def dibujar(self, win):
        radio = TAMANIO_CUADRADO // 2 - self.RELLENO 
        pygame.draw.circle(win, GRIS, (self.x, self.y), TAMANIO_CUADRADO // 2, radio)
        pygame.draw.circle(win, self.color, (self.x, self.y), TAMANIO_CUADRADO // 2, radio + self.CONTORNO)
        if self.rey:
           win.blit(CORONA, (self.x - CORONA.get_width() // 2, self.y - CORONA.get_height() // 2))

    def movimiento(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.calcular_posicion()
        
    def __repr__(self):
        return str(self.color)