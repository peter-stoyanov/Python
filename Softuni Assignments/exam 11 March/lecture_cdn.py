#!/usr/bin/env python
"""Softuni Lecture CDN"""

__author__ = "Petar Stoyanov"

from datetime import datetime, timedelta, date
import re
from functools import reduce


class Lecture():
    def __init__(self, name, trainer, course, duration, server):
        self.name = name
        self.trainer = trainer
        self.course = course
        #self.duration = datetime.strptime(duration, '%Hh%Mm')
        self.hours = get_hours(duration)
        self.minutes = get_minutes(duration)
        self.duration = get_duration(duration)
        self.server = server

def get_hours(text):
    tokens = re.split('h|m', text)
    return int(tokens[0])

def get_minutes(text):
    tokens = re.split('h|m', text)
    return int(tokens[1])

def get_duration(text):
    return get_hours(text) * 60 + get_minutes(text)

def main():
    """Docstring
    lecture:{name};trainer:{trainer};course:{trainer};duration:{hours}h{minutes}m
    """

    lectures = []
    # current_server_capacity = datetime.strptime('10h00m', '%Hh%Mm')
    current_server_capacity = 10 * 60
    current_server = 1

    while True:
        tokens = input()
        if tokens[:6] == 'scrape':
            break
        lecture, trainer, course, duration = extract_tokens(tokens)
        # parsed_duration = datetime.strptime(duration, '%Hh%Mm')
        parsed_duration = get_duration(duration)
        if current_server_capacity < parsed_duration:
            current_server += 1
            current_server_capacity = 10 * 60
        lectures.append(Lecture(lecture, trainer, course, duration, current_server))
        current_server_capacity -= parsed_duration 
    
    scrape_for_course = tokens.split(' ')[1].lower() == 'course'
    if scrape_for_course:
        course_name = tokens.split(' ')[2]
        filtered = [c for c in lectures if course_name == c.course]
        for course in filtered:
            print(f'https://streamcdn{course.server}.softuni.bg/course={course.course}&lecture={course.name}&trainer={course.trainer}')
        hours = sum([i.hours for i in filtered])
        minutes = sum([i.minutes for i in filtered])
        hours_from_minutes = minutes // 60
        minutes = minutes % 60
        hours = hours + hours_from_minutes
        print(f'total duration: {hours:02d}:{minutes:02d}:00')
    else:
        trainer_name = tokens.split(' ')[2]
        filtered = [c for c in lectures if trainer_name == c.trainer]
        for course in filtered:
            print(f'https://streamcdn{course.server}.softuni.bg/course={course.course}&lecture={course.name}&trainer={course.trainer}')
        hours = sum([i.hours for i in filtered])
        minutes = sum([i.minutes for i in filtered])
        hours_from_minutes = minutes // 60
        minutes = minutes % 60
        hours = hours + hours_from_minutes
        print(f'total duration: {hours:02d}:{minutes:02d}:00')


def extract_tokens(text):
    lecture = re.search(r'lecture:([\w-]+)($|(?=;))', text)
    trainer = re.search(r'trainer:([\w-]+)($|(?=;))', text)
    course = re.search(r'course:([\w-]+)($|(?=;))', text)
    duration = re.search(r'duration:(\d+h\d+m)($|(?=;))', text)

    return (lecture.group(1), trainer.group(1), course.group(1), duration.group(1))

if __name__ == '__main__':
    main()
