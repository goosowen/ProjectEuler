#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 270
=======================

A square piece of paper with integer dimensions N×N is placed with a
corner at the origin and two of its sides along the x- and y-axes. Then,
we cut it up respecting the following rules:

 • We only make straight cuts between two points lying on different sides
   of the square, and having integer coordinates.
 • Two cuts cannot cross, but several cuts can meet at the same border
   point.
 • Proceed until no more legal cuts can be made.

Counting any reflections or rotations as distinct, we call C(N) the number
of ways to cut an N×N square. For example, C(1) = 2 and C(2) = 30 (shown
below).

[Image: 270_CutSquare.gif]

What is C(30) mod 10^8?

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
