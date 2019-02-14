#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 122
=======================

The most naive way of computing n^15 requires fourteen multiplications:

n * n * ... * n = n^15

But using a "binary" method you can compute it in six multiplications:

n * n = n^2
n^2 * n^2 = n^4
n^4 * n^4 = n^8
n^8 * n^4 = n^12
n^12 * n^2 = n^14
n^14 * n = n^15

However it is yet possible to compute it in only five multiplications:

n * n = n^2
n^2 * n = n^3
n^3 * n^3 = n^6
n^6 * n^6 = n^12
n^12 * n^3 = n^15

We shall define m(k) to be the minimum number of multiplications to
compute n^k; for example m(15) = 5.

For 1 k 200, find m(k).

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
