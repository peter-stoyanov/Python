#!/usr/bin/env python
"""Padawan Equipment"""

__author__ = "Petar Stoyanov"

import math

def main():
    """Docstring"""

    available_money = float(input())
    students_count = int(input())
    lightsabre_price = float(input())
    robe_price = float(input())
    belt_price = float(input())

    lightsabres_cost = math.ceil(students_count * 1.10) * lightsabre_price
    robes_cost = students_count * robe_price
    belts_cost = (students_count - int(students_count / 6)) * belt_price

    total_cost = lightsabres_cost + robes_cost + belts_cost

    if total_cost <= available_money:
        print(f'The money is enough - it would cost {total_cost:.2f}lv.')
    else:
        missing = total_cost - available_money
        print(f'Ivan Cho will need {missing:.2f}lv more.')


if __name__ == '__main__':
    main()
