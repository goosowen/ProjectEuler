#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 292
=======================

We shall define a Pythagorean polygon to be a convex polygon with the
following properties:

 • there are at least three vertices,
 • no three vertices are aligned,
 • each vertex has integer coordinates,
 • each edge has integer length.

For a given integer n, define P(n) as the number of distinct Pythagorean
polygons for which the perimeter is ≤ n.
Pythagorean polygons should be considered distinct as long as none is a
translation of another.

You are given that P(4) = 1, P(30) = 3655 and P(60) = 891045.
Find P(120).

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
