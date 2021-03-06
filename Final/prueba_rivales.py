import pygame as pg
from libreria import*
from Personaje2 import*
from Bala import*
from Enemigos import*
from Enemigos2 import*
from Spawn import*
import time

if __name__ == '__main__':

    # PANTALLA
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    fuente=pg.font.Font(None,32)

    # GRUPOS
    jugadores=pg.sprite.Group()
    balas_jugador=pg.sprite.Group()
    enemigos = pg.sprite.Group()
    enemigos2 = pg.sprite.Group()
    balas_enemigos = pg.sprite.Group()
    spawns = pg.sprite.Group()
    # JUGADOR
    dirreccion_imagen_jugador="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Personaje/jugador/nave_terminada.png"
    imagen_jugador=pg.image.load(dirreccion_imagen_jugador)
    matriz_jugador=matriz_sprites(imagen_jugador,320,512,64,64)
    #EXPLOSION JUGADOR
    dirreccion_imagen_jugador_explosion="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Blue Effects/explosion_blue.png"
    imagen_jugador_explosion=pg.image.load(dirreccion_imagen_jugador_explosion)
    matriz_jugador_explosion=matriz_sprites(imagen_jugador_explosion,1088,64,64,64)

    # BALAS
    # BALAS JUGADOR
    direccion_imagen_bala_jugador="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_blue.png"
    imagen_bala_jugador=pg.image.load(direccion_imagen_bala_jugador)
    matriz_bala_jugador=matriz_sprites(imagen_bala_jugador,304,38,38,38)
    # BALAS ENEMIGO
    direccion_imagen_bala_enemigo="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Efectos/bullets_red.png"
    imagen_bala_enemigo=pg.image.load(direccion_imagen_bala_enemigo)
    matriz_bala_enemigo=matriz_sprites(imagen_bala_enemigo,304,38,38,38)
    # ENEMIGOS
    direccion_imagen_enemigo="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/Enemy_animation/enemigo11.png"
    imagen_enemigo=pg.image.load(direccion_imagen_enemigo)
    matriz_enemigo=matriz_sprites(imagen_enemigo,560,80,80,80)
    #MUERTE ENEMIGOS
    direccion_imagen_enemigo_expl="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    imagen_enemigo_explosion=pg.image.load(direccion_imagen_enemigo_expl)
    matriz_enemigo_explosion=matriz_sprites(imagen_enemigo_explosion,896,64,64,64)
    ##SPAWN DE LOS ENEMIGOS
    direccion_imagen_spawn_enemigo = "/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/comm_redship/spawn.png"
    imagen_spawn_enemigo = pg.image.load(direccion_imagen_spawn_enemigo)
    matriz_spawn_enemigo=matriz_sprites(imagen_spawn_enemigo,273,88,91,88)
    #MUERTE DE LOS ENEMIGOS
    direccion_imagen_spawn_enemigo_explosion = "/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    imagen_spawn_enemigo_explosion = pg.image.load(direccion_imagen_spawn_enemigo_explosion)
    matriz_spawn_enemigo_explosion=matriz_sprites(imagen_spawn_enemigo_explosion,896,64,64,64)
    # ENEMIGOS2
    direccion_imagen_enemigo2="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Red/small_ship_animation/enemigo2.png"
    imagen_enemigo2=pg.image.load(direccion_imagen_enemigo2)
    matriz_enemigo2=matriz_sprites(imagen_enemigo2,340,61,68,61)
    #MUERTE ENEMIGOS
    direccion_imagen_enemigo2_expl="/home/nicolas/github/Proyecto1_CG/Sprites/Proyecto1/Complete_sprites/Spaceship_art_pack_larger/Effects/Red Explosion/explosion_red.png"
    imagen_enemigo2_explosion=pg.image.load(direccion_imagen_enemigo2_expl)
    matriz_enemigo2_explosion=matriz_sprites(imagen_enemigo2_explosion,896,64,64,64)
    # CREACION DE JUGADOR
    j=Jugador(matriz_jugador,matriz_jugador_explosion)
    jugadores.add(j)
    #manejo de la vidas jugador
    vidas_jugador = j.vidas
    #CREACION SPAWN
    spawns = pg.sprite.Group()
    x = 980
    y = 60
    esp_entre = 20
    s = Spawn([x,y],matriz_spawn_enemigo,matriz_spawn_enemigo_explosion)
    ##aumentar x para que el spawn quede fuera de la pantalla
    for i in range(y,alto - s.rect.height-esp_entre,s.rect.height+esp_entre):
        s = Spawn([x,y],matriz_spawn_enemigo,matriz_spawn_enemigo_explosion)
        spawns.add(s)
        y += s.rect.height+esp_entre

    #CREACION DE LOS ENEMIGOS
    vidas_spawn = s.vidas

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
                if event.key == pg.K_DOWN:
                    j.vely=10
                    j.velx=0
                    j.fila=4
                if event.key == pg.K_UP:
                    j.vely=-10
                    j.velx=0
                    j.fila=7
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
        #CREACION DE LOS RIVALES DESDE EL SPAWN
        for s in spawns:
            if s.tempo == 0 :
                s.tempo = random.randrange(50,100)
                pos = s.rect.topleft
                e = Rival(matriz_enemigo,matriz_enemigo_explosion,pos)
                e2 = Rival2(matriz_enemigo2,matriz_enemigo2_explosion,pos)
                enemigos.add(e)
                
                enemigos2.add(e2)
        #DISPAROS DE LOS RIVALES
        for e in enemigos:
            if e.tempo == 0:
                e.tempo = random.randrange(10)
                pos = e.rect.topleft
                pos1 = [pos[0],pos[1]+20]
                e = Bala(pos1,matriz_bala_enemigo,5)
                balas_enemigos.add(e)
                e.velx = -20
        #COLISION DE LAS BALAS DEL JUGADOR CON LOS ENEMIGOS
        for b in balas_jugador:
            le = pg.sprite.spritecollide(b,enemigos,False)#no borra cuando hay colisión
            for r in le:
                r.muerte = 1
                print(r.muerte)
                balas_jugador.remove(b)
        #Eliminar enemigos con balas jugador
        for e in enemigos:
            if e.muerte == 1 and e.col2 == 13:
                enemigos.remove(e)
        #eliminar enemigos2 con balas jugador
        for e in enemigos2:
            if e.muerte == 1 and e.col2 == 13:
                enemigos2.remove(e)
        #Eliminar spawn con balas jugador
        for b in balas_jugador:
            ls = pg.sprite.spritecollide(b,spawns,False)#
            for r in ls:
                r.vidas -= 1
                #print(r.vidas)
                balas_jugador.remove(b)
        for s in spawns:
            if s.vidas <= 0 and s.col2 == 13:
                spawns.remove(s)

        #COLISION DE LAS BALAS DE LOS ENEMIGOS CON EL JUGADOR
        for b in balas_enemigos:
            ls = pg.sprite.spritecollide(b,jugadores,False)
            for r in ls:
                balas_enemigos.remove(b)
                # vidas_jugador = j.vidas -1
                j.vidas -= 1
                print(vidas_jugador)
                if vidas_jugador > 0:
                    vidas_jugador = j.vidas

        for j in jugadores:
            if j.vidas <= 0 and j.col2 == 16:
                jugadores.remove(j)
                fin = True





        jugadores.update()
        balas_jugador.update()
        balas_enemigos.update()
        spawns.update()
        enemigos.update()
        enemigos2.update()
        pantalla.fill(negro)
        jugadores.draw(pantalla)
        spawns.draw(pantalla)
        enemigos.draw(pantalla)
        enemigos2.draw(pantalla)
        balas_jugador.draw(pantalla)
        balas_enemigos.draw(pantalla)
        #mostrar vidas en pantalla
        j_vidas = 'Vidas:'+ str(vidas_jugador)
        texto = fuente.render(j_vidas,True,blanco)
        pantalla.blit(texto,[50,20])
        #Refresco de pantalla
        pg.display.flip()
        reloj.tick(60)
