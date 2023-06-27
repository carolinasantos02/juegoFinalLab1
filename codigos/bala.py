import pygame
import time
from constantes import *
from jugador import *
from funciones import *
from enemigo import *

class Bala:
    def __init__(self, x, y, personaje, velocidad, frame_rate_ms):
        self.frame = 0
        self.superficie_d = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\weapons\\bala.png", 1, 1)
        self.superficie_i = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\weapons\\bala.png", 1, 1, True)
        self.velocidad = velocidad
        self.orientacion = DERECHA
        self.animacion = self.superficie_d
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.frame_rate_ms = frame_rate_ms #cada cuantos ms queremos cambiar la animacion
        self.tiempo_transcurrido = 0
        self.rect.center = (x, y)
        self.ultima_bala_disparada = 0
        self.tiempo_entre_balas = 0.5

    def actualizar(self, personaje, lista_e):
        self.rect.centery = personaje.rect.centery + 13
        if self.orientacion == DERECHA:
            self.rect.x += self.velocidad
        else:
            self.rect.x -= self.velocidad
        if self.colisiono_con_enemigo(lista_e):
                for enemigo in lista_e:
                    lista_e.remove(enemigo)

    def colisiono_con_enemigo(self, lista):
        for enemigo in lista:
            if self.rect.colliderect(enemigo):
                return True
            else:
                return False

    def dibujar(self, screen, personaje):
        if personaje.animacion == personaje.disparando_d or personaje.animacion == personaje.disparando_i:
            self.imagen = self.animacion[self.frame]
            screen.blit(self.imagen, self.rect)