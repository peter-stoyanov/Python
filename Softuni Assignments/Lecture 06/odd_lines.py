#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""

    input_file_path = "./Resources/01. Odd Lines/Input.txt"
    output_file_path = "./Output/01. Odd Lines/Output.txt"

    with open(input_file_path) as input_file:

        odd_lines = [line.split("\n")[0] for number, line in enumerate(input_file) if number % 2 == 1]

        with open(output_file_path, 'w') as output_file:

            for line in odd_lines[:-1]:
                output_file.write(line + "\n")

            output_file.write(odd_lines[-1])


if __name__ == '__main__':
    main()
