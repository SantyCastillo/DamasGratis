import pygame
from constantes import *
from pieza import Pieza

class Tablero:
    def __init__(self):
        self.tablero = []
        self.pieza_seleccionada = None
        self.piezas_rojas = self.blancas = 12
        self.rey_roja = self.rey_blanca = 0
        self.crear_tablero()

    def dibujar_casillas(self, win):
        win.fill(NEGRO)
        
        for fila in range(FILAS):
            for columna in range(fila % 2, COLUMNAS, 2):
                pygame.draw.rect(win, ROJO, (fila * TAMANIO_CUADRADO, columna * TAMANIO_CUADRADO, TAMANIO_CUADRADO, TAMANIO_CUADRADO))

    def movimiento(self, pieza, fila, columna):
        self.tablero[pieza.fila][pieza.columna], self.tablero[fila][columna] = self.tablero[fila][columna], self.tablero[pieza.fila][pieza.columna]
        pieza.movimiento(fila, columna)

        if fila == FILAS or columna == 0:
            pieza.crear_rey()
            if pieza.color == BLANCO:
                self.rey_blanca += 1
            else:
                self.rey_roja += 1

    def obt_pieza(self, fila, columna):
        return self.tablero[fila][columna]
    
    def crear_tablero(self):
        for fila in range(FILAS):
            self.tablero.append([])
            for columna in range(COLUMNAS):
                if columna % 2 == ((fila + 1) % 2):
                    if fila < 3:
                        self.tablero[fila].append(Pieza(fila, columna, BLANCO))
                    elif fila > 4:
                        self.tablero[fila].append(Pieza(fila, columna, ROJO))
                    else:
                        self.tablero[fila].append(0)
                else:
                    self.tablero[fila].append(0)

    def dibujar(self, win):
        self.dibujar_casillas(win)

        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                pieza = self.tablero[fila][columna]
                if pieza != 0:
                    pieza.calcular_posicion()
                    pieza.dibujar(win)


                        