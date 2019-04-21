print ('start')
import pygame as pg

pg.init()

F = pg.display.set_mode((400,700))
run=1
while run:
    pg.display.update()


    msgs=pg.event.get()

    for m in msgs:
        print(m)
        if m.type == pg.MOUSEMOTION :
            F.fill((m.pos[0] %255,m.pos[1] % 255 ,255))
            #F.fill((255,255,255))

        if m.type==pg.QUIT:


         run=0
print('fin')
