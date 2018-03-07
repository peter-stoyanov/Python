#!/usr/bin/env python
"""Find all valid hexadecimal numbers in a string"""

__author__ = "Petar Stoyanov"

import re

def main():
    """
    0x - not required
    One or more hexadecimal digits 0-9 A-F
    """

    #text = input()
    text = '1F 0xG 0x1F G 0x4G 4G 0xAB 0xFG FG 0x10   10 AB  FF'

    regex = re.compile(r"""
        \b
        (0x)?
        [0-9A-F]+
        \b
        """, re.VERBOSE)

    matches = regex.finditer(text)

    for match in matches:
        print(match.group(), end=' ')


if __name__ == '__main__':
    main()
