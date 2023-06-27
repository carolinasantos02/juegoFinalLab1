import pygame
from constantes import *
from funciones import *

class Plataforma:
    def __init__(self, x, y, ancho, alto, tipo):
        self.imagen = pygame.image.load("recursos\\Assets\\pngwing.com.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_base = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, ALTO_RECT_PIES)
        

    def dibujar(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, ROJO, self.rect_base)
        screen.blit(self.imagen, self.rect)



    
    
