import pygame
from constantes import *
from funciones import *
from enemigo import *
import time
from bala import *



class Personaje:
    def __init__(self, rectx, recty, x, y, velocidad_caminata, gravedad, salto, frame_rate_ms):
        self.caminar_d = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\walk.png", 15, 1)
        self.caminar_i = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\walk.png", 15, 1, True)
        self.quieto_d = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\idle.png", 16, 1)
        self.quieto_i = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\idle.png", 16, 1, True)
        self.disparando_d = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\angry weapon solo.png", 1, 1)
        self.disparando_i = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\angry weapon solo.png", 1, 1, True)

        self.salto_d = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\jump.png", 33, 1, False, 1)
        self.salto_i = Funciones.obtener_superficie_del_sprite("recursos\\Assets\\players\\green_hat\\jump.png", 33, 1, True, 1)

        self.frame = 0
        self.vidas = 3
        self.puntos = 0
        self.move_x = x
        self.move_y = y
        self.velocidad_caminata = velocidad_caminata
        self.gravedad = gravedad
        self.salto = salto
        self.orientacion = DERECHA
        self.tiempo_transcurrido = 0
        self.frame_rate_ms = frame_rate_ms #cada cuantos ms queremos cambiar la animacion
        self.ultima_colision_enemigo = 0
        self.tiempo_entre_colisiones_enemigo = 2

        self.animacion = self.quieto_d
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = rectx
        self.rect.y = recty
        self.rect_pies = pygame.Rect((self.rect.x + self.rect.w / 3), (self.rect.y + self.rect.h - ALTO_RECT_PIES), (self.rect.w / 3), ALTO_RECT_PIES)


        self.esta_saltando = False


    def botones_presionados(self, botones, lista_balas):
        if botones[pygame.K_LEFT] and not botones[pygame.K_RIGHT]:
            self.caminar(IZQUIERDA)
        if not botones[pygame.K_LEFT] and botones[pygame.K_RIGHT]:
            self.caminar(DERECHA)
        if not botones[pygame.K_LEFT] and not botones[pygame.K_RIGHT] and not botones[pygame.K_SPACE]:
            self.estar_quieto()
        if botones[pygame.K_LEFT] and botones[pygame.K_RIGHT] and not botones[pygame.K_SPACE]:
            self.estar_quieto()
        if not botones[pygame.K_LEFT] and not botones[pygame.K_RIGHT] and botones[pygame.K_SPACE]:
            self.saltar()
        if not botones[pygame.K_LEFT] and not botones[pygame.K_RIGHT] and not botones[pygame.K_SPACE] and botones[pygame.K_x]:
            self.disparar()
            nueva_bala = Bala(self.rect.centerx, self.rect.centery, self, 10, 25)
            lista_balas.append(nueva_bala)

    def caminar(self, orientacion):
        self.orientacion = orientacion
        if orientacion == DERECHA:
            self.frame = 0
            self.move_x = self.velocidad_caminata
            self.animacion = self.caminar_d
        if orientacion == IZQUIERDA:
            self.move_x = -self.velocidad_caminata
            self.animacion = self.caminar_i

    def disparar(self):
        if self.orientacion == DERECHA:
            self.animacion = self.disparando_d
        if self.orientacion == IZQUIERDA:
            self.animacion = self.disparando_i
        self.move_x = 0
        self.move_y = 0
        self.frame = 0

    def saltar(self):
        if self.esta_saltando == False:

            if self.orientacion == DERECHA:
                self.move_y = -self.salto
                self.animacion = self.salto_d
            else:
                self.move_y = -self.salto
                self.animacion = self.salto_i
            self.frame = 0
            self.esta_saltando = True
            

    def estar_quieto(self):
        if not self.animacion == self.quieto_d and not self.animacion == self.quieto_i:
            if self.orientacion == DERECHA:
                self.animacion = self.quieto_d
            if self.orientacion == IZQUIERDA:
                self.animacion = self.quieto_i
            self.move_x = 0
            self.move_y = 0
            self.frame = 0


    def actualizar(self, delta_ms, lista_p, lista_e, lista_f):
        #permite modificar los FPS que permita la computadora sin que eso haga mas lento o mas rapido el juego, mientras mas fps solo es mas fluido
        #dejo de actualizar en el loop principal
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido >= self.frame_rate_ms:

            self.tiempo_transcurrido = 0
            if (self.frame < len(self.animacion) -1):
                self.frame += 1
            else:
                self.frame = 0
                if self.esta_saltando == True:
                    self.esta_saltando = False
                    self.move_y = 0

            self.mover_rect_juntos_x(self.move_x)
            self.mover_rect_juntos_y(self.move_y)

            if(self.rect.y < 600):
                self.rect.y += self.gravedad
                self.rect_pies.y += self.gravedad 
            if (self.esta_en_plataforma(lista_p)) == False:
                self.mover_rect_juntos_y(self.gravedad)
            
            if self.colisiono_con_enemigo(lista_e) and self.vidas > 0:
                self.vidas -= 1
                if DEBUG:
                    print(self.vidas)
            
            if self.colisiono_con_fruta(lista_f):
                for fruta in lista_f:
                    lista_f.remove(fruta)
                    if self.vidas <= 4:
                        self.vidas += 1
                    elif self.vidas == 5:
                        pass


    def esta_en_plataforma(self, lista):
        retorno = False
        if self.rect.bottom >= 50:
            retorno = True
        for plataforma in lista:
                if self.rect_pies.colliderect(plataforma.rect):
                    self.rect.y = plataforma.rect.y - self.rect.height
                    self.rect_pies.y = self.rect.y + self.rect.height - ALTO_RECT_PIES
                    retorno = True
        return retorno
    
    def colisiono_con_enemigo(self, lista):
        tiempo_actual = time.time()
        for enemigo in lista:
            if self.rect.colliderect(enemigo.rect) and tiempo_actual - self.ultima_colision_enemigo > self.tiempo_entre_colisiones_enemigo:
                self.ultima_colision_enemigo = tiempo_actual
                return True
        return False

    def colisiono_con_fruta(self, lista):
        for fruta in lista:
            if self.rect.colliderect(fruta):
                return True
            else:
                return False

    def mover_rect_juntos_x(self, posicion):
        self.rect.x += posicion
        self.rect_pies.x += posicion

    def mover_rect_juntos_y(self, posicion):
        self.rect.y += posicion
        self.rect_pies.y += posicion

    def dibujar(self, screen):
        if DEBUG: 
            pygame.draw.rect(screen, ROJO, self.rect)
            pygame.draw.rect(screen, AZUL, self.rect_pies)


        try:
            self.imagen = self.animacion[self.frame]
        except IndexError:
            print("IndexError")
        screen.blit(self.imagen, self.rect)
