import pygame as pg
from libreria import*

class Mothership_E(pg.sprite.Sprite):
    """clase mothership"""
    def __init__(self,archivo):
        pg.sprite.Sprite.__init__(self)
        self.image=archivo
        self.rect=self.image.get_rect()
        self.rect.x=ancho
        self.rect.y= -200
        self.disparo=self.rect.midtop
        self.velx= -2
        self.vely=0

    def update(self):
        # LIMITES DE PANTALLA PERSONAJE
        if self.rect.x < (ancho-300 ):
            self.rect.x = ancho-300
            self.velx=0
        self.rect.x+=self.velx
