print ('start')
import pygame as pg

pg.init()
pg.mixer.set_num_channels(100)

F = pg.display.set_mode((400,700))
run=1
mode='menu'
s_menufnd= pg.image.load('data/space/fndmenu.png');
s_menu= pg.image.load('data/space/menu.png');
s_menuc= pg.image.load('data/space/menucredit.png');
s_menuq= pg.image.load('data/space/menuquit.png');
s_menus= pg.image.load('data/space/menustart.png');
snd_2 = pg.mixer.Sound('data/space/snd/2.aiff')
snd_3 = pg.mixer.Sound('data/space/snd/3.aiff')
pg.mixer.music.load('data/space/snd/music.mp3')
pg.mixer.music.play(1)

mpos=(0,0)
def drawmenu():
    F.blit(s_menufnd,(0,0))
    F.blit(s_menu, (0, 0))
    if mpos[1]>130:
        if mpos[1]<185:
            F.blit(s_menus,(0,0))

    if mpos[1]>185:
        if mpos[1]<245:
            F.blit(s_menuc,(0,0))

    if mpos[1]>245:
        if mpos[1]<300:
            F.blit(s_menuq,(0,0))

def click (p):
    global run
    i=0;
    while pg.mixer.Channel(i).get_busy() :
        i+=1;
    pg.mixer.Channel(i).play(snd_2)
    pg.mixer.Channel(i+1).play(snd_3)
    if p[1]>245:
        if p[1]<300:
            run=0
while run:
    if mode=='menu':
        drawmenu()
    msgs=pg.event.get()
    for m in msgs:
        print(m)
        if m.type==pg.MOUSEBUTTONDOWN:
            click (m.pos)
        if m.type == pg.MOUSEMOTION :
            mpos=m.pos
            #F.fill((m.pos[0] %255,m.pos[1] % 255 ,255))
            #F.fill((255,255,255))
        if m.type==pg.QUIT:
            run=0
    pg.display.update()
print('fin')
