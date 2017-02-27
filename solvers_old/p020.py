#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

fact = 1
for i in xrange(1,101):
	fact *= i

tot = 0
for c in str(fact):
	tot += int(c)

print tot