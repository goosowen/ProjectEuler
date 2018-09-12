#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 298
=======================

Larry and Robin play a memory game involving of a sequence of random
numbers between 1 and 10, inclusive, that are called out one at a time.
Each player can remember up to 5 previous numbers. When the called number
is in a player's memory, that player is awarded a point. If it's not, the
player adds the called number to his memory, removing another number if
his memory is full.

Both players start with empty memories. Both players always add new missed
numbers to their memory but use a different strategy in deciding which
number to remove:
Larry's strategy is to remove the number that hasn't been called in the
longest time.
Robin's strategy is to remove the number that's been in the memory the
longest time.

Example game:

           Turn Called  Larry's   Larry's  Robin's   Robin's
                number   memory    score    memory    score
           1    1      1          0       1          0
           2    2      1,2        0       1,2        0
           3    4      1,2,4      0       1,2,4      0
           4    6      1,2,4,6    0       1,2,4,6    0
           5    1      1,2,4,6    1       1,2,4,6    1
           6    8      1,2,4,6,8  1       1,2,4,6,8  1
           7    10     1,4,6,8,10 1       2,4,6,8,10 1
           8    2      1,2,6,8,10 1       2,4,6,8,10 2
           9    4      1,2,4,8,10 1       2,4,6,8,10 3
           10   1      1,2,4,8,10 2       1,4,6,8,10 3

Denoting Larry's score by L and Robin's score by R, what is the expected
value of |L-R| after 50 turns? Give your answer rounded to eight decimal
places using the format x.xxxxxxxx .

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
