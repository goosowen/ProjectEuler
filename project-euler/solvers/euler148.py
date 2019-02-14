#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 148
=======================

We can easily verify that none of the entries in the first seven rows of
Pascal's triangle are divisible by 7:

                                    1
                                 1     1
                              1     2     1
                           1     3     3     1
                        1     4     6     4     1
                     1     5    10    10     5     1
                  1     6    15    20    15     6     1

However, if we check the first one hundred rows, we will find that only
2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one
billion (10^9) rows of Pascal's triangle.

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
