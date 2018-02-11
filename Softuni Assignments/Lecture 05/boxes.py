#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def calculate_distance(self, point1, point2):
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y
        distance = int(sqrt(pow((self.x1 - self.x2), 2) + pow((self.y1 - self.y2), 2)))
        return distance


class Rectangle:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    @staticmethod
    def calculate_perimeter(width, height):
        if width * height == 0:
            return 0
        return int(2 * width + 2 * height)

    @staticmethod
    def calculate_area(width, height):
        return int(width * height)


def main():
    """Docstring"""

    data = {}
    counter = 0
    while True:
        input_string = input()
        
        if input_string == "end":
            break
        
        input_string = input_string.split(" | ")
    
        collection = [Point(item.split(":")[0], item.split(":")[1]) for item in input_string]
    
        data.update({counter: collection})
    
        counter += 1
    
    for item in sorted(data):
        points = data[item]
        width = points[3].calculate_distance(points[0], points[1])
        height = points[3].calculate_distance(points[0], points[2])
        area = Rectangle.calculate_area(width=width, height=height)
        perimeter = Rectangle.calculate_perimeter(width=width, height=height)
    
        print(f'Box: {width}, {height}')
        print(f'Perimeter: {perimeter}')
        print(f'Area: {area}')

if __name__ == '__main__':
    main()
