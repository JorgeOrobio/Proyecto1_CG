import pygame as pg
from libreria import*

class Rival(pg.sprite.Sprite):
    """clase rival"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([40,40])
        self.image.fill(rojo)
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.velx=-5
        self.vely=0
        self.tempo=random.randrange(200)

    def update(self):
        # BRASHEO DE RIVALES CONTINUO
        if self.rect.x < 0:
            self.velx= 5
        if self.rect.x > ancho - self.rect.width:
            self.velx= -5
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.tempo -=1
