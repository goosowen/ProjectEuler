#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 260
=======================

A game is played with three piles of stones and two players.
At her turn, a player removes one or more stones from the piles. However,
if she takes stones from more than one pile, she must remove the same
number of stones from each of the selected piles.

In other words, the player chooses some N>0 and removes:

 • N stones from any single pile; or
 • N stones from each of any two piles (2N total); or
 • N stones from each of the three piles (3N total).

The player taking the last stone(s) wins the game.

A winning configuration is one where the first player can force a win.
For example, (0,0,13), (0,11,11) and (5,5,5) are winning configurations
because the first player can immediately remove all stones.

A losing configuration is one where the second player can force a win, no
matter what the first player does.
For example, (0,1,2) and (1,3,3) are losing configurations: any legal move
leaves a winning configuration for the second player.

Consider all losing configurations (x[i],y[i],z[i]) where x[i] ≤ y[i] ≤
z[i] ≤ 100. We can verify that Σ(x[i]+y[i]+z[i]) = 173895 for these.

Find Σ(x[i]+y[i]+z[i]) where (x[i],y[i],z[i]) ranges over the losing
configurations with x[i] ≤ y[i] ≤ z[i] ≤ 1000.

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
