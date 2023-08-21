import pygame
from constantes import ROJO, BLANCO, AZUL, TAMANIO_CUADRADO
from tablero import Tablero

class Juego:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.tablero.dibujar(self.win)
        self.dibujar_mov_validos(self.mov_validos)
        pygame.display.update()


    def _init(self):
        self.seleccionado = None
        self.tablero = Tablero()
        self.turno = ROJO
        self.mov_validos = {}

    def ganador(self):
        return self.tablero.ganador()
    
    def reset(self):
        self._init()

    def seleccionar(self, fila, columna):
        if self.seleccionado:
            resultado = self._mover(fila, columna)
            if not resultado:
                self.seleccionado = None
                self.seleccionar(fila, columna)

        pieza = self.tablero.obt_pieza(fila, columna)
        if pieza != 0 and pieza.color == self.turno:
            self.seleccionado = pieza
            self.mov_validos = self.tablero.obt_mov_validos(pieza)
            return True
        
        return False

    def _mover(self, fila, columna):
        pieza = self.tablero.obt_pieza(fila, columna)
        if self.seleccionado and pieza == 0 and (fila, columna) in self.mov_validos:
            self.tablero.mover(self.seleccionado, fila, columna)
            skipped = self.mov_validos[(fila, columna)]
            if skipped:
                self.tablero.eliminar(skipped)
            self.cambiar_turno()
        else:
            return False
        
        return True
    
    def dibujar_mov_validos(self, movimientos):
        for movimiento in movimientos:
            fila, col = movimiento
            pygame.draw.circle(self.win, AZUL, (col * TAMANIO_CUADRADO + TAMANIO_CUADRADO//2, fila * TAMANIO_CUADRADO + TAMANIO_CUADRADO//2), 15)

    def cambiar_turno(self):
        self.mov_validos = {}
        if self.turno == ROJO:
            self.turno = AZUL
        else:
            self.turno = ROJO     

    def obt_tablero(self):
        return self.tablero

    def ai_move(self, tablero):
        self.tablero = tablero
        self.cambiar_turno()

