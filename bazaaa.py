#!/usr/bin/env python
# -*- coding: utf-8 -*-



from peewee import *

baza_nazwa = 'quiz.db'
baza = SqliteDatabase(baza_nazwa)  # instancja bazy

### MODELE #
class KlasaBaza(Model):
    class Meta:
        database = baza

class Kategoria(KlasaBaza):
    kategoria = CharField(null=False)


class Pytanie(KlasaBaza):
    pytanie = CharField(null=False)
    id_kat = ForeignKeyField(Kategoria, related_name="id")
   


class Odpowiedz(KlasaBaza):
    
    id_kat = ForeignKeyField(Pytanie, related_name="id")
    odpowiedz = CharField(null=False)
    odpok = BooleanField(Default=0)
    

def main(args):
    
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Kategoria, Pytanie,Odpowiedz])   #mapowanie ORM (odwzorować)
    
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
