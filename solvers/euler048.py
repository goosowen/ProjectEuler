#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 48
=======================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

DIGITS_THAT_MATTER = 10
SERIES_CAP = 1000


def main():
    total = 0
    for i in range(1, SERIES_CAP + 1):
        total += i ** i
        total_str = str(total)
        if len(total_str) > DIGITS_THAT_MATTER:
            total_str = total_str[len(total_str) - DIGITS_THAT_MATTER:]
        total = int(total_str)

    return total


if __name__ == "__main__":
    print(main())
