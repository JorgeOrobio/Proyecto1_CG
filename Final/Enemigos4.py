import pygame as pg
from libreria import*

class Rival2(pg.sprite.Sprite):
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
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=-5
        self.vely=0
        self.tempo=random.randrange(300)
        self.tempoy1=random.randrange(100)
        self.tempoy2=random.randrange(100)
        self.luck = False
        self.muerte = 0


    def update(self):
        # PARA LOS SEGUNDOS ENEMIGOS DEL SEGUNDO NIVEL SE DEBE HACER QUE TANTO SU
        # MOVIMIENTO COMO SU VELOCIDAD SEAN ALEATORIOS PARA AGREGAR MAS DIFICULTAD
        # AL JUEGO ADEMAS DE QUE ESTOS ENEMIGOS TAMBIEN VAN A PODER DISPARAR
        # PROYECTILES, PERO ESTOS NO VAN A SEGUIR AL JUGADOR

        self.rect.x += self.velx
        self.rect.y += self.vely
        self.tempo -=1
        self.tempoy1 -=1
        self.tempoy2 -=1

        if self.tempoy1 <=0:
            self.tempoy1=random.randrange(100)
            self.vely = 10
        elif self.tempoy2 <=0:
            self.tempoy2=random.randrange(100)
            self.vely = -self.vely

        # LIMITES DE PANTALLA ENEMIGO
        if self.rect.y > (alto - self.rect.height):
            self.rect.y = alto - self.rect.height
            self.velx= -self.vely
        if self.rect.y < 0:
            self.rect.y=0
            self.velx= -self.vely
        if self.rect.x >= (ancho - self.rect.width):
            self.velx= -10

        if self.muerte == 0:
            self.image = self.matriz[self.col][self.fila]
            if self.col >=4:
                self.col=0
            else:
                self.col+=1

        if self.muerte == 1:
            self.image = self.matriz2[self.col2][self.fila2]
            if self.col2 >=13:
                self.col2=0
            else:
                self.col2+=1
                print(self.col2)
