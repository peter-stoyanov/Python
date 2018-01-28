#!/usr/bin/env python
"""Finds the sign of an integer"""

__author__ = "Petar Stoyanov"


def main():
    """Finds the sign of an integer"""

    number = int(input())

    if number > 0:
        print(f'The number {number} is positive.')
    elif number < 0:
        print(f'The number {number} is negative.')
    else:
        print(f'The number {number} is zero.')


if __name__ == '__main__':
    main()
