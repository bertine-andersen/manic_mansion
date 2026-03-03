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
        self.spillerMedSau_raw = pg.image.load(IMAGE_DIR / "spillermedsau.png")

        self.spiller_left = pg.transform.scale(self.spiller_raw, (SPILLER_STØRRELSE, SPILLER_HØYDE))
        self.spiller_right  = pg.transform.flip(self.spiller_left, True, False)

        self.spillerMedSau_left = pg.transform.scale(self.spillerMedSau_raw, (SPILLER_STØRRELSE, SPILLER_HØYDE))
        self.spillerMedSau_right  = pg.transform.flip(self.spillerMedSau_left, True, False)

        self.retning = "right"
        self.spiller_img = self.spiller_right

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
                self.rect.y -= fart
        if keys[pg.K_LEFT]:
            self.retning = "left"
            self.rect.x -= fart
            if self.utenforKant() or self.hindret(hindringer):
                self.rect.x += fart
        if keys[pg.K_RIGHT]:
            self.retning = "right"
            self.rect.x += fart
            if self.utenforKant() or self.hindret(hindringer):
                self.rect.x -= fart

        self.treffSpøkelse(spøkelser)

    def draw(self, vindu: pg.Surface) -> None:
        if self.harSau:
            if self.retning == "right":
                bilde = self.spillerMedSau_right
            else:
                bilde = self.spillerMedSau_left
        else:
            if self.retning == "right":
                bilde = self.spiller_right
            else:
                bilde= self.spiller_left

        vindu.blit(bilde, self.rect) 


class Sau:
    def __init__(self, banedel: pg.Rect) -> None:
        #Finner ut om sauen skal plasseres i midten av startsonen eller sausonen (litt overkomplisert)
        xMuligheter = (FRISONE_BREDDE//2-SAU_STØRRELSE//2, VINDU_BREDDE-FRISONE_BREDDE//2-SAU_STØRRELSE//2)
        xKord = min(xMuligheter, key=lambda x: abs(x - banedel.centerx))

        self.rect = pg.Rect(xKord,
                    rd.randint(banedel.top+SAU_STØRRELSE//2,banedel.bottom-SAU_STØRRELSE//2),SAU_STØRRELSE,SAU_STØRRELSE)
        
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

        # Brukes i update
        self.imgRect = pg.Rect(0,0,0,0)
        self.imgRect.width = self.rect.width * 1.7
        self.imgRect.height = self.rect.height * 1.7
        self.imgRect.y -= 5

        self.spøkelse_raw = pg.image.load(IMAGE_DIR / "spøkelse.png")
        self.spøkelse_left = pg.transform.scale(self.spøkelse_raw, (self.imgRect.width, self.imgRect.height))
        self.spøkelse_right = pg.transform.flip(self.spøkelse_left, True, False)
    
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
        if self.vx > 0:
            bilde = self.spøkelse_right
        else:
            bilde = self.spøkelse_left

        self.imgRect.center = self.rect.center
        vindu.blit(bilde, self.imgRect)


class Hindring:
    def __init__(self) -> None:
        self.rect = pg.Rect(rd.randint(FRISONE_BREDDE,VINDU_BREDDE-FRISONE_BREDDE-HINDRING_STØRRELSE),
                    rd.randint(0,VINDU_HØYDE-HINDRING_STØRRELSE),HINDRING_STØRRELSE,HINDRING_STØRRELSE)
        
        # Justerer recten til bildet for å passe med kollisjonsrecten
        self.imgRect = self.rect.copy()
        self.imgRect.width = self.rect.width * 1.7
        self.imgRect.height = self.rect.height * 1.7
        self.imgRect.center = self.rect.center
        self.imgRect.y -= 5

        self.stein_raw = pg.image.load(IMAGE_DIR / "stein.png")
        self.stein_img = pg.transform.scale(self.stein_raw,(self.imgRect.height,self.imgRect.width))
    
    def draw(self,vindu:pg.Surface) -> None:
        vindu.blit(self.stein_img, self.imgRect)