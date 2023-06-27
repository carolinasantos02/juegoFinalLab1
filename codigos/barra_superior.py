import sys
import pygame
from constantes import *
from jugador import Personaje
import pygame.font


class Barra:
    def __init__(self, personaje):
        self.superficie = pygame.image.load("recursos\\Assets\\barra superior.png")
        self.superficie = pygame.transform.scale(self.superficie, (ANCHO_VENTANA, self.superficie.get_height()))
        self.texto = "Vidas: {}".format(personaje.vidas)
        self.fuente = pygame.font.Font(None, 40)
        self.texto_superficie = self.fuente.render(self.texto, True, (255, 255, 255))

    def actualizar(self, personaje):
         self.texto_superficie = self.fuente.render("Vidas: {}".format(personaje.vidas), True, (255, 255, 255))

    def dibujar(self, screen):
            screen.blit(self.superficie, [0, 0]) 
            screen.blit(self.texto_superficie, [10, 10])