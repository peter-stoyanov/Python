#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

import os

def main():
    """Docstring"""

    file_extension = input()
    input_path = "./Resources/04. Filter-Extensions/input"
    all_files = []

    for dirs, subdirs, files in os.walk(input_path):
        for file in files:
            all_files.append(file)

    for file in filter(
        lambda filename: filename.split(".")[-1] == file_extension, all_files
        ):
        print(file)


if __name__ == '__main__':
    main()
