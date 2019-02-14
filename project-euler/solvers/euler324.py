#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 324
=======================

Let f(n) represent the number of ways one can fill a 3×3×n tower with
blocks of 2×1×1. You're allowed to rotate the blocks in any way you like;
however, rotations, reflections etc of the tower itself are counted as
distinct. For example (with q = 100000007):

f(2) = 229,
f(4) = 117805,
f(10) mod q = 96149360,
f(10^3) mod q = 24806056,
f(10^6) mod q = 30808124.

Find f(10^10000) mod 100000007.

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
