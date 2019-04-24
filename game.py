print ('start')
import pygame as pg
import time
import random as rnd
import math

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

s_w=pg.image.load('data/space/w.png');
s_w1=pg.image.load('data/space/w1.png');
s_w2=pg.image.load('data/space/w2.png');
s_w3=pg.image.load('data/space/w3.png');
s_w4=pg.image.load('data/space/w4.png');

s_boom=pg.image.load('data/space/boom.png')
s_booms=[];
for i in range(9*6):
    print(s_boom)
    r = pg.Rect(100*(i%9),100*int(i/9),100,100)
    print(i,r)
    s_booms+=[s_boom.subsurface(r)]

bads=[]
def newbad():
    global bads
    bad={}
    bad['speed']=50+(time.time()*1000)%100
    bad["pos"]=[(time.time()*1000)%350,-50]
    bad["vie"] = 1
    bad['img']=rnd.choice([s_bad1,s_bad2,s_bad3])
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
    global bads
    i=0;
    if mpos[1]>130:
        if mpos[1]<185:
            mode='game'
            bads=[]
    if p[1]>245:
        if p[1]<300:
            run=0

t=0;
def drawgame():
    global dt
    global mode
    global modew
    global bads
    #newbad()
    F.blit(s_gamefnd,(0,0))

    F.blit(s_w, (modew *100, 600))

    F.blit(s_w1,(0,600))
    F.blit(s_w2,(100,600))
    F.blit(s_w3,(200,600))
    F.blit(s_w4,(300,600))
    listbad = []

    for b in bads:
        if b['vie']==1:
            F.blit(b['img'],(b["pos"][0]-25,b["pos"][1]-25))
            listbad+=[b]
        else:
            bdt = time.time()-b["bb"]
            if bdt < 3:
                F.blit(s_booms[int(len(s_booms)*bdt/3)], (b["pos"][0] - 50, b["pos"][1] - 50))
                listbad += [b]

        b['pos'][1]+=b["speed"]*dt
        if b["pos"][1]>550:
            mode='menu'
    bads = listbad


def dist(p1,p2):
    return math.hypot(p2[0]-p1[0],p2[1]-p1[1])

def click_game(p):
    global mode
    global modew
    global bads
    if modew==0:
        dd = 100
    if modew==1:
        dd = 50
    if modew==2:
        dd = 25
    if modew==3:
        dd = 100
    for b in bads:
        if dist(p,b["pos"]) <= dd :
            b["speed"]=0
            if modew != 3:
                if b["vie"]:
                    b['bb'] = time.time()
                b["vie"]=0;

    if p[1]>600:
        modew=int(p[0]/100)
    mode = "game"
    piou(snd_3)
    newbad()
t=time.time()
modew=1
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
