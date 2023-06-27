import pygame
from constantes import *


class Funciones:

    def obtener_superficie_del_sprite(path,columnas,filas,flip=False, step = 1):
        lista = []
        superficie_imagen = pygame.image.load(path)
        fotograma_ancho = int(superficie_imagen.get_width()/columnas)
        fotograma_alto = int(superficie_imagen.get_height()/filas)
        x = 0
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(flip):
                    superficie_fotograma = pygame.transform.flip(superficie_fotograma,True,False)
                lista.append(superficie_fotograma)
        return lista