#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 265
=======================

2^N binary digits can be placed in a circle so that all the N-digit
clockwise subsequences are distinct.

For N=3, two such circular arrangements are possible, ignoring rotations:

[Image: 265_BinaryCircles.gif]

For the first arrangement, the 3-digit subsequences, in clockwise order,
are: 000, 001, 010, 101, 011, 111, 110 and 100.

Each circular arrangement can be encoded as a number by concatenating the
binary digits starting with the subsequence of all zeros as the most
significant bits and proceeding clockwise. The two arrangements for N=3
are thus represented as 23 and 29:

                           00010111 [2] = 23
                           00011101 [2] = 29

Calling S(N) the sum of the unique numeric representations, we can see
that S(3) = 23 + 29 = 52.

Find S(5).

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
