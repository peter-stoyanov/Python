#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

import collections

def main():
    """Docstring"""

    input_dictionary = {}
    manipulated_dictionary = {}

    while True:
        line = input().split(':')

        if line[0] == "end":
            break

        key_line = line[0]
        value_line = line[1].split('/')
        value_line = list(map(int, value_line))

        input_dictionary[key_line] = value_line

    for key, value in input_dictionary.items():
        for element in value:
            manipulated_dictionary[element] = key

    manipulated_dictionary = collections.OrderedDict(sorted(manipulated_dictionary.items()))

    [print(value, end='') for key, value in manipulated_dictionary.items()]


if __name__ == '__main__':
    main()
