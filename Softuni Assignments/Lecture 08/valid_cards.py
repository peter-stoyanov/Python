#!/usr/bin/env python
"""Find all integer and floating-point numbers in a string."""

__author__ = "Petar Stoyanov"

import re

def main():
    """
    power – 2, 3, 4… 10, J, Q, K, A.
    suit – S, H, D, C

    in: 2S3S4S5S6S
    out: 2S 3S 4S 5S 6S
    """

    #text = input()
    text = '2SASKS6SJSQSOS'

    regex = re.compile(r"""
        ([2-9]|[JQKA]|10)
        [SHDC]
        """, re.VERBOSE)

    cards = [chunk for chunk in chunkstring(text, 2) if regex.match(chunk)]

    print(' '.join(cards))


def chunkstring(string, length):
    '''
    This function returns a generator, using a generator comprehension. 
    The generator returns the string sliced, from 0 + a multiple of the length of the chunks, 
    to the length of the chunks + a multiple of the length of the chunks.
    You can iterate over the generator like a list, tuple or string - for i in chunkstring(s,n): 
    , or convert it into a list (for instance) with list(generator)
    '''

    return (string[0+i:length+i] for i in range(0, len(string), length))


if __name__ == '__main__':
    main()
