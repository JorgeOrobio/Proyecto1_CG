import pygame as pg
from libreria import*

class Skin(pg.sprite.Sprite):
    """clase rival"""
    def __init__(self,archivo,archivo2,pos):
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

        self.rect=self.image.get_rect()
        self.limit = pos[0]
        self.rect.x=pos[0] + 300
        self.rect.y=pos[1]
        self.velx=-5
        self.vely=0
        self.tempo=random.randrange(300)
        self.muerte = 0

    def update(self):
        self.rect.x += self.velx
        self.tempo -=1

        if self.muerte == 0:
            self.image = self.matriz[self.col][self.fila]
            if self.col >=2:
                self.col=0
            else:
                self.col+=1

        if self.muerte == 1:
            self.image = self.matriz2[self.col2][self.fila2]
            if self.col2 >=16:
                self.col2=0
            else:
                self.col2+=1
