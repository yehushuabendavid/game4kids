print ('start')
import pygame as pg

pg.init()

F = pg.display.set_mode((400,700))
run=1
mode='menu'
s_menufnd= pg.image.load('data/space/fndmenu.png');
s_menu= pg.image.load('data/space/menu.png');
s_menuc= pg.image.load('data/space/menucredit.png');
s_menuq= pg.image.load('data/space/menuquit.png');
s_menus= pg.image.load('data/space/menustart.png');
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
