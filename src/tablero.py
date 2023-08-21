import pygame
from constantes import *
from pieza import Pieza

class Tablero:
    def __init__(self):
        self.tablero = []
        self.piezas_rojas = self.blancas = 12
        self.rey_roja = self.rey_blanca = 0
        self.crear_tablero()

    def dibujar_casillas(self, win):
        win.fill(NEGRO)
        
        for fila in range(FILAS):
            for columna in range(fila % 2, COLUMNAS, 2):
                pygame.draw.rect(win, BLANCO, (fila * TAMANIO_CUADRADO, columna * TAMANIO_CUADRADO, TAMANIO_CUADRADO, TAMANIO_CUADRADO))

    def evaluar(self):
        return self.blancas - self.piezas_rojas + (self.rey_blanca * 0.5 - self.rey_roja * 0.5)

    def obt_todas_piezas(self, color):
        piezas = []
        for fila in self.tablero:
            for pieza in fila:
                if pieza != 0 and pieza.color == color:
                    piezas.append(pieza)
        return piezas

    def mover(self, pieza, fila, columna):
        self.tablero[pieza.fila][pieza.columna], self.tablero[fila][columna] = self.tablero[fila][columna], self.tablero[pieza.fila][pieza.columna]
        pieza.mover(fila, columna)

        if fila == FILAS - 1 or fila == 0:
            pieza.crear_rey()
            if pieza.color == AZUL:
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
                        self.tablero[fila].append(Pieza(fila, columna, AZUL))
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
                    pieza.dibujar(win)

    
    def eliminar(self, piezas):
        for pieza in piezas:
            self.tablero[pieza.fila][pieza.columna] = 0
            if pieza != 0:
                if pieza.color == ROJO:
                    self.piezas_rojas -= 1
                else:
                    self.blancas -= 1

    def ganador(self):
        if self.piezas_rojas <= 0 or not self.obt_todas_piezas(ROJO):
            return AZUL
        elif self.blancas <= 0 or not self.obt_todas_piezas(AZUL):
            return ROJO

        return None


    def obt_mov_validos(self, pieza):
        movimientos = {}
        izq = pieza.columna - 1
        der = pieza.columna + 1
        fila = pieza.fila
        
        if pieza.color == ROJO or pieza.rey:
            movimientos.update(self._diagonal_izquierda(fila -1, max(fila-3, -1), -1, pieza.color, izq))
            movimientos.update(self._diagonal_derecha(fila -1, max(fila-3, -1), -1, pieza.color, der))

        if pieza.color == AZUL or pieza.rey:
            movimientos.update(self._diagonal_izquierda(fila +1, min(fila+3, FILAS), 1, pieza.color, izq))
            movimientos.update(self._diagonal_derecha(fila +1, min(fila+3, FILAS), 1, pieza.color, der))
    
        return movimientos
    def _diagonal_izquierda(self, empezar, final, paso, color, izquierda, skipped=[]):
        movimientos = {}
        ultimo = []
        for r in range(empezar, final, paso):
            if izquierda < 0:
                break

            actual = self.tablero[r][izquierda]
            if actual == 0:
                if skipped and not ultimo:
                    break
                elif skipped:
                    movimientos[(r, izquierda)] = ultimo + skipped
                else:
                    movimientos[(r, izquierda)] = ultimo

                if ultimo:
                    if paso == -1:
                        fila = max(r-3, 0)
                    else:
                        fila = min(r+3, FILAS)
                    movimientos.update(self._diagonal_izquierda(r+paso, fila, paso, color, izquierda-1, skipped=ultimo))
                    movimientos.update(self._diagonal_derecha(r+paso, fila, paso, color, izquierda+1, skipped=ultimo))
                break
            elif actual.color == color:
                break
            else:
                ultimo = [actual]
            

            izquierda -= 1

        return movimientos

    
    def _diagonal_derecha(self, empezar, final, paso, color, derecha, skipped=[]):
        movimientos = {}
        ultimo = []
        for r in range(empezar, final, paso):
            if derecha >= COLUMNAS:
                break
            
            actual = self.tablero[r][derecha]
            if actual == 0:
                if skipped and not ultimo:
                    break
                elif skipped:
                    movimientos[(r,derecha)] = ultimo + skipped
                else:
                    movimientos[(r, derecha)] = ultimo
                
                if ultimo:
                    if paso == -1:
                        fila = max(r-3, 0)
                    else:
                        fila = min(r+3, FILAS)
                    movimientos.update(self._diagonal_izquierda(r+paso, fila, paso, color, derecha-1,skipped=ultimo))
                    movimientos.update(self._diagonal_derecha(r+paso, fila, paso, color, derecha+1,skipped=ultimo))
                break
            elif actual.color == color:
                break
            else:
                ultimo = [actual]

            derecha += 1
        
        return movimientos