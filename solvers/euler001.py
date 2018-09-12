#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""


def get_sum_multiples(x, threshold):
    num_multiples_of_x = (threshold - 1) / x
    sum_multiples_of_x = x * (num_multiples_of_x + 1) * num_multiples_of_x / 2
    return sum_multiples_of_x


def main():
    threshold = 1000
    return get_sum_multiples(3, threshold) + get_sum_multiples(5, threshold) - get_sum_multiples(15, threshold)


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
