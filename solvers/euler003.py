#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from common import get_prime_factors


def main():
    factors = get_prime_factors(600851475143)
    return max(factors.keys())


if __name__ == "__main__":
    print(main())
