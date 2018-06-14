#!/usr/bin/env python3
# Sieve of Eratosthenes
from math import sqrt
from sys import argv

def prime_sieve(n):
    sieve = [True] * n
    sieve[0:2] = [False, False]

    for i in range(2, int(sqrt(n)) + 1):
        pointer = i * 2
        while pointer < n:
            sieve[pointer] = False
            pointer += i

    return [i for i in range(len(sieve)) if sieve[i]]

primes = prime_sieve(int(argv[1]))
print('{} primes found through {}: {}'.format(len(primes), argv[1], primes))
