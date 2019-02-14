#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 326
=======================

Let a[n] be a sequence recursively defined by:

[Image: 326_formula1.gif]

So the first 10 elements of a[n] are: 1,1,0,3,0,3,5,4,1,9.

Let f(N,M) represent the number of pairs (p,q) such that:

[Image: 326_formula2.gif]

It can be seen that f(10,10)=4 with the pairs (3,3), (5,5), (7,9) and
(9,10). You are also given that f(10^4,10^3)=97158.

Find f(10^12,10^6).

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
