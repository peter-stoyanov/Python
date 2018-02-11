#!/usr/bin/env python
"""You have been tasked to create an ordered database of websites"""

__author__ = "Petar Stoyanov"


class Website:
    def __init__(self, host, domain, query=''):
        self.host = host
        self.domain = domain
        self.query = [q.strip() for q in query.split(",") if q != '']

    def output(self):
        if len(self.query) > 0:
            query_string = '&'.join(['[' + item + ']' for item in self.query])
            result = f'https://www.{self.host}.{self.domain}/query?={query_string}'
        else:
            result = f'https://www.{self.host}.{self.domain}'
        
        return result


def main():
    """Docstring"""

    websites = []
    while True:
        input_data = [item for item in input().split(" | ")]
        if input_data[0] == "end":
            break
        try:
            websites.append(Website(input_data[0], input_data[1], input_data[2]))
        except:
            websites.append(Website(input_data[0], input_data[1]))
    
    for item in websites:
        print(item.output())


if __name__ == '__main__':
    main()
