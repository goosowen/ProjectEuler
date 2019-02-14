#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 197
=======================

Given is the function f(x) = 2^30.403243784-x^2 * 10^-9 ( is the
floor-function),
the sequence u[n] is defined by u[0] = -1 and u[n+1] = f(u[n]).

Find u[n] + u[n+1] for n = 10^12.
Give your answer with 9 digits after the decimal point.

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
