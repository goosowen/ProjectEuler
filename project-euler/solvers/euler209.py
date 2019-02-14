#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 209
=======================

A k-input binary truth table is a map from k input bits(binary digits, 0
[false] or 1 [true]) to 1 output bit. For example, the 2-input binary
truth tables for the logical AND and XOR functions are:

            ┌────┬────┬─────────┐        ┌────┬────┬─────────┐
            │ x  │ y  │ x AND y │        │ x  │ y  │ x XOR y │
            ├────┼────┼─────────┤        ├────┼────┼─────────┤
            │ 0  │ 0  │    0    │        │ 0  │ 0  │    0    │
            ├────┼────┼─────────┤        ├────┼────┼─────────┤
            │ 0  │ 1  │    0    │        │ 0  │ 1  │    1    │
            ├────┼────┼─────────┤        ├────┼────┼─────────┤
            │ 1  │ 0  │    0    │        │ 1  │ 0  │    1    │
            ├────┼────┼─────────┤        ├────┼────┼─────────┤
            │ 1  │ 1  │    1    │        │ 1  │ 1  │    0    │
            └────┴────┴─────────┘        └────┴────┴─────────┘

How many 6-input binary truth tables, τ, satisfy the formula

     τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0

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
