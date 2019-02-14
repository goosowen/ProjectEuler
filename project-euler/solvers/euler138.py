#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 138
=======================

Consider the isosceles triangle with base length, b = 16, and legs, L =
17.

By using the Pythagorean theorem it can be seen that the height of the
triangle, h = (17^2 8^2) = 15, which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base
length, and this is the second smallest isosceles triangle with the
property that h = b 1.

Find L for the twelve smallest isosceles triangles for which h = b 1 and
b, L are positive integers.

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
