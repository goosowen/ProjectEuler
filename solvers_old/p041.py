#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import common

# 
def is_pandigital(i):
	if len(i) > 9 or '0' in i:
		return False

	for j in xrange(1,len(i)+1):
		if str(j) not in i:
			return False

	return True

for i in xrange(10**9, 1, -1):
	if is_pandigital(str(i)) and common.is_prime(i):
		print i
		break