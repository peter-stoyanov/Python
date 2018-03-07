#!/usr/bin/env python
"""Write a Program to match full names from a 
list of names and print them on the console."""

__author__ = "Petar Stoyanov"

import re

def main():
    """ in: Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan	Ivanov
        out: Ivan Ivanov Test Testov
    """

    #names = input()
    text = 'Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan	Ivanov'
    pattern = r'(?<!\w)[A-Z][a-z]+ [A-Z][a-z]+'
    regex = re.compile(pattern)

    matches = regex.findall(text)

    for match in matches:
        print(match, end=' ')


if __name__ == '__main__':
    main()
