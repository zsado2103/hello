#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py

import sqlite3

def kwerenda1(cur):
    cur.execute("""
        SELECT * FROM nazwiska INNER JOIN oceny ON nazwiska.nr_ucznia = oceny.nr_ucznia 
        """)
    
         #  SELECT * FROM nazwiska WHERE  nazwisko LIKE 'G%' # % Dowolna liczba np liter
         #  SELECT * FROM nazwiska WHERE  imie1  LIKE 'A__a' # określona liczba liter
         #  SELECT COUNT(*) FROM nazwiska WHERE  imie1  LIKE 'A__a' # zlicza ilość rekordów
         #  SELECT * FROM nazwiska INNER JOIN dane_osobowe ON nazwiska.nr_ucznia = dane_osobowe.nr_ucznia #
         #  SELECT COUNT(*) FROM nazwiska INNER JOIN dane_osobowe ON nazwiska.nr_ucznia = dane_osobowe.nr_ucznia WHERE miejsce_urodz <>'Gdańsku' # <>-nie
         #  SELECT * FROM nazwiska INNER JOIN dane_osobowe ON nazwiska.nr_ucznia = dane_osobowe.nr_ucznia WHERE miesiac ='7' OR miesiac ='8'

    for row in cur.fetchall():
        print(tuple(row))



def main(args):
    # Konfiguracja ################
    baza = 'uczniowie'
    tabele = ['nazwiska', 'dane_osobowe', 'oceny']
    roz = '.txt'
    naglowki = True  # czy pliki zawierają nagłówki?
    ###############################
    con = sqlite3.connect(baza + '.db')  # połączenie
    cur = con.cursor() # obiekt kursora
    
    kwerenda1(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
