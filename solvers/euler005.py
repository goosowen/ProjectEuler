#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?

"""

from operator import mul
from functools import reduce
from common.euler_functions import is_prime


def main():
    other_divisors = []
    prime_divisors = []
    for divisor in range(2, 21, 1):
        if is_prime(divisor):
            prime_divisors.append(divisor)
        else:
            other_divisors.append(divisor)

    primes_product = reduce(mul, prime_divisors, 1)

    for i in range(1, 1000):
        n = primes_product * i
        passes = True
        for d in other_divisors:
            if n % d != 0:
                passes = False
                break

        if passes:
            return n

    return "Unknown"


if __name__ == "__main__":
    import ntpath
    import time
    from common.shared_functions import verify_solution

    problem_number = int(ntpath.basename(__file__).replace("euler", "").replace(".py", ""))
    print("Retrieving my answer to Euler Problem {0} ...".format(problem_number))

    ts = time.time()
    my_answer = main()
    te = time.time()

    print("My answer: {1}".format(problem_number, my_answer))

    verification_type = verify_solution(problem_number, my_answer)
    print("Verification: {0}".format(verification_type.name))
    print("Took {0} seconds.".format(te - ts))
