#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

#for i in xrange(0,51,10):
x = 2**1000
tot = 0
for c in str(x):
	tot += int(c)
print tot