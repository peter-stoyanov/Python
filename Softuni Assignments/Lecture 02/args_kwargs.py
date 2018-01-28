#!/usr/bin/env python
"""Args, Kwargs"""

__author__ = "Petar Stoyanov"

def main(*args, **kwargs):
    """Docstring"""
    for arg in args:
        print(arg)
    for (key, value) in kwargs.items():
        print("{} - {}".format(key, value))

if __name__ == '__main__':
    main(1, 2, 3, name='pesho', age=30)
