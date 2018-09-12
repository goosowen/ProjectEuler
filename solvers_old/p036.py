#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
from common import is_palindrome

LIMIT = 1000000

summation = 0
for num in xrange(LIMIT):
    if is_palindrome(str(num)) and is_palindrome(bin(num)[2:]):
        summation += num

print summation
