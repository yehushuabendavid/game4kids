print ('start')
import pygame as pg
import time

pg.init()
pg.mixer.set_num_channels(100)

F = pg.display.set_mode((400,700))
run=1
mode='menu'
s_menufnd= pg.image.load('data/space/fndmenu.png');
s_gamefnd= pg.image.load('data/space/fndgame.png');
s_menu= pg.image.load('data/space/menu.png');
s_menuc= pg.image.load('data/space/menucredit.png');
s_menuq= pg.image.load('data/space/menuquit.png');
s_menus= pg.image.load('data/space/menustart.png');
snd_2 = pg.mixer.Sound('data/space/snd/2.aiff')
snd_3 = pg.mixer.Sound('data/space/snd/3.aiff')
pg.mixer.music.load('data/space/snd/music.mp3')
s_bad1=pg.image.load('data/space/e1.png');
s_bad2=pg.image.load('data/space/e2.png');
s_bad3=pg.image.load('data/space/e3.png');
bads=[]
def newbad():
    global bads
    bad={}
    bad['speed']=50+(time.time()*1000)%100
    bad["pos"]=[(time.time()*1000)%350,-50]
    bad["vie"] = 100
    bad['img']=s_bad3
    bads+=[bad]
def piou(snd):
    pg.mixer.Channel(0).play(snd)
pg.mixer.music.play(-1)
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

def click_menu (p):
    global run
    global mode
    i=0;
    if mpos[1]>130:
        if mpos[1]<185:
            mode='game'
    if p[1]>245:
        if p[1]<300:
            run=0

t=0;
def drawgame():
    global dt
    newbad()
    F.blit(s_gamefnd,(0,0))
    for b in bads:
        F.blit(b['img'],b["pos"])
        b['pos'][1]+=b["speed"]*dt



def click_game(p):
    global mode
    mode = "game"
    piou(snd_2)
    newbad()
t=time.time()

while run:
    dt=time.time() - t;
    print(dt)
    t=time.time()
    if mode=='menu':
        drawmenu()
    if mode=='game':
        drawgame()
    msgs=pg.event.get()
    for m in msgs:
        print(m)
        if m.type==pg.MOUSEBUTTONDOWN:
            if mode == "menu":
                click_menu(m.pos)
            else:
                click_game(m.pos)
        if m.type == pg.MOUSEMOTION :
            mpos=m.pos
            #F.fill((m.pos[0] %255,m.pos[1] % 255 ,255))
            #F.fill((255,255,255))
        if m.type==pg.QUIT:
            run=0
    pg.display.update()
print('fin')
