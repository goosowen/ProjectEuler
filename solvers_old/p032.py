#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
products = set()

for two_digit_num in xrange(1,100):
	two_str = str(two_digit_num)
	if "0" in two_str:
		continue
	for three_digit_num in xrange(100,10000):
		three_str = str(three_digit_num)
		if "0" in three_str:
			continue
		product = two_digit_num * three_digit_num
		product_str = str(product)
		if "0" in product_str:
			continue

		if len(product_str) + len(three_str) + len(two_str) != 9:
			continue

		digits = set()
		for c in two_str:
			digits.add(c)

		for c in three_str:
			digits.add(c)

		for c in product_str:
			digits.add(c)

		if len(digits) == 9:
			products.add(product)



# 45228
print sum(products)