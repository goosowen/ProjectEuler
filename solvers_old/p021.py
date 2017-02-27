#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math

# maps numbers to the sum of their proper divisors
mem = {}

# sum of all amicable numbers under 10000
total = 0

for i in xrange(1,10000):
	# sum of all proper divisors of i
	divisors_sum = 0

	for j in xrange(1,int(math.sqrt(i))):
		if i%j == 0:
			divisors_sum += j
			other = i/j
			if other != j and other != i:
				divisors_sum += other

	# check if amicable
	if mem.get(divisors_sum):
		if mem.get(divisors_sum) == i:
			print i, divisors_sum
			total += i
			total += divisors_sum

	mem[i] = divisors_sum

print total


