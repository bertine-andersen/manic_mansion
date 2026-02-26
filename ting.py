#from __future__ import annotations
import pygame as pg
from konstanter import *
from dataclasses import dataclass
import random as rd

@dataclass(slots=True)
class Spiller:
    # Områder på spillbrettet
    rect = pg.Rect((FRISONE_BREDDE-SPILLER_STØRRELSE)//2,
                   (VINDU_HØYDE-SPILLER_STØRRELSE)//2,SPILLER_STØRRELSE,SPILLER_STØRRELSE)

    levende: bool = True
    harSau: bool = False

    def plukkOpp(self):
        pass

    def treffSpøkelse(self):
        pass

    def hindring(self):
        pass

    def kant(self):
        pass

    def update(self):
        pass

    def draw(self,vindu:pg.Surface) -> None:
        pg.draw.rect(vindu,RED,self.rect)


class Sau:
    def __init__(self):
        self.rect = pg.Rect(VINDU_BREDDE-(FRISONE_BREDDE+SAU_STØRRELSE)//2,
                    rd.randint(0,VINDU_HØYDE-SAU_STØRRELSE),SAU_STØRRELSE,SAU_STØRRELSE)
        self.plukketOpp: bool = False

    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu,WHITE,self.rect)

@dataclass(slots=True)
class Spøkelse:
    rect = pg.Rect(
            rd.randint(FRISONE_BREDDE, VINDU_BREDDE - FRISONE_BREDDE - SPØKELSE_STØRRELSE),
            rd.randint(0, VINDU_HØYDE - SPØKELSE_STØRRELSE),
            SPØKELSE_STØRRELSE,
            SPØKELSE_STØRRELSE
        )
    vx: int = 3
    vy: int = 3
    kollidert: bool = False

    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.right >= VINDU_BREDDE - FRISONE_BREDDE:
            self.vx *= -1
        if self.rect.left <= FRISONE_BREDDE:
            self.vx *= -1

        if self.rect.bottom >= VINDU_HØYDE:
            self.vy *= -1
        if self.rect.top <= 0:
            self.vy *= -1

    def draw(self, vindu:pg.Surface):
        pg.draw.rect(vindu, GREY, self.rect)

class Hindring:
    def __init__(self):
        self.rect = pg.Rect(rd.randint(FRISONE_BREDDE,VINDU_BREDDE-FRISONE_BREDDE-HINDRING_STØRRELSE),
                            rd.randint(0,VINDU_HØYDE-HINDRING_STØRRELSE),HINDRING_STØRRELSE,HINDRING_STØRRELSE)
    
    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu,BLACK,self.rect)