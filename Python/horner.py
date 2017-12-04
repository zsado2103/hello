#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  horner.py
#  

def horner(k, tbwsp, x):
    wynik = tbwsp[0]
    for i in range(1, k+1):
        wynik= wynik*x + tbwsp[i]
        
    return wynik

def main(args):
    k = 3
    tbwsp = []
    x = int(input("Podaj liczbę "))
    
    for i in range(0, 4):
        tmp = int(input("Podaj wspolczynnik "))
        tbwsp.append(tmp)
        #tbwsp[4]=int(input("Podaj współczynniki "))
        
    print("Wynik ", horner(k, tbwsp, x))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
