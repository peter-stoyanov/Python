#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

import re

def main():
    """Docstring"""

    filter = input()
    filter_letter = filter[0]
    filter_number = int(filter[1])

    sentence_pattern = r'^[A-Z][^\.!\?]*[\.\!\?]$'
    sentence_regex = re.compile(sentence_pattern)

    valid_words = []
    while True:
        sentence = input()
        
        if sentence == 'end':
            break
        
        if not sentence_regex.match(sentence):
            continue
        
        words = re.findall(r'\w+\b', sentence)
        for word in words:
            if word.count(filter_letter) == filter_number:
                valid_words.append(word)

    print(*valid_words, sep=", ")


if __name__ == '__main__':
    main()
