import pygame as pg
from libreria import*
import random

class Fondo(pg.sprite.Sprite):
    """docstring for Fondo."""
    # /home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Fondo/fondo2.jpg
    def __init__(self):
        self.image = pg.image.load('/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Fondo/fondo2.jpg')
        self.rect = self.image.get_rect()
        self.x = -100
        self.velfondox = 5

    def update(self):
        self.x -= self.velfondox
    def display(self,pantalla):
        pantalla.blit(self.image,[self.x,-100])
        pg.display.flip()
        pass

def background(pantalla,fondo):
    if fondo.x<((fondo.rect.width - ancho)*-1):
        fondo.x=0
    else:
        fondo.update()
    fondo.display(pantalla)
    reloj.tick(30)


if __name__ == '__main__':
    pg.init
    pantalla = pg.display.set_mode([ancho,alto])
    reloj=pg.time.Clock()
    fondo = Fondo()
    fin = False
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
        background(pantalla,fondo)
