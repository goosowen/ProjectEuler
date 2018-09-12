#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?

"""

from common.euler_functions import is_prime_mem


def main():
    primes = []
    for possible_prime in range(2, 1000000):
        if is_prime_mem(possible_prime, primes):
            primes.append(possible_prime)
            if len(primes) == 10001:
                return possible_prime

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
