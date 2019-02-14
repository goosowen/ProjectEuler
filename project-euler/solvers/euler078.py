#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 78
=======================

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can separated into piles in
exactly seven different ways, so p(5)=7.

                            OOOOO

                            OOOO   O

                            OOO   OO

                            OOO   O   O

                            OO   OO   O

                            OO   O   O   O

                            O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

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
