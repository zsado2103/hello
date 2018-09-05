#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    osoba = input(' Jak masz na imię?\n ')
    
    print("Witaj!", osoba, "!")
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
