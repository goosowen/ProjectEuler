#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 251
=======================

A triplet of positive integers (a,b,c) is called a Cardano Triplet if it
satisfies the condition:

[Image: 251_cardano.gif]

For example, (2,1,5) is a Cardano Triplet.

There exist 149 Cardano Triplets for which a+b+c ≤ 1000.

Find how many Cardano Triplets exist such that a+b+c ≤ 110,000,000.

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
