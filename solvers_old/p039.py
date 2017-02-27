#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import math

def is_right_triangle(a,b,c):
	return a**2 + b**2 == c**2

max_p_sols = 0
max_p = 0
for p in xrange(1,1000):
	print p
	sols = set()
	for a in xrange(1,p/2):
		a_squared = a**2
		for b in xrange(a,p-a-1):
			c = p-a-b
			if a_squared + b**2 == c**2:
				sols.add(frozenset([a,b,c]))

	num_sols = len(sols)
	if num_sols > max_p_sols:
		max_p_sols = num_sols
		max_p = p

print max_p