from __future__ import annotations
import pygame as pg
from konstanter import *
import random as rd


class Spiller:
    def __init__(self) -> None:
        self.rect = pg.Rect((FRISONE_BREDDE-SPILLER_STØRRELSE)//2,
                    (VINDU_HØYDE-SPILLER_HØYDE)//2, SPILLER_STØRRELSE, SPILLER_HØYDE)

        self.levende: bool = True
        self.harSau: bool = False

        self.spiller_raw = pg.image.load(IMAGE_DIR / "spiller.png")
        self.spiller_img = pg.transform.scale(self.spiller_raw,(SPILLER_STØRRELSE,SPILLER_HØYDE))

        self.spillerMedSau_raw = pg.image.load(IMAGE_DIR / "spillermedsau.png")
        self.spillerMedSau_img = pg.transform.scale(self.spillerMedSau_raw,(SPILLER_STØRRELSE,SPILLER_HØYDE))

    def plukkOppSau(self, sauer: list[Sau]) -> list[Sau]:
        for sau in sauer:
            if self.rect.colliderect(sau):
                sauer.remove(sau)
                self.harSau = True
                return sauer
        else:
            return sauer

    def treffSpøkelse(self, spøkelser: list[Spøkelse]) -> None:
        for spøkelse in spøkelser:
            if self.rect.colliderect(spøkelse):
                self.levende = False

    def hindret(self, hindringer: list[Hindring]) -> bool:
        for hindring in hindringer:
            if self.rect.colliderect(hindring):
                return True
        return False

    def utenforKant(self) -> bool:
        if (self.rect.x < 0 or self.rect.x > VINDU_BREDDE - SPILLER_STØRRELSE
             or  self.rect.y < 0 or self.rect.y > VINDU_HØYDE - SPILLER_HØYDE):
            return True
        else:
            return False

    def update(self, hindringer: list[Hindring], spøkelser: list[Spøkelse], sauer: list[Sau]) -> None:
        fart = SPILLER_FART
        if self.harSau:
            fart = fart // 1.5
        
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.rect.y -= fart
            if self.utenforKant() or self.hindret(hindringer):
                self.rect.y += fart
        if keys[pg.K_DOWN]:
            self.rect.y += fart
            if self.utenforKant() or self.hindret(hindringer):
                self.rect.y -= SPILLER_FART
        if keys[pg.K_LEFT]:
            self.rect.x -= fart
            if self.utenforKant() or self.hindret(hindringer):
                self.rect.x += SPILLER_FART
        if keys[pg.K_RIGHT]:
            self.rect.x += SPILLER_FART
            if self.utenforKant() or self.hindret(hindringer):
                self.rect.x -= SPILLER_FART

        self.treffSpøkelse(spøkelser)

    def draw(self,vindu: pg.Surface) -> None:
        if self.harSau:
            vindu.blit(self.spillerMedSau_img, self.rect) 
        else:
            vindu.blit(self.spiller_img, self.rect) 


class Sau:
    def __init__(self) -> None:
        self.rect = pg.Rect(VINDU_BREDDE-(FRISONE_BREDDE+SAU_STØRRELSE)//2,
                    rd.randint(0,VINDU_HØYDE-SAU_STØRRELSE),SAU_STØRRELSE,SAU_STØRRELSE)
        self.plukketOpp: bool = False
        self.sau_raw = pg.image.load(IMAGE_DIR / "sau.png")
        self.sau_img = pg.transform.scale(self.sau_raw,(SAU_STØRRELSE,SAU_STØRRELSE))

    def draw(self,vindu:pg.Surface):
        vindu.blit(self.sau_img, self.rect)


class Spøkelse:
    def __init__(self) -> None:
    
        self.rect = pg.Rect(
                rd.randint(FRISONE_BREDDE, VINDU_BREDDE - FRISONE_BREDDE - SPØKELSE_STØRRELSE),
                rd.randint(0, VINDU_HØYDE - SPØKELSE_STØRRELSE),
                SPØKELSE_STØRRELSE,
                SPØKELSE_STØRRELSE
        )
        self.vx: int = 3
        self.vy: int = 3
        self.kollidert: bool = False

        self.spøkelse_raw = pg.image.load(IMAGE_DIR / "spøkelse.png")
        self.spøkelse_img = pg.transform.scale(self.spøkelse_raw,(SPØKELSE_STØRRELSE,SPØKELSE_STØRRELSE))
    
    def update(self) -> None:
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

    def draw(self, vindu:pg.Surface) -> None:
        vindu.blit(self.spøkelse_img, self.rect)


class Hindring:
    def __init__(self) -> None:
        self.rect = pg.Rect(rd.randint(FRISONE_BREDDE,VINDU_BREDDE-FRISONE_BREDDE-HINDRING_STØRRELSE),
                    rd.randint(0,VINDU_HØYDE-HINDRING_STØRRELSE),HINDRING_STØRRELSE,HINDRING_STØRRELSE)
        self.stein_raw = pg.image.load(IMAGE_DIR / "stein.png")
        self.stein_img = pg.transform.scale(self.stein_raw,(HINDRING_STØRRELSE,HINDRING_STØRRELSE))
    
    def draw(self,vindu:pg.Surface) -> None:
        vindu.blit(self.stein_img, self.rect)