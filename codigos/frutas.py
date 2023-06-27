import pygame
from constantes import *
from jugador import *
from funciones import *
from enemigo import *

class Fruta:
    def __init__(self, x, y):
        self.frame = 0
        self.superficie = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\food\\carrot\\carrot__x1_1_x1_2_x1_3_x1_4_png_1354829740.png", 4, 1)
        self.animacion = self.superficie
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
    def dibujar(self, screen):
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen, self.rect)