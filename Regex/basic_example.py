#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

import re

def main():
    """Docstring"""

    example_string = '''
    Jessica is 15 years old, and Daniel is 27 years old.
    Edward is 97 years old, and his grandfather, Oscar, is 102. 
    '''

    ages = re.findall(r'\d{1,3}', example_string)
    names = re.findall(r'[A-Z][a-z]*', example_string)

    print(ages)
    print(names)

if __name__ == '__main__':
    main()
