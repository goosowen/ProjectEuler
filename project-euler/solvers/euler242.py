#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 242
=======================

Given the set {1,2,...,n}, we define f(n,k) as the number of its k-element
subsets with an odd sum of elements. For example, f(5,3) = 4, since the
set {1,2,3,4,5} has four 3-element subsets having an odd sum of elements,
i.e.: {1,2,4}, {1,3,5}, {2,3,4} and {2,4,5}.

When all three values n, k and f(n,k) are odd, we say that they make
an odd-triplet [n,k,f(n,k)].

There are exactly five odd-triplets with n ≤ 10, namely:
[1,1,f(1,1) = 1], [5,1,f(5,1) = 3], [5,5,f(5,5) = 1], [9,1,f(9,1) = 5] and
[9,9,f(9,9) = 1].

How many odd-triplets are there with n ≤ 10^12?

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
