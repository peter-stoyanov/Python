#!/usr/bin/env python
"""Find all integer and floating-point numbers in a string."""

__author__ = "Petar Stoyanov"

import re

def main():
    """
    in: 1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5
    out: 1	-1 123 -123 123.456 -123.456
    """

    #text = input()
    text = '1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5'

    regex = re.compile(r"""
        (^|(?<=\s))
        (?P<number>
            -?
            \d+
            \.?
            \d*
        )
        ($|(?=\s))
        """, re.VERBOSE)

    matches = regex.finditer(text)

    for match in matches:
        print(match.group('number'), end=' ')


if __name__ == '__main__':
    main()
