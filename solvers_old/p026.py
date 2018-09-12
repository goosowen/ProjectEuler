#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
import math

longest_cycle = 6
best_num = 7
for i in xrange(11, 1000):

    # only look for prime numbers. Other numbers will have cycles equivalent to their prime factor with the shortest cycle
    prime = True
    for j in xrange(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            break

    if prime:
        cycle_length = 0
        remainders_hit = set()

        if i < 100:
            remainder = 100 % i
            while remainder not in remainders_hit:
                cycle_length += 1
                remainders_hit.add(remainder)

                while remainder < i:
                    remainder *= 10
                remainder = remainder % i
        else:  # 100 <= i < 1000
            remainder = 1000 % i
            while remainder not in remainders_hit:
                cycle_length += 1
                remainders_hit.add(remainder)

                while remainder < i:
                    remainder *= 10
                remainder = remainder % i

    if cycle_length > longest_cycle:
        longest_cycle = cycle_length
        best_num = i

print best_num, longest_cycle, 1.0 / best_num
