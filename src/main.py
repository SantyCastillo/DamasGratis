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


def jugar_contra_bot(dificultad):
    pygame.init()
    reloj = pygame.time.Clock()
    juego = Juego(VENTANA)

    while True:
        reloj.tick(FPS)

        if juego.turno == BLANCO:
            valor, nuevo_tablero = minimax(juego.obt_tablero(), 4, BLANCO, juego, dificultad)
            juego.ai_move(nuevo_tablero)

        ganador = juego.ganador()
        if ganador is not None:
            mensaje = f"Ha ganado {'Rojo' if ganador == ROJO else 'Blanco'}!!"
            print(mensaje)
            mostrar_mensaje(mensaje)
            quit()

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

def jugar_entre_jugadores(mi_socket):
    pygame.init()
    reloj = pygame.time.Clock()
    juego = Juego(VENTANA)

    while True:
        reloj.tick(FPS)

        # Código para recibir el tablero actualizado del otro jugador a través del socket
        try:
            data = mi_socket.recv(4096)
            juego.tablero = pickle.loads(data)
        except:
            pass

        ganador = juego.ganador()
        if ganador is not None:
            mensaje = f"Ha ganado {'Rojo' if ganador == ROJO else 'Blanco'}!!"
            print(mensaje)
            mostrar_mensaje(mensaje)
            quit()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                fila, columna = obt_fila_col_mouse(pos)
                juego.seleccionar(fila, columna)

        # Código para enviar el tablero actualizado al otro jugador a través del socket
        data = pickle.dumps(juego.tablero)
        mi_socket.sendall(data)

        juego.update()

    pygame.quit()

def main():
    menu = Menu()

    while True:
        opcion_menu = menu.mostrar_menu_principal()

        if opcion_menu == "un_jugador":
            dificultad = menu.mostrar_menu_dificultad()
            jugar_contra_bot(dificultad)

        if opcion_menu == "dos_jugadores":
            # Establecer la comunicación por sockets para el modo de dos jugadores
            mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            mi_socket.connect(("localhost", 12346))  # Aquí debes reemplazar "localhost" con la dirección IP del otro jugador

            # Iniciar el juego en hilos separados para poder enviar y recibir movimientos al mismo tiempo
            hilo_juego = Thread(target=jugar_entre_jugadores, args=(mi_socket,))
            hilo_juego.start()

            # Mantener el programa principal en espera para poder manejar eventos
            #hilo_juego.join()

    pygame.quit()

main()


"""
TODO:
    - Agregar dos jugadores
"""