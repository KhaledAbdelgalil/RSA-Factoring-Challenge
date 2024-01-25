#!/usr/bin/python3
from sys import argv
import math



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def pollards_rho3(n):
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

    if is_prime(d):
        return d
    else:
        return min(factor for factor in range(2, int(math.sqrt(n)) + 1) if n % factor == 0 and is_prime(factor))

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
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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
        d = gcd(abs(x - y), n)

    return d

def pollards_rho2(n):
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
    return min(d, n // d)
def smallest_prime_factor(n):
    if n < 2:
        return None  # No prime factors for numbers less than 2
    result = pollards_rho(n)
    return result if result != n else None
def factorize_faster(number):
    if number == 1:
        return None, None

    factor1 = smallest_prime_factor(number)
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
            factor1, factor2 = factorize_faster(number)
            print(f"{number}={factor1}*{factor2}")
            line = file.readline()
except:
    pass
