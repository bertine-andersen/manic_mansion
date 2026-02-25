#from __future__ import annotations
import pygame as pg
from konstanter import *
from dataclasses import dataclass

@dataclass(slots=True)
class Spiller:
    # Områder på spillbrettet
    rect: pg.Rect

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

    def draw(self):
        pass

@dataclass(slots=True)
class Sau:
    rect: pg.Rect
    plukketOpp: bool

@dataclass(slots=True)
class Spøkelse:
    rect: pg.Rect
    
    def update(self):
        pass

    def draw(self):
        pass

@dataclass(slots=True)
class Hindring:
    rect: pg.Rect