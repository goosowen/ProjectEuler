#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 47
=======================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""


# TODO use LogDebug
# TODO optimize, takes ~90 seconds
def main():
    from common.euler_functions import get_prime_factors

    consecutive = []
    consecutive_debug = []
    mem = {}
    for i in range(2, 1000000):
        if len(consecutive) == 4:
            #     print(consecutive)
            #     print(consecutive_debug)
            return consecutive[0]

        # if len(consecutive) >= 3:
        #     print(consecutive)
        #     print(consecutive_debug)

        # if i % 10000 == 0:
        #     print("Processing at", i, "...")

        mem[i] = get_prime_factors(i, mem)
        if len(mem[i]) == 4:
            consecutive.append(i)
            consecutive_debug.append(mem[i])
        else:
            consecutive = []
            consecutive_debug = []


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
