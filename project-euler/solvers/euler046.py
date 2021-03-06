#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 46
=======================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?

"""


# TODO lazy initialization of squares and primes in runner
def main():
    from common.euler_functions import is_prime_mem

    limit_squares = 1000

    twice_squares = []
    for i in range(1, limit_squares):
        twice_squares.append(2 * i**2)

    primes = set()

    for i in range(3, twice_squares[-1], 2):
        if is_prime_mem(i, primes):
            primes.add(i)
            continue

        for s in twice_squares:
            leftover = i - s

            if leftover < 1:
                return i

            if is_prime_mem(leftover, primes):
                primes.add(leftover)
                break


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
