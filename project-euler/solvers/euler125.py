#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 125
=======================

The palindromic number 595 is interesting because it can be written as the
sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be
written as consecutive square sums, and the sum of these palindromes is
4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is
concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic
and can be written as the sum of consecutive squares.

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
