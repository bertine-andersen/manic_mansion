import pygame as pg
from konstanter import *
from ting import *

class Spillbrett:
    def __init__(self) -> None:
        # Områder på spillbrettet
        self.startsone = pg.Rect(0,0,FRISONE_BREDDE,VINDU_HØYDE)
        self.faresone = pg.Rect(FRISONE_BREDDE,0,VINDU_BREDDE-2*FRISONE_BREDDE,VINDU_HØYDE)
        self.sauSone = pg.Rect(VINDU_BREDDE-FRISONE_BREDDE,0,FRISONE_BREDDE,VINDU_HØYDE)

        # Sauer plukket opp
        self.poeng: int = 0

        # Status for spillet
        self.running: bool = True

        # Ting
        self.spiller = Spiller()

        self.hindringer: list[Hindring] = [Hindring(),Hindring(),Hindring()]

        self.spøkelser: list[Spøkelse] = [Spøkelse()]

        self.sauer: list[Sau] = [Sau(self.sauSone), Sau(self.sauSone)]
        self.reddaSauer: list[Sau] = []

        self.font = pg.font.SysFont(["arial", "helvetica"], 32)
        self.gameOverFont = pg.font.SysFont(["arial", "helvetica"], 50)


        #Bakgrunnsbilder
        # Frisone
        self.frisone_raw = pg.image.load(IMAGE_DIR / "frisoneBakgrunn.png")
        self.frisone_img = pg.transform.scale(self.frisone_raw,(FRISONE_BREDDE, VINDU_HØYDE))

        # Faresone
        self.faresone_raw = pg.image.load(IMAGE_DIR / "faresoneBakgrunn.png")
        self.faresone_img = pg.transform.scale(self.faresone_raw,(VINDU_BREDDE - 2*FRISONE_BREDDE, VINDU_HØYDE))

    def nyHindring(self) -> None:
        self.hindringer.append(Hindring())

    def nySau(self) -> None:
        self.sauer.append(Sau(self.sauSone))

    def reddetSau(self) -> None:
        self.reddaSauer.append(Sau(self.spiller.rect))

    def nyttSpøkelse(self) -> None:
        self.spøkelser.append(Spøkelse())

    def fåPoeng(self) -> None:
        self.poeng += 1
        self.spiller.harSau = False

        self.nyHindring()
        self.nySau()
        self.reddetSau()
        self.nyttSpøkelse()

    
    def update(self) -> None:
        if not self.running:
            return None
        
        self.spiller.update(self.hindringer, self.spøkelser, self.sauer)
        
        if not self.spiller.harSau:
            self.sauer = self.spiller.plukkOppSau(self.sauer)
        else:
            if self.startsone.contains(self.spiller):
                self.fåPoeng()

        if not self.spiller.levende:
            self.running = False

        for spøkelse in self.spøkelser:
            spøkelse.update()


    def draw(self,vindu:pg.Surface) -> None:
        vindu.blit(self.frisone_img, self.startsone)
        vindu.blit(self.faresone_img, self.faresone)
        vindu.blit(self.frisone_img, self.sauSone)

        self.spiller.draw(vindu)

        for hindring in self.hindringer:
            hindring.draw(vindu)

        for sau in self.sauer:
            sau.draw(vindu)

        for sau in self.reddaSauer:
            sau.draw(vindu)
        
        for spøkelse in self.spøkelser:
            spøkelse.draw(vindu)

        tekst = self.font.render(f'Sauer reddet: {self.poeng}', True, BLACK)
        tekstRect = tekst.get_rect()
        tekstRect.center = (230, 30)
        pg.draw.rect(vindu, WHITE, tekstRect)

        vindu.blit(tekst,tekstRect)

        if not self.running:
            overlay = pg.Surface((VINDU_BREDDE, VINDU_HØYDE))
            overlay.set_alpha(100)
            overlay.fill((0, 0, 0))
            vindu.blit(overlay, (0, 0))

            boks = pg.Rect(300, 150, 400, 250)
            pg.draw.rect(vindu, WHITE, boks)
            pg.draw.rect(vindu, BLACK, boks, 3)

            tekst1 = self.gameOverFont.render("GAME OVER", True, BLACK)
            tekst2 = self.font.render(f"Sauer reddet: {self.poeng}", True, BLACK)
            tekst3 = self.font.render("Klikk her for restart", True, BLACK)
            tekst4 = self.font.render("Klikk nederst for avslutt", True, BLACK)

            tekst1Rect = tekst1.get_rect()
            tekst2Rect = tekst2.get_rect()
            tekst3Rect = tekst3.get_rect()
            tekst4Rect = tekst4.get_rect()

            tekst1Rect.center = (VINDU_BREDDE//2, 200)
            tekst2Rect.center = (VINDU_BREDDE//2, 250)
            tekst3Rect.center = (VINDU_BREDDE//2, 300)
            tekst4Rect.center = (VINDU_BREDDE//2, 350)

            vindu.blit(tekst1, tekst1Rect)
            vindu.blit(tekst2, tekst2Rect)
            vindu.blit(tekst3, tekst3Rect)
            vindu.blit(tekst4, tekst4Rect)

            self.restart_rect = pg.Rect(350, 290, 300, 40)
            self.avslutt_rect = pg.Rect(350, 330, 300, 40)