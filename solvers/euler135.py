#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 135
=======================

Given the positive integers, x, y, and z, are consecutive terms of an
arithmetic progression, the least value of the positive integer, n, for
which the equation, x^2 y^2 z^2 = n, has exactly two solutions is n = 27:

                    34^2 27^2 20^2 = 12^2 9^2 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten
solutions.

How many values of n less than one million have exactly ten distinct
solutions?

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
