from copy import deepcopy
import random
from constantes import *


def minimax(posicion, prof, max_jugador, juego, dificultad=None):
    """
    Algoritmo que se usara para la IA del Bot
    :param posicion: Posicion del tablero actual
    :param prof: Profundidad del algoritmo
    :param max_jugador: Jugador maximo
    :param juego: Juego actual
    :param dificultad: Dificultad del Bot
    """
    if prof == 0 or posicion.ganador() is not None:
        return posicion.evaluar(), posicion

    if max_jugador:
        maxEval = float("-inf")
        mejor_mov = None
        movimientos_posibles = list(obt_todos_mov(posicion, AZUL, juego))

        if not movimientos_posibles:
            return float("-inf"), None

        for mov in movimientos_posibles:
            evaluacion = minimax(mov, prof - 1, AZUL, juego, dificultad)[0]
            if evaluacion > maxEval:
                maxEval = evaluacion
                mejor_mov = mov
        if random.random() < dificultad:
            mejor_mov = random.choice(movimientos_posibles)

        return maxEval, mejor_mov
    else:
        minEval = float("inf")
        mejor_mov = None
        movimientos_posibles = list(obt_todos_mov(posicion, ROJO, juego))

        if not movimientos_posibles:
            return float("inf"), None

        for mov in movimientos_posibles:
            evaluation = minimax(mov, prof - 1, True, juego, dificultad)[0]
            if evaluation < minEval:
                minEval = evaluation
                mejor_mov = mov

        return minEval, mejor_mov


def obt_todos_mov(tablero, color, juego):
    """
    Devuelve todos los movimientos posibles para el Bot
    :param tablero: Tablero actual
    :param color: Color del Bot
    :param juego: Juego actual
    """
    movimientos = []

    for pieza in tablero.obt_todas_piezas(color):
        movimientos_validos = tablero.obt_mov_validos(pieza)
        for mov, skip in movimientos_validos.items():
            temp_tablero = deepcopy(tablero)
            temp_pieza = temp_tablero.obt_pieza(pieza.fila, pieza.columna)
            nuevo_tablero = simular_mov(temp_pieza, mov, temp_tablero, juego, skip)
            if nuevo_tablero is not None:
                movimientos.append(nuevo_tablero)

    return movimientos


def simular_mov(pieza, mov, tablero, juego, skip):
    """
    Simula el movimiento del Bot
    :param pieza: Pieza a mover
    :param mov: Movimiento a realizar
    :param tablero: Tablero actual
    :param juego: Juego actual
    :param skip: Pieza a saltar
    """
    if not pieza or not tablero or not juego:
        return None

    fila, columna = mov
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        return None

    tablero.mover(pieza, fila, columna)
    if skip:
        tablero.eliminar(skip)

    return tablero
