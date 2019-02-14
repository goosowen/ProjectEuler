#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 243
=======================

A positive fraction whose numerator is less than its denominator is called
a proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example,
with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 ,
8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient
fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be
the ratio of its proper fractions that are resilient; for example, R(12) =
4/11.
In fact, d = 12 is the smallest denominator having a resilience R(d) <
4/10.

Find the smallest denominator d, having a resilience R(d) < 15499/94744.

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
