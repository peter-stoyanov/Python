#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """14284124 : Alex
        Gosho : 088423123
        Ivan : 412048192
        Over

        Alex -> 14284124 (sorted alphabetically)
    """

    phones = {}

    command = input()

    while command != 'OVER':
        tokens = [token.strip() for token in command.split(':')]
        
        if len(tokens) != 2:
            continue
        
        # decide which token is number
        try:
            phone_number = int(tokens[0])
            name = tokens[1]
        except Exception:
            phone_number = int(tokens[1])            
            name = tokens[0]
        
        phones[name] = phone_number

        command = input()

    results = [f"{key} -> {phones[key]}" for key in sorted(phones.keys())]

    print('\n'.join(results))


if __name__ == '__main__':
    main()
