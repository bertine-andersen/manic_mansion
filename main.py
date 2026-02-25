import pygame as pg
from konstanter import *
from klasser import *

# Setter opp rutenettet vårt:
frisone1 = pg.Rect(0,0,100,200)
frisone2 = pg.Rect(100,0,200,200)
faresone = pg.Rect(300,0,100,200)

spillbrett = Spillbrett(frisone1,frisone2,faresone)
bredde,hoyde = (400,200)

pg.init()
vindu = pg.display.set_mode( (bredde, hoyde) )
clock = pg.time.Clock()

framecounter = 0
running = True
while running:
    framecounter+=1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = event.pos
            kolonne = mx // CELLE_STR
            rad = my // CELLE_STR
            spillbrett.klikk(rad, kolonne)
            # Nullstill frameCounter (Så man har tid til å klikke på flere før animasjonen fortsetter):
            framecounter = 1




    # Tegner objektene våre (på et blankt hvitt lerret):
    vindu.fill(WHITE)
    spillbrett.draw(vindu)


    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame:
pg.quit()
