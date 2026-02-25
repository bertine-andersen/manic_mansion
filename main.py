import pygame as pg
from konstanter import *
from spillbrett import Spillbrett


spillbrett = Spillbrett()

pg.init()
vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HØYDE))
clock = pg.time.Clock()

while spillbrett.running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            spillbrett.running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            spillbrett.running = False

    # Tegner objektene våre (på et blankt hvitt lerret):
    vindu.fill(WHITE)
    spillbrett.draw(vindu)
    spillbrett.update()

    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)

# While running er slutt: Avslutt pygame:
pg.quit()
