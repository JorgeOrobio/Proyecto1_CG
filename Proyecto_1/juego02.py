import pygame as pg
from libreria import*
from Personaje import*
from Bala import*
from Mothership import *
from Objetos import *
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
    bloques = pg.sprite.Group()

    # IMAGENES
    # background = pg.image.load("/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/background.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background = pg.image.load("/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/mapa2.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC

    # APARTADO DE BLOQUES
    tam_sy, tam_sx = 64,64
    x,y=0,0
    i,j=0,0
    matrix_background = matriz_sprites(background,9216,1344,tam_sx,tam_sy)
    mapaf = open("mapa.txt",'r')
    mapaf = mapaf.read()
    mapaf=mapaf.split('\n')
    # AGREGANDO BLOQUES DEL MAPA
    for filas in mapaf:
        for ele in filas:
            # AQUI PUEDE AGREGAR LA CONDICION PARA AGREGAR BLOQUES
            if ele == "#":
                x,y = 0,0
                b = Bloque(matrix_background[x][y],[i,j])
                bloques.add(b)
            if ele == ".":
                x,y = 0,4
            # pantalla.blit(matrix_background[x][y],[i,j])
            i+=tam_sx
        i=0
        j+=tam_sy
    i=4

    # JUGADOR
    dirreccion_imagen_jugador="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada_sf.png"
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
    i=240
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
        ls = pg.sprite.spritecollide(j,bloques,False)
        for b in ls:
            # print(j.rect.center)
            # print(b.rect.center)
            # print(j.pos)
            if b.OnLimit(j.pos):
                j.BlockDeath(b)

        i-=6
        jugadores.update()
        nodriza_a.update()
        nodriza_e.update()
        balas_jugador.update()
        bloques.update()
        # pantalla.fill(negro)
        pantalla.blit(background,[i,0])
        jugadores.draw(pantalla)
        bloques.draw(pantalla)
        nodriza_a.draw(pantalla)
        nodriza_e.draw(pantalla)
        balas_jugador.draw(pantalla)
        pg.display.flip()
        reloj.tick(60)
