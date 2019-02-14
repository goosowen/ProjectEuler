#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 176
=======================

The four rectangular triangles with sides (9,12,15), (12,16,20), (5,12,13)
and (12,35,37) all have one of the shorter sides (catheti) equal to 12. It
can be shown that no other integer sided rectangular triangle exists with
one of the catheti equal to 12.

Find the smallest integer that can be the length of a cathetus of exactly
47547 different integer sided rectangular triangles.

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
