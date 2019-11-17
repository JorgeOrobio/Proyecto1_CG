import pygame as pg
from libreria import*

class Bala(pg.sprite.Sprite):
    """clase bala"""
    def __init__(self,pos,archivo,columna = 0):
        pg.sprite.Sprite.__init__(self)
        self.fila=0
        self.col=columna
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x += self.velx
        self.rect.y +=self.vely
