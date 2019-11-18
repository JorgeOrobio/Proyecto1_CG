import pygame as pg
from libreria import*

class Rival(pg.sprite.Sprite):
    """clase rival"""
    def __init__(self,archivo,pos):
        pg.sprite.Sprite.__init__(self)
        self.fila=0
        self.col=0
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        print(pos[1])
        self.rect.y=pos[1]
        self.velx=-5
        self.vely=0
        self.tempo=random.randrange(100)

    def update(self):
        self.rect.x += self.velx
        self.tempo -=1
        self.image = self.matriz[self.col][self.fila]
        if self.col >=6:
            self.col=0
        else:
            self.col+=1
