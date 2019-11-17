import pygame as pg
from libreria import*
import random
import configparser as cp
import sys

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    display = pg.display.set_mode([ancho,alto])

    # FINALIZADORES DE ETAPAS(JUEGO, PAUSA, MENU)

    end = False
    game_over = False
    pause = False
    p1,p2,p3,p4 = False,False,False,False
    while not end and not game_over and not pause:
        event=pg.event.get()
        if display != None:
            p1,p2,p3,p4 = menu(display,p1,p2,p3,p4)
        for e in event:
            if e.type == pg.QUIT:
                end = True
            if e.type == pg.MOUSEBUTTONDOWN and p4:
                end = True
            if e.type == pg.MOUSEBUTTONDOWN and p3:
                pg.display.quit()
                display = None
                display_credits = pg.display.set_mode([ancho,alto])
                display_credits.fill(negro)
                p3 = False
                pg.display.flip()
            if e.type == pg.MOUSEBUTTONDOWN and p2:
                pg.display.quit()
                display = None
                display_options = pg.display.set_mode([ancho,alto])
                display_options.fill(negro)
                p2 = False
                pg.display.flip()
            if e.type == pg.MOUSEBUTTONDOWN and p1:
                pg.display.quit()
                display = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p1 = False
                pg.display.flip()
