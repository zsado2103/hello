#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    m = float(input("Podaj swoją masę: "))
    print(m)
    w = float(input("Podaj swój wzrost w metrach: "))
    print(w)

    b = m / (w * w)
    print ("Twoje BMI wynosi: ", b)

    if b < 18.5:
        print ("niedowaga")
    elif b >= 24.9:
        print("norma")
    elif b >= 25:
        print("nadwaga")
    elif b >= 30:
        print("otyłość")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
