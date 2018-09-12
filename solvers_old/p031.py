#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

coins = [200, 100, 50, 20, 10, 5, 2]  # the 1 is implied in find_combos
GOAL = 200

combos = 0
tot = 0


def find_combos(coins, remaining):
    if not coins:
        return 1

    tot = 0
    val = coins[0]
    for i in xrange(remaining / val + 1):
        tot += find_combos(coins[1:], remaining - val * i)

    return tot


print find_combos(coins, 200)
