#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from common import is_prime_mem


def main():
    primes = []
    for possible_prime in xrange(2, 1000000):
        if is_prime_mem(possible_prime, primes):
            primes.append(possible_prime)
            if len(primes) == 10001:
                return possible_prime

    print(len(primes))
    return "Unknown"


if __name__ == "__main__":
    print(main())
