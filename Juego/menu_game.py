import pygame as pg
from libreria import*
import random
import configparser as cp
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

    # FINALIZADORES DE ETAPAS(JUEGO, PAUSA, MENU)

    end = False
    game_over = False
    pause = False
    p1,p2,p3,p4,p5,p6,p7 = False,False,False,False,False,False,False
    while not end and not game_over and not pause:
        event=pg.event.get()
        if display != None:
            p1,p2,p3,p4 = menu(display,p1,p2,p3,p4)
        if display_game != None:# EL JUEGO NO DEBE TENER MENU, PERO POR AHORA DEJEMOSLO ASI
            p1,p2,p3,p4 = menu(display_game,p1,p2,p3,p4)
        if display_credits != None:
            p5,p6 = menu_creditos(display_credits,p5,p6)
        if display_options != None:# CAMBIAR LAS OPCIONES CUANDO SE NOS OCURRA ALGO
            p1,p2,p3,p4 = menu(display_options,p1,p2,p3,p4)
        for e in event:
            if e.type == pg.QUIT:
                end = True
            # OPCIONES DEL MENU PRINCIPAL
            if e.type == pg.MOUSEBUTTONDOWN and p4 or e.type == pg.MOUSEBUTTONDOWN and p6:
                end = True
            if e.type == pg.MOUSEBUTTONDOWN and p3:
                pg.display.quit()
                display = None
                display_game = None
                display_options = None
                display_credits = pg.display.set_mode([ancho,alto])
                display_credits.fill(negro)
                p3 = False
                pg.display.flip()
            if e.type == pg.MOUSEBUTTONDOWN and p2:
                pg.display.quit()
                display = None
                display_game = None
                display_credits = None
                display_options = pg.display.set_mode([ancho,alto])
                display_options.fill(negro)
                p2 = False
                pg.display.flip()
            if e.type == pg.MOUSEBUTTONDOWN and p1:
                pg.display.quit()
                display = None
                display_credits = None
                display_options = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p1 = False
                pg.display.flip()
            # OPCIONES DE CREDITOS
            if e.type == pg.MOUSEBUTTONDOWN and p5:
                pg.display.quit()
                display_game = None
                display_credits = None
                display_options = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p5 = False
                pg.display.flip()
            # OPCIONES DEL MENU DE OPCIONES XD
