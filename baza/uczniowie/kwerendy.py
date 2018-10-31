#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py

import sqlite3

def kwerenda1(cur):
    cur.execute("""
                SELECT klasa, przedmiot, AVG(ocena) AS srednia FROM oceny
                INNER JOIN przedmioty ON oceny.id_przedmiot=przedmioty.id
                INNER JOIN uczniowie ON uczniowie.id=oceny.id_uczen
                INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
                WHERE przedmiot = 'matematyka'
                GROUP BY klasa
                ORDER BY srednia DESC
                
                """)
                
                
                # Średnie ocen z matematyki poszczególnych klas / Najwyższa ocena z matematyki
                # SELECT klasa, przedmiot, AVG(ocena) AS srednia FROM oceny
                # INNER JOIN przedmioty ON oceny.id_przedmiot=przedmioty.id
                # INNER JOIN uczniowie ON uczniowie.id=oceny.id_uczen
                # INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
                # WHERE przedmiot = 'matematyka'
                # GROUP BY klasa
                # ORDER BY srednia DESC
                

                
                # ------- Średnie ocen z poszczególnych przedmiotów
                #  SELECT przedmiot, AVG(ocena) FROM oceny
                #  INNER JOIN przedmioty ON oceny.id_przedmiot=przedmioty.id
                #  GROUP BY przedmiot
                #  ORDER BY srednia DESC

               # ------- Średnie ocen poszczególnych klas
               # SELECT klasa, AVG(ocena) AS srednia FROM oceny
               # INNER JOIN uczniowie ON uczniowie.id=oceny.id_uczen
               # INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
               # GROUP BY klasy.id
               # ORDER BY srednia DESC


        #     WITH srednie AS (
        #     SELECT nazwisko, imie, AVG(ocena) AS srednia FROM uczniowie
        #     INNER JOIN oceny ON uczniowie.id=oceny.id_uczen
        #     GROUP BY uczniowie.id
        #      ) SELECT COUNT (srednia) FROM srednie
        #     WHERE srednia > 3.8
        
        
        #  SELECT klasa, COUNT(uczniowie.id) AS ilosc  FROM uczniowie
        #  INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
        #  GROUP BY klasa
        #  ORDER BY ilosc DESC
        
        #  SELECT nazwisko, imie, klasa FROM uczniowie
        #  INNER JOIN klasy ON uczniowie.id_klasa=klasy.id
        #  SELECT plec,  AVG(egz_mat), AVG(egz_hum), AVG(egz_jez) FROM uczniowie
        #  GROUP BY plec                
        #  SELECT AVG(egz_mat) FROM uczniowie - ŚREDNIA
        #  ORDER BY - uporządkuj według itp
        #  ASC - rosnąco, DESC- malejąco
        #  WHERE egz_mat > 40 AND egz_hum > 40
        
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
