import pygame as pg
from konstanter import *
from dataclasses import dataclass
from ting import *

@dataclass(slots=True)
class Spillbrett:
    # Områder på spillbrettet
    frisone1 = pg.Rect(0,0,FRISONE_BREDDE,VINDU_HØYDE)
    faresone = pg.Rect(FRISONE_BREDDE,0,VINDU_BREDDE-2*FRISONE_BREDDE,VINDU_HØYDE)
    frisone2 = pg.Rect(VINDU_BREDDE-FRISONE_BREDDE,0,FRISONE_BREDDE,VINDU_HØYDE)

    # Sauer plukket opp
    poeng: int = 0

    # Status for spillet
    running: bool = True

    # Ting
    spiller = Spiller()

    hindringer = [Hindring(),Hindring(),Hindring()]

    sauer = [Sau()]

    def nyHindring(self):
        self.hindringer.append(Hindring())

    def nySau(self):
        self.sauer.append(Sau())

    def nyttSpøkelse(self):
        pass
    
    def update(self):
        self.spiller.update()

    def draw(self,vindu:pg.Surface) -> None:
        pg.draw.rect(vindu,GREEN,self.frisone1)
        pg.draw.rect(vindu,WHITE,self.faresone)
        pg.draw.rect(vindu,GREEN,self.frisone2)

        self.spiller.draw(vindu)

        for hindring in self.hindringer:
            hindring.draw(vindu)

        for sau in self.sauer:
            sau.draw(vindu)