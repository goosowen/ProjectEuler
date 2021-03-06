#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

from common.euler_functions import is_palindrome


def main():
    three_digit_nums = range(999, 100, -1)

    for possible_palindrome in range(999 * 999, 100 * 100, -1):
        if is_palindrome(str(possible_palindrome)):
            for i in three_digit_nums:
                if possible_palindrome % i == 0:
                    if possible_palindrome / i < 1000 and possible_palindrome / i > 99:
                        return possible_palindrome


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
