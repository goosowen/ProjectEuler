#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 146
=======================

The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7,
n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all
such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?

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
