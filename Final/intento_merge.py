import pygame as pg
from libreria import*
from Personaje2 import*
from Spawn import *
from Spawn2 import *
from Spawn3 import *
from Bala import*
from Bala_Seguidora import*
from Mothership import *
from Objetos import *
from Enemigos import *
from Enemigos2 import *
from Enemigos3 import *
from Enemigos4 import *
from Mothership_E import *
from Modificador1 import*
from Modificador2 import*
from Modificador3 import*
import time
import random
import sys

def menu_options():
    pass

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
    return spawns


def load_map2(bloques,background):
##################################################################################################################################################################
    # EXPLOSION DE LOS BLOQUES
    dirreccion_imagen_explosion="Sprites/Efectos/explosion_asteroides.png"
    imagen_explosion=pg.image.load(dirreccion_imagen_explosion)
    matriz_explosion=matriz_sprites(imagen_explosion,384,64,64,64)
    # APARTADO DE BLOQUES
    tam_sy, tam_sx = 51,51
    matrix_x,matrix_y=0,0
    i,j=0,0
    ancho_fondo = 204
    alto_fondo = 51
    matrix_background = matriz_sprites(background,ancho_fondo,alto_fondo,tam_sx,tam_sy)
    mapaf = open("mapa2n.txt",'r')
    mapaf = mapaf.read()
    mapaf=mapaf.split('\n')
    # AGREGANDO BLOQUES DEL MAPA
    for filas in mapaf:
        for ele in filas:
            # AQUI PUEDE AGREGAR LA CONDICION PARA AGREGAR BLOQUES
            if ele == "&":
                matrix_x,matrix_y = 0,0
                b = Bloque(matrix_background[matrix_x][matrix_y],[i,j],matriz_explosion)
                bloques.add(b)
            if ele == "#":
                matrix_x,matrix_y = 1,0
                b = Bloque(matrix_background[matrix_x][matrix_y],[i,j],matriz_explosion)
                bloques.add(b)
            if ele == "*":
                matrix_x,matrix_y = 2,0
                b = Bloque(matrix_background[matrix_x][matrix_y],[i,j],matriz_explosion)
                bloques.add(b)
            if ele == "$":
                matrix_x,matrix_y = 3,0
                b = Bloque(matrix_background[matrix_x][matrix_y],[i,j],matriz_explosion)
                bloques.add(b)
            if ele == ".":
                matrix_x,matrix_y = 4,0
            # display_game.blit(matrix_background[x][matrix_y],[i,j])
            i+=tam_sx
        i=0
        j+=tam_sy
    return bloques,matriz_explosion
##################################################################################################################################################################
    pass

def create_spawns2():
    spawns2 = pg.sprite.Group()
    spawns3 = pg.sprite.Group()
    ##SPAWN DE LOS ENEMIGOS2
    direccion_imagen_spawn_enemigo2 = "Sprites/Personaje/enemigos/spawn2.png"
    imagen_spawn_enemigo2 = pg.image.load(direccion_imagen_spawn_enemigo2)
    matriz_spawn_enemigo2 =matriz_sprites(imagen_spawn_enemigo2,128,64,64,64)

    dir_red_explotion2="Sprites/Efectos/Explosion_red.png"
    imagen_red_explotion2=pg.image.load(dir_red_explotion2)
    matriz_red_explotion=matriz_sprites(imagen_red_explotion2,896,64,64,64)

    #SPAWN ENEMIGOS 3
    direccion_imagen_spawn_enemigo3 = "Sprites/Personaje/enemigos/spawns3.png"
    imagen_spawn_enemigo3 = pg.image.load(direccion_imagen_spawn_enemigo3)
    matriz_spawn_enemigo3 =matriz_sprites(imagen_spawn_enemigo3,128,64,64,64)

    #CREACION SPAWN
    posx_spawns2 = 980
    posy_spawns2 = -alto + 150
    posx_spawns3 = 980
    posy_spawns3 = -alto + 20
    esp_entre = 40
    s2 = Spawn2([posx_spawns2,posy_spawns2],matriz_spawn_enemigo2,matriz_red_explotion)
    s3 = Spawn3([posx_spawns3,posy_spawns3],matriz_spawn_enemigo3,matriz_red_explotion)
    spawns3.add(s3)
    ##aumentar posx_spawns para que el spawn quede fuera de la pantalla
    for i in range(posy_spawns2,0 - s2.rect.height-esp_entre,s2.rect.height+esp_entre):
        s2 = Spawn2([posx_spawns2,posy_spawns2],matriz_spawn_enemigo2,matriz_red_explotion,alto+posy_spawns2)
        spawns2.add(s2)
        posy_spawns2 += s2.rect.height+esp_entre
    return spawns2,spawns3




def clean_group(grupo):
    for g in grupo:
        grupo.remove(g)
    return grupo
    pass

def animacion_final_nivel_1(display_game,nodriza_a,nodriza_e,jugadores,modificadores3,background2,healt,reloj,i,subnivel):
    print("animacion")
    while healt >= 0:
        healt-=10
        Messages = pg.font.Font(None,32)
        healt_s = str(healt)
        hp = Messages.render(healt_s,True,negro,gris)
        hp_n =Messages.render(healt_s,True,negro,negro)
        display_game.blit(hp_n,[100,0])
        pg.display.flip()
        display_game.blit(hp,[100,0])
        pg.display.flip()
        reloj.tick(30)
    print("1")
    for e in nodriza_a:
        while e.rect.x <= 500 - e.rect.width:
            e.rect.x += 10
            display_game.blit(background2,[i,subnivel])
            jugadores.draw(display_game)
            enemigos.draw(display_game)
            enemigos2.draw(display_game)
            modificadores3.draw(display_game)
            nodriza_a.draw(display_game)
            nodriza_e.draw(display_game)
            pg.display.flip()
            reloj.tick(30)
    print("2")
    time.sleep(2)
    for e in nodriza_a:
        while e.rect.x >= 300 - e.rect.width:
            e.rect.x -= 10
            display_game.blit(background2,[i,subnivel])
            jugadores.draw(display_game)
            enemigos.draw(display_game)
            enemigos2.draw(display_game)
            modificadores3.draw(display_game)
            nodriza_a.draw(display_game)
            nodriza_e.draw(display_game)
            pg.display.flip()
            reloj.tick(30)
    nuclear = pg.sprite.Group()
    dir_nuclear = "Sprites/Efectos/misil.png"
    imag_nuclear = pg.image.load(dir_nuclear)
    matriz_nuclear = matriz_sprites(imag_nuclear,150,150,150,150)
    dir_exploma = "Sprites/Efectos/explosion_madre.png"
    imag_exploma = pg.image.load(dir_exploma)
    matriz_exploma = matriz_sprites(imag_exploma,8080,1024,1010,1024)
    print("3")
    for e in nodriza_e:
        bomba = Bala(e.rect.center,matriz_nuclear)
        bomba.velx = -10
        nuclear.add(bomba)
        while(bomba.rect.x >= 50):
            nuclear.update()
            display_game.blit(background2,[i,subnivel])
            enemigos.draw(display_game)
            enemigos2.draw(display_game)
            modificadores3.draw(display_game)
            nodriza_a.update()
            jugadores.draw(display_game)
            nodriza_a.draw(display_game)
            nuclear.draw(display_game)
            nodriza_e.draw(display_game)
            pg.display.flip()
            reloj.tick(30)
        print("4")
    for n in nodriza_a:
        n.animacion = True
        n.velx = -2
        for i in range(5):
            n.explosion(matriz_exploma,i)
            display_game.blit(background2,[i,subnivel])
            enemigos.draw(display_game)
            enemigos2.draw(display_game)
            modificadores3.draw(display_game)
            nodriza_a.update()
            jugadores.draw(display_game)
            nodriza_a.draw(display_game)
            # nuclear.draw(display_game)
            nodriza_e.draw(display_game)
            pg.display.flip()
            reloj.tick(30)
    for e in nodriza_a:
        while e.rect.x >= -e.rect.width:
            e.rect.x -= 10
            display_game.blit(background2,[i,subnivel])
            # nodriza_a.draw(display_game)
            jugadores.draw(display_game)
            nodriza_a.draw(display_game)
            # nuclear.draw(display_game)
            nodriza_e.draw(display_game)
            pg.display.flip()
            reloj.tick(30)
    for e in nodriza_e:
        while e.rect.x <= ancho:
            e.rect.x += 10
            display_game.blit(background2,[i,subnivel])
            # nodriza_a.draw(display_game)
            jugadores.draw(display_game)
            nodriza_a.draw(display_game)
            # nuclear.draw(display_game)
            nodriza_e.draw(display_game)
            pg.display.flip()
            reloj.tick(30)



        ####################################################################
        # CUADRAR ANIMACION DE LA NAVE ENEMIGA CON LA BOMBA NUCLEAR
        ####################################################################

    pass

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    display = pg.display.set_mode([ancho,alto])
    display_credits = None
    display_controls = None
    display_game = None
    display_endgame = None
    display_pause = None
    display_win = None
    # GRUPOS
    bloques = pg.sprite.Group()
    bloques2 = pg.sprite.Group()
    jugadores=pg.sprite.Group()
    balas_jugador=pg.sprite.Group()
    nodriza_a = pg.sprite.Group()
    enemigos = pg.sprite.Group()
    enemigos2 = pg.sprite.Group()
    enemigos3 = pg.sprite.Group()
    enemigos4 = pg.sprite.Group()
    balas_enemigos = pg.sprite.Group()
    nodriza_e = pg.sprite.Group()
    spawns = pg.sprite.Group()
    spawns2 = pg.sprite.Group()
    spawns3 = pg.sprite.Group()
    modificadores1 = pg.sprite.Group()
    modificadores2 = pg.sprite.Group()
    modificadores3 = pg.sprite.Group()

##################################################################################################################################################################
    # IMAGENES DE BLOQUES Y FONDO
    background = pg.image.load("Sprites/Mapa/mapa2.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background2 = pg.image.load("Sprites/Mapa/mapa_sf.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
    background3 = pg.image.load("Sprites/Efectos/asteroides.png") #CAMBIAR LA IMAGEN A SU RESPECTIVO SITIO DEPENDIENDO DEL PC
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

    # ENEMIGOS 3
    direccion_imagen_enemigo3="Sprites/Personaje/enemigos/n7.png"
    imagen_enemigo3=pg.image.load(direccion_imagen_enemigo3)
    matriz_enemigo3=matriz_sprites(imagen_enemigo3,128,64,64,64)

    # ENEMIGOS 4
    direccion_imagen_enemigo4="Sprites/Personaje/enemigos/nave5.png"
    imagen_enemigo4=pg.image.load(direccion_imagen_enemigo4)
    matriz_enemigo4=matriz_sprites(imagen_enemigo4,128,64,64,64)

    # NAVE NODRIZA ENEMIGA
    dirreccion_imagen_naveME="Sprites/Personaje/enemigos/mothership.png"
    imagen_naveME=pg.image.load(dirreccion_imagen_naveME)

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

    # MISIL ENEMIGO
    direccion_imagen_misil_enemigo="Sprites/Efectos/misilc.png"
    imagen_misil_enemigo=pg.image.load(direccion_imagen_misil_enemigo)
    matriz_misil_enemigo=matriz_sprites(imagen_misil_enemigo,80,40,40,40)

##################################################################################################################################################################

    # CREACIONES

    # CREACION DE JUGADOR
    j=Jugador(matriz_jugador,matriz_blue_explotion,matriz_jugador2)
    jugadores.add(j)
    #manejo de la vidas jugador
    vidas_jugador = j.vidas

    # CREACION DE SPAWNS
    spawns = create_spawns()
    spawns2,spawns3 = create_spawns2()

    # CREACION NAVE NODRIZA
    mothership = Mothership(imagen_naveM)
    nodriza_a.add(mothership)
    mothership2 = Mothership_E(imagen_naveME, False)
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

    tiempoM = "TIME"
    tiempoM = Messages.render(tiempoM,True,negro,gris)

    temporizador = 90
    milisegundos = 99
    temporizador_s = str(temporizador)+":"+str(milisegundos )
    tiempo = Messages.render(temporizador_s,True,negro,gris)

    vida_nodriza = mothership2.vida
    vida_total_nod = vida_nodriza
    vida_nes = str(vida_nodriza)+"/"+str(vida_total_nod)
    vida_nes = Messages.render(vida_nes,True,negro,gris)

##################################################################################################################################################################
    #MUSICA
    pg.mixer.init()
    ms_juego = pg.mixer.Sound("Musica/fondo_sc.ogg")
    ms_click = pg.mixer.Sound("Musica/Click.ogg")
    ms_menu = pg.mixer.Sound("Musica/menu.ogg")
    ms_perdio = pg.mixer.Sound("Musica/NoHope.ogg")
    ms_disparo_j = pg.mixer.Sound("Musica/laser_jugador.ogg")
    ms_disparo_e = pg.mixer.Sound("Musica/laser_enemigo.ogg")
    ms_modBuenos = pg.mixer.Sound("Musica/powerUp1.ogg")
    ms_modMalos =  pg.mixer.Sound("Musica/lowDown.ogg")
    ms_explosion = pg.mixer.Sound("Musica/explosion.ogg")

##################################################################################################################################################################
    # FINALIZADORES DE ETAPAS(JUEGO, PAUSA, MENU), Y VARIABLES
    mensaje_de_introduccion = False
    mensaje_primer_jefe = False
    puntaje = 0
    cargar_mapa2 = False
    i=240 #POSICION DEL FONDO PARA EL DESPLAZAMIENTO
    subnivel=0
    nivel = 1
    probMod1 = 30
    probMod2 = 10
    reloj=pg.time.Clock()
    end = False
    game_over = False
    pause = False
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14 = False,False,False,False,False,False,False,False,False,False,False,False,False,False
    ms_menu.play()
    ms_menu.set_volume(.1)
    while not end and not game_over and not pause:
        event=pg.event.get()
        if display != None:
            p1,p2,p3,p4 = menu(display,p1,p2,p3,p4)
        if display_credits != None:
            p5,p6 = menu_creditos(display_credits,p5,p6)
        if display_endgame != None:
            p8,p9 = endgame(display_endgame,p8,p9)
        if display_pause != None:
            p10,p11 = pausegame(display_pause,p10,p11)
        if display_win != None:
            p12 = win(display_win,p12)
        if display_controls != None:# CAMBIAR LAS OPCIONES CUANDO SE NOS OCURRA ALGO
            p13,p14 = controls(display_controls,p13,p14)
        for event in event:
            if event.type == pg.QUIT:
                end = True
            # OPCIONES DEL MENU PRINCIPAL
            if event.type == pg.MOUSEBUTTONDOWN and p4 or event.type == pg.MOUSEBUTTONDOWN and p6 or event.type == pg.MOUSEBUTTONDOWN and p12 or event.type == pg.MOUSEBUTTONDOWN and p14: #GANA EL JUEGO:
                end = True
            if event.type == pg.MOUSEBUTTONDOWN and p3:
                ms_click.play()
                ms_click.set_volume(0.2)
                pg.display.quit()
                display = None
                display_game = None
                display_controls = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_credits = pg.display.set_mode([ancho,alto])
                display_credits.fill(negro)
                p3 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p2:
                ms_click.play()
                ms_click.set_volume(0.2)
                pg.display.quit()
                display = None
                display_game = None
                display_credits = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_controls = pg.display.set_mode([ancho,alto])
                display_controls.fill(negro)
                p2 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p1:
                ms_click.play()
                ms_click.set_volume(0.2)
                pg.display.quit()
                ms_menu.stop()
                ms_perdio.stop()
                ms_juego.stop()
                mensaje_de_introduccion = False
                # ms_creditos.stop()
                display = None
                display_credits = None
                display_controls = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p1 = False
                pg.display.flip()
            # OPCIONES DE CREDITOS
            if event.type == pg.MOUSEBUTTONDOWN and p5:
                ms_click.play()
                ms_click.set_volume(0.2)
                pg.display.quit()
                display_game = None
                display_credits = None
                display_controls = None
                display_endgame = None
                display_pause = None
                display_win = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p5 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p8:# PERDIO Y VA A REINTENTAR
                ms_perdio.stop()
                ms_click.play()
                ms_click.set_volume(0.2)
                ms_juego.play()
                ms_juego.set_volume(0.4)
                pg.display.quit()
                display_endgame = None
                display_credits = None
                display_controls = None
                display = None
                display_pause = None
                display_win = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p8 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p9: #PERDIO Y VA A SALIR
                ms_perdio.stop()
                ms_click.play()
                ms_click.set_volume(0.2)
                ms_juego.play()
                ms_juego.set_volume(0.4)
                pg.display.quit()
                display_game = None
                display_credits = None
                display_controls = None
                display_endgame = None
                display_pause = None
                display_win = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p9 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p10: #PAUSA Y VUELVE A JUGAR
                ms_click.play()
                ms_click.set_volume(0.2)
                ms_menu.stop()
                ms_juego.play()
                ms_juego.set_volume(0.4)
                pg.display.quit()
                display = None
                display_credits = None
                display_controls = None
                display_endgame = None
                display_pause = None
                display_win = None
                display_game = pg.display.set_mode([ancho,alto])
                display_game.fill(negro)
                p10 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p11: #PAUSA Y VA A SALIR
                ms_click.play()
                pg.display.quit()
                ms_juego.stop()
                display_game = None
                display_credits = None
                display_controls = None
                display_endgame = None
                display_pause = None
                display_win = None
                j.modificador = False
                i=240
                subnivel = 0
                nivel = 1
                healt=1000
                healt_s = str(healt)
                hp = Messages.render(healt_s,True,negro,gris)
                temporizador = 90
                milisegundos = 99
                temporizador_s = str(temporizador)+":"+str(milisegundos )
                tiempo = Messages.render(temporizador_s,True,negro,gris)
                j.shield=1000000
                shield_s = str(j.shield)
                shield_M = Messages.render(shield_s,True,negro,gris)
                j.rect.y=centro_y
                spawns= create_spawns()
                bloques = clean_group(bloques)
                bloques = load_map(bloques,background)
                enemigos = clean_group(enemigos)
                nodriza_a.remove(mothership)
                mothership = Mothership(imagen_naveM)
                nodriza_a.add(mothership)
                nodriza_e.remove(mothership2)
                mothership2 = Mothership_E(imagen_naveME,False)
                nodriza_e.add(mothership2)
                modificadores1 =clean_group(modificadores1)
                modificadores2 = clean_group(modificadores2)
                modificadores3 = clean_group(modificadores3)
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p11 = False
                pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN and p13:
                ms_click.play()
                ms_click.set_volume(0.2)
                pg.display.quit()
                display_game = None
                display_credits = None
                display_controls = None
                display_endgame = None
                display_pause = None
                display_win = None
                display = pg.display.set_mode([ancho,alto])
                display.fill(negro)
                p13 = False
                pg.display.flip()
            # OPCIONES DE CREDITOS
            # OPCIONES DEL MENU DE OPCIONES XD
            if display_game != None:
##################################################################################################################################################################
                if event.type==pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pg.display.quit()
                        ms_juego.stop()
                        ms_menu.play()
                        ms_menu.set_volume(0.3)
                        display_game = None
                        display_credits = None
                        display_controls = None
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
                    if nivel == 2:
                        if event.key == pg.K_RIGHT:
                                j.velx=10
                                j.vely=0
                                j.fila=2
                                j.fila3=2
                        if event.key == pg.K_LEFT:
                                j.velx=-10
                                j.vely=0
                                j.fila=2
                                j.fila3=2
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
                    j.fila3=2
##################################################################################################################################################################
        ###################################
        # LIMPIEZA DE OBJETOS EN TODOS LOS NIVELES
        ###################################
        if display_game != None:
            ###################################
            # TEXTO DEL PRELUDIO
            ###################################
            if not mensaje_de_introduccion:
                preludio(display_game)
                mensaje_de_introduccion = True
                ms_juego.play()
                ms_juego.set_volume(0.4)
            ###################################

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
            ###################################
            # CONTROLES DEL NIVEL 1
            ###################################
            if nivel == 1:
                if subnivel == -64*11:
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
                            e.velx = -30
                            balas_enemigos.add(e)
                            ms_disparo_e.play()

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
                    # COLISION DE LAS BALAS DEL JUGADOR CON LA NAVE NODRIZA
                    for b in balas_jugador:
                        lm = pg.sprite.spritecollide(b,nodriza_e,False)
                        for r in lm:
                            r.vida -= 1
                            vida_nodriza = r.vida
                            vida_nes = str(vida_nodriza)+"/"+str(vida_total_nod)
                            vida_nes = Messages.render(vida_nes,True,negro,gris)
                            display_game.blit(vida_nes,[ancho-300,0])
                            pg.display.flip()
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
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
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
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
                            enemigos.remove(e)
                    # EXPLOSION DE LA NAVE NODRIZA FALTAN LOS SPRITES
                    for e in nodriza_e:
                        if e.vida <= vida_total_nod/2:
                            e.activate = False
                            # if len(enemigos) <= 0 or len(enemigos2) <= 0:
                            animacion_final_nivel_1(display_game,nodriza_a,nodriza_e,jugadores,modificadores3,background2,healt,reloj,i,subnivel)
                            interludio(display_game)
                            nivel = 2
                            i = 0
                            puntaje += temporizador
                            temporizador = 90
                            subnivel = 0
                            e.vida = 1000
                            vida_nodriza = 100
                            vida_total_nod = 100
                    #######################################################
                    # COLISION DEL JUGADOR CON LOS MODIFICADORES
                    if len(modificadores1) >= 0:
                        #COLISION DEL JUGADOR CON LOS MODIFICADORES 1
                        le = pg.sprite.spritecollide(j,modificadores1,False)#no borra cuando hay colision
                        for r in le:
                            ms_modBuenos.play()
                            r.muerte = 1
                            j.modificador = True
                            punto_partida_modificador1 = i
                            j.modificador3 = False
                    if len(modificadores2) >= 0:
                        # COLISION DEL JUGADOR CON EL MODIFICADOR 2
                        lV = pg.sprite.spritecollide(j,modificadores2,False)#no borra cuando hay colision
                        for r in lV:
                            ms_modBuenos.play()
                            r.muerte = 1
                            if r.masvida:
                                r.masvida = False
                                j.vidas += 1
                                vidas_jugador = j.vidas
                    if len(modificadores3) >= 0:
                        #COLISION DEL JUGADOR CON LOS MODIFICADORES 1
                        le = pg.sprite.spritecollide(j,modificadores3,False)#no borra cuando hay colision
                        for r in le:
                            ms_modMalos.play()
                            r.muerte = 1
                            j.modificador3 = True
                            j.modificador = False
                    # print(j.vidas)
                    # FIN DEL MODIFICADOR
                        # POR DEFINIR

                    ################################################################################################
                    #EXPLOSION MODIFICADOR CON EL JUGADOR
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
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
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
                    # COLISION DE ENEMIGOS CON LA NAVE NODRIZA ALIADA
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
                    # INTERACCION O PUESTA EN ESCENA DEL JEFE FINAL 1
                    for e in nodriza_e:
                        if e.activate:
                            mothership2.tempo -= 1
                            if mothership2.tempo <= 0:
                                mothership2.tempo = random.randrange(20,50)
                                pos = [(mothership2.rect.x+100),random.randrange(50,500)]
                                e = Rival(matriz_enemigo,matriz_red_explotion,pos)
                                enemigos.add(e)
                                pos = [(mothership2.rect.x+100),random.randrange(50,500)]
                                e2 = Rival2(matriz_enemigo2,matriz_red_explotion,pos)
                                enemigos2.add(e2)
                                pos = [(mothership2.rect.x+100),random.randrange(50,500)]
                                mod = Slow(matriz_modificador3,matriz_red_explotion,pos)
                                modificadores3.add(mod)
                            pass

                    #######################################################
                    # ELIMINACION DEL JUGADOR
                    for j in jugadores:
                        if j.vidas <= 0 and j.col2 == 16:
                            ms_juego.stop()
                            ms_menu.stop()
                            ms_perdio.play()
                            j.vidas = 3
                            j.modificador = False
                            vidas_jugador = j.vidas
                            pg.display.quit()
                            display_game = None
                            display_credits = None
                            display_controls = None
                            display_win = None
                            i=240
                            subnivel = 0
                            nivel = 1
                            healt=1000
                            healt_s = str(healt)
                            hp = Messages.render(healt_s,True,negro,gris)
                            temporizador = 90
                            milisegundos = 99
                            temporizador_s = str(temporizador)+":"+str(milisegundos )
                            tiempo = Messages.render(temporizador_s,True,negro,gris)
                            j.shield=1000000
                            shield_s = str(j.shield)
                            shield_M = Messages.render(shield_s,True,negro,gris)
                            j.rect.y=centro_y
                            spawns = create_spawns()
                            bloques = pg.sprite.Group()
                            bloques = load_map(bloques,background)
                            enemigos = pg.sprite.Group()
                            balas_enemigos = pg.sprite.Group()
                            nodriza_a.remove(mothership)
                            mothership = Mothership(imagen_naveM)
                            nodriza_a.add(mothership)
                            nodriza_e.remove(mothership2)
                            mothership2 = Mothership_E(imagen_naveME,False)
                            nodriza_e.add(mothership2)
                            modificadores1 = pg.sprite.Group()
                            modificadores2 = pg.sprite.Group()
                            modificadores3 = pg.sprite.Group()
                            display_endgame = pg.display.set_mode([ancho,alto])
                            display_endgame.fill(negro)

##################################################################################################################################################################
##################################################################################################################################################################
            if nivel == 2:
                ###################################
                # CONTROLES DEL NIVEL 2
                ###################################

                if subnivel == 0 and not cargar_mapa2:
                    ###################################
                    # ENTRADA DE EL NUEVO MAPA
                    ###################################
                    bloques,matriz_explosion = load_map2(bloques,background3)
                    cargar_mapa2 = True
                if subnivel == 0:
                    #COLISION DE LAS BALAS DEL JUGADOR CON LOS BLOQUES
                    for b in balas_jugador:
                        le = pg.sprite.spritecollide(b,bloques,False)#no borra cuando hay colision
                        for r in le:
                            r.muerte = 1
                            balas_jugador.remove(b)
                    ##EXPLOSION BLOQUES CON BALAS DE JUGADOR Y CREACION DE LOS MODIFICADORES 2
                    for e in bloques:
                        if e.muerte == 1 and e.col2 == 5:
                            if not(e.luck):
                                e.luck = True
                                luck = random.randrange(100)
                                if luck < 80:
                                    pos = e.rect.topleft
                                    m = Mas1Vida(matriz_modificador2,matriz_blue_explotion,pos)
                                    modificadores2.add(m)
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
                            bloques.remove(e)
                    if len(modificadores2) >= 0:
                        # COLISION DEL JUGADOR CON EL MODIFICADOR 2
                        lV = pg.sprite.spritecollide(j,modificadores2,False)#no borra cuando hay colision
                        for r in lV:
                            ms_modBuenos.play()
                            r.muerte = 1
                            if r.masvida:
                                r.masvida = False
                                j.vidas += 1
                                vidas_jugador = j.vidas
                    # EXPLOSION MODIFICADORES 2
                    for e in modificadores2:
                        if e.muerte == 1 and e.col2 == 16:
                            modificadores2.remove(e)

                if subnivel == -64*11 and nivel == 2:
                    ###################################
                    # ENTRADA DE ENEMIGOS
                    ###################################

                    #CREACION DE LOS RIVALES DESDE EL SPAWN
                    for s in spawns2:
                        if s.tempo == 0 :
                            s.tempo = random.randrange(50,100)
                            pos = s.rect.topleft
                            e = Rival4(matriz_enemigo4,matriz_red_explotion,pos)
                            enemigos4.add(e)
                            oportunidad = random.randrange(100)
                            if oportunidad > 80:
                                mod = Slow(matriz_modificador3,matriz_red_explotion,pos)
                                modificadores3.add(mod)
                    #CREACION DE LOS  OTROS RIVALES DESDE EL SPAWN
                    for s in spawns3:
                        if s.tempo == 0 :
                            s.tempo = random.randrange(50,150)
                            pos = s.rect.topleft
                            e = Rival3(matriz_enemigo3,matriz_red_explotion,pos)
                            enemigos3.add(e)
                            oportunidad = random.randrange(100)
                            if oportunidad > 80:
                                mod = Slow(matriz_modificador3,matriz_red_explotion,pos)
                                modificadores3.add(mod)

                    #DISPAROS DE LOS RIVALES
                    for e in enemigos3:
                        if e.tempo == 0:
                            e.tempo = random.randrange(10)
                            pos = e.rect.topleft
                            pos1 = [pos[0],pos[1]+20]
                            pos2 = [pos[0]-200,alto]
                            e = Bala_seguidora(pos1,pos2,matriz_bala_enemigo,5,matriz_misil_enemigo,matriz_explosion)
                            balas_enemigos.add(e)
                            ms_disparo_e.play()

                    for e in enemigos4:
                        if e.tempo == 0:
                            e.tempo = random.randrange(10)
                            pos = e.rect.topleft
                            pos1 = [pos[0],pos[1]+20]
                            pos2 = [j.rect.x,j.rect.y]
                            e = Bala_seguidora(pos1,pos2,matriz_bala_enemigo,5)
                            balas_enemigos.add(e)
                            ms_disparo_e.play()

                    ############################################################
                    if len(spawns2) <= 0 and len(spawns3) <= 0:
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
                    #COLISION DE LAS BALAS DEL JUGADOR CON LOS ENEMIGOS3
                    for b in balas_jugador:
                        le = pg.sprite.spritecollide(b,enemigos3,False)#no borra cuando hay colision
                        for r in le:
                            r.muerte = 1
                            balas_jugador.remove(b)
                    #COLISION DE LAS BALAS DEL JUGADOR CON LOS ENEMIGOS4
                    for b in balas_jugador:
                        le = pg.sprite.spritecollide(b,enemigos4,False)#no borra cuando hay colision
                        for r in le:
                            r.muerte = 1
                            balas_jugador.remove(b)
                    #COLISION DE LAS BALAS DEL JUGADOR CON LOS Misiles
                    for b in balas_jugador:
                        le = pg.sprite.spritecollide(b,enemigos4,False)#no borra cuando hay colision
                        for r in le:
                            r.muerte = 1
                            balas_jugador.remove(b)
                    # COLISION DE LAS BALAS DEL JUGADOR CON LA NAVE NODRIZA
                    for b in balas_jugador:
                        lm = pg.sprite.spritecollide(b,nodriza_e,False)
                        for r in lm:
                            r.vida -= 1
                            vida_nodriza = r.vida
                            vida_nes = str(vida_nodriza)+"/"+str(vida_total_nod)
                            vida_nes = Messages.render(vida_nes,True,negro,gris)
                            display_game.blit(vida_nes,[ancho-300,0])
                            balas_jugador.remove(b)

                    ################################################################
                    if len(spawns2) <= 0 and len(spawns3) <= 0:
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
                                ms_explosion.play()
                                ms_explosion.set_volume(0.2)
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
                                ms_explosion.play()
                                ms_explosion.set_volume(0.2)
                                enemigos.remove(e)
                                pass

                    #EXPLOSION ENEMIGOS CON BALAS DE JUGADOR Y CREACION DE LOS MODIFICADORES 1
                    for e in enemigos3:
                        if e.muerte == 1 and e.col2 == 12:
                            if not(e.luck):
                                e.luck = True
                                luck = random.randrange(100)
                                if luck < probMod1:
                                    pos = e.rect.topleft
                                    m = Skin(matriz_modificador1,matriz_blue_explotion,pos)
                                    modificadores1.add(m)
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
                            enemigos3.remove(e)
                    ##EXPLOSION ENEMIGOS CON BALAS DE JUGADOR Y CREACION DE LOS MODIFICADORES 2
                    for e in enemigos4:
                        if e.muerte == 1 and e.col2 == 12:
                            if not(e.luck):
                                e.luck = True
                                luck = random.randrange(100)
                                if luck < probMod2:
                                    pos = e.rect.topleft
                                    m = Mas1Vida(matriz_modificador2,matriz_blue_explotion,pos)
                                    modificadores2.add(m)
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
                            enemigos4.remove(e)
                    # EXPLOSION DE LA NAVE NODRIZA FALTAN LOS SPRITES
                    for e in nodriza_e:
                        if e.vida <= 0:
                            e.activate = False
                            # if len(enemigos) <= 0 or len(enemigos2) <= 0:
                            puntaje += temporizador
                            ms = "Puntaje: "+str(puntaje)+" Felicitaciones"
                            ms = Messages.render(ms,True,azul,rojo)
                            display_game.blit(ms,[400,300])
                            time.sleep(3)
                            pg.display.quit()
                            display_game = None
                            display_credits = None
                            display_controls = None
                            display_endgame = None
                            display_pause = None
                            display = None
                            display_win = pg.display.set_mode([ancho,alto])
                            display_win.fill(negro)
                            nodriza_e.remove(e)


                    #######################################################
                    # COLISION DEL JUGADOR CON LOS MODIFICADORES
                    if len(modificadores1) >= 0:
                        #COLISION DEL JUGADOR CON LOS MODIFICADORES 1
                        le = pg.sprite.spritecollide(j,modificadores1,False)#no borra cuando hay colision
                        for r in le:
                            ms_modBuenos.play()
                            r.muerte = 1
                            j.modificador = True
                            punto_partida_modificador1 = i
                            j.modificador3 = False
                    if len(modificadores2) >= 0:
                        # COLISION DEL JUGADOR CON EL MODIFICADOR 2
                        lV = pg.sprite.spritecollide(j,modificadores2,False)#no borra cuando hay colision
                        for r in lV:
                            ms_modBuenos.play()
                            r.muerte = 1
                            if r.masvida:
                                r.masvida = False
                                j.vidas += 1
                                vidas_jugador = j.vidas
                    if len(modificadores3) >= 0:
                        #COLISION DEL JUGADOR CON LOS MODIFICADORES 1
                        le = pg.sprite.spritecollide(j,modificadores3,False)#no borra cuando hay colision
                        for r in le:
                            ms_modMalos.play()
                            r.muerte = 1
                            j.modificador3 = True
                            j.modificador = False
                    # print(j.vidas)
                    # FIN DEL MODIFICADOR
                        # POR DEFINIR

                    ################################################################################################
                    #EXPLOSION MODIFICADOR CON EL JUGADOR
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
                        ls = pg.sprite.spritecollide(b,spawns2,False)#
                        for r in ls:
                            r.vidas -= 1
                            balas_jugador.remove(b)
                        ls = pg.sprite.spritecollide(b,spawns3,False)#
                        for r in ls:
                            r.vidas -= 1
                            balas_jugador.remove(b)

                    # ELIMINACION DE SPAWNS
                    for s in spawns2:
                        if s.vidas <= 0 and s.col2 == 13:
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
                            spawns2.remove(s)
                    for s in spawns3:
                        if s.vidas <= 0 and s.col2 == 13:
                            ms_explosion.play()
                            ms_explosion.set_volume(0.2)
                            spawns3.remove(s)
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
                    # # COLISION DE ENEMIGOS CON LA NAVE NODRIZA ALIADA
                    # ls = pg.sprite.spritecollide(mothership,enemigos,False)
                    # for c in ls:
                    #     if c.rect.x <= 150:
                    #         enemigos.remove(c)
                    #         healt-=10
                    #         healt_s = str(healt)
                    #         hp = Messages.render(healt_s,True,negro,gris)
                    # ls = pg.sprite.spritecollide(mothership,enemigos2,False)
                    # for c in ls:
                    #     if c.rect.x <= 150:
                    #         enemigos2.remove(c)
                    #         healt-=10
                    #         healt_s = str(healt)
                    #         hp = Messages.render(healt_s,True,negro,gris)

                    #######################################################
                    # INTERACCION O PUESTA EN ESCENA DEL JEFE FINAL 2
                    for e in nodriza_e:
                        # print(e.activate)
                        if e.activate:
                            e.tempo -= 1
                            if e.tempo <= 0:
                                e.tempo = random.randrange(50,100)
                                pos = [(e.rect.x+100),random.randrange(50,500)]
                                e = Rival(matriz_enemigo,matriz_red_explotion,pos)
                                enemigos.add(e)
                                pos = [(e.rect.x+100),random.randrange(50,500)]
                                e2 = Rival2(matriz_enemigo2,matriz_red_explotion,pos)
                                enemigos2.add(e2)
                                pos = [(e.rect.x+100),random.randrange(50,500)]
                                e3 = Rival3(matriz_enemigo3,matriz_red_explotion,pos)
                                enemigos3.add(e3)
                                pos = [(e.rect.x+100),random.randrange(50,500)]
                                e4 = Rival4(matriz_enemigo4,matriz_red_explotion,pos)
                                enemigos4.add(e4)
                            pass

                    #######################################################
                    # ELIMINACION DEL JUGADOR
                    for j in jugadores:
                        if j.vidas <= 0 and j.col2 == 16:
                            ms_juego.stop()
                            ms_menu.stop()
                            ms_perdio.play()
                            j.vidas = 3
                            j.modificador = False
                            vidas_jugador = j.vidas
                            pg.display.quit()
                            display_game = None
                            display_credits = None
                            display_controls = None
                            display_win = None
                            i=240
                            subnivel = 0
                            nivel = 1
                            healt=1000
                            healt_s = str(healt)
                            hp = Messages.render(healt_s,True,negro,gris)
                            temporizador = 90
                            milisegundos = 99
                            temporizador_s = str(temporizador)+":"+str(milisegundos )
                            tiempo = Messages.render(temporizador_s,True,negro,gris)
                            j.shield=1000000
                            shield_s = str(j.shield)
                            shield_M = Messages.render(shield_s,True,negro,gris)
                            j.rect.y=centro_y
                            spawns = create_spawns()
                            bloques = pg.sprite.Group()
                            bloques = load_map(bloques,background)
                            enemigos = pg.sprite.Group()
                            balas_enemigos = pg.sprite.Group()
                            nodriza_a.remove(mothership)
                            mothership = Mothership(imagen_naveM)
                            nodriza_a.add(mothership)
                            nodriza_e.remove(mothership2)
                            mothership2 = Mothership_E(imagen_naveME,False)
                            nodriza_e.add(mothership2)
                            modificadores1 = pg.sprite.Group()
                            modificadores2 = pg.sprite.Group()
                            modificadores3 = pg.sprite.Group()
                            display_endgame = pg.display.set_mode([ancho,alto])
                            display_endgame.fill(negro)

##################################################################################################################################################################
            ###################################
            # MOSTRAR EN LOS NIVELES
            ###################################
            if display_game != None:
                loser = False
                if healt <= 0 or j.shield <=0 or temporizador <=0:
                    ms_juego.stop()
                    ms_menu.stop()
                    ms_perdio.play()
                    ms_perdio.set_volume(0.4)
                    j.vidas = 3
                    j.modificador = False
                    vidas_jugador = j.vidas
                    pg.display.quit()
                    display_game = None
                    display_credits = None
                    display_controls = None
                    display_win = None
                    loser = True
                    i=240
                    subnivel = 0
                    nivel = 1
                    healt=1000
                    healt_s = str(healt)
                    hp = Messages.render(healt_s,True,negro,gris)
                    temporizador = 90
                    milisegundos = 99
                    temporizador_s = str(temporizador)+":"+str(milisegundos )
                    tiempo = Messages.render(temporizador_s,True,negro,gris)
                    j.shield=1000000
                    shield_s = str(j.shield)
                    shield_M = Messages.render(shield_s,True,negro,gris)
                    j.rect.y=centro_y
                    spawns = create_spawns()
                    bloques = pg.sprite.Group()
                    bloques = load_map(bloques,background)
                    enemigos = pg.sprite.Group()
                    balas_enemigos = pg.sprite.Group()
                    nodriza_a.remove(mothership)
                    mothership = Mothership(imagen_naveM)
                    nodriza_a.add(mothership)
                    nodriza_e.remove(mothership2)
                    mothership2 = Mothership_E(imagen_naveME,False)
                    nodriza_e.add(mothership2)
                    modificadores1 = pg.sprite.Group()
                    modificadores2 = pg.sprite.Group()
                    display_endgame = pg.display.set_mode([ancho,alto])
                    display_endgame.fill(negro)

                if i == -ancho_fondo + ancho:
                    i = 0
                    subnivel = -64*11
                    bloques = clean_group(bloques)
    ##################################################################################################################################################################
                i-=8
                jugadores.update()
                if nivel == 1:          #NIVEL 1
                    if subnivel == 0:
                        bloques.update()
                    balas_jugador.update()
                    # ACTUALIZACIONES
                    if subnivel == -64*11:
                        # TIEMPO EN DESTRUIR LAS NAVES
                        milisegundos -= 3
                        temporizador_s = str(temporizador)+":"+str(milisegundos)
                        tiempo = Messages.render(temporizador_s,True,negro,gris)
                        if milisegundos == 0:
                            temporizador -=1
                            milisegundos = 99
                            temporizador_s = str(temporizador)+":"+str(milisegundos)
                            tiempo = Messages.render(temporizador_s,True,negro,gris)
                        nodriza_a.update()
                        spawns.update()
                        enemigos.update()
                        enemigos2.update()
                        balas_enemigos.update()
                        modificadores1.update()
                        modificadores2.update()
                        modificadores3.update()
                    if len(spawns) <= 0:      #JEFE FINAL PRIMER NIVEL
                        nodriza_e.update()
                        vida_nodriza = mothership2.vida
                        vida_nes = str(vida_nodriza)+"/"+str(vida_total_nod)
                        vida_nes = Messages.render(vida_nes,True,negro,gris)
                        display_game.blit(vida_nes,[ancho-300,0])
                        if mothership2.rect.x == ancho - 300:
                            if not mensaje_primer_jefe:
                                Messages2 = pg.font.Font(None,64)
                                EndMessage= "TO  BE  CONTINUE  ... "
                                EndMessage = Messages2.render(EndMessage,True,rojo,azul)
                                pos_w = centrar_texto(EndMessage)
                                display_game.blit(EndMessage,[pos_w,300])
                                pg.display.flip()
                                time.sleep(5)
                                EndMessage= "TO  BE  CONTINUE  ... "
                                EndMessage = Messages2.render(EndMessage,True,negro,negro)
                                display_game.blit(EndMessage,[pos_w,300])
                                EndMessage= ".....  NOW ..... XD "
                                EndMessage = Messages2.render(EndMessage,True,rojo,azul)
                                pos_w = centrar_texto(EndMessage)
                                display_game.blit(EndMessage,[pos_w,300])
                                pg.display.flip()
                                time.sleep(5)
                                mensaje_primer_jefe = True
                            mothership2.activate = True
                    if not loser:
                        display_game.blit(background2,[i,subnivel])
                        jugadores.draw(display_game)
                    if subnivel ==0 and not loser:
                        # display_game.fill(negro)
                        display_game.blit(background2,[i,subnivel])
                        jugadores.draw(display_game)
                        bloques.draw(display_game)
                    if subnivel == -64*11 and not loser:
                        nodriza_a.draw(display_game)
                        spawns.draw(display_game)
                        enemigos.draw(display_game)
                        enemigos2.draw(display_game)
                        balas_jugador.draw(display_game)
                        balas_enemigos.draw(display_game)
                        modificadores1.draw(display_game)
                        modificadores2.draw(display_game)
                        modificadores3.draw(display_game)
                    if len(spawns) <= 0 and not loser:
                        nodriza_e.draw(display_game)
                    # MENSAJE DE ADVERTENCIA INICIAL
                    if i >= -2000 and subnivel == 0 and nivel == 1 and not loser:
                        display_game.blit(WarningM,[pos_w,0])
                    j_vidas = 'Vidas: '+ str(vidas_jugador)
                    texto = Messages.render(j_vidas,True,negro,gris)
                    if not loser:
                        # vida_nes = str(vida_nodriza)+"/"+str(vida_total_nod)
                        # vida_nes = Messages.render(vida_nes,True,negro,gris)
                        display_game.blit(vida_nes,[ancho-300,0])
                        display_game.blit(texto,[200,0])
                        display_game.blit(salud,[0,0])
                        display_game.blit(escudo,[0,32])
                        display_game.blit(tiempoM,[200,32])
                        display_game.blit(hp,[100,0])
                        display_game.blit(shield_M,[100,32])
                        display_game.blit(tiempo,[300,32])
###################################################################################################
                if nivel == 2:
                    if subnivel == 0:
                        bloques.update()
                        modificadores2.update()
                    balas_jugador.update()
                    if subnivel == -64*11:
                        # TIEMPO EN DESTRUIR LAS NAVES
                        milisegundos -= 3
                        temporizador_s = str(temporizador)+":"+str(milisegundos)
                        tiempo = Messages.render(temporizador_s,True,negro,gris)
                        if milisegundos == 0:
                            temporizador -=1
                            milisegundos = 99
                            temporizador_s = str(temporizador)+":"+str(milisegundos)
                            tiempo = Messages.render(temporizador_s,True,negro,gris)
                        # nodriza_a.update()
                        spawns2.update()
                        spawns3.update()
                        enemigos3.update()
                        enemigos4.update()
                        balas_enemigos.update()
                        modificadores1.update()
                        modificadores2.update()
                        modificadores3.update()
                        if len(spawns2) <= 0 and len(spawns3) <= 0:      #JEFE FINAL SEGUNDO NIVEL
                            nodriza_e.update()
                            vida_nodriza = mothership2.vida
                            vida_nes = str(vida_nodriza)+"/"+str(vida_total_nod)
                            vida_nes = Messages.render(vida_nes,True,negro,gris)
                            display_game.blit(vida_nes,[ancho-300,0])
                            if mothership2.rect.x == ancho - 300:
                                if not mensaje_primer_jefe:
                                    Messages2 = pg.font.Font(None,64)
                                    EndMessage= "TO  BE  CONTINUE  ... "
                                    EndMessage = Messages2.render(EndMessage,True,rojo,azul)
                                    pos_w = centrar_texto(EndMessage)
                                    display_game.blit(EndMessage,[pos_w,300])
                                    pg.display.flip()
                                    time.sleep(5)
                                    EndMessage= "TO  BE  CONTINUE  ... "
                                    EndMessage = Messages2.render(EndMessage,True,negro,negro)
                                    display_game.blit(EndMessage,[pos_w,300])
                                    EndMessage= ".....  NOW ..... XD "
                                    EndMessage = Messages2.render(EndMessage,True,rojo,azul)
                                    pos_w = centrar_texto(EndMessage)
                                    display_game.blit(EndMessage,[pos_w,300])
                                    pg.display.flip()
                                    time.sleep(5)
                                    mensaje_primer_jefe = True
                                mothership2.activate = True
                    print(len(spawns2))
                    print(len(spawns3))
                    if len(spawns2) <= 0 and len(spawns3) <=0:      #JEFE FINAL SEGUNDO NIVEL
                        nodriza_e.update()
                        vida_nodriza = mothership2.vida
                        vida_nes = str(vida_nodriza)+"/"+str(vida_total_nod)
                        vida_nes = Messages.render(vida_nes,True,negro,gris)
                        display_game.blit(vida_nes,[ancho-300,0])
                        if mothership2.rect.x >= ancho - 300:
                            mothership2.rect.x >= ancho - 300
                            mothership2.activate = True
                    if not loser:
                        display_game.blit(background2,[i,subnivel])
                        jugadores.draw(display_game)
                    if subnivel ==0 and not loser:
                        display_game.blit(background2,[i,subnivel])
                        jugadores.draw(display_game)
                        balas_jugador.draw(display_game)
                        modificadores2.draw(display_game)
                        bloques.draw(display_game)
                    if subnivel == -64*11 and not loser:
                        # nodriza_a.draw(display_game)
                        spawns2.draw(display_game)
                        spawns3.draw(display_game)
                        enemigos3.draw(display_game)
                        enemigos4.draw(display_game)
                        balas_jugador.draw(display_game)
                        balas_enemigos.draw(display_game)
                        modificadores1.draw(display_game)
                        modificadores2.draw(display_game)
                        modificadores3.draw(display_game)
                    if len(spawns2) <= 0 and len(spawns3) <= 0 and not loser:
                        enemigos.update()
                        enemigos2.update()
                        enemigos.draw(display_game)
                        enemigos2.draw(display_game)
                        nodriza_e.draw(display_game)
                    # MENSAJE DE ADVERTENCIA INICIAL
                    if i >= -2000 and subnivel == 0 and nivel == 1 and not loser:
                        display_game.blit(WarningM,[pos_w,0])
                    j_vidas = 'Vidas: '+ str(vidas_jugador)
                    texto = Messages.render(j_vidas,True,negro,gris)
                    if not loser:
                        display_game.blit(vida_nes,[ancho-300,0])
                        display_game.blit(texto,[200,0])
                        # display_game.blit(salud,[0,0])
                        display_game.blit(escudo,[0,32])
                        display_game.blit(tiempoM,[200,32])
                        # display_game.blit(hp,[100,0])
                        display_game.blit(shield_M,[100,32])
                        display_game.blit(tiempo,[300,32])

                pg.display.flip()
                reloj.tick(30)
