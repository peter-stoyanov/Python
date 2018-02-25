#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

from shutil import copyfile
import os

def main():
    """Docstring"""

    input_folder = "./Resources/08. Re-Directory/input"
    output_folder = "./Output/08. Re-Directory"

    extensions = set([ext.split(".")[-1] for ext in os.listdir(input_folder)])

    extension_files = {ext: [] for ext in extensions}

    for ext in extension_files:
        extension_files[ext] = [file for file in os.listdir(input_folder) if file.split(".")[-1] == ext]
    
    for ext in extension_files:
        destination_folder = output_folder + "/" + ext + "s"
        os.mkdir(destination_folder)
        
        for file in extension_files[ext]:
            source = input_folder + "/" + file
            destination = destination_folder + "/" + file
            copyfile(source, destination)

if __name__ == '__main__':
    main()
