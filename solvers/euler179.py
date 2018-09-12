#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 179
=======================

Find the number of integers 1 < n < 10^7, for which n and n + 1 have the
same number of positive divisors. For example, 14 has the positive
divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

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
