#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 10
=======================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from common import is_prime_mem


def main():
    total = 0
    limit = 2 * 10 ** 6
    primes = []
    for possible_num in range(2, limit):
        if is_prime_mem(possible_num, primes):
            primes.append(possible_num)
            total += possible_num

    return total


if __name__ == "__main__":
    print(main())
