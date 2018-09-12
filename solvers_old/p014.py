#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

mem = {1: 1}


def find_chain_length(num):
    if mem.get(num):
        return mem.get(num)

    next_num = 0
    if num % 2 == 0:
        next_num = num / 2
    else:
        next_num = 3 * num + 1

    chain_length = 1 + find_chain_length(next_num)
    mem[num] = chain_length
    return chain_length


for i in xrange(1, 1000000):
    find_chain_length(i)

max_val = 0
best_num = 0
for k in mem.keys():
    if mem[k] > max_val:
        best_num = k
        max_val = mem[k]

print best_num, max_val
