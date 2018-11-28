#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py
import os
from peewee import *


baza_plik = 'uczniowie.db' 
baza = SqliteDatabase(baza_plik)   # instancja wykorzystywanej bazy

################################## MODELE ####      192.168.3.10:8000      ##############################
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    klasa = CharField(null=False)
    rok_naboru = IntegerField(default=0)
    rok_matury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()           # tekstowe pole, textfield - długie pole
    id_klasa = IntegerField(default=0)
    egz_hum = FloatField(default=0)
    egz_mat = FloatField(default=0)
    egz_jez = FloatField(default=0)

    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

class Przedmiot(BazaModel):
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()

class Ocena(BazaModel):
    datad = DateField(null=False)
    id_uczen = IntegerField(default=0)
    id_przedmiot = IntegerField(default=0)
    ocena = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name= 'wyniki')
    przedmiot = ForeignKeyField(Przedmiot, related_name = 'ocena')

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()          # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])     # tworzenie tabel

    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
