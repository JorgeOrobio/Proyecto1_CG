import pygame as pg
from libreria import*

class Bala_seguidora(pg.sprite.Sprite):
    """clase bala"""
    def __init__(self,puntoi,puntof,archivo,columna = 0,archivo2 = None,archivo3 = None):
        pg.sprite.Sprite.__init__(self)
        self.fila=0
        self.fila2=0
        self.fila3=0
        self.col=columna
        self.col2=0
        self.col3=0
        self.matriz=archivo
        self.matriz2=archivo2
        self.matriz3=archivo3
        self.image = self.matriz[self.col][self.fila]
        self.rect=self.image.get_rect()
        self.puntof= puntof
        self.rect.x=puntoi[0]
        self.rect.y=puntoi[1]
        self.velx=-3
        self.vely=0
        self.muerte = 0
        try:
            self.m=((puntof[1]-puntoi[1])/(puntof[0]-puntoi[0]))
        except:
            self.m = 0
        self.b= self.rect.y - (self.m*self.rect.x)

    def recalY(self,m,b,x):
        y = m*x + b
        return(int(y))

    def update(self):
        if self.matriz2 != None and self.matriz3 != None :
            if self.muerte == 0:
                self.image = self.matriz2[self.col2][self.fila2]
                if self.col2 >=1:
                    self.col2=0
                else:
                    self.col+=1

            if self.muerte == 1:
                self.image = self.matriz3[self.col3][self.fila3]
                if self.col3 >=5:
                    self.col3=0
                else:
                    self.col3+=1
            pass

        self.rect.x += self.velx
        self.rect.y +=self.vely

        if self.rect.x > self.puntof[0]:
            self.rect.x += self.velx
            self.rect.y = self.recalY(self.m,self.b,self.rect.x)

    def repos(self,position):
        self.m = ((position[1]-self.rect.y)/(position[0]-self.rect.x))
        self.b= self.rect.y - (self.m*self.rect.x)
        self.puntof = position
