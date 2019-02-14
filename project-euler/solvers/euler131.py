#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 131
=======================

There are some prime values, p, for which there exists a positive integer,
n, such that the expression n^3 + n^2p is a perfect cube.

For example, when p = 19, 8^3 + 8^2 * 19 = 12^3.

What is perhaps most surprising is that for each prime with this property
the value of n is unique, and there are only four such primes below
one-hundred.

How many primes below one million have this remarkable property?

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
