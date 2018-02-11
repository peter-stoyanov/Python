#!/usr/bin/env python
"""Write a method to calculate the distance between two points p1 {x1, y1} and p2 {x2, y2}. 
Write a program to read two points (given as two integers) and print the Euclidean distance between them."""

__author__ = "Petar Stoyanov"

import math

class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def distanceFrom(self, point):
        if not isinstance(point, Point):
            raise TypeError('Argument must be of type Point.')

        deltaX = pow((point.x - self.x), 2)
        deltaY = pow((point.y - self.y), 2)
        
        return math.sqrt(deltaX + deltaY)


def main():
    """Docstring"""

    userInput = input().split()
    point1 = Point(userInput[0], userInput[1])
    
    userInput = input().split()
    point2 = Point(userInput[0], userInput[1])
    
    distance = point1.distanceFrom(point2)

    print(f'{distance:.3f}')


if __name__ == '__main__':
    main()
