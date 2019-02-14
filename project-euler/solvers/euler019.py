#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 19
=======================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?

"""


def main():
    days_in_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sunday = 7
    months_in_year = [('Jan',31), ('Feb',28), ('Mar',31), ('Apr',30), ('May',31), ('Jun',30), ('Jul',31), ('Aug',31),
              ('Sep',30), ('Oct',31), ('Nov',30), ('Dec',31)]

    year = 1900
    weekday = 1
    month = 1
    days_in_month = months_in_year[month - 1][1]
    month_day = 1

    count = 0
    tot = 0
    while year < 2001 and count < 100000:
        if year > 1900 and month_day == 1 and weekday == sunday:
            tot += 1

        weekday += 1
        if weekday > len(days_in_week):
            weekday = 1

        month_day += 1
        if month_day > days_in_month:
            month_day = 1

            month += 1
            if month > len(months_in_year):
                month = 1
                year += 1

            days_in_month = months_in_year[month - 1][1]
            if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_month += 1

        count += 1

        # if count % 5 == 0:
        #     print(days_in_week[weekday-1], months_in_year[month-1][0], month_day, year)
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
