#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''
import math

from common import timeit


def digit_factorial_sum(num):
    factorial_sum = 0
    for digit in str(num):
        factorial_sum += math.factorial(int(digit))
    return factorial_sum


limit = 9
while digit_factorial_sum(limit) > limit:
    limit = int(str(limit) + '9')

limit += 1
print "limit: ", limit


# 60.35 s
@timeit
def curious_numbers_basic(limit):
    curious_numbers = []
    for num in xrange(10, limit):
        factorial_sum = 0
        for digit in str(num):
            factorial_sum += math.factorial(int(digit))
        if factorial_sum == num:
            curious_numbers.append(num)
    print 'curious numbers:', curious_numbers
    print 'curious numbers sum:', sum(curious_numbers)


# 46.61 s
@timeit
def curious_numbers_memoize_factorials(limit):
    curious_numbers = []
    factorial_memory = {}
    for digit in xrange(10):
        factorial_memory[digit] = math.factorial(digit)

    for num in xrange(10, limit):
        factorial_sum = 0
        for digit in str(num):
            factorial_sum += factorial_memory[int(digit)]
        if factorial_sum == num:
            curious_numbers.append(num)

    factorial_memory = {}
    for digit in xrange(10):
        factorial_memory[digit] = math.factorial(digit)
    print 'curious numbers:', curious_numbers
    print 'curious numbers sum:', sum(curious_numbers)


# 11.36 s
@timeit
def curious_numbers_memoize_factorials_and_combos(limit):
    curious_numbers = []
    factorial_memory = {}
    for digit in xrange(10):
        factorial_memory[digit] = math.factorial(digit)

    digit_memory = {}

    for num in xrange(10, limit):
        digit_set = frozenset(str(num))

        factorial_sum = digit_memory.get(digit_set)
        if factorial_sum == None:
            factorial_sum = 0
            for digit in digit_set:
                factorial_sum += factorial_memory[int(digit)]
            digit_memory[digit_set] = factorial_sum

        if factorial_sum == num:
            curious_numbers.append(num)
    print 'curious numbers:', curious_numbers
    print 'curious numbers sum:', sum(curious_numbers)


curious_numbers_basic(limit)
curious_numbers_memoize_factorials(limit)
curious_numbers_memoize_factorials_and_combos(limit)
