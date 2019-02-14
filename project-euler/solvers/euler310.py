#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 310
=======================

Alice and Bob play the game Nim Square. Nim Square is just like ordinary
three-heap normal play Nim, but the players may only remove a square
number of stones from a heap. The number of stones in the three heaps
is represented by the ordered triple (a, b, c).

If 0 ≤ a ≤ b ≤ c ≤ 29 then the number of losing positions for the next
player is 1160.

Find the number of losing positions for the next player if
0 ≤ a ≤ b ≤ c ≤ 100 000.

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
