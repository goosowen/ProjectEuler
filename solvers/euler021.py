#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 21
=======================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""


def main():
    import math

    # maps numbers to the sum of their proper divisors
    mem = {}

    # sum of all amicable numbers under 10000
    tot = 0

    for i in range(1, 10000):
        # sum of all proper divisors of i
        divisors_sum = 0

        for j in range(1, int(math.sqrt(i))):
            if i % j == 0:
                divisors_sum += j
                other = i / j
                if other != j and other != i:
                    divisors_sum += int(other)

        # check if amicable
        if mem.get(divisors_sum):
            if mem.get(divisors_sum) == i:
                i, divisors_sum
                tot += i
                tot += divisors_sum

        mem[i] = divisors_sum

    return tot


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
