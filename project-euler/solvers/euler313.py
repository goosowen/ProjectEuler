#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 313
=======================

In a sliding game a counter may slide horizontally or vertically into an
empty space. The objective of the game is to move the red counter from the
top left corner of a grid to the bottom right corner; the space always
starts in the bottom right corner. For example, the following sequence of
pictures show how the game can be completed in five moves on a 2 by 2
grid.

[Image: 313_sliding_game_1.gif]

Let S(m, n) represent the minimum number of moves to complete the game on
an m by n grid. For example, it can be verified that S(5, 4) = 25.

[Image: 313_sliding_game_2.gif]

There are exactly 5482 grids for which S(m, n) = p^2, where p < 100 is
prime.

How many grids does S(m, n) = p^2, where p < 10^6 is prime?

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
