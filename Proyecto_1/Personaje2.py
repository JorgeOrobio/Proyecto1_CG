import pygame as pg
from libreria import*

class Jugador(pg.sprite.Sprite):
    """clase jugador"""
    def __init__(self,archivo,archivo2,archivo3):
        pg.sprite.Sprite.__init__(self)
        self.fila=2
        self.col=0
        self.matriz=archivo
        self.image = self.matriz[self.col][self.fila]
        ##Explosion
        self.fila2=0
        self.col2=0
        self.matriz2=archivo2
        self.image2 = self.matriz2[self.col2][self.fila2]
        ##Cambio de skin
        self.fila3=2
        self.col3=0
        self.matriz3=archivo3
        self.image3 = self.matriz3[self.col3][self.fila3]

        self.rect=self.image.get_rect()
        self.pos = [self.rect.center[0],self.rect.center[1]]
        self.rect.x=200
        self.rect.y=centro_y
        self.disparo=self.rect.midtop
        self.velx=0
        self.vely=0
        self.vidas = 3
        self.modificador = False
        self.modificador3 = False

    def update(self):
        # ANIMACION DE PERSONAJE
        if self.modificador == False:
            if self.vidas > 0:
                self.image = self.matriz[self.col][self.fila]
                if self.col >=4:
                    self.col=0
                else:
                    self.col+=1
        if self.modificador == True:
            if self.vidas > 0:
                self.image = self.matriz3[self.col3][self.fila3]
                if self.col3 >=4:
                    self.col3=0
                else:
                    self.col3+=1
        #llamado a matriz de la explosion
        if self.vidas <= 0:
            self.image = self.matriz2[self.col2][self.fila2]
            if self.col2 >=16:
                self.col2=0
            else:
                self.col2+=1

        # LIMITES DE PANTALLA PERSONAJE
        if self.rect.x > (ancho - self.rect.width):
            self.rect.x = ancho - self.rect.width
            self.vely=0
        if self.rect.x < 0:
            self.rect.x=0
            self.vely=0
        if self.rect.y > (alto - self.rect.height):
            self.rect.y = alto - self.rect.height
            self.velx=0
        if self.rect.y < 0:
            self.rect.y=0
            self.velx=0

        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.pos = [self.rect.center[0],self.rect.center[1]]

    def BlockDeath(self,block):
        condition=False
        # LOS CUATRO BORDES DEL JUGADOR
        liminfx=self.rect.left
        liminfy=self.rect.bottom
        liminf = [liminfx,liminfy]
        limsupx=self.rect.right
        limsupy=self.rect.top
        limsup = [limsupx,limsupy]
        # LOS CUATRO BORDES DEL BLOQUE
        posr = block.rect.right
        posl = block.rect.left
        posd = block.rect.bottom
        posu = block.rect.top
        if  posl - 8 < limsupx < posl + 8:
            print("murio")
            condition=True
            self.vely = 0
        elif posu + self.vely < liminfy < posu - self.vely:
            self.rect.y = posu - 64
            self.vely=0
        elif posd == limsupy:
            self.rect.y = posd
            self.vely=0
        else:
            condition=False
        return condition
        pass

    def get_all(self):
        pass
        return self.rect.x,self.rect.y
