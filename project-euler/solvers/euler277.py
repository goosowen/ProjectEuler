#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 277
=======================

A modified Collatz sequence of integers is obtained from a starting value
a[1] in the following way:

a[n+1] = a[n]/3 if a[n] is divisible by 3. We shall denote this as a large
downward step, "D".

a[n+1] = (4a[n] + 2)/3 if a[n] divided by 3 gives a remainder of 1. We
shall denote this as an upward step, "U".

a[n+1] = (2a[n] - 1)/3 if a[n] divided by 3 gives a remainder of 2. We
shall denote this as a small downward step, "d".

The sequence terminates when some a[n] = 1.

Given any integer, we can list out the sequence of steps.
For instance if a[1]=231, then the sequence
{a[n]}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps
"DdDddUUdDD".

Of course, there are other sequences that begin with that same sequence
"DdDddUUdDD....".
For instance, if a[1]=1004064, then the sequence is
DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
In fact, 1004064 is the smallest possible a[1] > 10^6 that begins with the
sequence DdDddUUdDD.

What is the smallest a[1] > 10^15 that begins with the sequence
"UDDDUdddDDUDDddDdDddDDUDDdUUDd"?

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
