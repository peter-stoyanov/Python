#!/usr/bin/env python
"""Kamino factory"""

__author__ = "Petar Stoyanov"

def main():
    """5
    1!0!1!1!0
    0!1!1!0!0
    Clone them!
    """

    sequences = []

    sequence_count = int(input())
    while True:
        raw_sequence = input()
        
        if raw_sequence == 'Clone them!':
            break

        sequence = [int(token) for token in raw_sequence if token == '1' or token == '0']
        sequences.append(sequence)
    
    for sequence in sequences:
        for num in sequence:
            pass        



if __name__ == '__main__':
    main()
