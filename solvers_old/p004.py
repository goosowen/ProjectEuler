#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
from common import is_palindrome

three_digit_nums = range(999, 100, -1)

def highest_palindrome():
	for possible_palindrome in xrange(999*999, 100*100, -1):
		if is_palindrome(str(possible_palindrome)):
			for i in three_digit_nums:
				if possible_palindrome % i == 0:
					if possible_palindrome / i < 1000 and possible_palindrome / i > 99:
						print i
						print possible_palindrome / i
						return possible_palindrome


print highest_palindrome()