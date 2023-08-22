import pygame
from constantes import ROJO, AZUL, TAMANIO_CUADRADO, VERDE
from tablero import Tablero


class Juego:
    """
    Clase que representa el juego.
    """

    def __init__(self, win):
        """
        Inicializa una instancia de la clase Juego.
        :param win: Ventana en la que se dibuja.
        """
        self._init()
        self.win = win

    def _init(self):
        self.seleccionado = None
        self.tablero = Tablero()
        self.turno = ROJO
        self.mov_validos = {}

    def ai_move(self, tablero):
        """
        Obtiene el movimiento de la IA.
        :param tablero: Tablero en el que se juega.
        """
        self.tablero = tablero
        self.cambiar_turno()

    def obt_tablero(self):
        """
        Obtiene el tablero.
        :return: Tablero en el que se juega.
        """
        return self.tablero

    def reset(self):
        """
        Reinicia el juego.
        """
        self._init()

    def update(self):
        """
        Actualiza el juego.
        """
        self.tablero.dibujar(self.win)
        self.dibujar_mov_validos(self.mov_validos)
        pygame.display.update()

    def ganador(self):
        """
        Obtiene el ganador del juego.
        :return: Color del ganador o None si no hay ganador.
        """
        return self.tablero.ganador()

    def seleccionar(self, fila, columna):
        """
        Selecciona una pieza en la casilla especificada.
        :param fila: Fila de la casilla.
        :param columna: Columna de la casilla.
        """
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

    def cambiar_turno(self):
        """
        Cambia el turno.
        """
        self.mov_validos = {}
        if self.turno == ROJO:
            self.turno = AZUL
        else:
            self.turno = ROJO

    def _mover(self, fila, columna):
        """
        Mueve la pieza en la casilla especificada.
        :param fila: Fila de la casilla.
        :param columna: Columna de la casilla.
        """
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
        """
        Dibuja los movimientos validos.
        :param movimientos: Movimientos validos.
        """
        for movimiento in movimientos:
            fila, col = movimiento
            pygame.draw.circle(
                self.win,
                VERDE,
                (
                    col * TAMANIO_CUADRADO + TAMANIO_CUADRADO // 2,
                    fila * TAMANIO_CUADRADO + TAMANIO_CUADRADO // 2,
                ),
                15,
            )
