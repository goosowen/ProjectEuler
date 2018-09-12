#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 141
=======================

A positive integer, n, is divided by d and the quotient and remainder are
q and r respectively. In addition d, q, and r are consecutive positive
integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also
be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common
ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102^2, happen to also be
perfect squares.
The sum of all progressive perfect squares below one hundred thousand is
124657.

Find the sum of all progressive perfect squares below one trillion
(10^12).

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
