import pygame as pg
from libreria import*
from Personaje import*
import time

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    fuente=pg.font.Font(None,32)

    # GRUPOS
    jugadores=pg.sprite.Group()
    # JUGADOR
    archivo="/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Personaje/jugador/nave_terminada.png"
    imagen=pg.image.load(archivo)
    matriz=matriz_sprites(imagen,320,512,64,64)
    j=Jugador(matriz)
    jugadores.add(j)
    # CONSTANTES
    salud=1000
    reloj=pg.time.Clock()
    fin_de_juego= False
    fin = False
    while (not fin) and (not fin_de_juego):
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
            #MOVIMIENTO DIRECCIONADO
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    j.velx=10
                    j.vely=0
                    j.fila=2
                if event.key == pg.K_LEFT:
                    j.velx=-10
                    j.vely=0
                    j.fila=5
                if event.key == pg.K_DOWN:
                    j.vely=10
                    j.velx=0
                    j.fila=0
                if event.key == pg.K_UP:
                    j.vely=-10
                    j.velx=0
                    j.fila=1
                if event.key == pg.K_RIGHT:
                    time.sleep(0.01)
                    if event.key == pg.K_UP:
                        j.velx=10
                        j.vely=-10
                        j.fila=7
                # if event.key == pg.K_LEFT:
                #     j.velx=-10
                #     j.vely=0
                # if event.key == pg.K_DOWN:
                #     j.vely=10
                #     j.velx=0
                # if event.key == pg.K_UP:
                #     j.vely=-10
                #     j.velx=0
                # if event.key== pg.K_SPACE:
                #     # CREAR BALA
                #     b=Bala(j.rect.midtop,verde)
                #     balas.add(b)
                #     b.vely=-10
            if event.type==pg.KEYUP:
                if event.key != pg.K_SPACE:
                    j.velx=0
                    j.vely=0
        jugadores.update()
        pantalla.fill(negro)
        jugadores.draw(pantalla)
        pg.display.flip()
        reloj.tick(30)
