#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as 
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import math


def is_abundant(i):
    divisors_sum = 0
    for j in xrange(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            divisors_sum += j
            other = i / j
            if other != j and other != i:
                divisors_sum += other

    return divisors_sum > i


non_abundant_summed = set(range(1, 28124))

abundant_nums = []

for i in xrange(1, 28124):
    if is_abundant(i):
        if 2 * i in non_abundant_summed: non_abundant_summed.remove(2 * i)
        for abundant_num in abundant_nums:
            if abundant_num + i in non_abundant_summed: non_abundant_summed.remove(abundant_num + i)
        abundant_nums.append(i)

print sum(non_abundant_summed)
