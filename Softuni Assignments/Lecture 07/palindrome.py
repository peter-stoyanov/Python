#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""

    words = input().split( )
    
    palindromes = set([word for word in words if word == word[::-1]])
    
    print(', '.join(sorted(palindromes, key=str.lower)))

if __name__ == '__main__':
    main()
