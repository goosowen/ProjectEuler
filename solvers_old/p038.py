#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def creates_pandigital(n, i):
    digits = ''
    for nn in range(1, n):
        if len(digits) > 9:
            return False

        product = nn * i
        for c in str(product):
            if c in digits or c == '0':
                return False
            digits += c

    if len(digits) != 9:
        return False

    return int(digits)


def find_largest_pandigital_from_range_set_and_other_integer():
    max_pandigital = 0
    max_n = 0
    max_i = 0

    for n in xrange(2, 9):
        range_n = range(1, n)
        for i in xrange(1, 10 ** (9 / n + 1)):
            pan = creates_pandigital(n, i)
            if pan != False:
                if pan > max_pandigital:
                    max_pandigital = pan
                    max_n = n
                    max_i = i

    print range(1, max_n)
    print max_i
    return max_pandigital


print find_largest_pandigital_from_range_set_and_other_integer()
