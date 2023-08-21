import pygame
from constantes import *
from juego import Juego
from bot import *
from menu import *


FPS = 60
dificultad = None
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("DamasGratis")


def mostrar_pantalla_victoria(color_ganador, tablero):
    pygame.init()
    fuente_mensaje = pygame.font.SysFont("comicsans", 50)
    fuente_opciones = pygame.font.SysFont("comicsans", 30)
    
    mensaje = f"Ha ganado el equipo {color_ganador.capitalize()}!"
    texto_mensaje = fuente_mensaje.render(mensaje, True, BLANCO)
    
    opcion_jugar = fuente_opciones.render("Jugar nuevamente", True, BLANCO)
    opcion_salir = fuente_opciones.render("Salir", True, BLANCO)
    
    banner_color = ROJO if color_ganador == "rojo" else AZUL
    banner_rect = pygame.Rect(0, ALTO // 3, ANCHO, ALTO // 3)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if ALTO // 2 + 20 <= y <= ALTO // 2 + 60 and ANCHO // 2 - opcion_jugar.get_width() // 2 <= x <= ANCHO // 2 + opcion_jugar.get_width() // 2:
                    return "jugar_nuevamente"
                elif ALTO // 2 + 60 <= y <= ALTO // 2 + 90 and ANCHO // 2 - opcion_salir.get_width() // 2 <= x <= ANCHO // 2 + opcion_salir.get_width() // 2:
                    return "volver_al_menu"

        tablero.dibujar(VENTANA)

        pygame.draw.rect(VENTANA, banner_color, banner_rect)
        
        VENTANA.blit(texto_mensaje, (ANCHO // 2 - texto_mensaje.get_width() // 2, ALTO // 2 - texto_mensaje.get_height()))
        
        VENTANA.blit(opcion_jugar, (ANCHO // 2 - opcion_jugar.get_width() // 2, ALTO // 2 + 20))
        VENTANA.blit(opcion_salir, (ANCHO // 2 - opcion_salir.get_width() // 2, ALTO // 2 + 60))

        pygame.display.update()

def obt_fila_col_mouse(pos):
    x, y = pos
    fila = y // TAMANIO_CUADRADO
    columna = x // TAMANIO_CUADRADO
    return fila, columna

def jugar_contra_bot(dificultad):
    pygame.init()
    reloj = pygame.time.Clock()
    juego = Juego(VENTANA)

    while True:
        reloj.tick(FPS)

        if juego.turno == AZUL:
            if dificultad == 1:
                profundidad = 4  
            elif dificultad == 0.5:
                profundidad = 3
            else:
                profundidad = 2

            valor, nuevo_tablero = minimax(juego.obt_tablero(), profundidad, AZUL, juego, dificultad)
            if nuevo_tablero is None:
                ganador = ROJO if juego.turno == AZUL else AZUL
                mostrar_pantalla_victoria("rojo" if ganador == ROJO else "azul", juego.obt_tablero())
                return

            juego.ai_move(nuevo_tablero)

        ganador = juego.ganador()
        if ganador is not None:
            color_ganador = "rojo" if ganador == ROJO else "azul"
            opcion_elegida = mostrar_pantalla_victoria(color_ganador, juego.obt_tablero())
            if opcion_elegida == "jugar_nuevamente":
                juego.reset()
                juego = Juego(VENTANA)
            elif opcion_elegida == "volver_al_menu":
                return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fila, columna = obt_fila_col_mouse(pos)
                juego.seleccionar(fila, columna)

        juego.update()

def main():
    menu = Menu()

    while True:
        opcion_menu = menu.mostrar_menu_principal()

        if opcion_menu == "un_jugador":
            dificultad = menu.mostrar_menu_dificultad()
            jugar_contra_bot(dificultad)

    pygame.quit()

main()