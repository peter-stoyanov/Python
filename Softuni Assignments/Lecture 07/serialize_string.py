#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""

    text = input()
    char_indexes = {}

    for index, ch in enumerate(text):
        if ch not in char_indexes:
            char_indexes[ch] = []
            char_indexes[ch].append(index)
        else:
            char_indexes[ch].append(index)
    
    for char, indexes in char_indexes.items():
        formatted_indexes = '/'.join([str(index) for index in indexes])
        print(f'{char}:{formatted_indexes}')


if __name__ == '__main__':
    main()

