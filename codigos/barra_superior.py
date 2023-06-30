import sys
import pygame
from constantes import *
from jugador import Personaje
import pygame.font


class Barra:
    def __init__(self, personaje):
        # self.contando = False
        self.superficie = pygame.image.load("recursos\\Assets\\barra superior.png")
        self.superficie = pygame.transform.scale(self.superficie, (ANCHO_VENTANA, self.superficie.get_height()))
        self.texto = "Vidas: {}".format(personaje.vidas)
        self.fuente = pygame.font.Font(None, 40)
        self.texto_superficie = self.fuente.render(self.texto, True, (255, 255, 255))
        self.tiempo_inicial = pygame.time.get_ticks() // 1000
        self.tiempo_restante = 31

    def actualizar(self, personaje):
        # if self.contando == True:
            tiempo_actual = pygame.time.get_ticks() // 1000
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
            self.tiempo_restante = max(31 - tiempo_transcurrido, 0)
            self.texto_superficie = self.fuente.render("Vidas: {0}     Tiempo: {1}".format(personaje.vidas, personaje.cronometro), True, (255, 255, 255))

    def dibujar(self, screen):
        screen.blit(self.superficie, [0, 0]) 
        screen.blit(self.texto_superficie, [10, 10])