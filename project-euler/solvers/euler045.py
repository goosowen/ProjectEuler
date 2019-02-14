#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 45
=======================

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle     T[n]=n(n+1)/2   1, 3, 6, 10, 15, ...
Pentagonal   P[n]=n(3n-1)/2  1, 5, 12, 22, 35, ...
Hexagonal    H[n]=n(2n-1)    1, 6, 15, 28, 45, ...

It can be verified that T[285] = P[165] = H[143] = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

"""


def main():
    pents = set()
    hexas = set()

    for n in range(1, 100000):
        tri = int(n * (n + 1) / 2)
        pent = int(n * (3 * n - 1) / 2)
        hexa = int(n * (2 * n - 1))

        pents.add(pent)
        hexas.add(hexa)

        if tri in pents and tri in hexas:
            if tri > 40755:
                return tri


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