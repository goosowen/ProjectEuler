#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 285
=======================

Albert chooses a positive integer k, then two real numbers a, b are
randomly chosen in the interval [0,1] with uniform distribution.
The square root of the sum (k·a+1)^2 + (k·b+1)^2 is then computed and
rounded to the nearest integer. If the result is equal to k, he scores k
points; otherwise he scores nothing.

For example, if k = 6, a = 0.2 and b = 0.85, then
(k·a+1)^2 + (k·b+1)^2 = 42.05.
The square root of 42.05 is 6.484... and when rounded to the nearest
integer, it becomes 6. This is equal to k, so he scores 6 points.

It can be shown that if he plays 10 turns with k = 1, k = 2, ..., k = 10,
the expected value of his total score, rounded to five decimal places, is
10.20914.

If he plays 10^5 turns with k = 1, k = 2, k = 3, ..., k = 10^5, what is
the expected value of his total score, rounded to five decimal places?

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
