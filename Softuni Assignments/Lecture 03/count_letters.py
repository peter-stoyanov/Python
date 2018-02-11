#!/usr/bin/env python
"""You will be given a single string, containing random ASCII character. 
Your task is to print every character, and how many times it has been used in the string"""

__author__ = "Petar Stoyanov"

def main(*args):
    """aaabbaaabbbccc

        a -> 6
        b -> 5
        c -> 3
    """

    letter_occurences = {}

    for letter in args[0]:
        if letter in letter_occurences:
            letter_occurences[letter] += 1
        else:
            letter_occurences[letter] = 1

    results = [f"{key} -> {letter_occurences[key]}" for key in letter_occurences.keys()]

    print('\n'.join(results))


if __name__ == '__main__':
    main('aaabbaaabbbccc')
