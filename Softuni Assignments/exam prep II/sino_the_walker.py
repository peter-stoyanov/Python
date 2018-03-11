#!/usr/bin/env python
"""Sino The Walker"""

__author__ = "Petar Stoyanov"

from datetime import datetime, timedelta

def main():
    """
    You will receive the time that Sino leaves SoftUni, the steps taken and time for each step, in seconds. 
    You need to print the exact time that he will arrive at home in the format specified.
    in: 12:30:30
        90
        1
    out: 
        Time Arrival: 12:32:00
    """

    leaving_time = datetime.strptime('23:49:13', '%H:%M:%S')
    steps_count = 5424 #int(input())
    step_time = 2 #int(input())


    arrival_time = addSecs(leaving_time, steps_count * step_time)

    print(f'Time Arrival: {arrival_time}')
    

def addSecs(tm, secs):
    fulldate = datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + timedelta(seconds=secs % 86400)
    return fulldate.time()


if __name__ == '__main__':
    main()
