#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 140
=======================

Consider the infinite polynomial series A[G](x) = xG[1] + x^2G[2] +
x^3G[3] + ..., where G[k] is the kth term of the second order recurrence
relation G[k] = G[k[1]] + G[k[2]], G[1] = 1 and G[2] = 4; that is, 1, 4,
5, 9, 14, 23, ... .

For this problem we shall be concerned with values of x for which A[G](x)
is a positive integer.

The corresponding values of x for the first five natural numbers are shown
below.

                           +-----------------+
                           |x        |A[G](x)|
                           |---------+-------|
                           |(51)/4   |1      |
                           |---------+-------|
                           |2/5      |2      |
                           |---------+-------|
                           |(222)/6  |3      |
                           |---------+-------|
                           |(1375)/14|4      |
                           |---------+-------|
                           |1/2      |5      |
                           +-----------------+

We shall call A[G](x) a golden nugget if x is rational, because they
become increasingly rarer; for example, the 20th golden nugget is
211345365.

Find the sum of the first thirty golden nuggets.

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
