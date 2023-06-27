import pygame
from pygame.locals import *
from gui_widget import Widget

class Boton(Widget):
    def __init__(self, master_superficie, x, y, ancho, alto, color_fondo, color_borde, on_click, on_click_parametros, text, font, font_size, font_color):
        super().__init__(master_superficie, x, y, ancho, alto, color_fondo, color_borde)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_parametros = on_click_parametros
        self.text = text
        self.font_sys = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

    def render(self):
        imagen_texto = self.font_sys.render(self.text, True, self.font_color, self.color_fondo)
        self.slave_superficie = pygame.surface.Surface((self.alto, self.ancho))
        self.slave_superficie_rect = self.slave_superficie.get_rect()
        self.slave_superficie_rect.x = self.x
        self.slave_superficie_rect.y = self.y
        self.slave_superficie.fill(self.color_fondo)
        self.slave_superficie_rect_collide = pygame.Rect(self.slave_superficie_rect)

        self.slave_superficie_rect_collide.x += self.master_superficie.x
        self.slave_superficie_rect_collide.y += self.master_superficie.y

        self.slave_superficie.blit(imagen_texto, (10, 10))
        

    def actualizar(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.slave_superficie_rect_collide.collidepoint(evento.pos):
                    self.on_click(self.on_click_parametros)


        self.render()

