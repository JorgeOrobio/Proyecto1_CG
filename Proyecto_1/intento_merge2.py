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

def load_map(bloques,background):
##################################################################################################################################################################
    # IMAGENES DE BLOQUES Y FONDO
    # background = pg.image.load("/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/background.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background = pg.image.load("/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/mapa2.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
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
    direccion_imagen_spawn_enemigo = "/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/comm_redship/spawn.png"
    #direccion_imagen_spawn_enemigo = "/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/comm_redship/spawn.png"
    imagen_spawn_enemigo = pg.image.load(direccion_imagen_spawn_enemigo)
    matriz_spawn_enemigo=matriz_sprites(imagen_spawn_enemigo,273,88,91,88)

    #MUERTE DE LOS SPAWNS ENEMIGOS
    direccion_imagen_spawn_enemigo_explosion = "/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    #direccion_imagen_spawn_enemigo_explosion = "/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    imagen_spawn_enemigo_explosion = pg.image.load(direccion_imagen_spawn_enemigo_explosion)
    matriz_spawn_enemigo_explosion=matriz_sprites(imagen_spawn_enemigo_explosion,896,64,64,64)

    #CREACION SPAWN
    posx_spawns = 980
    posy_spawns = 60
    esp_entre = 20
    s = Spawn([posx_spawns,posy_spawns],matriz_spawn_enemigo,matriz_spawn_enemigo_explosion)
    ##aumentar posx_spawns para que el spawn quede fuera de la pantalla
    for i in range(posy_spawns,alto - s.rect.height-esp_entre,s.rect.height+esp_entre):
        s = Spawn([posx_spawns,posy_spawns],matriz_spawn_enemigo,matriz_spawn_enemigo_explosion)
        spawns.add(s)
        posy_spawns += s.rect.height+esp_entre
    vidas_spawn = s.vidas
    return spawns,vidas_spawn,matriz_spawn_enemigo,matriz_spawn_enemigo_explosion

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    display = pg.display.set_mode([ancho,alto])
    display_credits = None
    display_options = None
    display_game = None
    display_endgame = None
    display_pause = None
    # GRUPOS
    bloques = pg.sprite.Group()
    jugadores=pg.sprite.Group()
    balas_jugador=pg.sprite.Group()
    nodriza_a = pg.sprite.Group()
    enemigos = pg.sprite.Group()
    balas_enemigos = pg.sprite.Group()
    nodriza_e = pg.sprite.Group()
    spawns = pg.sprite.Group()
    modificadores1 = pg.sprite.Group()
##################################################################################################################################################################
    # IMAGENES DE BLOQUES Y FONDO
    # background = pg.image.load("/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/mapa2.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background = pg.image.load("/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Mapa/mapa2.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    ancho_fondo = 9216
    bloques = load_map(bloques,background)
##################################################################################################################################################################

    # ALIADOS

    # JUGADOR
    dirreccion_imagen_jugador="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada_sf.png"
    #dirreccion_imagen_jugador="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada_sf.png"
    imagen_jugador=pg.image.load(dirreccion_imagen_jugador)
    matriz_jugador=matriz_sprites(imagen_jugador,320,512,64,64)

    #SKIN ROJA JUGADOR
    dirreccion_imagen_jugador_explosion="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada_sf_OP.png"
    #dirreccion_imagen_jugador_explosion="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada_sf_OP.png"
    imagen_jugador2=pg.image.load(dirreccion_imagen_jugador_explosion)
    matriz_jugador2=matriz_sprites(imagen_jugador2,320,512,64,64)

    #EXPLOSION JUGADOR
    dirreccion_imagen_jugador_explosion="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Blue Effects/explosion_blue.png"
    #dirreccion_imagen_jugador_explosion="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Blue Effects/explosion_blue.png"
    imagen_jugador_explosion=pg.image.load(dirreccion_imagen_jugador_explosion)
    matriz_jugador_explosion=matriz_sprites(imagen_jugador_explosion,1088,64,64,64)



    # NAVE NODRIZA
    dirreccion_imagen_naveM="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/mothership.png"
    #dirreccion_imagen_naveM="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/mothership.png"
    imagen_naveM=pg.image.load(dirreccion_imagen_naveM)


##################################################################################################################################################################
    # ENEMIGOS

    # ENEMIGOS
    direccion_imagen_enemigo="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/Enemy_animation/enemigo11.png"
    #direccion_imagen_enemigo="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/Enemy_animation/enemigo11.png"
    imagen_enemigo=pg.image.load(direccion_imagen_enemigo)
    matriz_enemigo=matriz_sprites(imagen_enemigo,560,80,80,80)

    # NAVE NODRIZA ENEMIGA
    dirreccion_imagen_naveME="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/enemigos/mothership.png"
    #dirreccion_imagen_naveM="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/mothership.png"
    imagen_naveME=pg.image.load(dirreccion_imagen_naveM)

    #MUERTE ENEMIGOS
    direccion_imagen_enemigo_expl="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    #direccion_imagen_enemigo_expl="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    imagen_enemigo_explosion=pg.image.load(direccion_imagen_enemigo_expl)
    matriz_enemigo_explosion=matriz_sprites(imagen_enemigo_explosion,896,64,64,64)

    ##SPAWN DE LOS ENEMIGOS
    direccion_imagen_spawn_enemigo = "/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/comm_redship/spawn.png"
    #direccion_imagen_spawn_enemigo = "/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/comm_redship/spawn.png"
    imagen_spawn_enemigo = pg.image.load(direccion_imagen_spawn_enemigo)
    matriz_spawn_enemigo=matriz_sprites(imagen_spawn_enemigo,273,88,91,88)

    #MUERTE DE LOS SPAWNS ENEMIGOS
    direccion_imagen_spawn_enemigo_explosion = "/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    #direccion_imagen_spawn_enemigo_explosion = "/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    imagen_spawn_enemigo_explosion = pg.image.load(direccion_imagen_spawn_enemigo_explosion)
    matriz_spawn_enemigo_explosion=matriz_sprites(imagen_spawn_enemigo_explosion,896,64,64,64)

    #MODIFICADORES DE ASPECTO
    direccion_imagen_modificador1 = "/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Blue/Spacemines/minas.png"
    #direccion_imagen_modificador1 = "/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Blue/Spacemines/minas.png"
    imagen_modificador1 = pg.image.load(direccion_imagen_modificador1)
    matriz_modificador1=matriz_sprites(imagen_modificador1,80,40,40,40)

    #MODIFICADOR DESTRUIDO
    direccion_imagen_modificador1_explosion = "/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Blue Effects/explosion_blue.png"
    #direccion_imagen_modificador1_explosion ="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Blue Effects/explosion_blue.png"
    imagen_modificador1_explosion = pg.image.load(direccion_imagen_modificador1_explosion)
    matriz_modificador1_explosion=matriz_sprites(imagen_modificador1_explosion,1088,64,64,64)
##################################################################################################################################################################
    # BALAS

    # BALAS JUGADOR
    direccion_imagen_bala_jugador="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_blue.png"
    #direccion_imagen_bala_jugador="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_blue.png"
    imagen_bala_jugador=pg.image.load(direccion_imagen_bala_jugador)
    matriz_bala_jugador=matriz_sprites(imagen_bala_jugador,304,38,38,38)

    # BALAS ENEMIGO
    direccion_imagen_bala_enemigo="/home/jorge/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_red.png"
    #direccion_imagen_bala_enemigo="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_red.png"
    imagen_bala_enemigo=pg.image.load(direccion_imagen_bala_enemigo)
    matriz_bala_enemigo=matriz_sprites(imagen_bala_enemigo,304,38,38,38)

##################################################################################################################################################################

    # CREACIONES

    # CREACION DE JUGADOR
    j=Jugador(matriz_jugador,matriz_jugador_explosion,matriz_jugador2)
    jugadores.add(j)
    #manejo de la vidas jugador
    vidas_jugador = j.vidas



    # CREACION DE SPAWNS
    spawns,vidas_spawn,matriz_spawn_enemigo,matriz_spawn_enemigo_explosion = create_spawns()

    # CREACION NAVE NODRIZA
    mothership = Mothership(imagen_naveM)
    nodriza_a.add(mothership)
    mothership2 = Mothership_E(imagen_naveME)
    nodriza_e.add(mothership2)

##################################################################################################################################################################
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
##################################################################################################################################################################
    #MUSICA
    pg.mixer.init()
    msfondo = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/MUSE.ogg")
    #msfondo = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/MUSE.ogg")
    ms_click = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/CloudClick.ogg")
    #ms_click = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/CloudClick.ogg")
    ms_disparo_j = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/laser_jugaddor.ogg")
    #ms_disparo_j = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/laser_jugaddor.ogg.ogg")
    ms_disparo_e = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/laser_enemigo.ogg")
    #ms_disparo_e = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/laser_enemigo.ogg.ogg")
    ms_creditos = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/End_Credits_Theme_ogg.ogg")
    #ms_creditos = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/End_Credits_Theme_ogg.ogg")
    ms_explosion = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/explosion.ogg")
    #ms_explosion = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/explosion.ogg")
    ms_perdio = pg.mixer.Sound("/home/jorge/github/Proyecto1_CG/Descargas/NoHope.ogg")
    #ms_perdio = pg.mixer.Sound("/home/nicolas/github/Proyecto1_CG/Descargas/NoHope.ogg")
##################################################################################################################################################################
    # FINALIZADORES DE ETAPAS(JUEGO, PAUSA, MENU), Y VARIABLES
    i=240 #POSICION DEL FONDO PARA EL DESPLAZAMIENTO
    nivel=0
    probMod1 = 80
    reloj=pg.time.Clock()
    end = False
    game_over = False
    pause = False
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11 = False,False,False,False,False,False,False,False,False,False,False
    msfondo.play()
    msfondo.set_volume(.1)
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
        for event in event:
            if event.type == pg.QUIT:
                end = True
            # OPCIONES DEL MENU PRINCIPAL
            if event.type == pg.MOUSEBUTTONDOWN and p4 or event.type == pg.MOUSEBUTTONDOWN and p6:
                end = True
            if event.type == pg.MOUSEBUTTONDOWN and p3:
                ms_click.play()
                #ms_click.set_volume(.3)
                pg.display.quit()
                display = None
                display_game = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_credits = pg.display.set_mode([ancho,alto])
                display_credits.fill(negro)
                p3 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p2:
                ms_click.play()
                pg.display.quit()
                display = None
                display_game = None
                display_credits = None
                display_endgame = None
                display_pause = None
                display_options = pg.display.set_mode([ancho,alto])
                display_options.fill(negro)
                p2 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p1:
                ms_click.play()
                pg.display.quit()
                display = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p1 = False
                pg.display.flip()
            # OPCIONES DE CREDITOS
            if event.type == pg.MOUSEBUTTONDOWN and p5:
                ms_click.play()

                pg.display.quit()
                display_game = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p5 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p8:# PERDIO Y VA A REINTENTAR
                ms_click.play()
                pg.display.quit()
                display_endgame = None
                display_credits = None
                display_options = None
                display = None
                display_pause = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p8 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p9: #PERDIO Y VA A SALIR
                ms_click.play()
                pg.display.quit()
                display_game = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p9 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p10: #PAUSA Y VUELVE A JUGAR
                ms_click.play()
                pg.display.quit()
                display = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p10 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p11: #PAUSA Y VA A SALIR
                ms_click.play()
                pg.display.quit()
                display_game = None
                display_credits = None
                display_options = None
                display_endgame = None
                display_pause = None
                j.modificador = False
                i=240
                nivel = 0
                healt=1000
                healt_s = str(healt)
                hp = Messages.render(healt_s,True,negro,gris)
                shield=100000
                shield_s = str(shield)
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
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p11 = False
                pg.display.flip()
            # OPCIONES DEL MENU DE OPCIONES XD
            if display_game != None:
##################################################################################################################################################################
                if event.type==pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pg.display.quit()
                        display_game = None
                        display_credits = None
                        display_options = None
                        display_endgame= None
                        display_pause = pg.display.set_mode([ancho,alto])
                        display_pause.fill(negro)
                        pass
                    if event.key == pg.K_DOWN:
                        j.vely=10
                        j.velx=0
                        j.fila=4
                        j.fila3 = 4
                    if event.key == pg.K_UP:
                        j.vely=-10
                        j.velx=0
                        j.fila=7
                        j.fila3 = 7
                    # if event.key == pg.K_RIGHT:
                    #     time.sleep(0.01)
                    #     if event.key == pg.K_UP:
                    #         j.velx=10
                    #         j.vely=-10
                    #         j.fila=7
                    if event.key== pg.K_SPACE:
                        # CREAR BALA
                        ms_disparo_j.play()
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
##################################################################################################################################################################
        if display_game != None:
        # CAJA DE CONTROL

            # LIMPIEZA DE BALAS AL SALIR DE PANTALLA
            for b in balas_jugador:
                if b.rect.x<0 or b.rect.x>ancho or b.rect.y>alto or b.rect.y<0:
                    balas_jugador.remove(b)

            # ESCUDO DE INTANGIBILIDAD
            ls = pg.sprite.spritecollide(j,bloques,False)
            for b in ls:
                if b.OnLimit(j.pos):
                    shield-=10
                    shield_s = str(shield)
                    shield_M = Messages.render(shield_s,True,negro,gris)
                    j.BlockDeath(b)
##################################################################################################################################################################

            if nivel != 0:
                #CREACION DE LOS RIVALES DESDE EL SPAWN
                for s in spawns:
                    if s.tempo == 0 :
                        s.tempo = random.randrange(50,100)
                        pos = s.rect.topleft
                        e = Rival(matriz_enemigo,matriz_enemigo_explosion,pos)
                        enemigos.add(e)
                #DISPAROS DE LOS RIVALES
                for e in enemigos:
                    if e.tempo == 0:
                        e.tempo = random.randrange(10)
                        pos = e.rect.topleft
                        pos1 = [pos[0],pos[1]+20]
                        e = Bala(pos1,matriz_bala_enemigo,5)
                        balas_enemigos.add(e)
                        ms_disparo_e.play()
                        e.velx = -30

                #COLISION DE LAS BALAS DEL JUGADOR CON LOS ENEMIGOS
                for b in balas_jugador:
                    le = pg.sprite.spritecollide(b,enemigos,False)#no borra cuando hay colision
                    for r in le:
                        r.muerte = 1
                        balas_jugador.remove(b)

                #Eliminar enemigos con balas jugador Y CREACION DE LOS MODIFICADORES 1
                for e in enemigos:
                    if e.muerte == 1 and e.col2 == 12:
                        if not(e.luck):
                            e.luck = True
                            luck = random.randrange(100)
                            if luck < probMod1:
                                pos = e.rect.topleft
                                m = Skin(matriz_modificador1,matriz_modificador1_explosion,pos)
                                modificadores1.add(m)
                        enemigos.remove(e)
                        ms_explosion.play()
                #COLISION DE LAS BALAS DEL JUGADOR CON LOS MODIFICADORES 1
                for b in balas_jugador:
                    le = pg.sprite.spritecollide(b,modificadores1,False)#no borra cuando hay colision
                    for r in le:
                        r.muerte = 1
                        j.modificador = True

                #Eliminar enemigos con balas jugador
                for e in modificadores1:
                    if e.muerte == 1 and e.col2 == 16:
                        modificadores1.remove(e)
                #Eliminar spawn con balas jugador
                for b in balas_jugador:
                    ls = pg.sprite.spritecollide(b,spawns,False)#
                    for r in ls:
                        r.vidas -= 1
                        balas_jugador.remove(b)

                # ELIMINACION DE SPAWNS
                for s in spawns:
                    if s.vidas <= 0 and s.col2 == 13:
                        ms_explosion.play()
                        spawns.remove(s)

                #COLISION DE LAS BALAS DE LOS ENEMIGOS CON EL JUGADOR
                for b in balas_enemigos:
                    ls = pg.sprite.spritecollide(b,jugadores,False)
                    for r in ls:
                        balas_enemigos.remove(b)
                        j.vidas -= 1
                        if vidas_jugador > 0:
                            vidas_jugador = j.vidas

                # ELIMINACION DEL JUGADOR
                for j in jugadores:
                    if j.vidas <= 0 and j.col2 == 16:
                        msfondo.stop()
                        ms_perdio.play()
                        print("loser")
                        j.vidas = 3
                        j.modificador = False
                        vidas_jugador = j.vidas
                        pg.display.quit()
                        display_game = None
                        display_credits = None
                        display_options = None
                        i=240
                        nivel = 0
                        healt=1000
                        healt_s = str(healt)
                        hp = Messages.render(healt_s,True,negro,gris)
                        shield=100000
                        shield_s = str(shield)
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
                        display_endgame = pg.display.set_mode([ancho,alto])
                        display_endgame.fill(negro)
##################################################################################################################################################################
            if display_game != None:
                if i == -ancho_fondo + ancho:
                    i = 0
                    nivel = -64*11
                    for b in bloques:
                        bloques.remove(b)
    ##################################################################################################################################################################
                i-=8
                if shield <=0:
                    game_over = True
                jugadores.update()
                if nivel != 0:
                    nodriza_a.update()
                    spawns.update()
                    enemigos.update()
                    balas_enemigos.update()
                    modificadores1.update()
                if len(spawns) <= 0:
                    nodriza_e.update()
                if nivel == 0:
                    bloques.update()
                balas_jugador.update()
                # ACTUALIZACIONES
                display_game.blit(background,[i,nivel])
                jugadores.draw(display_game)
                if nivel ==0:
                    bloques.draw(display_game)
                if nivel!=0:
                    print(len(modificadores1))
                    nodriza_a.draw(display_game)
                    spawns.draw(display_game)
                    enemigos.draw(display_game)
                    balas_jugador.draw(display_game)
                    balas_enemigos.draw(display_game)
                    modificadores1.draw(display_game)
                if len(spawns) <= 0:
                    nodriza_e.draw(display_game)

                # MENSAJE DE ADVERTENCIA INICIAL
                if i >= -2000 and nivel == 0:
                    display_game.blit(WarningM,[pos_w,0])
                j_vidas = 'Vidas: '+ str(vidas_jugador)
                texto = Messages.render(j_vidas,True,negro,gris)
                display_game.blit(texto,[200,0])
                display_game.blit(salud,[0,0])
                display_game.blit(escudo,[0,32])
                display_game.blit(hp,[100,0])
                display_game.blit(shield_M,[100,32])
                pg.display.flip()
                reloj.tick(30)
