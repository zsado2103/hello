#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_wstaw(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        # for (int i=0; i < n; i++ )
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] < el:  # wyszukiwanie pozycji >ros <mal
            lista[k + 1] = lista[k]  # przesuwanie elementów
            k -= 1
        lista[k + 1] = el  # wstawianie elementów
    return lista


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9, -6]
    lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(lista)
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [0, 3, 4, 7, 2, 3, 1, 9]
    print(sort_wstaw(lista))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
