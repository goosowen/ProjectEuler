#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 306
=======================

The following game is a classic example of Combinatorial Game Theory:

Two players start with a strip of n white squares and they take alternate
turns. On each turn, a player picks two contiguous white squares and
paints them black. The first player who cannot make a move loses.

 • If n = 1, there are no valid moves, so the first player loses
   automatically.
 • If n = 2, there is only one valid move, after which the second player
   loses.
 • If n = 3, there are two valid moves, but both leave a situation where
   the second player loses.
 • If n = 4, there are three valid moves for the first player; she can
   win the game by painting the two middle squares.
 • If n = 5, there are four valid moves for the first player (shown below
   in red); but no matter what she does, the second player (blue) wins.

[Image: 306_pstrip.gif]

So, for 1 ≤ n ≤ 5, there are 3 values of n for which the first player can
force a win. Similarly, for 1 ≤ n ≤ 50, there are 40 values of n for which
the first player can force a win.

For 1 ≤ n ≤ 1 000 000, how many values of n are there for which the first
player can force a win?

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
