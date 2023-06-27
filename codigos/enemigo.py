import pygame
from constantes import *
from jugador import *
from funciones import *

class Enemigo:
    def __init__(self, rectx, recty, x, y, velocidad, gravedad, frame_rate_ms):
        self.caminar_d = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\bosses\\bundle_of_joy\\camianrDe.png", 9, 1)
        self.caminar_i = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\bosses\\bundle_of_joy\\caminarIz.png", 8, 1)
        self.girar = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\bosses\\bundle_of_joy\\girar.png", 7, 1)

        self.frame = 0
        self.vidas = 3
        self.move_x = x
        self.move_y = y
        self.velocidad_caminata = velocidad
        self.gravedad = gravedad
        self.frame_rate_ms = frame_rate_ms #cada cuantos ms queremos cambiar la animacion
        self.orientacion = DERECHA
        self.contador_pasos = 0
        self.caminata_limite = 100
        self.tiempo_transcurrido = 0
        
        self.animacion = self.girar
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = rectx
        self.rect.y = recty


    def caminar(self):
        if self.orientacion == DERECHA:
            self.frame = 0
            self.move_x = self.velocidad_caminata
            self.animacion = self.caminar_d
        elif self.orientacion == IZQUIERDA:
            self.frame = 0
            self.move_x = -self.velocidad_caminata
            self.animacion = self.caminar_i

        self.rect.x += self.move_x  # ACTUALIZAR POSICION
        self.contador_pasos += abs(self.move_x)  # ACTUALIZAR PASOS ABS = VALOR ABSOLUTO
        if self.contador_pasos >= self.caminata_limite:
            self.contador_pasos = 0
            if self.orientacion == DERECHA:
                self.orientacion = IZQUIERDA
            else:
                self.orientacion = DERECHA


    def actualizar(self, delta_ms):
        #permite modificar los FPS que permita la computadora sin que eso haga mas lento o mas rapido el juego, mientras mas fps solo es mas fluido
        #dejo de actualizar en el loop principal
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido >= self.frame_rate_ms:
            # if (self.inicio_de_salto - self.rect.y) > self.altura_maxima_salto and self.esta_saltando:
            #     self.move_y = 0

            self.tiempo_transcurrido = 0
            if (self.frame < len(self.animacion) -1):
                self.frame += 1

            self.caminar()

                
    def dibujar(self, screen):
        if DEBUG: 
            pygame.draw.rect(screen, AZUL, self.rect)

        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen, self.rect)