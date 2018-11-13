#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos_str.py
#  

def push(stos, rozmiar, SP,  dane):
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1
    else:
        print("Stack overflow")
    return SP
        
def pop(stos, rozmiar, SP):
    element = None
    SP -= 1 # DEKREMENTACJA
    if SP >= -1:
        element = (stos[SP])
        stos[SP] = None
    else:
        print("Stack overflow")
    return SP, element

def main(args):
    stos = [] # pusta lista, zasięg globalny
    SP = 0 # wskaźnik wierzchołka
    rozmiar = 3
    stos = [None] * rozmiar   # null, nil, none
    SP = push(stos, rozmiar, SP, 2)
    SP = push(stos, rozmiar, SP, 5)
    SP, element = pop(stos, rozmiar, SP)
    print(element)
    SP = push(stos, rozmiar, SP, 3)
    SP, element = pop(stos, rozmiar, SP)
    print(element)
    SP, element = pop(stos, rozmiar, SP)
    print(element)
    SP, element = pop(stos, rozmiar, SP)
    print(SP)
    print(stos)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
