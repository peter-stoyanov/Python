#!/usr/bin/env python
"""Match a date in the format dd{separator}MMM{separator}yyyy"""

__author__ = "Petar Stoyanov"

import re

def main():
    """
    Always starts with two digits, followed by a separator
    After that, it has one uppercase and two lowercase letters (e.g. Jan, Mar).
    After that, it has a separator and exactly 4 digits (for the year).
    The separator could be either of three things: a period ("."), a hyphen ("-") or a forward slash ("/")
    The separator needs to be the same for the whole date 

    output:
    Day: 13, Month: Jul, Year: 1928
    Day: 10, Month: Nov, Year: 1934
    Day: 25, Month: Dec, Year: 1937
    """

    #text = input()
    text = '13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016'

    regex = re.compile(r"""
        \b
        (?P<day>\d{2})
        (?P<sep>[.\-/])
        (?P<month>[A-Z][a-z]{2})
        (?P=sep)
        (?P<year>\d{4})
        \b
        """, re.VERBOSE)

    matches = regex.finditer(text)

    for match in matches:
        print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")


if __name__ == '__main__':
    main()
