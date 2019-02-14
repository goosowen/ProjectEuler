#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 167
=======================

For two positive integers a and b, the Ulam sequence U(a,b) is defined by
U(a,b)[1] = a, U(a,b)[2] = b and for k > 2,U(a,b)[k] is the smallest
integer greater than U(a,b)[(k-1)] which can be written in exactly one way
as the sum of two distinct previous members of U(a,b).

For example, the sequence U(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations
as the sum of two previous members, likewise 7 = 1 + 6 = 3 + 4.

Find U(2,2n+1)[k] for 2 n 10, where k = 10^11.

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
