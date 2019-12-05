import pygame as pg
from libreria import*
import random
import configparser as cp

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

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    reloj= pg.time.Clock()
    # CREACION DE GRUPOOS
    lineas = pg.sprite.Group()
    objetos=pg.sprite.Group()
    regiones = pg.sprite.Group()
    torres= pg.sprite.Group()
    # CUADRO
    r=Region([100,100])
    regiones.add(r)
    linea=Linea([900,100])
    linea.h=True
    lineas.add(linea)
    linea2=Linea([600,500],[300,5])
    linea2.h=False
    lineas.add(linea2)

    tor=Region([100,300],azul)
    torres.add(tor)
    pg.display.flip()
    fin = False
    while not fin:
        event=pg.event.get()
        for e in event:
            if e.type == pg.QUIT:
                fin = True
            if e.type == pg.MOUSEBUTTONDOWN:

                if tor.rect.collidepoint(e.pos):
                    for r in torres:
                        if r.rect.collidepoint(e.pos):
                            c=Torre(e.pos,azul)
                            c.click=True
                            objetos.add(c)
                if r.rect.collidepoint(e.pos):
                    for r in regiones:
                        if r.rect.collidepoint(e.pos):
                            c=Cuadro(e.pos)
                            c.click=True
                            objetos.add(c)
                    # obj.click = True
            if e.type == pg.MOUSEBUTTONUP:
                for o in objetos:
                    if o.click:
                        o.click=False
                        o.velx=10
                    # obj.click=False
                    pass
        for o in objetos:
            ls_col=pg.sprite.spritecollide(o,lineas,False)
            for l in ls_col:
                o.velx=l.velx
                o.vely=l.vely
        torres.update()
        lineas.update()
        objetos.update()
        pantalla.fill(negro)
        objetos.draw(pantalla)
        regiones.draw(pantalla)
        lineas.draw(pantalla)
        torres.draw(pantalla)
        pg.display.flip()
        reloj.tick(35)
