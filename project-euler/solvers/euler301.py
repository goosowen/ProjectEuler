#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 301
=======================

Nim is a game played with heaps of stones, where two players take it in
turn to remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as
follows:
- At the start of the game there are three heaps of stones.
- On his turn the player removes any positive number of stones from any
single heap.
- The first player unable to move (because no stones remain) loses.

If (n[1], n[2], n[3]) indicates a Nim position consisting of heaps of size
n[1], n[2] and n[3] then there is a simple function X(n[1], n[2], n[3]) —
that you may look up or attempt to deduce for yourself — that returns:

 • zero if, with perfect strategy, the player about to move will
   eventually lose; or
 • non-zero if, with perfect strategy, the player about to move will
   eventually win.

For example X(1, 2, 3) = 0 because, no matter what the current player does,
his opponent can respond with a move that leaves two heaps of equal size,
at which point every move by the current player can be mirrored by his
opponent until no stones remain; so the current player loses. To
illustrate:

- current player moves to (1, 2, 1)
- opponent moves to (1, 0, 1)
- current player moves to (0, 0, 1)
- opponent moves to (0, 0, 0), and so wins.

For how many positive integers n ≤ 2^30 does X(n, 2n, 3n) = 0?

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
