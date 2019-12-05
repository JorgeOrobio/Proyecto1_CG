import pygame as pg
from libreria import*
from Personaje2 import*
from Bala import*
from Mothership import *
from Mothership_E import *
import time

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    fuente=pg.font.Font(None,32)

    # GRUPOS
    jugadores=pg.sprite.Group()
    balas_jugador=pg.sprite.Group()
    nodriza_a = pg.sprite.Group()
    nodriza_e = pg.sprite.Group()
    # JUGADOR

    dirreccion_imagen_jugador="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada.png"
    # dirreccion_imagen_jugador="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada.png"
    imagen_jugador=pg.image.load(dirreccion_imagen_jugador)
    matriz_jugador=matriz_sprites(imagen_jugador,320,512,64,64)

    # NAVE NODRIZA
    dirreccion_imagen_naveM="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/mothership.png"
    # dirreccion_imagen_naveM="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/mothership.png"
    imagen_naveM=pg.image.load(dirreccion_imagen_naveM)

    # NAVE NODRIZA ENEMIGA
    dirreccion_imagen_naveME="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/enemigos/mothership.png"
    # dirreccion_imagen_naveM="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/mothership.png"
    imagen_naveME=pg.image.load(dirreccion_imagen_naveME)

    # BALAS
    # BALAS JUGADOR
    direccion_imagen_bala_jugador="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_blue.png"
    # direccion_imagen_bala_jugador="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_blue.png"
    imagen_bala_jugador=pg.image.load(direccion_imagen_bala_jugador)
    matriz_bala_jugador=matriz_sprites(imagen_bala_jugador,304,38,38,38)
    # BALAS ENEMIGO
    direccion_imagen_bala_enemigo="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_red.png"
    # direccion_imagen_bala_enemigo="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_red.png"
    imagen_bala_enemigo=pg.image.load(direccion_imagen_bala_enemigo)
    matriz_bala_enemigo=matriz_sprites(imagen_bala_enemigo,304,38,38,38)
    # CREACION DE JUGADOR
    j=Jugador(matriz_jugador)
    jugadores.add(j)

    # CREACION NAVE NODRIZA
    mothership = Mothership(imagen_naveM)
    nodriza_a.add(mothership)
    mothership2 = Mothership_E(imagen_naveME)
    nodriza_e.add(mothership2)

    # CONSTANTES
    salud=1000
    reloj=pg.time.Clock()
    fin_de_juego= False
    fin = False
    while (not fin) and (not fin_de_juego):
        # IMPRESION PARA PRUEBAS LIGERAS
        # print(j.rect.top)
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
            #MOVIMIENTO DIRECCIONADO
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    j.vely=10
                    j.velx=0
                    j.fila=4
                if event.key == pg.K_UP:
                    j.vely=-10
                    j.velx=0
                    j.fila=7
                # if event.key == pg.K_RIGHT:
                #     time.sleep(0.01)
                #     if event.key == pg.K_UP:
                #         j.velx=10
                #         j.vely=-10
                #         j.fila=7
                if event.key== pg.K_SPACE:
                    # CREAR BALA
                    if j.fila == 7 or j.fila == 4:
                        b=Bala(j.rect.midright,matriz_bala_jugador,5)
                        balas_jugador.add(b)
                        b.velx=30
                    if j.fila == 2:
                        b=Bala(j.rect.midright,matriz_bala_jugador,5)
                        b2=Bala(j.rect.topright,matriz_bala_jugador,5)
                        balas_jugador.add(b)
                        balas_jugador.add(b2)
                        b.velx=30
                        b2.velx=30
                    if j.fila == 5:
                        b=Bala(j.rect.midleft,matriz_bala_jugador,4)
                        b2=Bala(j.rect.topleft,matriz_bala_jugador,4)
                        balas_jugador.add(b)
                        balas_jugador.add(b2)
                        b.velx=-30
                        b2.velx=-30
            if event.type==pg.KEYUP:
                if event.key != pg.K_SPACE:
                    j.velx=0
                    j.vely=0
                    j.fila=2
        # LIMPIEZA DE BALAS AL SALIR DE PANTALLA
        for b in balas_jugador:
            if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                balas_jugador.remove(b)
        jugadores.update()
        nodriza_a.update()
        nodriza_e.update()
        balas_jugador.update()
        pantalla.fill(negro)
        jugadores.draw(pantalla)
        nodriza_a.draw(pantalla)
        nodriza_e.draw(pantalla)
        balas_jugador.draw(pantalla)
        pg.display.flip()
        reloj.tick(30)
