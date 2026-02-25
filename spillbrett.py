import pygame as pg
from konstanter import *
from dataclasses import dataclass
from ting import *

@dataclass(slots=True)
class Spillbrett:
    # Områder på spillbrettet
    HØYDE = 500
    frisone1 = pg.Rect(0,0,100,HØYDE)
    faresone = pg.Rect(100,0,500,HØYDE)
    frisone2 = pg.Rect(600,0,100,HØYDE)

    # Sauer plukket opp
    poeng: int = 0

    # Status for spillet
    running: bool = True

    def størrelse(self) -> tuple[int,int]:
        bredde = self.frisone1.width+self.frisone2.width+self.faresone.width
        høyde = self.frisone1.height
        return (bredde, høyde)
    def update(self):
        pass

    def nyHindring(self):
        pass

    def nySau(self):
        pass

    def nyttSpøkelse(self):
        pass

    def draw(self,vindu:pg.Surface):
        pg.draw.rect(vindu,GREEN,self.frisone1)
        pg.draw.rect(vindu,WHITE,self.faresone)
        pg.draw.rect(vindu,GREEN,self.frisone2)