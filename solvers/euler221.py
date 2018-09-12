#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 221
=======================

We shall call a positive integer A an "Alexandrian integer", if there
exist integers p, q, r such that:

A = p · q · r    and   1 = 1 + 1 + 1
                      A   p   q   r

For example, 630 is an Alexandrian integer (p = 5, q = −7, r = −18).In
fact, 630 is the 6th Alexandrian integer, the first 6 Alexandrian
integers being: 6, 42, 120, 156, 420 and 630.

Find the 150000th Alexandrian integer.

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
