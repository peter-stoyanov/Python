#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

import os

def main():
    """Docstring"""

    directory_path = "./Resources/07. Folder Size/TestFolder/"
    folder_size = 0

    for file_name in os.listdir(directory_path):
        filename = directory_path + file_name

        if os.path.isfile(filename):
            folder_size += os.stat(filename).st_size

    folder_size_in_MB = folder_size / 1024 / 1024

    print(folder_size_in_MB)

if __name__ == '__main__':
    main()
