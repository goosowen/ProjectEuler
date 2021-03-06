#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 227
=======================

"The Chase" is a game played with two dice and an even number of players.

The players sit around a table; the game begins with two opposite players
having one die each. On each turn, the two players with a die roll it.
If a player rolls a 1, he passes the die to his neighbour on the left; if
he rolls a 6, he passes the die to his neighbour on the right; otherwise,
he keeps the die for the next turn.
The game ends when one player has both dice after they have been rolled
and passed; that player has then lost.

In a game with 100 players, what is the expected number of turns the game
lasts?

Give your answer rounded to ten significant digits.

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
