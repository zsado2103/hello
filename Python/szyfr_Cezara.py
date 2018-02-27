#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    """Szyfrowanie tekstu za pomocą szyfru Cezara"""
    szyfrogram = ""
    klucz = klucz % 26
    for znak in tekst:
        if ord(znak)>64 and ord(znak)<91:
            ascii = ord(znak) + klucz
        if ascii > 90:
            ascii -= 26
        if ord(znak)>96 and ord(znak)<123:
            ascii = ord(znak) + klucz
        szyfrogram += chr(ascii)
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
    klucz = klucz % 26
    for znak in szyfrogram:
        if ord(znak) > 64 and ord(znak) < 91:
            ascii = ord(znak) - klucz
            if ascii > 90:
                ascii -= 26
        if ord(znak) > 96 and ord(znak) < 123:
            ascii = ord(znak) - klucz
        tekst += chr(ascii)
    return tekst

def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    # szyfrogram = szyfruj(tekst, klucz)
    # print(szyfrogram)
    print(deszyfruj(tekst, klucz))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
