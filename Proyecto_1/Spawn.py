import pygame as pg
from libreria import*

class Spawn(pg.sprite.Sprite):

    def __init__(self,pto,archivo):
        pg.sprite.Sprite.__init__(self)
        self.fila=0
        self.col=0
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        self.rect =self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.tempo=random.randrange(600)

    def update(self):
        # ANIMACION DE PERSONAJE
        self.image = self.matriz[self.col][self.fila]
        self.tempo -= 1
        if self.col >=2:
            self.col=0
        else:
            self.col+=1
