#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 149
=======================

Looking at the table below, it is easy to verify that the maximum possible
sum of adjacent numbers in any direction (horizontal, vertical, diagonal
or anti-diagonal) is 16 (= 8 + 7 + 1).

                           +-----------------+
                           | 2 | 5 | 3 | 2   |
                           |---+---+---+-----|
                           | 9 | 6 | 5 | 1   |
                           |---+---+---+-----|
                           | 3 | 2 | 7 | 3   |
                           |---+---+---+-----|
                           | 1 | 8 | 4 |   8 |
                           +-----------------+

Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form
of what is known as a "Lagged Fibonacci Generator":

For 1 k 55, s[k] = [100003 200003k + 300007k^3] (modulo 1000000) 500000.
For 56 k 4000000, s[k] = [s[k24] + s[k55] + 1000000] (modulo 1000000)
500000.

Thus, s[10] = 393027 and s[100] = 86613.

The terms of s are then arranged in a 2000 * 2000 table, using the first
2000 numbers to fill the first row (sequentially), the next 2000 numbers
to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any
direction (horizontal, vertical, diagonal or anti-diagonal).

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
