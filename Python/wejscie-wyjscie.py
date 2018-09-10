#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    masa = float(input("Podaj swoją masę: "))
    print(masa)
    wzrost = float(input(" Podaj swój wzrost w metrach: "))
    print(wzrost)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
