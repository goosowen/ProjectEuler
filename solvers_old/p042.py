#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word 
a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?
'''

from common import letter_to_score


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


if __name__ == "__main__":
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

    print total_triangle_words
