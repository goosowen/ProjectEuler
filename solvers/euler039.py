#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 39
=======================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?

"""


def main():
    def is_right_triangle(a, b, c):
        return a ** 2 + b ** 2 == c ** 2

    max_p_sols = 0
    max_p = 0
    for p in range(1, 1000):
        sols = set()
        for a in range(1, int(p / 2)):
            a_squared = a ** 2
            for b in range(a, p - a - 1):
                c = p - a - b
                if a_squared + b ** 2 == c ** 2:
                    sols.add(frozenset([a, b, c]))

        num_sols = len(sols)
        if num_sols > max_p_sols:
            max_p_sols = num_sols
            max_p = p

    return max_p


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
