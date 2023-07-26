import pygame
from constantes import *
from tablero import Tablero
from juego import Juego
from bot import *
from menu import *
FPS = 60

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("DamasGratis")

def mostrar_mensaje(mensaje):
    fuente = pygame.font.SysFont("comicsans", 50)
    texto = fuente.render(mensaje, True, AZUL)
    VENTANA.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)


def obt_fila_col_mouse(pos):
    x, y = pos
    fila = y // TAMANIO_CUADRADO
    columna = x // TAMANIO_CUADRADO
    return fila, columna


def jugar_contra_bot():
    pygame.init()
    reloj = pygame.time.Clock()
    juego = Juego(VENTANA)

    while True:
        reloj.tick(FPS)

        if juego.turno == BLANCO:
            valor, nuevo_tablero = minimax(juego.obt_tablero(), 4, BLANCO, juego)
            juego.ai_move(nuevo_tablero)

        ganador = juego.ganador()
        if ganador is not None:
            mensaje = f"Ha ganado {'Rojo' if ganador == ROJO else 'Blanco'}!!"
            print(mensaje)
            juego.mostrar_mensaje(mensaje)
            juego.reset()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fila, columna = obt_fila_col_mouse(pos)
                juego.seleccionar(fila, columna)

        juego.update()

    pygame.quit()

def main():
    menu = Menu()

    while True:
        opcion_menu = menu.mostrar_menu_principal()

        if opcion_menu == "un_jugador":
            jugar_contra_bot()
        
        if opcion_menu == "dos_jugadores":
            pass

    pygame.quit()

main()


"""
TODO:
    - Arreglar ventana ganador
    - Arreglar empate o sin movimientos
    - Agregar dos jugadores
"""