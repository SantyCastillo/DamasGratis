import pygame
from constantes import ANCHO, ALTO, AZUL, BLANCO, NEGRO

class Menu:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("DamasGratis")
        self.reloj = pygame.time.Clock()


    def mostrar_menu_principal(self):
        fuente = pygame.font.SysFont("comicsans", 50)
        texto_un_jugador = fuente.render("Un jugador", True, BLANCO)
        texto_dos_jugadores = fuente.render("Dos jugadores", True, BLANCO)
        texto_salir = fuente.render("Salir", True, BLANCO)

        while True:
            self.ventana.fill(NEGRO)
            self.ventana.blit(texto_un_jugador, (ANCHO // 2 - texto_un_jugador.get_width() // 2, 200))
            self.ventana.blit(texto_dos_jugadores, (ANCHO // 2 - texto_dos_jugadores.get_width() // 2, 300))
            self.ventana.blit(texto_salir, (ANCHO // 2 - texto_salir.get_width() // 2, 400))
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 200 <= y <= 250:
                        return "un_jugador"
                    elif 300 <= y <= 350:
                        return "dos_jugadores"
                    elif 300 <= y <= 450:
                        pygame.quit()
                        quit()


    def mostrar_menu_dificultad(self):
        fuente = pygame.font.SysFont("comicsans", 50)
        texto_facil = fuente.render("Facil", True, BLANCO)
        texto_medio = fuente.render("Medio", True, BLANCO)
        texto_dificil = fuente.render("Dificil", True, BLANCO)

        while True:
            self.ventana.fill(NEGRO)
            self.ventana.blit(texto_facil, (ANCHO // 2 - texto_facil.get_width() // 2, 200))
            self.ventana.blit(texto_medio, (ANCHO // 2 - texto_medio.get_width() // 2, 300))
            self.ventana.blit(texto_dificil, (ANCHO // 2 - texto_dificil.get_width() // 2, 400))
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 200 <= y <= 250:
                        return 1  # Dificultad: Facil
                    elif 300 <= y <= 350:
                        return 0.5  # Dificultad: Medio
                    elif 400 <= y <= 450:
                        return 0.1  # Dificultad: Dificil
