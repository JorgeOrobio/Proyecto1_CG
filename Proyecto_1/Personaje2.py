import pygame as pg
from libreria import*

class Jugador(pg.sprite.Sprite):
    """clase jugador"""
    def __init__(self,archivo,archivo2):
        pg.sprite.Sprite.__init__(self)
        self.fila=2
        self.col=0
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        ##Explosion
        self.fila2=0
        self.col2=0
        self.matriz2=archivo2
        self.image2 = self.matriz2[self.col2][self.fila2]
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y=centro_y
        self.disparo=self.rect.midtop
        self.velx=0
        self.vely=0
        self.vidas = 3

    def update(self):
        # ANIMACION DE PERSONAJE
        if self.vidas > 0:
            self.image = self.matriz[self.col][self.fila]
            if self.col >=4:
                self.col=0
            else:
                self.col+=1

        #llamado a matriz de la explosion
        if self.vidas <= 0:
            print('entro')
            self.image = self.matriz2[self.col2][self.fila2]
            if self.col2 >=16:
                self.col2=0
            else:
                self.col2+=1

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



    def get_all(self):
        pass
        return self.rect.x,self.rect.y
