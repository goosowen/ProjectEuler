#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 229
=======================

Consider the number 3600. It is very special, because

3600 = 48^2 +   36^2

3600 = 20^2 + 2×40^2

3600 = 30^2 + 3×30^2

3600 = 45^2 + 7×15^2

Similarly, we find that 88201 = 99^2 + 280^2 = 287^2 + 2×54^2 = 283^2 +
3×52^2 = 197^2 + 7×84^2.

In 1747, Euler proved which numbers are representable as a sum of two
squares.We are interested in the numbers n which admit representations of
all of the following four types:

n = a[1]^2 +   b[1]^2

n = a[2]^2 + 2×b[2]^2

n = a[3]^2 + 3×b[3]^2

n = a[7]^2 + 7×b[7]^2,

where the a[k] and b[k] are positive integers.

There are 75373 such numbers that do not exceed 10^7.
How many such numbers are there that do not exceed 2×10^9?

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
