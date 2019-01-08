#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys


class Plansza():
    """ Plansza gry """

    def __init__(self, szer, wys):
        """ Konstruktor, przygotowanie okna gry """
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        self.szer, self.wys = szer, wys
        pygame.display.set_caption('Gra w życie')

    def rysuj(self, *args):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((0, 0, 0))
        
        for obj in args:
            obj.rysuj_na(self.pow)
        
        pygame.display.update()


class LifeGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys, roz=10):
        pygame.init()
        self.plansza = Plansza(szer * roz, wys * roz)

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
                self.populacja.obsluz_mysze()
                 
            self.plansza.rysuj()
            
ALIVE = 1
DEAD = 0

class Populacja():
    def __init__(self, szer, wys, roz=10):
        self.roz, self.szer, self.wys = roz, szer, wys
        self.generacja = self.utworz_generacje()
        
    def utworz_generacje(self):
        generacja = []
        # ~for x in range(self.szer):
            # ~kolumna = []
            # ~for y in range(self.wys):
                # ~kolumna.append(DEAD)
            # ~generacja.append(kolumna)
        return [[DEAD for y in range(self.wys)] for x in range(self.szer)]
        
    def obsluz_mysze(self):
        przyciski = pygame.mouse.get_pressed()
        if not any(przyciski):
            return
        x, y = pygame.mouse.get.pos()
        x /= self.roz
        y /= self.roz
        
        stan = True if przyciski[0] else False
        print(stan)
        self.generacja[int(x)][int(y)] = ALIVE if stan else DEAD
        
    def rysuj_na(self):
        for x, y in self.zywe_komorki():
            pass 
            
    def zywe_komorki(self):
        """Generator zwracający współrzędne żywych komórek """
        
if __name__ == "__main__":
    gra = LifeGra(80, 40)
    gra.uruchom()
