import pygame as pg
from libreria import*
import random
import configparser as cp

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    # background = pg.image.load("/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/background.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background = pg.image.load("/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/mapa.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    matrix_background = matriz_sprites(background,6400,1344,64,64)

    reloj= pg.time.Clock()
    infomapa = cp.ConfigParser()
    infomapa.read('mapa.mp')
    # infomapa.read('/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/background.png')
    x,y=0,0
    s_mapa=infomapa.get('info','mp')
    print(s_mapa)
    mapa = s_mapa.split('\n')
    i,j=0,0
    xl=[]
    yl=[]
    for filas in mapa:
        for ele in filas:
            # AQUI PUEDE AGREGAR LA CONDICION PARA AGREGAR BLOQUES
            for elemento in infomapa.items(ele):
                if elemento[0] == 'col':
                    x=(int(elemento[1]))
                if elemento[0] == 'fil':
                    y=(int(elemento[1]))
                    # reloj.tick(1)
                    # reloj.tick(10)
            # print("")
            # print("x: ",x)
            # print("y: ",y)
            # print("i: ",i)
            # print("j: ",j)
            # print("")
            pantalla.blit(matrix_background[x][y],[i,j])
            i+=32
        i=0
        j+=32
        pg.display.flip()
    # CICLO PARA IR MOVIENDO LO ANTERIORMENTE MAPEADO
    # for i in range(0,2080):
    #     for j in range(0,)
    # print("SALIO")
    # for i in matriz:
    #     for j in i:
    #         pantalla.blit(j,[0,0])
    #         pg.display.flip()
    #         reloj.tick(1)
    # pantalla.blit(matriz[x][y],[0,0])
    pg.display.flip()
    reloj.tick(1)

    fin = False
    # CICLO PRINCIPAL
    while not fin:
        for event in pg.event.get():
            #EVENTOS
            if event.type ==pg.QUIT:
                fin = True
