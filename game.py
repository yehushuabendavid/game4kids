print ('start')
import pygame as pg
import time
import random as rnd
import math

pg.init()
pg.mixer.set_num_channels(100)
pg.display.set_caption("Code4Kids - Space Defence Force -")

F = pg.display.set_mode((400,700))
run=1
mode='menu'
s_menufnd= pg.image.load('data/space/fndmenu.png');
s_gamefnd= pg.image.load('data/space/fndgame.png');
s_menu= pg.image.load('data/space/menu.png');
s_menuc= pg.image.load('data/space/menucredit.png');
s_menuq= pg.image.load('data/space/menuquit.png');
s_menus= pg.image.load('data/space/menustart.png');
snd_1 = pg.mixer.Sound('data/space/snd/1.aiff')
snd_2 = pg.mixer.Sound('data/space/snd/2.aiff')
snd_3 = pg.mixer.Sound('data/space/snd/3.aiff')
snd_4 = pg.mixer.Sound('data/space/snd/4.aiff')
pg.mixer.music.load('data/space/snd/music.mp3')
s_bad1=pg.image.load('data/space/e1.png');
s_bad2=pg.image.load('data/space/e2.png');
s_bad3=pg.image.load('data/space/e3.png');

s_w=pg.image.load('data/space/w.png');
s_w1=pg.image.load('data/space/w1.png');
s_w2=pg.image.load('data/space/w2.png');
s_w3=pg.image.load('data/space/w3.png');
s_w4=pg.image.load('data/space/w4.png');


s_v=[pg.image.load('data/space/v1.png')];
s_v+=[pg.image.load('data/space/v2.png')];
s_v+=[pg.image.load('data/space/v3.png')];
s_v+=[pg.image.load('data/space/v4.png')];


s_laser=pg.image.load('data/space/laser.png');

s_team=pg.image.load('data/space/team.png');

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

pg.mixer.set_num_channels(50)
def piou(snd):
    i = 0 ;
    while pg.mixer.Channel(i).get_busy():
        i+=1
    if i == 51:
        i=10;
    pg.mixer.Channel(i).play(snd)
pg.mixer.music.play(-1)
mpos=(0,0)
def drawmenu():
    global team
    F.blit(s_menufnd,(0,0))
    F.blit(s_menu, (0, 0))
    if team == 1 :
        F.blit(s_team,(0,0));
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
    global team
    i=0;
    if mpos[1]>130:
        if mpos[1]<185:
            pg.mouse.set_visible(0)
            mode='game'
            bads=[]
            newbad()
            newbad()
            newbad()
    if mpos[1]>185:
        if mpos[1]<245:
            team=(team + 1) % 2
    if p[1]>245:
        if p[1]<300:
            run=0

t=0;
def drawgame():
    global dt
    global mode
    global modew
    global bads
    global mpos
    global obj_list
    tt = time.time();
    #newbad()
    F.blit(s_gamefnd,(0,0))

    F.blit(s_w, (modew *100, 600))

    F.blit(s_w1,(0,600))
    F.blit(s_w2,(100,600))
    F.blit(s_w3,(200,600))
    F.blit(s_w4,(300,600))
    listbad = []
    newobjlist = []

    for o in obj_list:
        if (tt - o["time"]) <= o["dur"]:
            newobjlist+=[o]
        F.blit(o["img"],o["pos"])
    obj_list = newobjlist;


    for b in bads:
        if b['vie']==1:
            F.blit(b['img'],(b["pos"][0]-25,b["pos"][1]-25))
            listbad+=[b]
        else:
            bdt = tt -b["bb"]
            if bdt < 3:
                F.blit(s_booms[int(len(s_booms)*bdt/3)], (b["pos"][0] - 50, b["pos"][1] - 50))
                listbad += [b]

        b['pos'][1]+=b["speed"]*dt
        if b["pos"][1]>550:
            pg.mouse.set_visible(1)
            mode='menu'
    bads = listbad

    F.blit(s_v[modew],(mpos[0]-s_v[modew].get_width()/2,mpos[1]-s_v[modew].get_height()/2))


obj_list = []

def dist(p1,p2):
    return math.hypot(p2[0]-p1[0],p2[1]-p1[1])

def click_game(p):
    global mode
    global modew
    global bads
    global obj_list

    if modew==0:
        piou(snd_1)


        dd = 100
    if modew==1:
        piou(snd_2)
        dd = 50
    if modew==2:
        piou(snd_3)
        dd = 25
        o={}
        o["img"] = s_laser
        o["pos"] = (p[0]-25,0)
        o["time"] = time.time()
        o["dur"] = 0.25
        obj_list+=[o]
    if modew==3:
        piou(snd_4)
        dd = 100
    for b in bads:
        if (dist(p,b["pos"]) <= dd) or ((modew==2) and (abs(b["pos"][0]-p[0])<=dd)) :
            b["speed"]=0
            if modew != 3:
                if b["vie"]:
                    b['bb'] = time.time()
                b["vie"]=0;

    if p[1]>600:
        modew=int(p[0]/100)
    mode = "game"

    newbad()
t=time.time()
modew=1
team=0;
wactive = 1;
while run:
    dt=time.time() - t;
    dt=dt*wactive;
    t=time.time()
    if mode=='menu':
        drawmenu()
    if mode=='game':
        drawgame()
    msgs=pg.event.get()
    for m in msgs:
        print(m)
        if m.type==pg.ACTIVEEVENT:
            wactive=m.gain;
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
