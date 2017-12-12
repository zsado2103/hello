#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib_iter(n):
    """Funkcja wyświetla kolejne wyrazy ciągu Fibonacciego.
    Funkcja zwraca n-ty wyraz w ciągu.
    F(0) = 0
    F(1) = 1
    F(n) = F(n-2) + F(n-1) dla n > 1 """
    a, b = (0, 1)
    if n == 0:
        print (a)
        return a
    # elif n == 1:
    #    print (b)
    #    return b

    print(a)
    for i in range(2, n):
        # tmp = b
        # b = a + b
        # a = tmp
        a, b = b, a + b
        print(a, " Wyraz ", i, ": ", b, "Iloraz: ", b / a)

    return b


def fib_iter2(n):
    a, b = (0, 1)

    while n > 0:
        a, b = b, a + b
        print(a, " ", b, "Iloraz: ", b / a)
        n = n - 1


# F(1) = 1
# F(n) = F(n-2) + F(n-1) dla n > 1
def fib_rek(n):
    if n < 2:
        return 1
    return fib_rek((n - 1) + (n - 2))


def main(args):
	fib_iter(20)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
