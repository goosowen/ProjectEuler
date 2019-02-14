#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 107
=======================

The following undirected network consists of seven vertices and twelve
edges with a total weight of 243.

The same network can be represented by the matrix below.

               +-----------------------------------------+
               |      | A  | B  | C  | D  | E  | F  | G  |
               |------+----+----+----+----+----+----+----|
               | A    | -  | 16 | 12 | 21 | -  | -  | -  |
               |------+----+----+----+----+----+----+----|
               | B    | 16 | -  | -  | 17 | 20 | -  | -  |
               |------+----+----+----+----+----+----+----|
               | C    | 12 | -  | -  | 28 | -  | 31 | -  |
               |------+----+----+----+----+----+----+----|
               | D    | 21 | 17 | 28 | -  | 18 | 19 | 23 |
               |------+----+----+----+----+----+----+----|
               | E    | -  | 20 | -  | 18 | -  | -  | 11 |
               |------+----+----+----+----+----+----+----|
               | F    | -  | -  | 31 | 19 | -  | -  | 27 |
               |------+----+----+----+----+----+----+----|
               | G    | -  | -  | -  | 23 | 11 | 27 | -  |
               +-----------------------------------------+

However, it is possible to optimise the network by removing some edges and
still ensure that all points on the network remain connected. The network
which achieves the maximum saving is shown below. It has a weight of 93,
representing a saving of 243 93 = 150 from the original network.

Using network.txt, a 6K text file containing a network with forty vertices,
and given in matrix form, find the maximum saving which can be achieved by
removing redundant edges whilst ensuring that the network remains connected.

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
