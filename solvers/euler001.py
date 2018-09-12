#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_sum_multiples(x, threshold):
    num_multiples_of_x = (threshold - 1) / x
    sum_multiples_of_x = x * (num_multiples_of_x + 1) * num_multiples_of_x / 2
    return sum_multiples_of_x


def main():
    threshold = 1000
    return get_sum_multiples(3, threshold) + get_sum_multiples(5, threshold) - get_sum_multiples(15, threshold)


if __name__ == "__main__":
    print(main())
