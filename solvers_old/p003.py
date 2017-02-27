'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

NUMBER = 600851475143

def get_prime_factors(n, prime_factor_list):
	is_prime = True
	for i in xrange(2, n/2):
		if n % i == 0:
			print i, n
			get_prime_factors(n/i, prime_factor_list)
			get_prime_factors(i, prime_factor_list)
			is_prime = False
			break

	if is_prime and n != NUMBER:
		prime_factor_list.append(n)

	return prime_factor_list

prime_factors =  get_prime_factors(NUMBER, [])
if prime_factors:
	print max(prime_factors)
else:
	print None