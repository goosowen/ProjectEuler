#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from itertools import permutations
DIGITS = ''.join(str(d) for d in range(10))

DIVISOR_LIST = [2,3,5,7,11,13,17]
def follows_property(num_str):
	for start_d in xrange(1,8):
		num_sub = int(num_str[start_d:start_d+3])
		if num_sub % DIVISOR_LIST[start_d-1] != 0:
			return False

	return True


#TESTING
# print is_pandigital("1234567890")
# print is_pandigital("1234567899")
# print follows_property("1406357289")

if __name__ == "__main__":
	pandigitals = [''.join(p) for p in permutations(DIGITS)]
	total = 0
	for num_str in pandigitals:
		if follows_property(num_str):
			total += int(num_str)

	print total


