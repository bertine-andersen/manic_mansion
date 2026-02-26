import pygame as pg
from konstanter import *
from ting import *

class Spillbrett:
    def __init__(self):
        # Områder på spillbrettet
        self.frisone1 = pg.Rect(0,0,FRISONE_BREDDE,VINDU_HØYDE)
        self.faresone = pg.Rect(FRISONE_BREDDE,0,VINDU_BREDDE-2*FRISONE_BREDDE,VINDU_HØYDE)
        self.frisone2 = pg.Rect(VINDU_BREDDE-FRISONE_BREDDE,0,FRISONE_BREDDE,VINDU_HØYDE)

        # Sauer plukket opp
        self.poeng: int = 0

        # Status for spillet
        self.running: bool = True

        # Ting
        self.spiller = Spiller()

        self.hindringer: list[Hindring] = [Hindring(),Hindring(),Hindring()]

        self.spøkelser: list[Spøkelse] = [Spøkelse()]

        self.sauer: list[Sau] = [Sau(), Sau()]

        self.font = pg.font.SysFont(["arial", "helvetica"], 32)

    def nyHindring(self):
        self.hindringer.append(Hindring())

    def nySau(self):
        self.sauer.append(Sau())

    def nyttSpøkelse(self):
        self.spøkelser.append(Spøkelse())

    def fåPoeng(self):
        self.poeng += 1
        self.spiller.harSau = False

        self.nyHindring()
        self.nySau()
        self.nyttSpøkelse()

    
    def update(self):
        self.spiller.update(self.hindringer, self.spøkelser, self.sauer)
        if not self.spiller.harSau:
            self.sauer = self.spiller.plukkOppSau(self.sauer)
        else:
            if self.frisone1.contains(self.spiller):
                self.fåPoeng()

        if not self.spiller.levende:
            self.running = False

        for spøkelse in self.spøkelser:
            spøkelse.update()


    def draw(self,vindu:pg.Surface) -> None:
        pg.draw.rect(vindu,GREEN,self.frisone1)
        pg.draw.rect(vindu,WHITE,self.faresone)
        pg.draw.rect(vindu,GREEN,self.frisone2)

        self.spiller.draw(vindu)

        for hindring in self.hindringer:
            hindring.draw(vindu)

        for sau in self.sauer:
            sau.draw(vindu)
        
        for spøkelse in self.spøkelser:
            spøkelse.draw(vindu)

        tekst = self.font.render(f'Sauer reddet: {self.poeng}', True, BLACK)
        tekstRect = tekst.get_rect()
        tekstRect.center = (200, 30)

        vindu.blit(tekst,tekstRect)