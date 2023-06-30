import sys
import pygame
import time
from constantes import *
from jugador import Personaje
from plataforma import Plataforma
from enemigo import *
from bala import *
from frutas import *
from barra_superior import *

tiempo_actual = time.time()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()
imagen_fondo = pygame.image.load("recursos\\Assets\\locations\\set_bg_01\\forest\\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
lista_balas = []
lista_enemigos = []
lista_plataformas = []
lista_frutas = []
jugador = Personaje(0, 600, 0, 0, 6, 8, 16, 25)
barra_superior = Barra(jugador)
lista_enemigos.append(Enemigo(400, 450, 0, 0, 2, 8, 25))
lista_frutas.append(Fruta(900, 475))
lista_plataformas.append(Plataforma(200, 500, 80, 80, 1))
lista_plataformas.append(Plataforma(900, 500, 80, 80, 1))
lista_plataformas.append(Plataforma(480, 500, 80, 80, 1))
lista_plataformas.append(Plataforma(400, 500, 80, 80, 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        botones = pygame.key.get_pressed()
        jugador.botones_presionados(botones, lista_balas)

    delta_ms = clock.tick(FPS)

    pantalla.blit(imagen_fondo, imagen_fondo.get_rect())  # Dibujar imagen de fondo primero

    barra_superior.dibujar(pantalla)
    for plataforma in lista_plataformas:
        plataforma.dibujar(pantalla)  # Dibujar las plataformas

    jugador.actualizar(delta_ms, lista_plataformas, lista_enemigos, lista_frutas)
    barra_superior.actualizar(jugador)
    for enemigo in lista_enemigos:
        enemigo.actualizar(delta_ms)
        enemigo.dibujar(pantalla)
    jugador.dibujar(pantalla)  # Dibujar al jugador
    for bala in lista_balas:
        bala.actualizar(jugador, lista_enemigos)
        bala.dibujar(pantalla, jugador)
        if tiempo_actual - bala.ultima_bala_disparada > bala.tiempo_entre_balas:
            bala.ultima_bala_disparada = tiempo_actual
        if bala.rect.x > ANCHO_VENTANA or bala.rect.x < 0:
            lista_balas.remove(bala)
    for fruta in lista_frutas:
        fruta.dibujar(pantalla)

    if len(lista_frutas) == 0 and len(lista_enemigos) == 0:
        imagen_fondo = pygame.image.load("recursos\\Assets\\gameover.png")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        for plataforma in lista_plataformas:
            lista_plataformas.remove(plataforma)
        jugador = Personaje(-100, -100, 0, 0, 6, 8, 16, 25)


    pygame.display.flip()
