#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 258
=======================

A sequence is defined as:

 • g[k] = 1, for 0 ≤ k ≤ 1999
 • g[k] = g[k-2000] + g[k-1999], for k ≥ 2000.

Find g[k] mod 20092010 for k = 10^18.

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
