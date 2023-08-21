import pygame
from constantes import ANCHO, ALTO, AZUL, BLANCO, NEGRO, FONDO, COLOR_RESALTADO, COLOR_NORMAL, ROJO

class Menu:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("DamasGratis")
        self.reloj = pygame.time.Clock()
        self.fondo = FONDO
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))
        
    def mostrar_menu_principal(self):
        fuente_titulo = pygame.font.SysFont("comicsans", 80, bold=True)
        titulo_azul = fuente_titulo.render("DAMAS", True, AZUL)
        titulo_rojo = fuente_titulo.render("GRATIS", True, ROJO)
        fuente_opciones = pygame.font.SysFont("comicsans", 50)

        mouse_sobre_un_jugador = False
        mouse_sobre_salir = False
    
        while True:
            self.ventana.fill(NEGRO)
            self.ventana.blit(self.fondo, (0, 0))
            
            self.ventana.blit(titulo_azul, (ANCHO // 2 - titulo_azul.get_width() // 2 - 30, 100))
            self.ventana.blit(titulo_rojo, (ANCHO // 2 - titulo_rojo.get_width() // 2 + 30, 180))  # Ajusta la coordenada Y            
            
            texto_un_jugador_rendered = fuente_opciones.render("Un jugador", True, COLOR_RESALTADO if mouse_sobre_un_jugador else COLOR_NORMAL)
            texto_salir_rendered = fuente_opciones.render("Salir", True, COLOR_RESALTADO if mouse_sobre_salir else COLOR_NORMAL)
            
            # Ajusta las coordenadas Y para mover las opciones más abajo
            self.ventana.blit(texto_un_jugador_rendered, (ANCHO // 2 - texto_un_jugador_rendered.get_width() // 2, 550))
            self.ventana.blit(texto_salir_rendered, (ANCHO // 2 - texto_salir_rendered.get_width() // 2, 650))
            
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    mouse_sobre_un_jugador = 550 <= y <= 600
                    mouse_sobre_salir = 650 <= y <= 700

                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 550 <= y <= 600:
                        return "un_jugador"
                    elif 650 <= y <= 700:
                        pygame.quit()
                        quit()

                
                


    def mostrar_menu_dificultad(self):
        fuente = pygame.font.SysFont("comicsans", 50)
        texto_facil = fuente.render("Facil", True, COLOR_NORMAL)
        texto_medio = fuente.render("Medio", True, COLOR_NORMAL)
        texto_dificil = fuente.render("Dificil", True, COLOR_NORMAL)
        
        mouse_sobre_facil = False
        mouse_sobre_medio = False
        mouse_sobre_dificil = False

        while True:
            self.ventana.fill(NEGRO)
            self.ventana.blit(self.fondo, (0, 0))
            
            if mouse_sobre_facil:
                texto_facil = fuente.render("Facil", True, COLOR_RESALTADO)
            else:
                texto_facil = fuente.render("Facil", True, COLOR_NORMAL)
            
            if mouse_sobre_medio:
                texto_medio = fuente.render("Medio", True, COLOR_RESALTADO)
            else:
                texto_medio = fuente.render("Medio", True, COLOR_NORMAL)
            
            if mouse_sobre_dificil:
                texto_dificil = fuente.render("Dificil", True, COLOR_RESALTADO)
            else:
                texto_dificil = fuente.render("Dificil", True, COLOR_NORMAL)
            
            self.ventana.blit(texto_facil, (ANCHO // 4 - texto_facil.get_width() // 2, 600))
            self.ventana.blit(texto_medio, (ANCHO // 2 - texto_medio.get_width() // 2, 600))
            self.ventana.blit(texto_dificil, (3 * ANCHO // 4 - texto_dificil.get_width() // 2, 600))
            
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    mouse_sobre_facil = (ANCHO // 4 - texto_facil.get_width() // 2) <= x <= (ANCHO // 4 + texto_facil.get_width() // 2) and 600 <= y <= 650
                    mouse_sobre_medio = (ANCHO // 2 - texto_medio.get_width() // 2) <= x <= (ANCHO // 2 + texto_medio.get_width() // 2) and 600 <= y <= 650
                    mouse_sobre_dificil = (3 * ANCHO // 4 - texto_dificil.get_width() // 2) <= x <= (3 * ANCHO // 4 + texto_dificil.get_width() // 2) and 600 <= y <= 650

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if (ANCHO // 4 - texto_facil.get_width() // 2) <= x <= (ANCHO // 4 + texto_facil.get_width() // 2) and 600 <= y <= 650:
                        return 1  
                    elif (ANCHO // 2 - texto_medio.get_width() // 2) <= x <= (ANCHO // 2 + texto_medio.get_width() // 2) and 600 <= y <= 650:
                        return 0.5
                    elif (3 * ANCHO // 4 - texto_dificil.get_width() // 2) <= x <= (3 * ANCHO // 4 + texto_dificil.get_width() // 2) and 600 <= y <= 650:
                        return 0 