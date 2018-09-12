'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math


# lower bound should be sqrt of num but for some reason that doesn't work
def is_prime(num, primes):
    low_bound = math.sqrt(num)
    for p in primes:
        if num % p == 0:
            return False
        if p > low_bound:
            return True

    return True


def find_prime():
    primes = [2, 3, 5, 7, 11, 13]
    for possible_num in xrange(14, 10000000):
        if is_prime(possible_num, primes):
            if len(primes) == 10001:
                return possible_num

    return "hah"


print find_prime()
