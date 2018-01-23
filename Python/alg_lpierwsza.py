#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor


def main(args):
	n = int(input("Podaj dowolną liczbę: "))
	i = 2
	while n % i != 0:
		if i * i <= n:
			print("Podano liczbę pierwszą. ")
		i = i + 1
	print("Podano liczbę złożoną. ")
	return 0
    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
