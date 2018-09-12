#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 250
=======================

Find the number of non-empty subsets of {1^1, 2^2, 3^3, ...,
250250^250250}, the sum of whose elements is divisible by 250. Enter the
rightmost 16 digits as your answer.

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
