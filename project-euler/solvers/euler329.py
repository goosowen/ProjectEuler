#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 329
=======================

Susan has a prime frog.
Her frog is jumping around over 500 squares numbered 1 to 500.He can only
jump one square to the left or to the right, with equal probability, and
he cannot jump outside the range [1;500].
(if it lands at either end, it automatically jumps to the only available
square on the next move.)

When he is on a square with a prime number on it, he croaks 'P' (PRIME)
with probability 2/3 or 'N' (NOT PRIME) with probability 1/3 just before
jumping to the next square.
When he is on a square with a number on it that is not a prime he croaks
'P' with probability 1/3 or 'N' with probability 2/3 just before jumping
to the next square.

Given that the frog's starting position is random with the same
probability for every square, and given that she listens to his first 15
croaks, what is the probability that she hears the sequence
PPPPNNPPPNPPNPN?

Give your answer as a fraction p/q in reduced form.

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
