#!/usr/bin/env python
"""Football League"""

__author__ = "Petar Stoyanov"

from collections import defaultdict
import re

team_points = defaultdict(int)
team_goals = defaultdict(int)

def main():
    """Docstring"""

    global team_points
    global team_goals

    enc_key = input()

    while True:
        command = input()

        if command == 'final':
            break
    
        teams = get_teams(command, enc_key)
        scores = get_points(command)
        
        populate_scores((teams[0], scores[0]), (teams[1], scores[1]))
        
    print('ended')
    print_standings()

def get_teams(command, enc_key):
    regex = re.compile(r"""
        (?<=$$$$$)
        (
            \w+?
        )
        (?=$$$$$)
        """.replace('$$$$$', re.escape(enc_key)), re.VERBOSE)

    return [name[::-1] for name in regex.findall(command)]


def get_points(command):
    return [int(token) for n in command.split(' ') for token in n.split(':') if ':' in n]

def populate_scores(team1_data, team2_data):
    global team_points
    global team_goals

    team1, score1 = team1_data
    team2, score2 = team2_data

    if score1 == score2:
        team_points[team1] += 1
        team_points[team2] += 1
    elif score1 > score2:
        team_points[team1] += 3
    else:
        team_points[team2] += 3
    
    team_goals[team1] += score1
    team_goals[team2] += score2

def print_standings():
    '''
    League standings:
    {place}. {TEAM NAME} {points}
    '''
    global team_points
    global team_goals

    print('League standings:')
    for index, key in enumerate(sorted(team_points.keys())):
        print(f'{index + 1}. {key.upper()} {team_points[key]}')

if __name__ == '__main__':
    main()
