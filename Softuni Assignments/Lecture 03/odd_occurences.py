#!/usr/bin/env python
"""Extracts from a given sequence of words all elements that present 
in it odd number of times (case-insensitive)."""

__author__ = "Petar Stoyanov"


def main(*args):
    """Docstring"""

    words = [word.lower() for word in args[0].split()]
    tokens_count = {}

    for word in words:
        if word in tokens_count:
            tokens_count[word] += 1
        else:
            tokens_count[word] = 1

    results = [key for key, value in tokens_count.items() if value % 2 != 0]

    print(', '.join(results))


if __name__ == '__main__':
    main('a a b c d e e e j j k')
