#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos_str.py
#  

stos = [] # pusta lista, zasięg globalny
SP = 0 # wskaźnik wierzchołka

def push(rozmiar, dane):
    global stos, SP
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1
    else:
        print("Stack overflow")
        
        
def pop(rozmiar):
    global stos, SP
    SP -= 1 # DEKREMENTACJA
    if SP >= -1:
        print(stos[SP])
        stos[SP] = None
    else:
        print("Stack overflow")


def main(args):
    global stos, SP
    rozmiar = int(input("Podaj rozmiar stosu. "))
    stos = [None] * rozmiar   # null, nil, none
    push(rozmiar,2)
    push(rozmiar,5)
    pop(rozmiar)
    push(rozmiar,3)
    pop(rozmiar)
    pop(rozmiar)
    pop(rozmiar)
    print(SP)
    print(stos)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
