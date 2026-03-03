import pygame as pg
pg.init()

from konstanter import *
from spillbrett import Spillbrett


spillbrett = Spillbrett()

vindu = pg.display.set_mode((VINDU_BREDDE,VINDU_HØYDE))
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if not spillbrett.running:

                if spillbrett.restart_rect.collidepoint(event.pos):
                    spillbrett.__init__()

                if spillbrett.avslutt_rect.collidepoint(event.pos):
                    running = False

    # Tegner objektene våre (på et blankt hvitt lerret):
    vindu.fill(WHITE)
    spillbrett.draw(vindu)
    spillbrett.update()

    # Oppdater displayet og klikk framover på klokka:
    pg.display.flip()
    clock.tick(FPS)

# While running er slutt: Avslutt pygame:
pg.quit()
