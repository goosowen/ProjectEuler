#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 273
=======================

Consider equations of the form: a^2 + b^2 = N, 0 ≤ a ≤ b, a, b and N
integer.

For N=65 there are two solutions:

a=1, b=8 and a=4, b=7.

We call S(N) the sum of the values of a of all solutions of a^2 + b^2 = N,
0 ≤ a ≤ b, a, b and N integer.

Thus S(65) = 1 + 4 = 5.

Find ∑S(N), for all squarefree N only divisible by primes of the form 4k+1
with 4k+1 < 150.

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
