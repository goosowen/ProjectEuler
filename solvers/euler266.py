#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 266
=======================

The divisors of 12 are: 1, 2, 3, 4, 6, and 12.
The largest divisor of 12 that does not exceed the square root of 12 is 3.
We shall call the largest divisor of an integer n that does not exceed the
square root of n the pseudo square root (PSR) of n.
It can be seen that PSR(3102) = 47.

Let p be the product of the primes below 190. Find PSR(p) mod 10^16.

"""


def main():
    return "unimplemented"


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
