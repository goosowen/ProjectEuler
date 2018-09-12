#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math


# lower bound should be sqrt of num but for some reason that doesn't work
def is_prime(num, primes):
    low_bound = math.sqrt(num)
    for p in primes:
        if p > low_bound:
            return True
        if num % p == 0:
            return False

    return True


def sum_primes(limit):
    primes = [2, 3, 5, 7]
    total = 2 + 3 + 5 + 7
    for possible_num in xrange(8, limit):
        if is_prime(possible_num, primes):
            primes.append(possible_num)
            total += possible_num

    return total


print sum_primes(2000000)

# wrong:
# 457143142877
