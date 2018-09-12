#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from operator import mul
from common import is_prime


def main():
    other_divisors = []
    prime_divisors = []
    for divisor in range(2, 21, 1):
        if is_prime(divisor):
            prime_divisors.append(divisor)
        else:
            other_divisors.append(divisor)

    primes_product = reduce(mul, prime_divisors, 1)

    for i in range(1, 1000):
        n = primes_product * i
        passes = True
        for d in other_divisors:
            if n % d != 0:
                passes = False
                break

        if passes:
            return n

    return "Unknown"


if __name__ == "__main__":
    print(main())
