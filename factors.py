#!/usr/bin/python3
from sys import argv
import math

def primefactor(n):
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(5, int((n)**0.5) + 1, 6):
            if n % i == 0:
                return int(i)
            if n % (i + 2) == 0:
                return primefactor(n/(i+2))
    return int(n)
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)
    return d

def factorize_faster(number):
    if number == 1:
        return None, None

    factor1 = pollards_rho(number)
    factor2 = number // factor1

    return factor1, factor2

def factorize(number):
    i = 2;
    if number < 2:
        return None, None
    while number % i:
        i = i + 1
    return number // i, i

def factorize2(number):
    i = primefactor(number)
    return i, number // i
if len(argv) != 2:
        exit(1)

input_file = argv[1]

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            number = int(line.split('\n')[0])
            factor1, factor2 = factorize2(number)
            print(f"{number}={factor1}*{factor2}")
            line = file.readline()
except:
    pass
