#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 256
=======================

Tatami are rectangular mats, used to completely cover the floor of a room,
without overlap.

Assuming that the only type of available tatami has dimensions 1×2, there
are obviously some limitations for the shape and size of the rooms that
can be covered.

For this problem, we consider only rectangular rooms with integer
dimensions a, b and even size s = a·b.
We use the term 'size' to denote the floor surface area of the room, and —
without loss of generality — we add the condition a ≤ b.

There is one rule to follow when laying out tatami: there must be no
points where corners of four different mats meet.
For example, consider the two arrangements below for a 4×4 room:

[Image: 256_tatami3.gif]

The arrangement on the left is acceptable, whereas the one on the right is
not: a red "X" in the middle, marks the point where four tatami meet.

Because of this rule, certain even-sized rooms cannot be covered with
tatami: we call them tatami-free rooms.
Further, we define T(s) as the number of tatami-free rooms of size s.

The smallest tatami-free room has size s = 70 and dimensions 7×10.
All the other rooms of size s = 70 can be covered with tatami; they are:
1×70, 2×35 and 5×14.
Hence, T(70) = 1.

Similarly, we can verify that T(1320) = 5 because there are exactly 5
tatami-free rooms of size s = 1320:
20×66, 22×60, 24×55, 30×44 and 33×40.
In fact, s = 1320 is the smallest room-size s for which T(s) = 5.

Find the smallest room-size s for which T(s) = 200.

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
