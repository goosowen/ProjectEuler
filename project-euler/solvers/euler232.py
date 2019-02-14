#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 232
=======================

Two players share an unbiased coin and take it in turns to play "The
Race". On Player 1's turn, he tosses the coin once: if it comes up Heads,
he scores one point; if it comes up Tails, he scores nothing. On Player
2's turn, she chooses a positive integer T and tosses the coin T times: if
it comes up all Heads, she scores 2^T-1 points; otherwise, she scores
nothing. Player 1 goes first. The winner is the first to 100 or more
points.

On each turn Player 2 selects the number, T, of coin tosses that maximises
the probability of her winning.

What is the probability that Player 2 wins?

Give your answer rounded to eight decimal places in the form 0.abcdefgh.

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
