#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

def main():
    """Docstring"""
    array = [int(n) for n in input().split(' ')]
    while True:
        command = input()
        if command == 'end':
            break
        array = dispatcher(array, command)
    print_array(array)
    
def print_array(arr):
    print('[' + ', '.join([str(n) for n in arr]) + ']')
        
def index_in_array(arr, index):
    return index >= 0 and index < len(arr)
        
def dispatcher(arr, cmd):
    """Executes the passed command if such exists"""
    cmd_start_token = cmd[:3].lower()
    commands = {
        'exc' : exchange,
        'max' : get_max,
        'min' : get_min,
        'fir' : get_first,
        'las' : get_last}
    return commands[cmd_start_token](arr, cmd) if cmd_start_token in commands else 'No such command.'

def exchange(arr, cmd):
    flip_index = int(cmd.split(' ')[1])
    if flip_index > len(arr) - 1 or flip_index < 0:
        print("Invalid index")
        return arr
    return arr[flip_index + 1:] + arr[:flip_index + 1]

def get_max(arr, cmd):
    is_odd = cmd.split(' ')[1].lower() == 'odd'
    if is_odd:
        sorted_odds = [n for n in sorted(arr, reverse=True) if n % 2 != 0]
        print(arr.index(sorted_odds[0]) if len(sorted_odds) > 0 else 'No matches')
    else:
        sorted_evens = [n for n in sorted(arr, reverse=True) if n % 2 == 0]
        print(arr.index(sorted_evens[0]) if len(sorted_evens) > 0 else 'No matches')
    return arr

def get_min(arr, cmd):
    is_odd = cmd.split(' ')[1].lower() == 'odd'
    if is_odd:
        sorted_odds = [n for n in sorted(arr) if n % 2 != 0]
        print(arr.index(sorted_odds[0]) if len(sorted_odds) > 0 else 'No matches')
    else:
        sorted_evens = [n for n in sorted(arr) if n % 2 == 0]
        print(arr.index(sorted_evens[0]) if len(sorted_evens) > 0 else 'No matches')
    return arr

def get_first(arr, cmd):
    count = int(cmd.split(' ')[1].lower())
    is_odd = cmd.split(' ')[2].lower() == 'odd'
    if is_odd:
        odds = [n for n in arr if n % 2 != 0][:count]
        print_array(odds) if count <= len(arr) else print('Invalid count')
    else:
        evens = [n for n in arr if n % 2 == 0][:count]
        print_array(evens) if count <= len(arr) else print('Invalid count')
    return arr

def get_last(arr, cmd):
    count = int(cmd.split(' ')[1].lower())
    is_odd = cmd.split(' ')[2].lower() == 'odd'
    if is_odd:
        odds = [n for n in arr if n % 2 != 0][-count:]
        print_array(odds) if count <= len(arr) else print('Invalid count')
    else:
        evens = [n for n in arr if n % 2 == 0][-count:]
        print_array(evens) if count <= len(arr) else print('Invalid count')
    return arr


if __name__ == '__main__':
    main()
