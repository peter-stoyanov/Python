#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""

    text = input().lower()
    search_term = input().lower()

    counter = 0
    index = 0

    while True:
        if text.find(search_term, index) == -1:
            break
        else:
            counter += 1
            index = text.find(search_term, index) + 1

    print(counter)

if __name__ == '__main__':
    main()
