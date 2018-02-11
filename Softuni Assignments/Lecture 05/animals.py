#!/usr/bin/env python
"""Docstring"""

__author__ = "Petar Stoyanov"


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, legs):
        super().__init__(self, name, age)
        self.legs = legs

    def talk(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

    def information(self):
        print(f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.legs}')


class Cat(Animal):
    def __init__(self, name, age, iq):
        super().__init__(self, name, age)
        self.iq = iq

    def talk(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

    def information(self):
        print(f'Cat: {self.name}, Age: {self.age}, IQ: {self.iq}')


class Snake(Animal):
    def __init__(self, name, age, cruelty):
        super().__init__(self, name, age)
        self.cruelty = cruelty

    def talk(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def information(self):
        print(f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty}')


def main():
    """Docstring"""

    animals = {}

    while True:
        inputLine = input()
        
        if inputLine == "I'm your Huckleberry":
            break
        
        inputLine = inputLine.split()
        
        if inputLine[0] == "Dog":
            animals.update({inputLine[1]: Dog(inputLine[1], inputLine[2], inputLine[3])})
        elif inputLine[0] == "Cat":
            animals.update({inputLine[1]: Cat(inputLine[1], inputLine[2], inputLine[3])})
        elif inputLine[0] == "Snake":
            animals.update({inputLine[1]: Snake(inputLine[1], inputLine[2], inputLine[3])})
        elif inputLine[0] == "talk":
            animals[inputLine[1]].talk()

    for animal in animals:
        animal.information()


if __name__ == '__main__':
    main()

