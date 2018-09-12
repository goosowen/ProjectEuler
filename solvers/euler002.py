#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""


def main():
    mem = {}
    mem[0] = 1
    mem[1] = 2

    limit = 4 * 10 ** 6
    total = 0
    i = 1
    current = 2
    while current < limit:

        if current % 2 == 0:
            total += current

        i += 1
        current = mem[i - 1] + mem[i - 2]
        mem[i] = current

    return total


if __name__ == "__main__":
    print(main())
