#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 296
=======================

Given is an integer sided triangle ABC with BC ≤ AC ≤ AB.
k is the angular bisector of angle ACB.
m is the tangent at C to the circumscribed circle of ABC.
n is a line parallel to m through B.
The intersection of n and k is called E.

How many triangles ABC with a perimeter not exceeding 100 000 exist such
that BE has integral length?

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
