#!/usr/bin/env python
"""Remove negatives and reverses the list"""

__author__ = "Petar Stoyanov"

def main(*args):
    """Docstring"""

    array = [int(num) for num in args[0].split(" ")]

    positives = [str(num) for num in array if num >= 0][::-1]

    print(' '.join(positives) if len(positives) > 0 else 'empty')

if __name__ == '__main__':
    # main("1 2 -9 -11 25 16 -8 0 1")
    main("-9 -11 -8")
