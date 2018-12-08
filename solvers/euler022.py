#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 22
=======================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

"""


def main():
    import csv
    import os
    from config import WORKING_DIR
    from common.constants import letter_to_score

    names = []
    os.chdir(WORKING_DIR)
    with open("resources/p022_names.txt", 'r') as f:
        for row in csv.reader(f, delimiter=','):
            names.append(row)

    names = sorted(names[0])

    tot = 0
    for i in range(len(names)):
        name = names[i]
        word_total = 0
        for c in name:
            word_total += letter_to_score[c]

        pos_total = word_total * (i + 1)
        tot += pos_total

    return tot


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
