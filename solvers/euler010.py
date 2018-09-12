#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 10
=======================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from common.euler_functions import is_prime_mem


def main():
    total = 0
    limit = 2 * 10 ** 6
    primes = []
    for possible_num in range(2, limit):
        if is_prime_mem(possible_num, primes):
            primes.append(possible_num)
            total += possible_num

    return total


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
