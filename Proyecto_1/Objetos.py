import pygame as pg
from libreria import*


class Bloque(pg.sprite.Sprite):
    """clase bloque"""
    def __init__(self,imagen,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = imagen
        self.rect=self.image.get_rect()
        self.pos = pos
        self.rect.x=pos[0]+240
        self.rect.y=pos[1]
        self.velx=-6
        self.error=32
        # self.grito_arc="/home/jorge/Escritorio/CGrafica/Music/Wilhelm_Scream.ogg"
        # self.grito = pg.mixer.Sound(self.grito_arc)
    def update(self):
        self.rect.x+=self.velx

    def OnLimit(self,pos_jugador):
        condition=False
        liminfx=self.rect.center[0] - self.error
        liminfy=self.rect.center[1] + self.error
        liminf = [liminfx,liminfy]
        limsupx=self.rect.center[0] + self.error
        limsupy=self.rect.center[1] - self.error
        limsup = [limsupx,limsupy]
        if  liminf < pos_jugador <limsup :
            condition=True
        else:
            condition=False
        return condition

    def Death(self,pos_jugador):
        condition=False
        liminfx=self.rect.center[0] - self.error
        liminfy=self.rect.center[1] + self.error
        liminf = [liminfx,liminfy]
        limsupx=self.rect.center[0] + self.error
        limsupy=self.rect.center[1] - self.error
        limsup = [limsupx,limsupy]
        posr = pos_jugador[0] + 32
        posl = pos_jugador[0] - 32
        posu = pos_jugador[1] + 32
        posd = pos_jugador[1] - 32
        if  posr == liminfx:
            condition=True
        else:
            condition=False
        return condition




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
