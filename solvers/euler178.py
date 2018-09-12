#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 178
=======================

Consider the number 45656.
It can be seen that each pair of consecutive digits of 45656 has a
difference of one.
A number for which every pair of consecutive digits has a difference of
one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least
once.
How many pandigital step numbers less than 10^40 are there?


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
