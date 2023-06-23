import pygame
from constantes import *
from tablero import Tablero
FPS = 60

VENTANA = pygame.display.set_mode((ANCHO, ALTO ))
pygame.display.set_caption("DamasGratis")

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
                pass

        tablero.dibujar_casillas(VENTANA)
        pygame.display.update()

    pygame.quit()
    
main()