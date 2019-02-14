#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 311
=======================

ABCD is a convex, integer sided quadrilateral with 1 ≤ AB < BC < CD < AD.
BD has integer length. O is the midpoint of BD. AO has integer length.
We'll call ABCD a biclinic integral quadrilateral if AO = CO ≤ BO = DO.

For example, the following quadrilateral is a biclinic integral
quadrilateral:
AB = 19, BC = 29, CD = 37, AD = 43, BD = 48 and AO = CO = 23.

[Image: 311_biclinic.gif]

Let B(N) be the number of distinct biclinic integral quadrilaterals ABCD
that satisfy AB^2 + BC^2 + CD^2 + AD^2 ≤ N.
We can verify that B(10 000) = 49 and B(1 000 000) = 38239.

Find B(10 000 000 000).

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
