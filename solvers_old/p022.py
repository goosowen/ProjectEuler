#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import csv
from common import letter_to_score

names = []
with open("resources/p022_names.txt", 'r') as f:
	for row in csv.reader(f, delimiter=','):
		names.append(row)

names = sorted(names[0])

total = 0
for i in xrange(len(names)):
	name = names[i]
	word_total = 0
	for c in name:
		word_total += letter_to_score[c]
	total += word_total * (i+1)

print total



		