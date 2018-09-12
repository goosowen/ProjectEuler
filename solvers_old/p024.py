#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math

# The first factorial above 1,000,000 is 10. 10! = 3,628,800. Working backwards, that means there
# are 362,880 orderings with 0 in front. Then another 362,880 with 1 in front. 2 is front. Work from this.

final_number = ""
non_fixed_nums = range(10)
total = 999999

factorials = [math.factorial(x) for x in range(1, 11)]
print factorials

while total > 0:
    for pos in xrange(10, 0, -1):
        for i in xrange(pos, 0, -1):
            fact = factorials[i - 1]
            if fact <= total:
                final_number += str(non_fixed_nums.pop(total / fact))
                print total, i, fact, final_number[-1], total / fact
                total = total % fact

                break

for remainder_num in non_fixed_nums:
    final_number += str(remainder_num)

print final_number
2783915604
