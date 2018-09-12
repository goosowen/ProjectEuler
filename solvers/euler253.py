#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 253
=======================

A small child has a “number caterpillar” consisting of forty jigsaw
pieces, each with one number on it, which, when connected together in a
line, reveal the numbers 1 to 40 in order.

Every night, the child's father has to pick up the pieces of the
caterpillar that have been scattered across the play room. He picks up the
pieces at random and places them in the correct order.
As the caterpillar is built up in this way, it forms distinct segments
that gradually merge together.
The number of segments starts at zero (no pieces placed), generally
increases up to about eleven or twelve, then tends to drop again before
finishing at a single segment (all pieces placed).

For example:

                     ┌────────────┬───────────────┐
                     │Piece Placed│Segments So Far│
                     ├────────────┼───────────────┤
                     │     12     │       1       │
                     ├────────────┼───────────────┤
                     │     4      │       2       │
                     ├────────────┼───────────────┤
                     │     29     │       3       │
                     ├────────────┼───────────────┤
                     │     6      │       4       │
                     ├────────────┼───────────────┤
                     │     34     │       5       │
                     ├────────────┼───────────────┤
                     │     5      │       4       │
                     ├────────────┼───────────────┤
                     │     35     │       4       │
                     ├────────────┼───────────────┤
                     │     …      │       …       │
                     └────────────┴───────────────┘

Let M be the maximum number of segments encountered during a random
tidy-up of the caterpillar.
For a caterpillar of ten pieces, the number of possibilities for each M is

                        ┌────────┬─────────────┐
                        │   M    │Possibilities│
                        ├────────┼─────────────┤
                        │   1    │    512      │
                        ├────────┼─────────────┤
                        │   2    │ 250912      │
                        ├────────┼─────────────┤
                        │   3    │1815264      │
                        ├────────┼─────────────┤
                        │   4    │1418112      │
                        ├────────┼─────────────┤
                        │   5    │ 144000      │
                        └────────┴─────────────┘

so the most likely value of M is 3 and the average value is
^385643⁄[113400] = 3.400732, rounded to six decimal places.

The most likely value of M for a forty-piece caterpillar is 11; but what
is the average value of M?

Give your answer rounded to six decimal places.

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
