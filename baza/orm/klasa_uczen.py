#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py
import os
from peewee import *


baza_plik = 'test_orm.db' 
baza = SqliteDatabase(baza_plik)   # instancja wykorzystywanej bazy

################################## MODELE ####      192.168.3.10:8000      ##############################
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)           # tekstowe pole, textfield - długie pole
    roknaboru = IntegerField(default=0)     # typ liczby przechowywanej
    rokmatury = IntegerField(default=0)


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie') #atrybut przyjmuje wartość z obiektu klasy(numer klasy)


class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki') #identyfikator ucznia


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()          # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])     # tworzenie tabel
    
    kl3A = Klasa() #instancja obiektu
    kl3A.nazwa = '3A'
    kl3A.roknaboru = 2010
    kl3A.rokmatury = 2013
    kl3A.save() # zapisanie instancji obiektu
    kl2A = Klasa(nazwa='2A', roknaboru='2009', rokmatury='2012')
    kl2A.save()
    ucz1 = Uczen(imie='Adam', 
                 nazwisko='Słodowy', 
                 plec=False, 
                 klasa=kl3A)
    ucz1.save()
    
    ucz2 = Uczen(imie='Ewa', 
                 nazwisko='Kolorowa', 
                 plec=True, 
                 klasa=kl2A)
    ucz2.save()
    

    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
