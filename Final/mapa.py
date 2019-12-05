import pygame as pg
from libreria import*
from Objetos import*
import random
import configparser as cp

def load_map():
    pass


if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    # GRUPOS
    bloques = pg.sprite.Group()

    # IMAGENES
    # background = pg.image.load("/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/background.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background = pg.image.load("/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/mapa.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC


    tam_sy, tam_sx = 64,64
    x,y=0,0
    i,j=0,0
    matrix_background = matriz_sprites(background,9216,1344,tam_sx,tam_sy)
    # TIEMPOS
    reloj= pg.time.Clock()
    # MAPA
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
        pg.display.flip()
    i=4
    fin = False
    # CICLO PRINCIPAL
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True

        i-=4
        bloques.update()
        bloques.draw(pantalla)
        pantalla.blit(background,[i,0])
        print(i)
        pg.display.flip()
        reloj.tick(60)
