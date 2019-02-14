#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 214
=======================

Let φ be Euler's totient function, i.e. for a natural number n,φ(n) is the
number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

By iterating φ, each positive integer generates a decreasing chain of
numbers ending in 1.
E.g. if we start with 5 the sequence 5,4,2,1 is generated.
Here is a listing of all chains with length 4:

                                                                  5,4,2,1
                                                                  7,6,2,1
                                                                  8,4,2,1
                                                                  9,6,2,1
                                                                 10,4,2,1
                                                                 12,4,2,1
                                                                 14,6,2,1
                                                                 18,6,2,1

Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40000000 which generate a chain of
length 25?

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
