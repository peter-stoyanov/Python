#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""

    stop_words = input().split()
    text = input()
    
    for stop_word in stop_words:
        text = text.replace(stop_word, "*" * len(stop_word))
    
    print(text)

if __name__ == '__main__':
    main()
