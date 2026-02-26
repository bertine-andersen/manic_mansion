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
    spiller_img = pg.image.load(IMAGE_DIR / "spiller.png")

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

    def draw(self,vindu: pg.Surface) -> None:
        vindu.blit(self.spiller_img, self.rect) 


class Sau:
    def __init__(self):
        self.rect = pg.Rect(VINDU_BREDDE-(FRISONE_BREDDE+SAU_STØRRELSE)//2,
                    rd.randint(0,VINDU_HØYDE-SAU_STØRRELSE),SAU_STØRRELSE,SAU_STØRRELSE)
        self.plukketOpp: bool = False
        self.sau_img = pg.image.load(IMAGE_DIR / "sau.png")

    def draw(self,vindu:pg.Surface):
        vindu.blit(self.sau_img, self.rect)

@dataclass(slots=True)
class Spøkelse:
    rect: pg.Rect
    spøkelse_img = pg.image.load(IMAGE_DIR / "spøkelse.png")
    
    def update(self):
        pass

    def draw(self,vindu:pg.Surface):
        vindu.blit(self.spøkelse_img, self.rect)

class Hindring:
    def __init__(self):
        self.rect = pg.Rect(rd.randint(FRISONE_BREDDE,VINDU_BREDDE-FRISONE_BREDDE-HINDRING_STØRRELSE),
                    rd.randint(0,VINDU_HØYDE-HINDRING_STØRRELSE),HINDRING_STØRRELSE,HINDRING_STØRRELSE)
        self.stein_img = pg.image.load(IMAGE_DIR / "stein.png")
    
    def draw(self,vindu:pg.Surface):
        vindu.blit(self.stein_img, self.rect)