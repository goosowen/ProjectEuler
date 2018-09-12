#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 48
=======================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

DIGITS_THAT_MATTER = 10
SERIES_CAP = 1000


def main():
    total = 0
    for i in range(1, SERIES_CAP + 1):
        total += i ** i
        total_str = str(total)
        if len(total_str) > DIGITS_THAT_MATTER:
            total_str = total_str[len(total_str) - DIGITS_THAT_MATTER:]
        total = int(total_str)

    return total


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
