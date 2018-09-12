#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 108
=======================

In the following equation x, y, and n are positive integers.

                                1 + 1 = 1
                                x   y   n

For n = 4 there are exactly three distinct solutions:

                                1 + 1  = 1
                                5   20   4
                                1 + 1  = 1
                                6   12   4
                                1 + 1  = 1
                                8   8    4

What is the least value of n for which the number of distinct solutions
exceeds one-thousand?

NOTE: This problem is an easier version of problem 110; it is strongly
advised that you solve this one first.

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
