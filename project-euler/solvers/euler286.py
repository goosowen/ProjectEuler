#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 286
=======================

Barbara is a mathematician and a basketball player. She has found that the
probability of scoring a point when shooting from a distance x is exactly
(1 - ^x/[q]), where q is a real constant greater than 50.

During each practice run, she takes shots from distances x = 1, x = 2,
..., x = 50 and, according to her records, she has precisely a 2 % chance
to score a total of exactly 20 points.

Find q and give your answer rounded to 10 decimal places.

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
