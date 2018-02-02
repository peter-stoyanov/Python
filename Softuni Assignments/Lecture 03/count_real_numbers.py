#!/usr/bin/env python
"""Read a list of real numbers and print them in ascending order 
along with their number of occurrences."""

__author__ = "Petar Stoyanov"

import collections

def main(*args):
    """8 2.5 2.5 8 2.5

        2.5 -> 3 times
        8 -> 2 times
    """

    numbers = [float(num) for num in args[0].split()]

    number_occurences = {}

    for number in numbers:
        if number in number_occurences:
            number_occurences[number] += 1
        else:
            number_occurences[number] = 1

    results = [f"{key} -> {number_occurences[key]} times" for key in sorted(number_occurences.keys())]

    print('\n'.join(results))


if __name__ == '__main__':
    main('8 2.5 2.5 8 2.5')
