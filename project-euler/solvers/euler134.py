#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 134
=======================

Consider the consecutive primes p[1] = 19 and p[2] = 23. It can be
verified that 1219 is the smallest number such that the last digits are
formed by p[1] whilst also being divisible by p[2].

In fact, with the exception of p[1] = 3 and p[2] = 5, for every pair of
consecutive primes, p[2] > p[1], there exist values of n for which the
last digits are formed by p[1] and n is divisible by p[2]. Let S be the
smallest of these values of n.

Find S for every pair of consecutive primes with 5 p[1] 1000000.

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
