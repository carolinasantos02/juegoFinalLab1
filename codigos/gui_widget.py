import pygame
from gui_form import *
from pygame.locals import *

class Widget(Form):
    def __init__(self, master_superficie, x, y, ancho, alto, color_fondo, color_borde, active):
        super().__init__(self, master_superficie, x, y, ancho, alto, color_fondo, color_borde, active)
        self.master_superficie = master_superficie
        self.slave_superficie = pygame.Surface((10,10))
        self.slave_superficie_rect = self.slave_superficie.get_rect()
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color_fondo = color_fondo
        self.color_borde = color_borde
        self.active = active
    
    def render(self):
        pass

    def actualizar(self):
        pass

    def dibujar(self):
        self.master_superficie.blit(self.slave_superficie, self.slave_superficie_rect)
