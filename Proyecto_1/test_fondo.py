import pygame as pg
from libreria import*
import random

class Fondo(pg.sprite.Sprite):
    """docstring for Fondo."""
    # /home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Fondo/fondo2.jpg
    def __init__(self, imagen):
        super(Fondo, self).__init__()
        self.arg = arg

def background(pantalla):
    x,velx = 0,0
    background=pg.image.load('/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Fondo/fondo2.jpg')
    loop_background(pantalla,background)
    pass

def loop_background(pantalla,background):
    reloj=pg.time.Clock()
    info=background.get_rect()
    print(info)
    fondox=-100
    velx=7
    fin = False
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
        if fondox<((info[2]-ancho)*-1):
            fondox=0
        else:
            fondox-=velx
        pantalla.blit(background,[fondox,-100])
        reloj.tick(60)
        pg.display.flip()


if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ancho,alto])
    background(pantalla)
