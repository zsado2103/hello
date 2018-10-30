#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py
#  


def main(args):
    masa = float(input("Podaj swoją masę w kilogramach: "))
    print(masa)
    wzrost = float(input("Podaj swój wzrost w centymetrach: "))
    print(wzrost)

    bmi = masa / ((wzrost*0.01) **2)
    print ("Twoje BMI wynosi: ", bmi)

    if bmi < 18.5:
        print ("Niedowaga!")
    elif bmi <= 24.9:
        print("Norma!")
    elif bmi <= 30:
        print("Nadwaga!")
    elif bmi > 30:
        print("Otyłość")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
