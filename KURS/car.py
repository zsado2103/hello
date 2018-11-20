#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py

# napisz definicjÄ obiektu samochĂłd z nast. atrybutami:
# marka, np. "Fiat"
# model, np. "Tipo"
# rok produkcji, np. "2005"
# nadwozie, np. "sedan"
# metody obiektu:
# wiek() â zwraca wiek auta w latach

from datetime import date

class Samochod():
    
    def __init__(self, rok_p):
        self.rok_p = rok_p
    
    def wiek(self):
        return date.today().year - self.rok_p
        
s = Samochod(2005)
print("Wiek:", s.wiek())
