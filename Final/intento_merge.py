import pygame as pg
from libreria import*
from Personaje2 import*
from Spawn import *
from Bala import*
from Mothership import *
from Objetos import *
from Enemigos import *
from Enemigos2 import *
from Mothership_E import *
from Modificador1 import*
from Modificador2 import*
from Modificador3 import*
import time
import random
import sys

def menu_options():
    pass
def endgame(display,p8,p9):
    display.fill(negro)
    size_img = 32
    Messages = pg.font.Font(None,size_img)
    Messages2 = pg.font.Font(None,size_img*2)
    creator_1 = "GAME OVER"
    creator_1 = Messages.render(creator_1,True,verde,blanco)

    creator_2 = "MANCO CULIAO"
    creator_2 = Messages.render(creator_2,True,verde,blanco)

    back_message = "TRY AGAIN"
    if not p8:
        back_message = Messages2.render(back_message,True,rojo,azul)
    else:
        back_message = Messages2.render(back_message,True,azul,rojo)

    exit_message = "EXIT"
    if not p9:
        exit_message = Messages2.render(exit_message,True,rojo,azul)
    else:
        exit_message = Messages2.render(exit_message,True,azul,rojo)


    y = size_img * 2
    x = centrar_texto(back_message)
    display.blit(back_message,[x,y])
    p8= rango_menu(back_message,[x,y])

    y += size_img *2
    x = centrar_texto(exit_message)
    display.blit(exit_message,[x,y])
    p9 = rango_menu(exit_message,[x,y])

    y += size_img * 4
    x = centrar_texto(creator_1)
    display.blit(creator_1,[x,y])

    y += size_img
    x = centrar_texto(creator_2)
    display.blit(creator_2,[x,y])

    pg.display.flip()
    return p8,p9
    pass


def pausegame(display,p10,p11):
    display.fill(negro)
    size_img = 32
    Messages = pg.font.Font(None,size_img)
    Messages2 = pg.font.Font(None,size_img*2)
    creator_1 = "PAUSE"
    creator_1 = Messages.render(creator_1,True,verde,blanco)

    creator_2 = "TAKE A BREAK :V"
    creator_2 = Messages.render(creator_2,True,verde,blanco)

    back_message = "CONTINUE"
    if not p10:
        back_message = Messages2.render(back_message,True,rojo,azul)
    else:
        back_message = Messages2.render(back_message,True,azul,rojo)

    exit_message = "EXIT"
    if not p11:
        exit_message = Messages2.render(exit_message,True,rojo,azul)
    else:
        exit_message = Messages2.render(exit_message,True,azul,rojo)


    y = size_img * 2
    x = centrar_texto(back_message)
    display.blit(back_message,[x,y])
    p10= rango_menu(back_message,[x,y])

    y += size_img *2
    x = centrar_texto(exit_message)
    display.blit(exit_message,[x,y])
    p11 = rango_menu(exit_message,[x,y])

    y += size_img * 4
    x = centrar_texto(creator_1)
    display.blit(creator_1,[x,y])

    y += size_img
    x = centrar_texto(creator_2)
    display.blit(creator_2,[x,y])

    pg.display.flip()
    return p10,p11

def win(display,p12):
    display.fill(negro)
    size_img = 32
    Messages = pg.font.Font(None,size_img)
    Messages2 = pg.font.Font(None,size_img*2)
    creator_1 = "CONGRATULATIONS"
    creator_1 = Messages2.render(creator_1,True,verde,blanco)

    creator_2 = "YA NO ERES UN MANCO CULIAO"
    creator_2 = Messages2.render(creator_2,True,verde,blanco)

    exit_message = "EXIT"
    if not p12:
        exit_message = Messages2.render(exit_message,True,rojo,azul)
    else:
        exit_message = Messages2.render(exit_message,True,azul,rojo)
    y = size_img * 4
    x = centrar_texto(creator_1)
    display.blit(creator_1,[x,y])

    y += size_img *2
    x = centrar_texto(creator_2)
    display.blit(creator_2,[x,y])

    y += size_img * 4
    x = centrar_texto(exit_message)
    display.blit(exit_message,[x,y])
    p12 = rango_menu(exit_message,[x,y])


    pg.display.flip()
    return p12


def load_map(bloques,background):
##################################################################################################################################################################
    # IMAGENES DE BLOQUES Y FONDO
    # background = pg.image.load("/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/background.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    # APARTADO DE BLOQUES
    tam_sy, tam_sx = 64,64
    matrix_x,matrix_y=0,0
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
                matrix_x,matrix_y = 0,0
                b = Bloque(matrix_background[matrix_x][matrix_y],[i,j])
                bloques.add(b)
            if ele == ".":
                matrix_x,matrix_y = 0,4
            # display_game.blit(matrix_background[x][matrix_y],[i,j])
            i+=tam_sx
        i=0
        j+=tam_sy
    return bloques
##################################################################################################################################################################
    pass

def create_spawns():

    spawns = pg.sprite.Group()
    ##SPAWN DE LOS ENEMIGOS
    direccion_imagen_spawn_enemigo = "Sprites/Personaje/enemigos/Spawn.png"
    imagen_spawn_enemigo = pg.image.load(direccion_imagen_spawn_enemigo)
    matriz_spawn_enemigo=matriz_sprites(imagen_spawn_enemigo,273,88,91,88)

    dir_red_explotion="Sprites/Efectos/Explosion_red.png"
    imagen_red_explotion=pg.image.load(dir_red_explotion)
    matriz_red_explotion=matriz_sprites(imagen_red_explotion,896,64,64,64)

    #CREACION SPAWN
    posx_spawns = 980
    posy_spawns = 60
    esp_entre = 40
    s = Spawn([posx_spawns,posy_spawns],matriz_spawn_enemigo,matriz_red_explotion)
    ##aumentar posx_spawns para que el spawn quede fuera de la pantalla
    for i in range(posy_spawns,alto - s.rect.height-esp_entre,s.rect.height+esp_entre):
        s = Spawn([posx_spawns,posy_spawns],matriz_spawn_enemigo,matriz_red_explotion)
        spawns.add(s)
        posy_spawns += s.rect.height+esp_entre
    vidas_spawn = s.vidas
    return spawns,vidas_spawn,matriz_spawn_enemigo,matriz_red_explotion

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    display = pg.display.set_mode([ancho,alto])
    display_credits = None
    display_options = None
    display_game = None
    display_endgame = None
    display_pause = None
    display_win = None
    # GRUPOS
    bloques = pg.sprite.Group()
    jugadores=pg.sprite.Group()
    balas_jugador=pg.sprite.Group()
    nodriza_a = pg.sprite.Group()
    enemigos = pg.sprite.Group()
    enemigos2 = pg.sprite.Group()
    balas_enemigos = pg.sprite.Group()
    nodriza_e = pg.sprite.Group()
    spawns = pg.sprite.Group()
    modificadores1 = pg.sprite.Group()
    modificadores2 = pg.sprite.Group()
    modificadores3 = pg.sprite.Group()
##################################################################################################################################################################
    # IMAGENES DE BLOQUES Y FONDO
    background = pg.image.load("Sprites/Mapa/mapa2.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    ancho_fondo = 9216
    bloques = load_map(bloques,background)
##################################################################################################################################################################

    # ALIADOS

    # JUGADOR
    dirreccion_imagen_jugador="Sprites/Personaje/jugador/nave_terminada_sf.png"
    imagen_jugador=pg.image.load(dirreccion_imagen_jugador)
    matriz_jugador=matriz_sprites(imagen_jugador,320,512,64,64)

    #SKIN ROJA JUGADOR
    dirreccion_imagen_jugador_OP="Sprites/Personaje/jugador/nave_terminada_sf_OP.png"
    imagen_jugador2=pg.image.load(dirreccion_imagen_jugador_OP)
    matriz_jugador2=matriz_sprites(imagen_jugador2,320,512,64,64)

    # NAVE NODRIZA
    dirreccion_imagen_naveM="Sprites/Personaje/jugador/mothership.png"
    imagen_naveM=pg.image.load(dirreccion_imagen_naveM)


##################################################################################################################################################################
    # EXPLOSIONES

    #EXPLOSION JUGADOR
    blue_explotion="Sprites/Efectos/Explosion_blue.png"
    imagen_blue_explotion=pg.image.load(blue_explotion)
    matriz_blue_explotion=matriz_sprites(imagen_blue_explotion,1088,64,64,64)

    #MUERTE ENEMIGOS
    dir_red_explotion="Sprites/Efectos/Explosion_red.png"
    imagen_red_explotion=pg.image.load(dir_red_explotion)
    matriz_red_explotion=matriz_sprites(imagen_red_explotion,896,64,64,64)

##################################################################################################################################################################
    # ENEMIGOS

    # ENEMIGOS
    direccion_imagen_enemigo="Sprites/Personaje/enemigos/Enemigo1.png"
    imagen_enemigo=pg.image.load(direccion_imagen_enemigo)
    matriz_enemigo=matriz_sprites(imagen_enemigo,560,80,80,80)

    # ENEMIGOS 2
    direccion_imagen_enemigo2="Sprites/Personaje/enemigos/Enemigo2.png"
    imagen_enemigo2=pg.image.load(direccion_imagen_enemigo2)
    matriz_enemigo2=matriz_sprites(imagen_enemigo2,340,61,68,61)

    # NAVE NODRIZA ENEMIGA
    dirreccion_imagen_naveME="Sprites/Personaje/enemigos/mothership.png"
    imagen_naveME=pg.image.load(dirreccion_imagen_naveM)

    ##SPAWN DE LOS ENEMIGOS
    direccion_imagen_spawn_enemigo = "Sprites/Personaje/enemigos/Spawn.png"
    imagen_spawn_enemigo = pg.image.load(direccion_imagen_spawn_enemigo)
    matriz_spawn_enemigo=matriz_sprites(imagen_spawn_enemigo,273,88,91,88)


##################################################################################################################################################################

    # MODIIFCADORES

    #MODIFICADORES DE ASPECTO
    direccion_imagen_modificador1 = "Sprites/Modificadores/Minas.png"
    imagen_modificador1 = pg.image.load(direccion_imagen_modificador1)
    matriz_modificador1=matriz_sprites(imagen_modificador1,80,40,40,40)

    #MODIFICADORES DE VIDA
    direccion_imagen_modificador2 = "Sprites/Modificadores/Bomba.png"
    imagen_modificador2 = pg.image.load(direccion_imagen_modificador2)
    matriz_modificador2=matriz_sprites(imagen_modificador2,90,23,30,23)

    #MODIFICADORES DE SLOW
    direccion_imagen_modificador3 = "Sprites/Modificadores/Mine_red.png"
    imagen_modificador3 = pg.image.load(direccion_imagen_modificador3)
    matriz_modificador3=matriz_sprites(imagen_modificador3,80,40,40,40)

##################################################################################################################################################################
    # BALAS

    # BALAS JUGADOR
    direccion_imagen_bala_jugador="Sprites/Efectos/bullets_blue.png"
    imagen_bala_jugador=pg.image.load(direccion_imagen_bala_jugador)
    matriz_bala_jugador=matriz_sprites(imagen_bala_jugador,304,38,38,38)

    # BALAS ENEMIGO
    direccion_imagen_bala_enemigo="Sprites/Efectos/bullets_red.png"
    imagen_bala_enemigo=pg.image.load(direccion_imagen_bala_enemigo)
    matriz_bala_enemigo=matriz_sprites(imagen_bala_enemigo,304,38,38,38)

##################################################################################################################################################################

    # CREACIONES

    # CREACION DE JUGADOR
    j=Jugador(matriz_jugador,matriz_blue_explotion,matriz_jugador2)
    jugadores.add(j)
    #manejo de la vidas jugador
    vidas_jugador = j.vidas

    # CREACION DE SPAWNS
    spawns,vidas_spawn,matriz_spawn_enemigo,explosion_red = create_spawns()

    # CREACION NAVE NODRIZA
    mothership = Mothership(imagen_naveM)
    nodriza_a.add(mothership)
    mothership2 = Mothership_E(imagen_naveME)
    nodriza_e.add(mothership2)

##################################################################################################################################################################
    # MENSAJES DE ESCUDO, VIDAS Y ADVERTENCIA
    Messages = pg.font.Font(None,32)
    shield_s = str(j.shield)
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
##################################################################################################################################################################
    #MUSICA
    # pg.mixer.init()
    # msfondo = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Music/rise.ogg")
    # #msfondo = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Music/rise.ogg")
    # ms_click = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/CloudClick.ogg")
    # #ms_click = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/CloudClick.ogg")
    # ms_disparo_j = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/laser_jugaddor.ogg")
    # #ms_disparo_j = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/laser_jugaddor.ogg.ogg")
    # ms_disparo_e = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/laser_enemigo.ogg")
    # #ms_disparo_e = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/laser_enemigo.ogg.ogg")
    # ms_creditos = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/End_Credits_Theme_ogg.ogg")
    # #ms_creditos = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/End_Credits_Theme_ogg.ogg")
    # ms_explosion = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/explosion.ogg")
    # #ms_explosion = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/explosion.ogg")
    # ms_perdio = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/NoHope.ogg")
    # #ms_perdio = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/NoHope.ogg")
    # ms_modBuenos = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Music/powerUp1.ogg")
    # # ms_modBuenos = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Music/powerUp1.ogg")
    # ms_modMalos =  pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Music/lowDown.ogg")
    # # ms_modMalos =  pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Music/lowDown.ogg")
    # ms_juego =  pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/MUSE.ogg")
    # # ms_juego =  pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/MUSE.ogg")


##################################################################################################################################################################
    # FINALIZADORES DE ETAPAS(JUEGO, PAUSA, MENU), Y VARIABLES
    i=240 #POSICION DEL FONDO PARA EL DESPLAZAMIENTO
    nivel=0
    probMod1 = 30
    probMod2 = 10
    reloj=pg.time.Clock()
    end = False
    game_over = False
    pause = False
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12 = False,False,False,False,False,False,False,False,False,False,False,False
    # msfondo.play()
    # msfondo.set_volume(.1)
    while not end and not game_over and not pause:
        event=pg.event.get()
        if display != None:
            p1,p2,p3,p4 = menu(display,p1,p2,p3,p4)
        if display_credits != None:
            p5,p6 = menu_creditos(display_credits,p5,p6)
        if display_endgame != None:
            p8,p9 = endgame(display_endgame,p8,p9)
        if display_options != None:# CAMBIAR LAS OPCIONES CUANDO SE NOS OCURRA ALGO
            p1,p2,p3,p4 = menu(display_options,p1,p2,p3,p4)
        if display_pause != None:
            p10,p11 = pausegame(display_pause,p10,p11)
        if display_win != None:
            p12 = win(display_win,p12)
        for event in event:
            if event.type == pg.QUIT:
                end = True
            # OPCIONES DEL MENU PRINCIPAL
            if event.type == pg.MOUSEBUTTONDOWN and p4 or event.type == pg.MOUSEBUTTONDOWN and p6 or event.type == pg.MOUSEBUTTONDOWN and p12: #GANA EL JUEGO:
                end = True
            if event.type == pg.MOUSEBUTTONDOWN and p3:
                # ms_click.play()
                # ms_click.set_volume(0.2)
                pg.display.quit()
                display = None
                display_game = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_credits = pg.display.set_mode([ancho,alto])
                display_credits.fill(negro)
                p3 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p2:
                # ms_click.play()
                # ms_click.set_volume(0.2)
                pg.display.quit()
                display = None
                display_game = None
                display_credits = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_options = pg.display.set_mode([ancho,alto])
                display_options.fill(negro)
                p2 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p1:
                # ms_click.play()
                # ms_click.set_volume(0.2)
                pg.display.quit()
                # msfondo.stop()
                # ms_perdio.stop()
                # ms_juego.stop()
                # ms_creditos.stop()
                # ms_juego.play()
                # ms_juego.set_volume(0.4)
                display = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p1 = False
                pg.display.flip()
            # OPCIONES DE CREDITOS
            if event.type == pg.MOUSEBUTTONDOWN and p5:
                # ms_click.play()
                # ms_click.set_volume(0.2)
                pg.display.quit()
                display_game = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_win = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p5 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p8:# PERDIO Y VA A REINTENTAR
                # ms_perdio.stop()
                # ms_click.play()
                # ms_click.set_volume(0.2)
                # ms_juego.play()
                # ms_juego.set_volume(0.4)
                pg.display.quit()
                display_endgame = None
                display_credits = None
                display_options = None
                display = None
                display_pause = None
                display_win = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p8 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p9: #PERDIO Y VA A SALIR
                # ms_perdio.stop()
                # ms_click.play()
                # ms_click.set_volume(0.2)
                # ms_juego.play()
                # ms_juego.set_volume(0.4)
                pg.display.quit()
                display_game = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_win = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p9 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p10: #PAUSA Y VUELVE A JUGAR
                # ms_click.play()
                # ms_click.set_volume(0.2)
                # msfondo.stop()
                # ms_juego.play()
                # ms_juego.set_volume(0.4)
                pg.display.quit()
                display = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p10 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p11: #PAUSA Y VA A SALIR
                # ms_click.play()
                pg.display.quit()
                # ms_juego.stop()
                display_game = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_win = None
                j.modificador = False
                i=240
                nivel = 0
                healt=1000
                healt_s = str(healt)
                hp = Messages.render(healt_s,True,negro,gris)
                j.shield=1000000
                shield_s = str(j.shield)
                shield_M = Messages.render(shield_s,True,negro,gris)
                j.rect.y=centro_y
                spawns,vidas_spawn,matriz_spawn_enemigo,matriz_spawn_enemigo_explosion = create_spawns()
                bloques = pg.sprite.Group()
                bloques = load_map(bloques,background)
                enemigos = pg.sprite.Group()
                nodriza_a.remove(mothership)
                mothership = Mothership(imagen_naveM)
                nodriza_a.add(mothership)
                nodriza_e.remove(mothership2)
                mothership2 = Mothership_E(imagen_naveME)
                nodriza_e.add(mothership2)
                modificadores1 = pg.sprite.Group()
                modificadores2 = pg.sprite.Group()
                modificadores3 = pg.sprite.Group()
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p11 = False
                pg.display.flip()
            # OPCIONES DE CREDITOS
            # OPCIONES DEL MENU DE OPCIONES XD
            if display_game != None:
##################################################################################################################################################################
                if event.type==pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pg.display.quit()
                        # ms_juego.stop()
                        # msfondo.play()
                        # msfondo.set_volume(0.3)
                        display_game = None
                        display_credits = None
                        display_options = None
                        display_endgame= None
                        display_win = None
                        display_pause = pg.display.set_mode([ancho,alto])
                        display_pause.fill(negro)
                        pass
                    if event.key == pg.K_DOWN:
                        if j.modificador:
                            j.vely=15
                            j.velx=0
                            j.fila3=4
                        elif j.modificador3:
                            j.vely=5
                            j.velx=0
                            j.fila=4
                        else:
                            j.vely= 10
                            j.velx= 0
                            j.fila = 4
                    if event.key == pg.K_UP:
                        if j.modificador:
                            j.vely=-15
                            j.velx=0
                            j.fila3=7
                        elif j.modificador3:
                            j.vely=-5
                            j.velx=0
                            j.fila=7
                        else:
                            j.vely=-10
                            j.velx=0
                            j.fila = 7
                    # if event.key == pg.K_RIGHT:
                    #     time.sleep(0.01)
                    #     if event.key == pg.K_UP:
                    #         j.velx=10
                    #         j.vely=-10
                    #         j.fila=7
                    if event.key== pg.K_SPACE:
                        # CREAR BALA
                        # ms_disparo_j.play()
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
                    j.fila3=2
##################################################################################################################################################################
        if display_game != None:
            # CAJA DE CONTROL
            # LIMPIEZA DE BALAS AL SALIR DE PANTALLA
            for b in balas_jugador:
                if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                    balas_jugador.remove(b)

            for b in balas_enemigos:
                if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                    balas_enemigos.remove(b)

            # LIMPIEZA DE MODIFICADORES
            for m in modificadores1:
                if m.rect.x <= 100:
                    modificadores1.remove(m)
            for m in modificadores2:
                if m.rect.x <= 100:
                    modificadores2.remove(m)
            for m in modificadores3:
                if m.rect.x <= 100:
                    modificadores3.remove(m)

######################################################################################################
            # ESCUDO DE INTANGIBILIDAD
            ls = pg.sprite.spritecollide(j,bloques,False)
            for b in ls:
                if b.OnLimit(j.pos):
                    j.shield-=10
                    shield_s = str(j.shield)
                    shield_M = Messages.render(shield_s,True,negro,gris)
                    j.BlockDeath(b)
##################################################################################################################################################################

            if nivel != 0:
                #CREACION DE LOS RIVALES DESDE EL SPAWN
                for s in spawns:
                    if s.tempo == 0 :
                        s.tempo = random.randrange(50,150)
                        pos = s.rect.topleft
                        e = Rival(matriz_enemigo,matriz_red_explotion,pos)
                        enemigos.add(e)
                        oportunidad = random.randrange(100)
                        if oportunidad > 80:
                            mod = Slow(matriz_modificador3,matriz_red_explotion,pos)
                            modificadores3.add(mod)
                    if s.tempo2 == 0 :
                        s.tempo2 = random.randrange(300,500)
                        pos = s.rect.topleft
                        e = Rival2(matriz_enemigo2,matriz_red_explotion,pos)
                        enemigos2.add(e)
                #DISPAROS DE LOS RIVALES
                for e in enemigos:
                    if e.tempo == 0:
                        e.tempo = random.randrange(10)
                        pos = e.rect.topleft
                        pos1 = [pos[0],pos[1]+20]
                        e = Bala(pos1,matriz_bala_enemigo,5)
                        balas_enemigos.add(e)
                        e.velx = -30
                        # ms_disparo_e.play()

                ############################################################
                #COLISION DE LAS BALAS DEL JUGADOR CON LOS ENEMIGOS
                for b in balas_jugador:
                    le = pg.sprite.spritecollide(b,enemigos,False)#no borra cuando hay colision
                    for r in le:
                        r.muerte = 1
                        balas_jugador.remove(b)
                #COLISION DE LAS BALAS DEL JUGADOR CON LOS ENEMIGOS2
                for b in balas_jugador:
                    le = pg.sprite.spritecollide(b,enemigos2,False)#no borra cuando hay colision
                    for r in le:
                        r.muerte = 1
                        balas_jugador.remove(b)

                ################################################################
                #EXPLOSION ENEMIGOS CON BALAS DE JUGADOR Y CREACION DE LOS MODIFICADORES 1
                for e in enemigos2:
                    if e.muerte == 1 and e.col2 == 12:
                        if not(e.luck):
                            e.luck = True
                            luck = random.randrange(100)
                            if luck < probMod1:
                                pos = e.rect.topleft
                                m = Skin(matriz_modificador1,matriz_blue_explotion,pos)
                                modificadores1.add(m)
                        # ms_explosion.play()
                        enemigos2.remove(e)
                ##EXPLOSION ENEMIGOS CON BALAS DE JUGADOR Y CREACION DE LOS MODIFICADORES 2
                for e in enemigos:
                    if e.muerte == 1 and e.col2 == 12:
                        if not(e.luck):
                            e.luck = True
                            luck = random.randrange(100)
                            if luck < probMod2:
                                pos = e.rect.topleft
                                m = Mas1Vida(matriz_modificador2,matriz_blue_explotion,pos)
                                modificadores2.add(m)
                        # ms_explosion.play()
                        enemigos.remove(e)

                #######################################################
                # COLISION DEL JUGADOR CON LOS MODIFICADORES
                if len(modificadores1) >= 0:
                    #COLISION DEL JUGADOR CON LOS MODIFICADORES 1
                    le = pg.sprite.spritecollide(j,modificadores1,False)#no borra cuando hay colision
                    for r in le:
                        # ms_modBuenos.play()
                        r.muerte = 1
                        j.modificador = True
                        punto_partida_modificador1 = i
                        j.modificador3 = False
                if len(modificadores2) >= 0:
                    # COLISION DEL JUGADOR CON EL MODIFICADOR 2
                    lV = pg.sprite.spritecollide(j,modificadores2,False)#no borra cuando hay colision
                    for r in lV:
                        # ms_modBuenos.play()
                        r.muerte = 1
                        if r.masvida:
                            r.masvida = False
                            j.vidas += 1
                            vidas_jugador = j.vidas
                if len(modificadores3) >= 0:
                    #COLISION DEL JUGADOR CON LOS MODIFICADORES 1
                    le = pg.sprite.spritecollide(j,modificadores3,False)#no borra cuando hay colision
                    for r in le:
                        # ms_modMalos.play()
                        r.muerte = 1
                        j.modificador3 = True
                        j.modificador = False
                # print(j.vidas)
                # FIN DEL MODIFICADOR
                    # POR DEFINIR

                ################################################################################################
                #EXPLOSION ENEMIGOS CON BALAS DE JUGADOR
                for e in modificadores1:
                    if e.muerte == 1 and e.col2 == 16:
                        modificadores1.remove(e)

                # EXPLOSION MODIFICADORES 2
                for e in modificadores2:
                    if e.muerte == 1 and e.col2 == 16:
                        modificadores2.remove(e)

                for e in modificadores3:
                    if e.muerte == 1 and e.col2 == 12:
                        modificadores2.remove(e)
                #################################################
                #DISMINUIR VIDAS DE SPAWN CON BALAS DE JUGADOR
                for b in balas_jugador:
                    ls = pg.sprite.spritecollide(b,spawns,False)#
                    for r in ls:
                        r.vidas -= 1
                        balas_jugador.remove(b)

                # ELIMINACION DE SPAWNS
                for s in spawns:
                    if s.vidas <= 0 and s.col2 == 13:
                        # ms_explosion.play()
                        spawns.remove(s)
                #######################################################
                #COLISION DE LAS BALAS DE LOS ENEMIGOS CON EL JUGADOR
                for b in balas_enemigos:
                    ls = pg.sprite.spritecollide(b,jugadores,False)
                    for r in ls:
                        balas_enemigos.remove(b)
                        j.vidas -= 1
                        if vidas_jugador > 0:
                            vidas_jugador = j.vidas

                ######################################################
                # COLISION DE ENEMIGOS CON LA NAVE NODRIZA
                ls = pg.sprite.spritecollide(mothership,enemigos,False)
                for c in ls:
                    if c.rect.x <= 150:
                        enemigos.remove(c)
                        healt-=10
                        healt_s = str(healt)
                        hp = Messages.render(healt_s,True,negro,gris)
                ls = pg.sprite.spritecollide(mothership,enemigos2,False)
                for c in ls:
                    if c.rect.x <= 150:
                        enemigos2.remove(c)
                        healt-=10
                        healt_s = str(healt)
                        hp = Messages.render(healt_s,True,negro,gris)
                #######################################################
                # ELIMINACION DEL JUGADOR
                for j in jugadores:
                    if j.vidas <= 0 and j.col2 == 16:
                        print("loser")
                        # ms_juego.stop()
                        # msfondo.stop()
                        # ms_perdio.play()
                        j.vidas = 3
                        j.modificador = False
                        vidas_jugador = j.vidas
                        pg.display.quit()
                        display_game = None
                        display_credits = None
                        display_options = None
                        display_win = None
                        i=240
                        nivel = 0
                        healt=1000
                        healt_s = str(healt)
                        hp = Messages.render(healt_s,True,negro,gris)
                        j.shield=1000000
                        shield_s = str(j.shield)
                        shield_M = Messages.render(shield_s,True,negro,gris)
                        j.rect.y=centro_y
                        spawns,vidas_spawn,matriz_spawn_enemigo,matriz_spawn_enemigo_explosion = create_spawns()
                        bloques = pg.sprite.Group()
                        bloques = load_map(bloques,background)
                        enemigos = pg.sprite.Group()
                        balas_enemigos = pg.sprite.Group()
                        nodriza_a.remove(mothership)
                        mothership = Mothership(imagen_naveM)
                        nodriza_a.add(mothership)
                        nodriza_e.remove(mothership2)
                        mothership2 = Mothership_E(imagen_naveME)
                        nodriza_e.add(mothership2)
                        modificadores1 = pg.sprite.Group()
                        modificadores2 = pg.sprite.Group()
                        modificadores3 = pg.sprite.Group()
                        display_endgame = pg.display.set_mode([ancho,alto])
                        display_endgame.fill(negro)
##################################################################################################################################################################
            if display_game != None:
                loser = False
                if healt <= 0 or j.shield <=0:
                    print("loser")
                    # ms_juego.stop()
                    # msfondo.stop()
                    # ms_perdio.play()
                    # ms_perdio.set_volume(0.4)
                    j.vidas = 3
                    j.modificador = False
                    vidas_jugador = j.vidas
                    pg.display.quit()
                    display_game = None
                    display_credits = None
                    display_options = None
                    display_win = None
                    loser = True
                    i=240
                    nivel = 0
                    healt=1000
                    healt_s = str(healt)
                    hp = Messages.render(healt_s,True,negro,gris)
                    j.shield=1000000
                    shield_s = str(j.shield)
                    shield_M = Messages.render(shield_s,True,negro,gris)
                    j.rect.y=centro_y
                    spawns,vidas_spawn,matriz_spawn_enemigo,matriz_spawn_enemigo_explosion = create_spawns()
                    bloques = pg.sprite.Group()
                    bloques = load_map(bloques,background)
                    enemigos = pg.sprite.Group()
                    balas_enemigos = pg.sprite.Group()
                    nodriza_a.remove(mothership)
                    mothership = Mothership(imagen_naveM)
                    nodriza_a.add(mothership)
                    nodriza_e.remove(mothership2)
                    mothership2 = Mothership_E(imagen_naveME)
                    nodriza_e.add(mothership2)
                    modificadores1 = pg.sprite.Group()
                    modificadores2 = pg.sprite.Group()
                    display_endgame = pg.display.set_mode([ancho,alto])
                    display_endgame.fill(negro)

                if i == -ancho_fondo + ancho:
                    i = 0
                    nivel = -64*11
                    for b in bloques:
                        bloques.remove(b)
    ##################################################################################################################################################################
                i-=8
                jugadores.update()
                if nivel != 0:
                    nodriza_a.update()
                    spawns.update()
                    enemigos.update()
                    enemigos2.update()
                    balas_enemigos.update()
                    modificadores1.update()
                    modificadores2.update()
                    modificadores3.update()
                continuara = False
                if len(spawns) <= 0:
                    nodriza_e.update()
                    if mothership2.rect.x == ancho - 200:
                        EndMessage= "TO  BE  CONTINUE  ... "
                        EndMessage = Messages.render(EndMessage,True,rojo,azul)
                        pos_w = centrar_texto(EndMessage)
                        display_game.blit(EndMessage,[pos_w,300])
                        pg.display.flip()
                        j.vidas = 3
                        continuara= True
                        j.modificador = False
                        vidas_jugador = j.vidas
                        time.sleep(5)
                        pg.display.quit()
                        display_game = None
                        display_credits = None
                        display_options = None
                        display_pause= None
                        display_endgame= None
                        # ms_juego.stop()
                        # ms_perdio.stop()
                        # msfondo.stop()
                        # ms_creditos.play()
                        # ms_creditos.set_volume(0.3)
                        i=240
                        nivel = 0
                        healt=1000
                        healt_s = str(healt)
                        hp = Messages.render(healt_s,True,negro,gris)
                        j.shield=1000000
                        shield_s = str(j.shield)
                        shield_M = Messages.render(shield_s,True,negro,gris)
                        j.rect.y=centro_y
                        spawns,vidas_spawn,matriz_spawn_enemigo,matriz_spawn_enemigo_explosion = create_spawns()
                        bloques = pg.sprite.Group()
                        bloques = load_map(bloques,background)
                        enemigos = pg.sprite.Group()
                        balas_enemigos = pg.sprite.Group()
                        nodriza_a.remove(mothership)
                        mothership = Mothership(imagen_naveM)
                        nodriza_a.add(mothership)
                        nodriza_e.remove(mothership2)
                        mothership2 = Mothership_E(imagen_naveME)
                        nodriza_e.add(mothership2)
                        modificadores1 = pg.sprite.Group()
                        modificadores2 = pg.sprite.Group()
                        modificadores3 = pg.sprite.Group()
                        display_win = pg.display.set_mode([ancho,alto])
                        display_win.fill(negro)
                if nivel == 0:
                    bloques.update()
                balas_jugador.update()
                # ACTUALIZACIONES
                if not continuara and not loser:
                    display_game.fill(negro)
                    # display_game.blit(background2,[i,nivel])
                    jugadores.draw(display_game)
                if nivel ==0 and not continuara and not loser:
                    display_game.fill(negro)
                    # display_game.blit(background2,[i,nivel])
                    jugadores.draw(display_game)
                    bloques.draw(display_game)
                if nivel!=0 and not continuara and not loser:
                    nodriza_a.draw(display_game)
                    spawns.draw(display_game)
                    enemigos.draw(display_game)
                    enemigos2.draw(display_game)
                    balas_jugador.draw(display_game)
                    balas_enemigos.draw(display_game)
                    modificadores1.draw(display_game)
                    modificadores2.draw(display_game)
                    modificadores3.draw(display_game)
                if len(spawns) <= 0 and  not continuara and not loser:
                    nodriza_e.draw(display_game)

                # MENSAJE DE ADVERTENCIA INICIAL
                if i >= -2000 and nivel == 0 and not continuara and not loser:
                    display_game.blit(WarningM,[pos_w,0])
                j_vidas = 'Vidas: '+ str(vidas_jugador)
                texto = Messages.render(j_vidas,True,negro,gris)
                if not continuara and not loser:
                    display_game.blit(texto,[200,0])
                    display_game.blit(salud,[0,0])
                    display_game.blit(escudo,[0,32])
                    display_game.blit(hp,[100,0])
                    display_game.blit(shield_M,[100,32])
                pg.display.flip()
                reloj.tick(30)