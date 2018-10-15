#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza.py
import csv
import sqlite3

def czytaj_dane(plik, separator=","):
    dane = []
    with open(plik, 'r', newline='',encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for rekord in tresc:
            dane.append(rekord)
    print(dane)
    return dane


def main(args):
    con = sqlite3.connect('bazagus.db')  # połączenie
    cur = con.cursor() # obiekt kursora
    
    with open('bazagus.sql', 'r') as plik:
        cur.executescript(plik.read())
    
    dane = czytaj_dane('miasta.csv')
    dane.pop(0) # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO miasta VALUES(?, ?, ?)', dane)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
