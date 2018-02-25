#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

import re

def main():
    """Docstring"""

    text = input()
    diamond_value = 0

    regex = r"(<\w+>)"
    matches = re.finditer(regex, text)

    for match in matches:
        match = match.group()
    
        for ch in match:
            if ch.isdigit():
                diamond_value += int(ch)
    
    if diamond_value == 0:
        print('Better luck next time')
    else:
        print(f'Found {diamond_value} carat diamond')

if __name__ == '__main__':
    main()
