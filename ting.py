#from __future__ import annotations
import pygame as pg
from konstanter import *
from dataclasses import dataclass
import random as rd


class Spiller:
    def __init__(self):
        # Områder på spillbrettet
        self.rect = pg.Rect((FRISONE_BREDDE-SPILLER_STØRRELSE)//2,
                    (VINDU_HØYDE-SPILLER_STØRRELSE)//2,SPILLER_STØRRELSE,SPILLER_STØRRELSE)

        self.levende: bool = True
        self.harSau: bool = False

    def plukkOpp(self):
        pass

    def treffSpøkelse(self):
        pass

    def hindring(self):
        pass

    def utenforKant(self) -> bool:
        if (self.rect.x < 0 or self.rect.x > VINDU_BREDDE - SPILLER_STØRRELSE
             or  self.rect.y < 0 or self.rect.y > VINDU_HØYDE - SPILLER_STØRRELSE):
            return True
        else:
            return False

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.rect.y -= SPILLER_FART
            if self.utenforKant():
                self.rect.y += SPILLER_FART
        if keys[pg.K_DOWN]:
            self.rect.y += SPILLER_FART
            if self.utenforKant():
                self.rect.y -= SPILLER_FART
        if keys[pg.K_LEFT]:
            self.rect.x -= SPILLER_FART
            if self.utenforKant():
                self.rect.x += SPILLER_FART
        if keys[pg.K_RIGHT]:
            self.rect.x += SPILLER_FART
            if self.utenforKant():
                self.rect.x -= SPILLER_FART




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
    rect: pg.Rect
    
    def update(self):
        pass

    def draw(self):
        pass

class Hindring:
    def __init__(self):
        self.rect = pg.Rect(rd.randint(FRISONE_BREDDE,VINDU_BREDDE-FRISONE_BREDDE-HINDRING_STØRRELSE),
                    rd.randint(0,VINDU_HØYDE-HINDRING_STØRRELSE),HINDRING_STØRRELSE,HINDRING_STØRRELSE)
    
    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu,BLACK,self.rect)