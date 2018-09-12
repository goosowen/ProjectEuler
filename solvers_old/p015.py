#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

# It's 40 choose 20 = 137846528820
# There are 40 moves and 20 of them have to be down, 20 have to be right.
# It doesn't matter the order.
