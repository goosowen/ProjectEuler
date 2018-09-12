#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 187
=======================

A composite is a number containing at least two prime factors. For
example, 15 = 3 * 5; 9 = 3 * 3; 12 = 2 * 2 * 3.

There are ten composites below thirty containing precisely two, not
necessarily distinct, prime factors:4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two, not necessarily
distinct, prime factors?

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
