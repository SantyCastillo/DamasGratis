import pygame
from constantes import *
from tablero import Tablero

FPS = 60

VENTANA = pygame.display.set_mode((ANCHO, ALTO ))
pygame.display.set_caption("DamasGratis")

def obt_fila_col_mouse(pos):
    x, y = pos
    fila = y // TAMANIO_CUADRADO
    columna = x // TAMANIO_CUADRADO
    return fila, columna

def main():
    run = True
    reloj = pygame.time.Clock()
    tablero = Tablero()


    while run:
        reloj.tick(FPS)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fila, coluna = obt_fila_col_mouse(pos)
                pieza = tablero.obt_pieza(fila, coluna)
                tablero.movimiento(pieza, 4, 3)

        tablero.dibujar(VENTANA)
        pygame.display.update()

    pygame.quit()
    
main()