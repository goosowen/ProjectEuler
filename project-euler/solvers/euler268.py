#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 268
=======================

It can be verified that there are 23 positive integers less than 1000 that
are divisible by at least four distinct primes less than 100.

Find how many positive integers less than 10^16 are divisible by at least
four distinct primes less than 100.

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
