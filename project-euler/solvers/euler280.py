#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 280
=======================

A laborious ant walks randomly on a 5x5 grid. The walk starts from the
central square. At each step, the ant moves to an adjacent square at
random, without leaving the grid; thus there are 2, 3 or 4 possible moves
at each step depending on the ant's position.

At the start of the walk, a seed is placed on each square of the lower
row. When the ant isn't carrying a seed and reaches a square of the lower
row containing a seed, it will start to carry the seed. The ant will drop
the seed on the first empty square of the upper row it eventually reaches.

What's the expected number of steps until all seeds have been dropped in
the top row? Give your answer rounded to 6 decimal places.

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
