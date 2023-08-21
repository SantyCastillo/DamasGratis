import pygame
from constantes import *
from tablero import Tablero
from juego import Juego
from bot import *
from menu import *
from threading import Thread
import socket
import pickle



FPS = 60
dificultad = None
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("DamasGratis")

# ... Código anterior ...

# ... Código anterior ...

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
                if ALTO // 2 + 50 <= y <= ALTO // 2 + 100:
                    return "jugar_nuevamente"
                elif ALTO // 2 + 100 <= y <= ALTO // 2 + 150:
                    return "volver_al_menu"

        # Dibuja el tablero en el fondo
        tablero.dibujar(VENTANA)

        # Dibuja el banner encima del tablero
        pygame.draw.rect(VENTANA, banner_color, banner_rect)
        
        VENTANA.blit(texto_mensaje, (ANCHO // 2 - texto_mensaje.get_width() // 2, ALTO // 2 - texto_mensaje.get_height()))
        
        VENTANA.blit(opcion_jugar, (ANCHO // 2 - opcion_jugar.get_width() // 2, ALTO // 2 + 50))
        VENTANA.blit(opcion_salir, (ANCHO // 2 - opcion_salir.get_width() // 2, ALTO // 2 + 100))

        pygame.display.update()

# ... Resto del código ...








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
            valor, nuevo_tablero = minimax(juego.obt_tablero(), 4, AZUL, juego, dificultad)
            if nuevo_tablero is None:
                ganador = ROJO if juego.turno == AZUL else AZUL
                mensaje = f"Ha ganado {'Rojo' if ganador == ROJO else 'Azul'}!!"
                color_ganador = "rojo" if ganador == ROJO else "azul"
                opcion_elegida = mostrar_pantalla_victoria(color_ganador, juego.obt_tablero())
                if opcion_elegida == "jugar_nuevamente":
                    juego.reset()
                elif opcion_elegida == "volver_al_menu":
                    return

            juego.ai_move(nuevo_tablero)

        ganador = juego.ganador()
        if ganador is not None:
            color_ganador = "rojo" if ganador == ROJO else "azul"
            opcion_elegida = mostrar_pantalla_victoria(color_ganador, juego.obt_tablero())
            if opcion_elegida == "jugar_nuevamente":
                juego.reset()
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


def probar_pantalla_victoria():
    pygame.init()
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()

    while True:
        reloj.tick(FPS)

        ganador = "azul"  # Cambia esto a "azul" para probar con el equipo azul
        
        # Aquí deberías tener un objeto "tablero" que represente la partida actual
        tablero = Tablero()
        

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


        
#probar_pantalla_victoria()


def main():
    menu = Menu()

    while True:
        opcion_menu = menu.mostrar_menu_principal()

        if opcion_menu == "un_jugador":
            dificultad = menu.mostrar_menu_dificultad()
            jugar_contra_bot(dificultad)

    pygame.quit()

main()


