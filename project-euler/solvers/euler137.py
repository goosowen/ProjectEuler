#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 137
=======================

Consider the infinite polynomial series A[F](x) = xF[1] + x^2F[2] +
x^3F[3] + ..., where F[k] is the kth term in the Fibonacci sequence: 1, 1,
2, 3, 5, 8, ... ; that is, F[k] = F[k[1]] + F[k[2]], F[1] = 1 and F[2] =
1.

For this problem we shall be interested in values of x for which A[F](x)
is a positive integer.

Surprisingly A[F](1/2)  =  (1/2).1 + (1/2)^2.1 + (1/2)^3.2 + (1/2)^4.3 +
                           (1/2)^5.5 + ...
                        =  1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
                        =  2

The corresponding values of x for the first five natural numbers are shown
below.

                            +---------------+
                            |x      |A[F](x)|
                            |-------+-------|
                            |21     |1      |
                            |-------+-------|
                            |1/2    |2      |
                            |-------+-------|
                            |(132)/3|3      |
                            |-------+-------|
                            |(895)/8|4      |
                            |-------+-------|
                            |(343)/5|5      |
                            +---------------+

We shall call A[F](x) a golden nugget if x is rational, because they
become increasingly rarer; for example, the 10th golden nugget is
74049690.

Find the 15th golden nugget.

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
