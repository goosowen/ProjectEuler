#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 14
=======================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""


def main():
    mem = {1: 1}

    def find_chain_length(num):
        if mem.get(num):
            return mem.get(num)

        if num % 2 == 0:
            next_num = num / 2
        else:
            next_num = 3 * num + 1

        chain_length = 1 + find_chain_length(next_num)
        mem[num] = chain_length
        return chain_length

    for i in range(1, 1000000):
        find_chain_length(i)

    max_val = 0
    best_num = 0
    for k in mem.keys():
        if mem[k] > max_val:
            best_num = k
            max_val = mem[k]

    return best_num


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
