#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 121
=======================

A bag contains one red disc and one blue disc. In a game of chance a
player takes a disc at random and its colour is noted. After each turn the
disc is returned to the bag, an extra red disc is added, and another disc
is taken at random.

The player pays -L-1 to play and wins if they have taken more blue discs
than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning
is exactly 11/120, and so the maximum prize fund the banker should
allocate for winning in this game would be -L-10 before they would expect
to incur a loss. Note that any payout will be a whole number of pounds and
also includes the original -L-1 paid to play the game, so in the example
given the player actually wins -L-9.

Find the maximum prize fund that should be allocated to a single game in
which fifteen turns are played.

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
