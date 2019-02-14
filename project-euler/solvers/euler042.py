#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 42
=======================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?

"""


def main():
    # TODO put this in the template
    import os

    # TODO must be a better way to do relative paths here..
    from config import WORKING_DIR
    os.chdir(WORKING_DIR)

    from common.constants import letter_to_score

    class TriangleNumberPopulater:

        def __init__(self):
            self.triangle_numbers = set()
            self.max_calculated_number = 0
            self.max_calculated_sequence = 0

        def calc_triangle_number(self, n):
            return .5 * n * (n + 1)

        def is_triangle_number(self, num):
            while num > self.max_calculated_number:
                self.max_calculated_sequence += 1
                self.max_calculated_number = self.calc_triangle_number(self.max_calculated_sequence)
                self.triangle_numbers.add(self.max_calculated_number)

            return num in self.triangle_numbers

    def calculate_word_number(word):
        total = 0
        for c in word:
            total += letter_to_score[c]

        return total

    total_triangle_words = 0
    tnp = TriangleNumberPopulater()
    with open('resources/p042_words.txt', 'r') as f:
        words = f.read().split(',')
        for word in words:
            if word.startswith('"') and word.endswith('"'):
                word = word[1:-1]

            word_number = calculate_word_number(word)
            if tnp.is_triangle_number(word_number):
                total_triangle_words += 1

    return total_triangle_words


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
