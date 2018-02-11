#!/usr/bin/env python
"""Write a program to read two rectangles {left, top, width, height} 
and print whether the first is inside the second."""

__author__ = "Petar Stoyanov"


class Rectangle:
    def __init__(self, *geometry):
        self.x1 = geometry[0]
        self.y1 = geometry[1]
        self.width = geometry[2]
        self.height = geometry[3]
        self.x2 = self.x1 + self.width
        self.y2 = self.y1
        self.x3 = self.x2
        self.y3 = self.y1 + self.height
        self.x4 = self.x1
        self.y4 = self.y3


def main():
    """Docstring"""

    rect1 = Rectangle(*[int(n) for n in input().split()])
    rect2 = Rectangle(*[int(n) for n in input().split()])

    if (
        rect1.x2 in range(rect2.x1, rect2.x3 + 1) 
        and rect1.x2 in range(rect2.x1, rect2.x3 + 1) 
        and rect1.y1 in range(rect2.y1, rect2.y3 + 1) 
        and rect1.y1 in range(rect2.y1, rect2.y3 + 1)
    ):
        print("Inside")
    else:
        print("Not inside")
    

if __name__ == '__main__':
    main()
