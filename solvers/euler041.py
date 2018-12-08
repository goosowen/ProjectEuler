#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 41
=======================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?

"""


def main():
    from common.euler_functions import is_prime
    import itertools

    for n_digits in range(10, 1, -1):
        digits = ''.join([str(x) for x in list(range(1, n_digits))])
        pandigitals = sorted(list(itertools.permutations(digits)), reverse=True)
        for p in pandigitals:
            n = int(''.join(p))
            if is_prime(n):
                return n


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
