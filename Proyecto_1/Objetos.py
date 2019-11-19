import pygame as pg
from libreria import*


class Bloque(pg.sprite.Sprite):
    """clase bloque"""
    def __init__(self,imagen,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=-4
        self.error=10
        # self.grito_arc="/home/jorge/Escritorio/CGrafica/Music/Wilhelm_Scream.ogg"
        # self.grito = pg.mixer.Sound(self.grito_arc)
    def update(self):
        self.rect.x+=self.velx


class Torre(pg.sprite.Sprite):
    """clase torre"""
    def __init__(self,pos,cl=azul):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface([40,40])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False
    def update(self):
        if self.click:
            self.rect.center = pg.mouse.get_pos()


class Cuadro(pg.sprite.Sprite):
    """clase cuadro"""
    def __init__(self,pos,cl=verde):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface([40,40])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False
        self.velx=0
        self.vely=0
    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        if self.click:
            self.rect.center = pg.mouse.get_pos()

class Region(pg.sprite.Sprite):
    """clase Region"""
    def __init__(self,pos,cl=blanco):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface([100,100])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False
    # def update(self):
    #     if self.click:
    #         self.rect.center = pg.mouse.get_pos()

class Linea(pg.sprite.Sprite):
    """clase Linea"""
    def __init__(self,pos,c=[5,200]):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.Surface(c)
        self.image.fill(negro)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.click=False
        self.velx=0
        self.vely=0
        self.h=False
        self.v=False

    def update(self):
        if self.h:
            self.velx=0
            self.vely=5
        else:
            self.velx=-5
            self.vely=0
