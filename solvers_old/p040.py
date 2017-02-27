#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

frac_str = ''
for i in xrange(1,1000000):
	frac_str += str(i)

product = 1
for e in xrange(7):
	print 10**e - 1
	print frac_str[10**e - 1]
	product *= int(frac_str[10**e - 1])

print product