import pygame as pg
from libreria import*
from Personaje import*
from Bala import*
from Mothership import *
from Objetos import *
from Mothership_E import *
import time
import random
import sys

def menu_options():
    pass


if __name__ == '__main__':

    # PANTALLA
    pg.init()
    display = pg.display.set_mode([ancho,alto])
    display_credits = None
    display_options = None
    display_game = None

    # GRUPOS
    jugadores=pg.sprite.Group()
    balas_jugador=pg.sprite.Group()
    nodriza_a = pg.sprite.Group()
    nodriza_e = pg.sprite.Group()
    bloques = pg.sprite.Group()

    # IMAGENES DE BLOQUES Y FONDO
    # background = pg.image.load("/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/background.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background = pg.image.load("/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/mapa2.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC

    # APARTADO DE BLOQUES
    tam_sy, tam_sx = 64,64
    x,y=0,0
    i,j=0,0
    ancho_fondo = 9216
    alto_fondo = 1344
    matrix_background = matriz_sprites(background,ancho_fondo,alto_fondo,tam_sx,tam_sy)
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
            # display_game.blit(matrix_background[x][y],[i,j])
            i+=tam_sx
        i=0
        j+=tam_sy


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


    # MENSAJES DE ESCUDO, VIDAS Y ADVERTENCIA
    Messages = pg.font.Font(None,32)
    shield = 100000
    shield_s = str(shield)
    shield_M = Messages.render(shield_s,True,negro,gris)

    healt = 1000
    healt_s = str(healt)
    hp = Messages.render(healt_s,True,negro,gris)

    WarningM= "DO NOT TOUCH ANYTHING"
    WarningM = Messages.render(WarningM,True,rojo,gris)
    pos_w = centrar_texto(WarningM)

    salud= "HEALT"
    salud = Messages.render(salud,True,negro,gris)

    escudo= "SHIELD"
    escudo = Messages.render(escudo,True,negro,gris)

    # FINALIZADORES DE ETAPAS(JUEGO, PAUSA, MENU), Y VARIABLES
    i=240 #POSICION DEL FONDO PARA EL DESPLAZAMIENTO
    nivel=0
    reloj=pg.time.Clock()
    end = False
    game_over = False
    pause = False
    p1,p2,p3,p4,p5,p6,p7 = False,False,False,False,False,False,False

    while not end and not game_over and not pause:
        event=pg.event.get()
        if display != None:
            p1,p2,p3,p4 = menu(display,p1,p2,p3,p4)
        if display_credits != None:
            p5,p6 = menu_creditos(display_credits,p5,p6)
        if display_options != None:# CAMBIAR LAS OPCIONES CUANDO SE NOS OCURRA ALGO
            p1,p2,p3,p4 = menu(display_options,p1,p2,p3,p4)
        for event in event:
            if event.type == pg.QUIT:
                end = True
            # OPCIONES DEL MENU PRINCIPAL
            if event.type == pg.MOUSEBUTTONDOWN and p4 or event.type == pg.MOUSEBUTTONDOWN and p6:
                end = True
            if event.type == pg.MOUSEBUTTONDOWN and p3:
                pg.display.quit()
                display = None
                display_game = None
                display_options = None
                display_credits = pg.display.set_mode([ancho,alto])
                display_credits.fill(negro)
                p3 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p2:
                pg.display.quit()
                display = None
                display_game = None
                display_credits = None
                display_options = pg.display.set_mode([ancho,alto])
                display_options.fill(negro)
                p2 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p1:
                pg.display.quit()
                display = None
                display_credits = None
                display_options = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p1 = False
                pg.display.flip()
            # OPCIONES DE CREDITOS
            if event.type == pg.MOUSEBUTTONDOWN and p5:
                pg.display.quit()
                display_game = None
                display_credits = None
                display_options = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p5 = False
                pg.display.flip()
            # OPCIONES DEL MENU DE OPCIONES XD
            if display_game != None:
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
        if display_game != None:
            for b in balas_jugador:
                if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                    balas_jugador.remove(b)
            ls = pg.sprite.spritecollide(j,bloques,False)
            for b in ls:
                # print(j.rect.center)
                # print(b.rect.center)
                # print(j.pos)
                if b.OnLimit(j.pos):
                    shield-=10
                    shield_s = str(shield)
                    shield_M = Messages.render(shield_s,True,negro,gris)
                    j.BlockDeath(b)
            i-=6
            if shield <=0:
                game_over = True
            jugadores.update()
            if nivel != 0:
                nodriza_a.update()
                # nodriza_e.update()
            balas_jugador.update()
            bloques.update()
            # display_game.fill(negro)
            display_game.blit(background,[i,nivel])
            jugadores.draw(display_game)
            balas_jugador.draw(display_game)
            bloques.draw(display_game)
            nodriza_a.draw(display_game)
            nodriza_e.draw(display_game)
            if i >= -2000 and nivel == 0:
                display_game.blit(WarningM,[pos_w,0])
            print(i)
            if i == -ancho_fondo + ancho:
                i = 0
                nivel = -64*11
                for b in bloques:
                    bloques.remove(b)
            display_game.blit(salud,[0,0])
            display_game.blit(escudo,[0,32])
            display_game.blit(hp,[100,0])
            display_game.blit(shield_M,[100,32])
            pg.display.flip()
            reloj.tick(60)
