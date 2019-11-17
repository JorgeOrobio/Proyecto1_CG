import pygame as pg
from libreria import*

class Jugador(pg.sprite.Sprite):
    """clase jugador"""
    def __init__(self,archivo):
        pg.sprite.Sprite.__init__(self)
        self.fila=1
        self.col=0
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        self.rect=self.image.get_rect()
        self.rect.x=centro_x
        self.rect.y=centro_y
        self.disparo=self.rect.midtop
        self.velx=0
        self.vely=0
        self.vidas = 10

    def update(self):
        # ANIMACION DE PERSONAJE
        self.image = self.matriz[self.col][self.fila]
        if self.velx != 0 or self.vely !=0:
            if self.col >=4:
                self.col=0
            else:
                self.col+=1

        # LIMITES DE PANTALLA PERSONAJE
        if self.rect.x > (ancho - self.rect.width):
            self.rect.x = ancho - self.rect.width
            self.vely=0
        if self.rect.x < 0:
            self.rect.x=0
            self.vely=0
        if self.rect.y > (alto - self.rect.height):
            self.rect.y = alto - self.rect.height
            self.velx=0
        if self.rect.y < 0:
            self.rect.y=0
            self.velx=0

        self.rect.x+=self.velx
        self.rect.y+=self.vely
        """
        self.image=pg.transform.rotate(self.image,self.vely)
        self.disparo=Rotar_AntiHorario(self.disparo,self.vely)
        # CAMBIAR EL MOD DEL RADIO PARA CORREGIR EL AVANCE DE LA NAVE
        # self.rect.y, self.rect.x= Aumentar_Radio([self.rect.y,self.rect.x],self.velx,self.rect.midright)
        # self.disparo = Aumentar_Radio_Disparo([self.rect.y,self.rect.x],self.velx,self.rect.midright)
        """


    def get_all(self):
        pass
        return self.rect.x,self.rect.y
