#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sumuj(a, b):
    wynik = a + b
    return wynik


def odejmij(a, b):
    wynik = a - b
    return wynik


def iloczyn(a, b):
    wynik = a * b
    return wynik


def iloraz(a, b):
    wynik = a / b
    return wynik


def main(args):
    a = int(input("Podaj 1. liczbę"))
    print(a)
    b = int(input("Podaj 2. liczbę"))
    print(b)

    print("suma: ", sumuj(a, b))
    print("różnica: ", odejmij(a, b))
    print("iloczyn: ", iloczyn(a, b))
    print("iloraz: ", iloraz(a, b))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
