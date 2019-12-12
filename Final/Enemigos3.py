import pygame as pg
from libreria import*

class Rival3(pg.sprite.Sprite):
    """clase rival"""
    def __init__(self,archivo,archivo2,pos):
        pg.sprite.Sprite.__init__(self)
        self.fila=0
        self.col=0
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        ##para la explosion
        self.fila2=0
        self.col2=0
        self.matriz2=archivo2
        self.image2= self.matriz2[self.col2][self.fila2]
        self.rect=self.image.get_rect()
        self.limit = pos[0]
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=-3
        self.vely=0
        self.tempo=random.randrange(150)
        self.luck = False
        self.muerte = 0

    def update(self):

        # IMPLEMENTAR EL PUNTO PENDIENTE PARA SEGUIR A LA POSICION DEL SEGUIDOR EN UN INSTANTE DE TIEMPO
         # SE DEBE IMPLEMENTAR DENTRO DE LA CLASE BALA EL SEGUIMIENTO, ES DECIR, HACER OTRA BALA O ADAPTARLA
         # PARA EVITAR EXTENDER EL CODIGO
        self.rect.x += self.velx
        self.tempo -=1
        self.image = self.matriz[self.col][self.fila]


        # LIMITES DE PANTALLA PERSONAJE
        if self.rect.x > (ancho - self.rect.width):
            self.rect.x = ancho - self.rect.width
            self.velx= - self.velx
        if self.rect.x < 0:
            self.rect.x=0
            self.velx= -self.velx
        if self.rect.y > (alto - self.rect.height):
            self.rect.y = alto - self.rect.height
            self.vely = -self.vely
        if self.rect.y < 0:
            self.rect.y=0
            self.vely = -self.vely

        if self.muerte == 0:
            if self.col >=1:
                self.col=0
            else:
                self.col+=1

        if self.muerte == 1:
            self.image = self.matriz2[self.col2][self.fila2]
            if self.col2 >=13:
                self.col2=0
            else:
                self.col2+=1
