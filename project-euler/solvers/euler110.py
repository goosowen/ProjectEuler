#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 110
=======================

In the following equation x, y, and n are positive integers.

                                1 + 1 = 1
                                x   y   n

It can be verified that when n = 1260 there are 113 distinct solutions and
this is the least value of n for which the total number of distinct
solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions
exceeds four million?

NOTE: This problem is a much more difficult version of problem 108 and
as it is well beyond the limitations of a brute force approach it requires
a clever implementation.

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
