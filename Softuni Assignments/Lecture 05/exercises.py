#!/usr/bin/env python
"""Implement a class Exercise, which has a topic (string), a course_name (string), 
a judge_contest_link (string), and problems (collection of strings)."""

__author__ = "Petar Stoyanov"


class Exercise:
    def __init__(self, topic, course_name, link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = link
        self.problems = problems


def main():
    """Docstring"""

    exercises = []
    
    while True:
        inputLine = input().split(" -> ")
        if inputLine[0] == "go go go":
            break
        exercises.append(Exercise(inputLine[0], inputLine[1], inputLine[2], inputLine[3].split(", ")))
    
    for exercise in exercises:
        print(f'Exercises: {exercise.topic}')
        print(f'Problems for exercises and homework for the "{exercise.course_name}" course @ SoftUni.')
        print(f'Check your solutions here: {exercise.judge_contest_link}')
        
        for i in range(len(exercise.problems)):
            print("{}. {}".format(i + 1, exercise.problems[i]))


if __name__ == '__main__':
    main()
