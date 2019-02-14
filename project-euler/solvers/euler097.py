#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 97
=======================

The first known prime found to exceed one million digits was discovered in
1999, and is a Mersenne prime of the form 2^69725931; it contains exactly
2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p1,
have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which
contains 2,357,207 digits: 28433 * 2^7830457+1.

Find the last ten digits of this prime number.

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
