#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 220
=======================

Let D[0] be the two-letter string "Fa". For n≥1, derive D[n] from D[n-1]
by the string-rewriting rules:

"a" → "aRbFR"
"b" → "LFaLb"

Thus, D[0] = "Fa", D[1] = "FaRbFR", D[2] = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics
program, with "F" meaning "draw forward one unit", "L" meaning "turn left
90 degrees", "R" meaning "turn right 90 degrees", and "a" and "b" being
ignored. The initial position of the computer cursor is (0,0), pointing up
towards (0,1).

Then D[n] is an exotic drawing known as the Heighway Dragon of order n.
For example, D[10] is shown below; counting each "F" as one step, the
highlighted spot at (18,16) is the position reached after 500 steps.

[Image: 220.gif]

What is the position of the cursor after 10^12 steps in D[50]?
Give your answer in the form x,y with no spaces.

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
