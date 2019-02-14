#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 192
=======================

Let x be a real number.
A best approximation to x for the denominator bound d is a rational number
r/s in reduced form, with s d, such that any rational number which is
closer to x than r/s has a denominator larger than d:

                         |p/q-x| < |r/s-x| q > d

For example, the best approximation to 13 for the denominator bound 20 is
18/5 and the best approximation to 13 for the denominator bound 30 is
101/28.

Find the sum of all denominators of the best approximations to n for the
denominator bound 10^12, where n is not a perfect square and 1 < n 100000.

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
