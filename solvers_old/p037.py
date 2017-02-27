#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from common import is_prime


mem_primes = {'1':False}
LIMIT = 1000000

truncatable_primes = []
num = 10
while len(truncatable_primes) <= 11 and num < LIMIT:
	trunctable = True
	num_str_left = str(num)
	while len(num_str_left) > 0:
		if num == 3797:
			print num_str_left
		prime_mem = mem_primes.get(num_str_left)
		if prime_mem == None:
			if not is_prime(int(num_str_left)):
				trunctable = False
				mem_primes[num_str_left] = False
				break
			else:
				mem_primes[num_str_left] = True
				num_str_left = num_str_left[1:]
		elif prime_mem == True:
			num_str_left = num_str_left[1:]
		else:
			trunctable = False
			break

	if trunctable:
		num_str_right = str(num)[:-1]
		while len(num_str_right) > 0:
			if num == 3797:
				print num_str_right
			prime_mem = mem_primes.get(num_str_right)
			if prime_mem == None:
				if not is_prime(int(num_str_right)):
					trunctable = False
					mem_primes[num_str_right] = False
					break
				else:
					mem_primes[num_str_right] = True
					num_str_right = num_str_right[:-1]
			elif prime_mem:
				num_str_right = num_str_right[:-1]
			else:
				trunctable = False
				break

	if trunctable:
		truncatable_primes.append(num)

	num += 1

# print mem_primes
# print is_prime(9)
print truncatable_primes
print sum(truncatable_primes)