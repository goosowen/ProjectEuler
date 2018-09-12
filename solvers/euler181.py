#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 181
=======================

Having three black objects B and one white object W they can be grouped in
7 ways like this:

     (BBBW)  (B,BBW)  (B,B,BW)  (B,B,B,W)  (B,BB,W)  (BBB,W)  (BB,BW)

In how many ways can sixty black objects B and forty white objects W be
thus grouped?

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
