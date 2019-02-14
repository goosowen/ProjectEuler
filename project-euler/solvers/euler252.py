#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 252
=======================

Given a set of points on a plane, we define a convex hole to be a convex
polygon having as vertices any of the given points and not containing any
of the given points in its interior (in addition to the vertices, other
given points may lie on the perimeter of the polygon).

As an example, the image below shows a set of twenty points and a few such
convex holes. The convex hole shown as a red heptagon has an area equal to
1049694.5 square units, which is the highest possible area for a convex
hole on the given set of points.

[Image: 252_convexhole.gif]

For our example, we used the first 20 points (T[2k−1], T[2k]), for
k = 1,2,…,20, produced with the pseudo-random number generator:

                 S[0]   =    290797
                 S[n+1] =    S[n]^2 mod 50515093
                 T[n]   =    ( S[n] mod 2000 ) − 1000

i.e. (527, 144), (−488, 732), (−454, −947), …

What is the maximum area for a convex hole on the set containing the first
500 points in the pseudo-random sequence?
Specify your answer including one digit after the decimal point.

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
