import pygame as pg
import math
import random
import time
#colores
blanco = [255,255,255]
negro = [0,0,0]
rojo = [255,0,0]
azul = [0,0,255]
verde = [0,255,0]
gris = [156,156,156]
#dimensiones pantalla
ancho,alto = [1080,600]
#centro de la pantalla
centro_x = ancho//2
centro_y = alto//2
origen = [centro_x,centro_y]

#colores
def color_aleatorio():
    return [random.randrange(255),random.randrange(255),random.randrange(255)]

#funcion que dibuja el plano cartesiano
def Plano_Cartesiano(pantalla):
    ox=origen[0]
    oy=origen[1]
    pg.draw.line(pantalla,blanco,[ox,0],[ox,alto])
    pg.draw.line(pantalla,blanco,[0,oy],[ancho,oy])

#funcion para dibujar una Recta con el mouse
def Recta(coordenadas,pantalla,a,b):
    pg.draw.line(pantalla,rojo,coordenadas[a],coordenadas[b])

#funcion para dibujar un punto con el click
def Punto(coordenada,pantalla):
    pg.draw.circle(pantalla,rojo,coordenada,4)

#dibujar triangulo
def Triangulo_Lineas_Auto(coordenadas,pantalla):
    Recta(coordenadas,pantalla,0,1)
    Recta(coordenadas,pantalla,1,2)
    Recta(coordenadas,pantalla,0,2)

#funcion para dibujar un triangulo con el clicl
def Triangulo(coordenadas,pantalla,cont):
    if cont == 1:
        Recta(coordenadas,pantalla,cont-1,cont)
    if cont == 2:
        Recta(coordenadas,pantalla,cont-1,cont)
    if cont == 3:
        Recta(coordenadas,pantalla,cont-3,cont-1)

#Lista de puntos
def Por_Menos_Uno(puntos):
    ls=[]
    for e in puntos:
        x=e[0]*-1
        y=e[1]*-1
        ls.append([x,y])
    return ls

#Conjunto de lista de puntos
def Conjunto_Por_MenosUno(lista):
    temp=[]
    temp2=[]
    for i in lista:
        temp=Por_Menos_Uno(i)
        temp2.append(temp)
        temp=[]
    return temp2

#dibuja una lista de lineas
def Dibujar_lista_lineas(pantalla,lineas):
    for i in lineas:
        Recta(i,pantalla,0,1)

#dibuja un marco en la pantalla de una secuencia de lineas
def marco_pantalla(pantalla,lineas,velx,vely):
    Dibujar_lista_lineas(pantalla,lineas)
    while lineas[2][1][0]<ancho-10 and lineas[0][0][1]==30:
        velx=20
        vely=0
        for e in lineas:
            for i in e:
                i[0]+=velx
        Dibujar_lista_lineas(pantalla,lineas)
    while lineas[2][1][1]<alto-50:
        velx=0
        vely=30
        for e in lineas:
            for i in e:
                i[1]+=vely
        Dibujar_lista_lineas(pantalla,lineas)
    while lineas[0][0][0]>10:
        velx=-20
        vely=0
        for e in lineas:
            for i in e:
                i[0]+=velx
        Dibujar_lista_lineas(pantalla,lineas)
    while lineas[2][1][1]>40:
        velx=0
        vely=-30
        for e in lineas:
            for i in e:
                i[1]+=vely
        Dibujar_lista_lineas(pantalla,lineas)

#Define si un punto esta cerca o no de otro
def Esta_Cerca(mouse,punto):
    error=10
    ls=[]
    ls.append(punto[0])
    ls.append(punto[1])
    p1=ls[0]
    p2=ls[1]
    lim_inf_x=p1-error
    lim_inf_y=p2-error
    lim_sup_x=p1+error
    lim_sup_y=p2+error
    if(((mouse[0]<=lim_sup_x)and(mouse[0]>=lim_inf_x)) and
        ((mouse[1]<=lim_sup_y)and(mouse[1]>=lim_inf_y))):
        return True
    else:
        return False

#pasar de cartesiano a pantalla
def A_Pantalla(punto):
    xp=punto[0]+centro_x
    yp=-punto[1]+centro_y
    p=[xp,yp]
    return p

#pasar de pantalla a cartesiano
def A_Cartesiano(punto):
    xp= punto[0]-centro_x
    yp= -punto[1]+centro_y
    p=[xp,yp]
    return p

def DCA_UnPunto(punto,descentrar):
    xp=punto[0]+descentrar[0]
    yp=-punto[1]+descentrar[1]
    p=[xp,yp]
    return p

def CA_UnPunto(punto,centrar):
    xp= punto[0]-centrar[0]
    yp= -punto[1]+centrar[1]
    p=[xp,yp]
    return p

def cartesianas_a_polares(x,y):
    r = int(math.sqrt(x**2 + y **2))
    angulo = math.atan(y/x)
    angulo = angulo* 180 / math.pi
    return r,angulo

def coordenadas_polares1(r,angulo):
    angu1= math.radians(angulo)
    p =(int(r*math.cos(angu1)), int(r*math.sin(angu1)))
    return p

#Escalar
def Escalar(punto,escala):
	xp = punto[0]*escala[0]
	yp = punto[1]*escala[1]
	p=[xp,yp]
	return p

#Rotar
def Rotar_Horario(punto,angulo):
    rad = math.radians(angulo)
    xp = punto[0]*math.cos(rad)-punto[1]*math.sin(rad)
    yp = punto[0]*math.sin(rad)+punto[1]*math.cos(rad)
    p = [xp,yp]
    return p

def Rotar_AntiHorario(punto,angulo):
    punto= A_Cartesiano(punto)
    rad = math.radians(angulo)
    xp = punto[0]*math.sin(rad)+punto[1]*math.cos(rad)
    yp = -punto[0]*math.cos(rad)+punto[1]*math.sin(rad)
    p = [xp,yp]
    p = A_Pantalla(p)
    return p

def JRotar_AntiHorario(punto,angulo,centro):
    punto= CA_UnPunto(punto,centro)
    rad = math.radians(angulo)
    xp = punto[0]*math.sin(rad)+punto[1]*math.cos(rad)
    yp = -punto[0]*math.cos(rad)+punto[1]*math.sin(rad)
    p = [xp,yp]
    p = DCA_UnPunto(punto,centro)
    return p

def Aumentar_Radio(punto,radio,centro):
    punto = CA_UnPunto(punto,centro)
    r,angulo=cartesianas_a_polares(punto[0],punto[1])
    r += radio
    punto = coordenadas_polares1(r,angulo)
    punto=DCA_UnPunto(punto,centro)
    return punto[0],punto[1]

def Aumentar_Radio_Disparo(punto,radio,centro):
    punto = CA_UnPunto(punto,centro)
    r,angulo=cartesianas_a_polares(punto[0],punto[1])
    r += radio
    punto = coordenadas_polares1(r,angulo)
    punto=DCA_UnPunto(punto,centro)
    return [punto[0],punto[1]]

def Rosa_polar(a,tam):
	R = []
	for i in range(0,360):
		r = tam*(math.cos(a*math.radians(i)))
		p = (r*math.cos(math.radians(i)),r*math.sin(math.radians(i)))
		R.append(p)
	return R

def Pitagoricas(num_lados,Magnitud):
	Angulo = 0;
	R=[]
	for i in range(num_lados):
		punto = (Magnitud*math.cos(Angulo), Magnitud*math.sin(Angulo))
		R.append(punto)
		Angulo += math.radians(360/num_lados)
	return R
#Trasladar
def Trasladar(punto,traslacion):
	xp=punto[0]+traslacion[0]
	yp=punto[1]+traslacion[1]
	p=[xp,yp]
	return p

#pasa unos puntos de pantalla a cartesiano
def Puntos_A_Cartesiano(puntos):
	for i in range(len(puntos)):
		puntos[i] = A_Cartesiano(puntos[i])

#pasa unos puntos de cartesiano a pantalla
def Puntos_A_Pantalla(puntos):
	for i in range(len(puntos)):
		puntos[i] = A_Pantalla(puntos[i])
	#return puntos

def Escalar_Puntos(puntos,escala):
	for i in range(len(puntos)):
		puntos[i] = Escalar(puntos[i],escala)
	#return puntos

def Trasladar_Puntos(puntos,traslacion):
	for i in range(len(puntos)):
		puntos[i] = Trasladar(puntos[i],traslacion)
    #return puntos

def Rotar_Puntos_Horario(puntos,angulo):
	for i in range(len(puntos)):
		puntos[i] = Rotar_Horario(puntos[i],angulo)
    #return puntos

def Rotar_Puntos_AntiHorario(puntos,angulo):
	for i in range(len(puntos)):
		puntos[i] = Rotar_AntiHorario(puntos[i],angulo)
    #return puntos

def matriz_sprites(imagen,anc,alt,height,high):
    pass
    x,y = 0,0
    matriz=[]
    lista=[]
    for j in range(0,anc,height):
        for i in range(0,alt,high):
            imag=imagen.subsurface(j,i,height,high)
            lista.append(imag)
        matriz.append(lista)
        lista=[]
    return matriz

def centrar_texto(imagen):
    info = imagen.get_rect()
    position = centro_x - (info.width/2) #CENTRAR LA IMAGEN
    return(position)

def rango_menu(box,pos_box):
    limits = box.get_rect()
    pos = pg.mouse.get_pos()
    # print(pos)
    # print(limits)
    if pos_box[0] < pos[0] and pos[0] < pos_box[0] + limits.width and pos_box[1] < pos[1] and pos[1] < pos_box[1] + limits.height:
        # print("si")
        return True
    pass

def menu(display,p1,p2,p3,p4):
    display.fill(negro)
    size_img = 64
    Messages = pg.font.Font(None,size_img)
    top_message = "SOME SPACE GAME"
    top_message = Messages.render(top_message,True,rojo,blanco)

    play_message = "PLAY"
    if not p1:
        play_message = Messages.render(play_message,True,rojo,azul)
    else:
        play_message = Messages.render(play_message,True,azul,rojo)

    option_message = "CONTROLS"
    if not p2:
        option_message = Messages.render(option_message,True,rojo,azul)
    else:
        option_message = Messages.render(option_message,True,azul,rojo)

    credit_message = "CREDITS"
    if not p3:
        credit_message = Messages.render(credit_message,True,rojo,azul)
    else:
        credit_message = Messages.render(credit_message,True,azul,rojo)

    exit_message = "EXIT"
    if not p4:
        exit_message = Messages.render(exit_message,True,rojo,azul)
    else:
        exit_message = Messages.render(exit_message,True,azul,rojo)


    y = size_img * 2
    x = centrar_texto(top_message)
    display.blit(top_message,[x,size_img])

    y += size_img
    x = centrar_texto(play_message)
    display.blit(play_message,[x,y])
    p1 = rango_menu(play_message,[x,y])

    y += size_img
    x = centrar_texto(option_message)
    display.blit(option_message,[x,y])
    p2 = rango_menu(option_message,[x,y])

    y += size_img
    x = centrar_texto(credit_message)
    display.blit(credit_message,[x,y])
    p3 = rango_menu(credit_message,[x,y])

    y += size_img
    x = centrar_texto(exit_message)
    display.blit(exit_message,[x,y])
    p4 = rango_menu(exit_message,[x,y])

    pg.display.flip()
    return p1,p2,p3,p4

def menu_creditos(display,p5,p6):
    display.fill(negro)
    size_img = 32
    Messages = pg.font.Font(None,size_img)
    Messages2 = pg.font.Font(None,size_img*2)
    creator_1 = "Jorge Orobio Auz"
    creator_1 = Messages.render(creator_1,True,verde,blanco)

    creator_2 = "Nicolas Aguirre Espinosa"
    creator_2 = Messages.render(creator_2,True,verde,blanco)

    creator_3 = "Maria Paula Loaiza Lopez"
    creator_3 = Messages.render(creator_3,True,verde,blanco)


    back_message = "MENU"
    if not p5:
        back_message = Messages2.render(back_message,True,rojo,azul)
    else:
        back_message = Messages2.render(back_message,True,azul,rojo)

    exit_message = "EXIT"
    if not p6:
        exit_message = Messages2.render(exit_message,True,rojo,azul)
    else:
        exit_message = Messages2.render(exit_message,True,azul,rojo)


    y = size_img * 2
    x = centrar_texto(back_message)
    display.blit(back_message,[x,y])
    p5= rango_menu(back_message,[x,y])

    y += size_img *2
    x = centrar_texto(exit_message)
    display.blit(exit_message,[x,y])
    p6 = rango_menu(exit_message,[x,y])

    y += size_img * 4
    x = centrar_texto(creator_1)
    display.blit(creator_1,[x,y])

    y += size_img
    x = centrar_texto(creator_2)
    display.blit(creator_2,[x,y])

    y += size_img
    x = centrar_texto(creator_3)
    display.blit(creator_3,[x,y])


    pg.display.flip()
    return p5,p6

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

def controls(display,p13,p14):
    display.fill(negro)
    size_img = 32
    Messages = pg.font.Font(None,size_img)
    Messages2 = pg.font.Font(None,size_img*2)
    direccion_imagen_controls = "Sprites/controles.png"
    imagen_controls = pg.image.load(direccion_imagen_controls)

    back_message = "MENU"
    if not p13:
        back_message = Messages2.render(back_message,True,rojo,azul)
    else:
        back_message = Messages2.render(back_message,True,azul,rojo)

    exit_message = "EXIT"
    if not p14:
        exit_message = Messages2.render(exit_message,True,rojo,azul)
    else:
        exit_message = Messages2.render(exit_message,True,azul,rojo)


    y = size_img * 15
    x = centrar_texto(back_message)
    display.blit(back_message,[x,y])
    p13= rango_menu(back_message,[x,y])

    y += size_img *2
    x = centrar_texto(exit_message)
    display.blit(exit_message,[x,y])
    p14 = rango_menu(exit_message,[x,y])
    display.blit(imagen_controls,[0,0])
    pg.display.flip()
    return p13,p14

def preludio(pantalla):
	fondo= pg.image.load('Sprites/Fondo/fondo5.jpg')
	fuente=pg.font.Font(None,64)
	pantalla.blit(fondo,[0,0])
	mensaje="Durante milenios ha habido una lucha entre"
	mensaje1="el bien y el mal, se necesita restaurar por fin"
	mensaje2="la paz en toda la galaxia por ello la flota"
	mensaje3="real de Alpha Centuary debe viajar a una"
	mensaje4="reunión diplomatica para asi conseguir un"
	mensaje5="nuevo aliado que inclinaría labalanza hacia"
	mensaje6="el fin de este conflicto."


	mensaje7="Se necesita garantizar la seguridad de esta"
	mensaje8="flota, para ello contratan al piloto más"
	mensaje9="implacable de todo el universo, el capitán"
	mensaje10="Charles A. Ludwing con la nave más"
	mensaje11="poderosa conocida, Arcadia."



	mensaje12="Al inicio de su travesía son interceptados"
	mensaje13="por la Armada Galáctica,que supieron de"
	mensaje14="esta maniobra por un informante, el capitan"
	mensaje15="tiene un solo objetivo en mente, cumplir su"
	mensaje16="misión, decide actuar como cebo y"
	mensaje17="separarse de la flota real atrayendo así"
	mensaje18="a las naves cazas por una grieta lunar."



	texto=fuente.render(mensaje,True,blanco)
	texto1=fuente.render(mensaje1,True,blanco)
	texto2=fuente.render(mensaje2,True,blanco)
	texto3=fuente.render(mensaje3,True,blanco)
	texto4=fuente.render(mensaje4,True,blanco)
	texto5=fuente.render(mensaje5,True,blanco)
	texto6=fuente.render(mensaje6,True,blanco)
	texto7=fuente.render(mensaje7,True,blanco)
	texto8=fuente.render(mensaje8,True,blanco)
	texto9=fuente.render(mensaje9,True,blanco)
	texto10=fuente.render(mensaje10,True,blanco)
	texto11=fuente.render(mensaje11,True,blanco)
	texto12=fuente.render(mensaje12,True,blanco)
	texto13=fuente.render(mensaje13,True,blanco)
	texto14=fuente.render(mensaje14,True,blanco)
	texto15=fuente.render(mensaje15,True,blanco)
	texto16=fuente.render(mensaje16,True,blanco)
	texto17=fuente.render(mensaje17,True,blanco)
	texto18=fuente.render(mensaje18,True,blanco)



	pantalla.blit(texto,[90,94])
	pantalla.blit(texto1,[90,158])
	pantalla.blit(texto2,[90,222])
	pantalla.blit(texto3,[90,286])
	pantalla.blit(texto4,[90,350])
	pantalla.blit(texto5,[90,414])
	pantalla.blit(texto6,[90,478])

	pg.display.flip()
	time.sleep(10)
	pantalla.blit(fondo,[0,0])
	pantalla.blit(texto7,[100,158])
	pantalla.blit(texto8,[100,222])
	pantalla.blit(texto9,[100,286])
	pantalla.blit(texto10,[100,350])
	pantalla.blit(texto11,[100,414])

	pg.display.flip()
	time.sleep(10)
	pantalla.blit(fondo,[0,0])
	pantalla.blit(texto12,[100,94])
	pantalla.blit(texto13,[100,158])
	pantalla.blit(texto14,[100,222])
	pantalla.blit(texto15,[100,286])
	pantalla.blit(texto16,[100,350])
	pantalla.blit(texto17,[100,414])
	pantalla.blit(texto18,[100,478])

	pg.display.flip()
	time.sleep(10)

	pg.display.flip()


def interludio(pantalla):
    fondo= pg.image.load('Sprites/Fondo/fondo6.jpg')
    fondo2= pg.image.load('Sprites/Fondo/fondo7.jpg')
    fuente=pg.font.Font(None,64)

    pantalla.blit(fondo,[0,0])
    mensaje="Luego de haber estado al borde de la"
    mensaje1="muerte,todos los tripulantes de la flota"
    mensaje2="real han logrado desembarcar en Arcadia"
    mensaje3="para así disponerse a emprender"
    mensaje4="nuevamente su viaje hacia su destino final."

    texto=fuente.render(mensaje,True,blanco)
    texto1=fuente.render(mensaje1,True,blanco)
    texto2=fuente.render(mensaje2,True,blanco)
    texto3=fuente.render(mensaje3,True,blanco)
    texto4=fuente.render(mensaje4,True,blanco)

    pantalla.blit(texto,[90,158])
    pantalla.blit(texto1,[90,222])
    pantalla.blit(texto2,[90,286])
    pantalla.blit(texto3,[90,350])
    pantalla.blit(texto4,[90,414])

    pg.display.flip()
    time.sleep(10)

    pantalla.blit(fondo2,[0,0])
    pg.display.flip()
    time.sleep(3)
