import pygame as pg
from libreria import*


class Spawn(pg.sprite.Sprite):

    def __init__(self,pto):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([70,70])
        self.image.fill(azul)
        self.rect =self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
