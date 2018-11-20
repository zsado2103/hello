#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  onp_klasa.py

from stos_obj import Stos


class ONPKlasa(Stos):
    
    def __init__(self, onp_str=''):  # przesĹonienie konstruktora rodzica
        super().__init__(10)  # wywoĹanie konstruktora rodzica
        if not self.czy_poprawne(onp_str):
            print("BĹÄd wyraĹźenia!")
            onp_str = ''
        self.onp_str = onp_str
        self.log = []
        self.wynik = None
        
    def czy_poprawne(self, onp):
        for z in onp:
            if z.isalpha():
                return False
        return True

    def oblicz_onp(self):
        onp = self.onp_str.split(" ")
    
        for el in onp:
           if el.isdigit():
               self.push(el)
           else:
               a = self.pop()
               b = self.pop()
               self.log.append(str(b) + el + str(a))
               self.push(eval(str(b) + el + str(a)))
        
        self.wynik = self.pop()


def main(args):
    onp = input("Podaj wyr. ONP, oddzielajÄc operandy i operatory spacjami:\n")
    o1 = ONPKlasa(onp)
    o1.oblicz_onp()
    print("Obliczenia: ", o1.log)
    print("Wynik: ", o1.wynik)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
