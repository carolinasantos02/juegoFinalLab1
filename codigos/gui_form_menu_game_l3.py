import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from barra_superior import Barra
from jugador import *
from enemigo import *
from plataforma import *
from background import *
from bala import *
from frutas import *

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        # self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.sonido_active = True
        self.boton_pause = Button(master=self,x=400,y=10,w=100,h=30,color_background=None,color_border=None,image_background="recursos\\but pause.png",on_click=self.on_click_boton1,on_click_param="form_menu_B_3",text="",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_sound_off = Button(master=self,x=600,y=10,w=100,h=30,color_background=None,color_border=None,image_background="recursos\\but sonido off.png",on_click=self.on_click_boton2,on_click_param="",text="",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_sound_on = Button(master=self,x=800,y=10,w=100,h=30,color_background=None,color_border=None,image_background="recursos\\but sonido on.png",on_click=self.on_click_boton3,on_click_param="",text="",font="Verdana",font_size=30,font_color=C_WHITE)
    
        # self.pb_lives = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton_pause, self.boton_sound_off, self.boton_sound_on]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="recursos\\Assets\\locations\\set_bg_01\\mountain\\all.png")
        self.tiempo_actual = time.time()

        self.player_1 = Personaje(0, 600, 0, 0, 6, 8, 16, 25)
        self.barra_superior = Barra(self.player_1)
        self.enemy_list = []
        self.enemy_list.append (Enemigo(500, 650, 0, 0, 2, 8, 25))

        self.frutas_list = []

        self.plataform_list = []
        self.plataform_list.append(Plataforma(700, 500, 80, 80, 1))
        self.plataform_list.append(Plataforma(900, 250, 80, 80, 1))


        self.frutas_list.append(Fruta(905, 200))

        self.bullet_list = []



    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        self.sonido_active = False
        print(self.sonido_active)

    def on_click_boton3(self, parametro):
        self.sonido_active = True
        print(self.sonido_active)

        

    def update(self, lista_eventos,keys,delta_ms,evento_1000ms):
        if self.sonido_active:
            SONIDO_BACKGROUND.play()
        else:
            SONIDO_BACKGROUND.stop()
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        self.barra_superior.actualizar(self.player_1)

        for event in lista_eventos:
            if event.type == evento_1000ms:
                self.player_1.cronometro -= 1

        for bullet_element in self.bullet_list:
            bullet_element.actualizar(self.player_1, self.enemy_list)

        for enemy_element in self.enemy_list:
            enemy_element.actualizar(delta_ms)


        self.player_1.botones_presionados(keys, self.bullet_list)
        self.player_1.actualizar(delta_ms,self.plataform_list, self.enemy_list, self.frutas_list)


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        self.barra_superior.dibujar(self.surface)

        for plataforma in self.plataform_list:
            plataforma.dibujar(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for enemy_element in self.enemy_list:
            enemy_element.dibujar(self.surface)
        
        self.player_1.dibujar(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.dibujar(self.surface, self.player_1)
            if self.tiempo_actual - bullet_element.ultima_bala_disparada > bullet_element.tiempo_entre_balas:
                bullet_element.ultima_bala_disparada = self.tiempo_actual
            if bullet_element.rect.x > ANCHO_VENTANA or bullet_element.rect.x < 0:
                self.bullet_list.remove(bullet_element)
        
        for fruta in self.frutas_list:
            fruta.dibujar(self.surface)
        
        if len(self.frutas_list) == 0 and len(self.enemy_list) == 0:
            if self.sonido_active:
                SONIDO_BACKGROUND.stop()
                SONIDO_WIN.play()
            Form.set_active("form_menu_game_over")
            self.frutas_list.append(Fruta(905, 200))
            self.enemy_list.append (Enemigo(500, 650, 0, 0, 2, 8, 25))
            self.player_1 = Personaje(0, 600, 0, 0, 6, 8, 16, 25)

        if self.player_1.vidas == 0 or self.barra_superior.tiempo_restante == 0:
            if len(self.frutas_list) == 0:
                self.frutas_list.append(Fruta(905, 200))
            if self.sonido_active:
                SONIDO_BACKGROUND.stop()
                SONIDO_LOSE.play()
            Form.set_active("form_menu_ganador")
            self.barra_superior.tiempo_restante = 30
            self.player_1 = Personaje(0, 600, 0, 0, 6, 8, 16, 25)
            self.barra_superior.tiempo_inicial = pygame.time.get_ticks() // 1000
            self.barra_superior.tiempo_restante = 31