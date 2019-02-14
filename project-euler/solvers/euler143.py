#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 143
=======================

Let ABC be a triangle with all interior angles being less than 120
degrees. Let X be any point inside the triangle and let XA = p, XB = q,
and XC = r.

Fermat challenged Torricelli to find the position of X such that p + q + r
was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and
AMC are constructed on each side of triangle ABC, the circumscribed
circles of AOB, BNC, and AMC will intersect at a single point, T, inside
the triangle. Moreover he proved that T, called the Torricelli/Fermat
point, minimises p + q + r. Even more remarkable, it can be shown that
when the sum is minimised, AN = BM = CO = p + q + r and that AN, BM and CO
also intersect at T.

If the sum is minimised and a, b, c, p, q and r are all positive integers
we shall call triangle ABC a Torricelli triangle. For example, a = 399, b
= 455, c = 511 is an example of a Torricelli triangle, with p + q + r =
784.

Find the sum of all distinct values of p + q + r 110000 for Torricelli
triangles.

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
