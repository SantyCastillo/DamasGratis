import pygame
from constantes import ROJO, BLANCO
from tablero import Tablero

class Juego:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.tablero.dibujar(self.win)
        pygame.display.update()


    def _init(self):
        self.seleccionado = None
        self.tablero = Tablero()
        self.turno = ROJO
        self.mov_validos = {}

    def seleccionar(self, fila, columna):
        if self.seleccionado:
            resultado = self._mover(fila, columna)
            if not resultado:
                self.seleccionado = None
                self.seleccionado = (fila, columna)
        else:
            pieza = self.tablero.obt_pieza(fila, columna)
            if pieza != 0 and pieza.color == self.turno:
                self.seleccionado = pieza
                self.mov_validos = self.tablero.obt_mov_validos(pieza)
                return True
        
        return False

    def _mover(self, fila, columna):
        pieza = self.tablero.obt_pieza(fila, columna)
        if self.seleccionado and pieza == 0 and (fila, columna) in self.mov_validos:
            self.tablero.movimiento(self.seleccionado, fila, columna)
            self.cambiar_turno()
        else:
            return False
        return True

    def cambiar_turno(self):
        if self.turno == ROJO:
            self.turno = BLANCO
        else:
            self.turno = ROJO

    def reset(self):
        self._init()        
