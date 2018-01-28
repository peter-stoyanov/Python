#!/usr/bin/env python
"""Extract square numbers"""

__author__ = "Petar Stoyanov"

from math import sqrt

def main(*args):
    """Extrat square numbers = integer which is the square of any integer"""

    array = args[0].split(" ")

    square = [int(i) for i in array if int(i) > 0 if sqrt(int(i)) % 1 == 0]

    square.sort(reverse=True)

    for i in square:
        print(i, end=" ")

if __name__ == '__main__':
    main("1 2 3 4 5")

