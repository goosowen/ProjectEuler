#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 24
=======================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?

"""


def main():
    import math

    # The first factorial above 1,000,000 is 10. 10! = 3,628,800. Working backwards, that means there
    # are 362,880 orderings with 0 in front. Then another 362,880 with 1 in front. etc.

    final_number = ""
    non_fixed_nums = list(range(10))
    total = 999999

    factorials = [math.factorial(x) for x in range(1, 11)]

    while total > 0:
        for pos in range(10, 0, -1):
            for i in range(pos, 0, -1):
                fact = factorials[i - 1]
                if fact <= total:
                    final_number += str(non_fixed_nums.pop(total / fact))
                    total, i, fact, final_number[-1], total / fact
                    total = total % fact

                    break

    for remainder_num in non_fixed_nums:
        final_number += str(remainder_num)

    return final_number


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
