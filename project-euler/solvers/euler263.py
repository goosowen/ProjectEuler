#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 263
=======================

Consider the number 6. The divisors of 6 are: 1,2,3 and 6.
Every number from 1 up to and including 6 can be written as a sum of
distinct divisors of 6: 1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6.
A number n is called a practical number if every number from 1 up to and
including n can be expressed as a sum of distinct divisors of n.

A pair of consecutive prime numbers with a difference of six is called a
sexy pair (since "sex" is the Latin word for "six"). The first sexy pair
is (23, 29).

We may occasionally find a triple-pair, which means three consecutive sexy
prime pairs, such that the second member of each pair is the first member
of the next pair.

We shall call a number n such that:

 • (n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair, and
 • the numbers n-8, n-4, n, n+4 and n+8 are all practical,

an engineers’ paradise.

Find the sum of the first four engineers’ paradises.

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
