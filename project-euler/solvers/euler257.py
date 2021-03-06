#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 257
=======================

Given is an integer sided triangle ABC with sides a ≤ b ≤ c. (AB = c, BC =
a and AC = b).
The angular bisectors of the triangle intersect the sides at points E, F
and G (see picture below).

[Image: 257_bisector.gif]

The segments EF, EG and FG partition the triangle ABC into four smaller
triangles: AEG, BFE, CGF and EFG.
It can be proven that for each of these four triangles the ratio
area(ABC)/area(subtriangle) is rational.
However, there exist triangles for which some or all of these ratios are
integral.

How many triangles ABC with perimeter ≤ 100,000,000 exist so that the ratio
area(ABC)/area(AEG) is integral?

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
