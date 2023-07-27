from copy import deepcopy
import random
from constantes import *
ROJO = (255,0,0)
BLANCO = (255, 255, 255)

def minimax(posicion, prof, max_jugador, juego, dificultad=None):
    if prof == 0 or posicion.ganador() != None:
        return posicion.evaluar(), posicion
    
    if max_jugador:
        maxEval = float('-inf')
        mejor_mov = None
        for mov in obt_todos_mov(posicion, BLANCO, juego):
            evaluacion = minimax(mov, prof-1, False, juego, dificultad)[0]
            maxEval = max(maxEval, evaluacion)
            if maxEval == evaluacion:
                mejor_mov = mov

        
        if random.random() < dificultad:  
            mejor_mov = random.choice(list(obt_todos_mov(posicion, BLANCO, juego)))

        return maxEval, mejor_mov
    else:
        minEval = float('inf')
        mejor_mov = None
        for mov in obt_todos_mov(posicion, ROJO, juego):
            evaluation = minimax(mov, prof-1, True, juego, dificultad)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                mejor_mov = mov
        
        return minEval, mejor_mov


def simular_mov(pieza, mov, tablero, juego, skip):
    if not pieza or not tablero or not juego:
        return None

    fila, columna = mov
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        return None

    tablero.mover(pieza, fila, columna)
    if skip:
        tablero.eliminar(skip)

    return tablero



def obt_todos_mov(tablero, color, juego):
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