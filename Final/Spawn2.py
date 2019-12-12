import pygame as pg
from libreria import*

class Spawn2(pg.sprite.Sprite):

    def __init__(self,pto,archivo,archivo2,limit = 450):
        pg.sprite.Sprite.__init__(self)
        self.fila=0
        self.col=0
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        ##para la explosion
        self.fila2=0
        self.col2=0
        self.matriz2=archivo2
        self.image2= self.matriz2[self.col2][self.fila2]
        self.rect =self.image.get_rect()
        self.limit =  limit
        self.rect.x = pto[0]
        self.rect.y = pto[1] + 300
        self.vely = 5
        self.tempo=random.randrange(300)
        self.tempo2=random.randrange(600)
        self.vidas = 20

    def update(self):
        # ANIMACION DE PERSONAJE
        self.image = self.matriz[self.col][self.fila]
        self.tempo -= 1
        self.tempo2 -= 1
        if self.vidas > 0 :
            if self.col >=1:
                self.col=0
            else:
                self.col+=1
        if self.vidas <0:
            self.image = self.matriz2[self.col2][self.fila2]
            if self.col2 >=13:
                self.col2=0
            else:
                self.col2+=1
        if self.rect.y <= self.limit:
            self.rect.y += self.vely
