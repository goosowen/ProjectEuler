#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 240
=======================

There are 1111 ways in which five 6-sided dice (sides numbered 1 to 6) can
be rolled so that the top three sum to 15. Some examples are:

D[1],D[2],D[3],D[4],D[5] = 4,3,6,3,5
D[1],D[2],D[3],D[4],D[5] = 4,3,3,5,6
D[1],D[2],D[3],D[4],D[5] = 3,3,3,6,6
D[1],D[2],D[3],D[4],D[5] = 6,6,3,3,3

In how many ways can twenty 12-sided dice (sides numbered 1 to 12) be
rolled so that the top ten sum to 70?

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
