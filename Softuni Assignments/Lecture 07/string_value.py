#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""

    text = input()
    normalized = input()

    if normalized == "LOWERCASE":
        asci_value = sum([ord(ch) for ch in text if ch.isalpha() and ch == ch.lower()])

    if normalized == "UPPERCASE":
        asci_value = sum([ord(ch) for ch in text if ch.isalpha() and ch == ch.upper()])

    print(f'The total sum is: {asci_value}')

if __name__ == '__main__':
    main()
