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
        self.spiller_img = pg.image.load(IMAGE_DIR / "spiller.png")

    def plukkOpp(self):
        pass

    def treffSpøkelse(self):
        pass

    def hindret(self, hindringer: list[Hindring]):
        for hindring in hindringer:
            if self.rect.colliderect(hindring):
                return True
        return False

    def utenforKant(self) -> bool:
        if (self.rect.x < 0 or self.rect.x > VINDU_BREDDE - SPILLER_STØRRELSE
             or  self.rect.y < 0 or self.rect.y > VINDU_HØYDE - SPILLER_STØRRELSE):
            return True
        else:
            return False

    def update(self, hindringer: list[Hindring]):
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
    rect = pg.Rect(
            rd.randint(FRISONE_BREDDE, VINDU_BREDDE - FRISONE_BREDDE - SPØKELSE_STØRRELSE),
            rd.randint(0, VINDU_HØYDE - SPØKELSE_STØRRELSE),
            SPØKELSE_STØRRELSE,
            SPØKELSE_STØRRELSE
        )
    spøkelse_img = pg.image.load(IMAGE_DIR / "spøkelse.png")
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
        vindu.blit(self.spøkelse_img, self.rect)

class Hindring:
    def __init__(self):
        self.rect = pg.Rect(rd.randint(FRISONE_BREDDE,VINDU_BREDDE-FRISONE_BREDDE-HINDRING_STØRRELSE),
                    rd.randint(0,VINDU_HØYDE-HINDRING_STØRRELSE),HINDRING_STØRRELSE,HINDRING_STØRRELSE)
        self.stein_img = pg.image.load(IMAGE_DIR / "stein.png")
    
    def draw(self,vindu:pg.Surface):
        vindu.blit(self.stein_img, self.rect)