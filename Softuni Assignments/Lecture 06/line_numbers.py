#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""

    input_file_path = "./Resources/02. Line Numbers/Input.txt"
    output_file_path = "./Output/02. Line Numbers/Output.txt"

    with open(input_file_path) as input_file:

        contents = [str(index + 1) + ". " + line for index, line in enumerate(input_file)]

        with open(output_file_path, 'w') as output_file:
            writer = [output_file.write(item) for item in contents]


if __name__ == '__main__':
    main()
