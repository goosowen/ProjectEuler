#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 173
=======================

We shall define a square lamina to be a square outline with a square
"hole" so that the shape possesses vertical and horizontal symmetry. For
example, using exactly thirty-two square tiles we can form two different
square laminae:

With one-hundred tiles, and not necessarily using all of the tiles at one
time, it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be
formed?

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
