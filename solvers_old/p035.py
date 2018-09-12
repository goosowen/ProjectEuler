#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
from common import is_prime

LIMIT = 1000000

circular_primes = []
for num in xrange(2, LIMIT):
    num_rotations = 0
    num_str = str(num)
    circular_prime = True
    while num_rotations < len(num_str):
        if not is_prime(int(num_str)):
            circular_prime = False
            break
        else:
            num_rotations += 1
            num_str = num_str[1:] + num_str[:1]

    if circular_prime:
        circular_primes.append(num)

print circular_primes
print len(circular_primes)
