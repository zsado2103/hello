#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import floor


def wyszukaj_liniowo(l, el):
    for i in range(0, len(l)):
        if l[i] == el:
            return i
    return -1
#  int wyszukaj_liniowo(int l[], int n, int el){
#      for(int i = 0; i < n; i++){
#      if (l[i] == el)
#          return i;
#        }
#     return -1;
#     }


def wyszukaj_bin_it(lista, el):
    lewy, prawy = 0, len(lista) - 1
    while lewy < prawy:
        srodek = floor((lewy + prawy) / 2)
        # print(srodek)
        if el <= lista[srodek]:
            prawy = srodek
        else:
            lewy = srodek + 1
    if lista[lewy] == el:
        return lewy

    return -1


def wyszukaj_bin_rek(lewy, prawy, lista, el):
    if lewy > prawy:
        return -1  # elementu nie znaleziono

    srodek = floor((lewy + prawy) / 2)
    if el <= lista[srodek]:
        return srodek  # element znaleziono
    if el < lista[srodek]:
        return wyszukaj_bin_rek(lewy, srodek - 1, lista, el)
    else:
        return wyszukaj_bin_rek(srodek + 1, prawy, lista, el)


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9, -4]
    lista.sort()
    print(lista)
    el = 1
    # print(wyszukaj_liniowo(lista, el))
    # assert wyszukaj_liniowo(lista, 8) == -1
    print(wyszukaj_bin_it(lista, el))
    print(wyszukaj_bin_rek(0, len(lista) - 1, lista, el))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
