#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 47
=======================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from ..common import get_prime_factors


def main():
    consecutive = []
    consecutive_debug = []
    mem = {}
    for i in range(2, 1000000):
        if len(consecutive) == 4:
            print(consecutive)
            print(consecutive_debug)
            break

        if len(consecutive) >= 3:
            print(consecutive)
            print(consecutive_debug)

        if i % 10000 == 0:
            print("Processing at", i, "...")

        mem[i] = get_prime_factors(i, mem)
        if len(mem[i]) == 4:
            consecutive.append(i)
            consecutive_debug.append(mem[i])
        else:
            consecutive = []
            consecutive_debug = []

    return (consecutive[0])


if __name__ == "__main__":
    print(main())
