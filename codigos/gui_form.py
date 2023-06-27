import pygame
from constantes import *
from pygame.locals import *
from gui_widget import *
from button import Boton

class Form():
    def __init__(self, master_superficie, x, y, ancho, alto, color_fondo, color_borde, active):
        self.master_superficie = master_superficie
        self.slave_superficie = pygame.Surface((ancho, alto))
        self.slave_superficie_rect = self.slave_superficie.get_rect()
        self.slave_superficie_rect.x = x
        self.slave_superficie_rect.y = y
        self.active = active
        


    def render(self):
        pass
        

    def actualizar(self, eventos):
        pass

class FormMenu(Form):
    def __init__(self, master_superficie, x, y, ancho, alto, color_fondo, color_borde, active):
        super().__init__(master_superficie, x, y, ancho, alto, color_fondo, color_borde, active)
        self.lista_botones = []
        self.boton1 = Boton(self.slave_superficie, 100, 50, 50, 200, ROJO, AZUL, self.on_click_boton, "123", "MENU", "Verdana", 15, AZUL)
        self.lista_botones.append(self.boton1)

    def on_click_boton(self, param):
        print("on", param)

    def update(self, eventos):
        super().actualizar(eventos)
        for boton in self.lista_botones:
            boton.actualizar(eventos)
            boton.dibujar()
    
    def dibujar(self):
        super().dibujar()
        for boton in self.lista_botones:
            boton.dibujar()
