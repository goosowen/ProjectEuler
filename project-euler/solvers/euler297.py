#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 297
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. Starting with 1 and 2, the first 10 terms will
be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

Every positive integer can be uniquely written as a sum of nonconsecutive
terms of the Fibonacci sequence. For example, 100 = 3 + 8 + 89.
Such a sum is called the Zeckendorf representation of the number.

For any integer n>0, let z(n) be the number of terms in the Zeckendorf
representation of n. Thus, z(5) = 1, z(14) = 2, z(100) = 3 etc.
Also, for 0<n<10^6, ∑ z(n) = 7894453.

Find ∑ z(n) for 0<n<10^17.

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
