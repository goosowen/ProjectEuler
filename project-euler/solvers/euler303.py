#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 303
=======================

For a positive integer n, define f(n) as the least positive multiple of n
that, written in base 10, uses only digits ≤ 2.

Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

Also, ∑[f(n)/n] for 1 ≤ n ≤ 100 is 11363107.

Find ∑[f(n)/n] for 1 ≤ n ≤ 10000.

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
