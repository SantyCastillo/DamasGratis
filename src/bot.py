from copy import deepcopy
import pygame
import random
ROJO = (255,0,0)
BLANCO = (255, 255, 255)

def minimax(posicion, prof, max_jugador, juego):
    if prof == 0 or posicion.ganador() != None:
        return posicion.evaluar(), posicion
    
    if max_jugador:
        maxEval = float('-inf')
        mejor_mov = None
        for mov in obt_todos_mov(posicion, BLANCO, juego):
            evaluacion = minimax(mov, prof-1, False, juego)[0]
            maxEval = max(maxEval, evaluacion)
            if maxEval == evaluacion:
                mejor_mov = mov

        
        if random.random() < 0.05:  
            mejor_mov = random.choice(list(obt_todos_mov(posicion, BLANCO, juego)))

        return maxEval, mejor_mov
    else:
        minEval = float('inf')
        mejor_mov = None
        for mov in obt_todos_mov(posicion, ROJO, juego):
            evaluation = minimax(mov, prof-1, True, juego)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                mejor_mov = mov
        
        return minEval, mejor_mov


def simular_mov(pieza, mov, tablero, juego, skip):
    tablero.mover(pieza, mov[0], mov[1])
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
            movimientos.append(nuevo_tablero)
    
    return movimientos