#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 105
=======================

Let S(A) represent the sum of elements in set A of size n. We shall call
it a special sum set if for any two non-empty disjoint subsets, B and C,
the following properties are true:

 1. S(B) S(C); that is, sums of subsets cannot be equal.
 2. If B contains more elements than C then S(B) > S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set
because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159,
161, 139, 158} satisfies both rules for all possible subset pair
combinations and S(A) = 1286.

Using sets.txt, a 4K text file with one-hundred sets containing seven to
twelve elements (the two examples given above are the first two sets in the
file), identify all the special sum sets, A[1], A[2], ..., A[k], and find the
value of S(A[1]) + S(A[2]) + ... + S(A[k]).

NOTE: This problem is related to problems 103 and 106.

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
