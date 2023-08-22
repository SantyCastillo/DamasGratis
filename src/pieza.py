from constantes import *
import pygame


class Pieza:
    """
    Clase que representa las piezas del juego.
    """

    RELLENO = 15
    CONTORNO = 2

    def __init__(self, fila, columna, color):
        """
        Inicializa una instancia de la clase Pieza
        :param fila: Fila de la pieza
        :param columna: Columna de la pieza
        :param color: Color de la pieza
        """
        self.fila = fila
        self.columna = columna
        self.color = color
        self.rey = False
        self.x = 0
        self.y = 0
        self.calcular_posicion()

    def crear_rey(self):
        """
        Convierte una pieza en Rey
        """
        self.rey = True

    def dibujar(self, win):
        """
        Dibuja las piezas
        :param win: Ventana en la que se dibuja
        """
        radio = TAMANIO_CUADRADO // 2 - self.RELLENO
        pygame.draw.circle(win, BLANCO, (self.x, self.y), radio + self.CONTORNO)
        pygame.draw.circle(win, self.color, (self.x, self.y), radio)
        if self.rey:
            win.blit(
                CORONA,
                (self.x - CORONA.get_width() // 2, self.y - CORONA.get_height() // 2),
            )

    def calcular_posicion(self):
        """
        Calcula la posicion de la pieza
        """
        self.x = TAMANIO_CUADRADO * self.columna + TAMANIO_CUADRADO // 2
        self.y = TAMANIO_CUADRADO * self.fila + TAMANIO_CUADRADO // 2

    def mover(self, fila, columna):
        """
        Mueve la pieza a una posicion
        :param fila: Fila a la que se movera la pieza
        :param columna: Columna a la que se movera la pieza
        """
        self.fila = fila
        self.columna = columna
        self.calcular_posicion()

    def __repr__(self):
        return str(self.color)
