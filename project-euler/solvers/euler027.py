#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 27
=======================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.

"""


# TODO optimize prime finding
def main():
    import math

    primes = set()

    # hopefully up to 1 million is enough primes to store
    for num in range(1000000):
        prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.add(num)

    best_tuple = (0, 0)
    best_consecutive_vals = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            consecutive_vals = 0
            while (n ** 2 + a * n + b) in primes:
                consecutive_vals += 1
                n += 1

            if consecutive_vals > best_consecutive_vals:
                best_consecutive_vals = consecutive_vals
                best_tuple = (a, b)

    return best_tuple[0] * best_tuple[1]


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
