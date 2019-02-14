#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 158
=======================

Taking three different letters from the 26 letters of the alphabet,
character strings of length three can be formed.
Examples are 'abc', 'hat' and 'zyx'.
When we study these three examples we see that for 'abc' two characters
come lexicographically after its neighbour to the left.
For 'hat' there is exactly one character that comes lexicographically
after its neighbour to the left. For 'zyx' there are zero characters that
come lexicographically after its neighbour to the left.
In all there are 10400 strings of length 3 for which exactly one character
comes lexicographically after its neighbour to the left.

We now consider strings of n 26 different characters from the alphabet.
For every n, p(n) is the number of strings of length n for which exactly
one character comes lexicographically after its neighbour to the left.

What is the maximum value of p(n)?

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
