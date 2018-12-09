#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 34
=======================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""


def main():
    import math

    def digit_factorial_sum(num):
        factorial_sum = 0
        for digit in str(num):
            factorial_sum += math.factorial(int(digit))
        return factorial_sum

    def get_upper_limit():
        limit = 9
        while digit_factorial_sum(limit) > limit:
            limit = int(str(limit) + '9')

        limit += 1
        return limit

    limit = get_upper_limit()
    curious_numbers = []
    factorial_memory = {}
    for digit in range(10):
        factorial_memory[digit] = math.factorial(digit)

    digit_memory = {}
    for num in range(3, limit):
        digit_set = tuple(sorted(str(num)))

        factorial_sum = digit_memory.get(digit_set)
        if factorial_sum is None:
            factorial_sum = 0
            for digit in digit_set:
                factorial_sum += factorial_memory[int(digit)]
            digit_memory[digit_set] = factorial_sum

        if factorial_sum == num:
            curious_numbers.append(num)

    return sum(curious_numbers)


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
