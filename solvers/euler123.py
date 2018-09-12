#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 123
=======================

Let p[n] be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder
when (p[n]1)^n + (p[n]+1)^n is divided by p[n]^2.

For example, when n = 3, p[3] = 5, and 4^3 + 6^3 = 280 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.

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
