#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 86
=======================

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3,
and a fly, F, sits in the opposite corner. By travelling on the surfaces
of the room the shortest "straight line" distance from S to F is 10 and
the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given
cuboid and the shortest route is not always integer.

By considering all cuboid rooms up to a maximum size of M by M by M, there
are exactly 2060 cuboids for which the shortest distance is integer when
M=100, and this is the least value of M for which the number of solutions
first exceeds two thousand; the number of solutions is 1975 when M=99.

Find the least value of M such that the number of solutions first exceeds
one million.

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
