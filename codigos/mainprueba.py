import sys
import pygame
import time
from constantes import *
from button import *
from gui_form import *

tiempo_actual = time.time()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

form_menu = FormMenu(pantalla, 100, 100, 400, 400, AZUL, ROJO, True)
form_menu2 = FormMenu(pantalla, 400, 100, 400, 400, ROJO, AZUL, True)

while True:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        botones = pygame.key.get_pressed()
    
    delta_ms = clock.tick(FPS)

    if form_menu.active:
        form_menu.update(lista_eventos)
        form_menu.dibujar()
    if form_menu2.active:
        form_menu2.update(lista_eventos)
        form_menu2.dibujar()

    pygame.display.flip()

