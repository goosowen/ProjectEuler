#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 80
=======================

It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square roots
is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum
of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square
roots.

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
