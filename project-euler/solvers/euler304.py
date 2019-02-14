#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 304
=======================

For any positive integer n the function next_prime(n) returns the smallest
prime p such that p>n.

The sequence a(n) is defined by:
a(1)=next_prime(10^14) and a(n)=next_prime(a(n-1)) for n>1.

The fibonacci sequence f(n) is defined by:f(0)=0, f(1)=1 and
f(n)=f(n-1)+f(n-2) for n>1.

The sequence b(n) is defined as f(a(n)).

Find ∑b(n) for 1 ≤ n ≤ 100 000. Give your answer mod 1234567891011.

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
