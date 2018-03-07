#!/usr/bin/env python
"""match a valid phone number from Sofia."""

__author__ = "Petar Stoyanov"

import re

def main():
    """
    It starts with "+359"
    Then, it is followed by the area code (always 2)
    After that, it's followed by the number itself:
    The number consists of 7 digits (separated in two groups of 3 and 4 digits respectively). 
    The different parts are separated by either a space or a hyphen ('-').
    """

    #text = input()
    text = '+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222'

    regex = re.compile(r"""
        (?<=^| )        #beginning of string or space-like char
        \+359           
        (
            [ -]        #separator
        )
        2
        \1          #same separator
        \d{3}
        \1
        \d{4}
        \b
        """, re.VERBOSE)

    matches = regex.finditer(text)

    for match in matches:
        print(match.group(), end=' ')


if __name__ == '__main__':
    main()
