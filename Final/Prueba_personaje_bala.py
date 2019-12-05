import pygame as pg
from libreria import*
from Personaje import*
from Bala import*
import time

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    fuente=pg.font.Font(None,32)

    # GRUPOS
    jugadores=pg.sprite.Group()
    balas_jugador=pg.sprite.Group()
    # JUGADOR
    dirreccion_imagen_jugador="/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Personaje/jugador/nave_terminada.png"
    imagen_jugador=pg.image.load(dirreccion_imagen_jugador)
    matriz_jugador=matriz_sprites(imagen_jugador,320,512,64,64)
    # BALAS
    # BALAS JUGADOR
    direccion_imagen_bala_jugador="/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Efectos/bullets_blue.png"
    imagen_bala_jugador=pg.image.load(direccion_imagen_bala_jugador)
    matriz_bala_jugador=matriz_sprites(imagen_bala_jugador,304,38,38,38)
    # BALAS ENEMIGO
    direccion_imagen_bala_enemigo="/home/jorge/Escritorio/CGrafica/Sprites/Proyecto1/Efectos/bullets_red.png"
    imagen_bala_enemigo=pg.image.load(direccion_imagen_bala_enemigo)
    matriz_bala_enemigo=matriz_sprites(imagen_bala_enemigo,304,38,38,38)
    # CREACION DE JUGADOR
    j=Jugador(matriz_jugador)
    jugadores.add(j)
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
                # if event.key == pg.K_RIGHT:
                #     time.sleep(0.01)
                #     if event.key == pg.K_UP:
                #         j.velx=10
                #         j.vely=-10
                #         j.fila=7
                if event.key== pg.K_SPACE:
                    # CREAR BALA
                    if j.fila == 1:
                        b=Bala(j.rect.midtop,matriz_bala_jugador,0)
                        b2=Bala(j.rect.topleft,matriz_bala_jugador,0)
                        balas_jugador.add(b)
                        balas_jugador.add(b2)
                        b.vely=-30
                        b2.vely=-30
                    if j.fila == 0:
                        b=Bala(j.rect.midbottom,matriz_bala_jugador,2)
                        b2=Bala(j.rect.bottomleft,matriz_bala_jugador,2)
                        balas_jugador.add(b)
                        balas_jugador.add(b2)
                        b.vely=30
                        b2.vely=30
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
        # LIMPIEZA DE BALAS AL SALIR DE PANTALLA
        for b in balas_jugador:
            if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                balas_jugador.remove(b)
        jugadores.update()
        balas_jugador.update()
        pantalla.fill(negro)
        jugadores.draw(pantalla)
        balas_jugador.draw(pantalla)
        pg.display.flip()
        reloj.tick(30)
