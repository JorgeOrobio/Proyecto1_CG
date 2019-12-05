import pygame as pg
from libreria import*

class Slow(pg.sprite.Sprite):
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
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=-3
        self.vely=0
        self.masvida = True
        self.muerte = 0

    def update(self):
        self.rect.x += self.velx
        if self.muerte == 0:
            self.image = self.matriz[self.col][self.fila]
            if self.col >=1:
                self.col=0
            else:
                self.col+=1

        if self.muerte == 1:
            self.image = self.matriz2[self.col2][self.fila2]
            if self.col2 >=13:
                self.col2=0
            else:
                self.col2+=1
