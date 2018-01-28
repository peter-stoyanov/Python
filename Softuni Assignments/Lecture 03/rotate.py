#!/usr/bin/env python
"""Rotate list"""

__author__ = "Petar Stoyanov"

def main(*args):
    """Docstring"""

    array = args[0].split(" ")

    rotated = [array[-1]] + array[:-1]

    print(' '.join(rotated))

if __name__ == '__main__':
    main("a b c d e")
