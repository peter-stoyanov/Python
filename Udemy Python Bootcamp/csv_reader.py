import csv

#!/usr/bin/env python
"""CSV file reader"""

def main():
    """CSV file reader"""

    with open('d:\\PStoyanov\\repo\\Python\\Udemy Python Bootcamp\\example.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        dates = []
        colors = []
        for row in readCSV:
            color = row[3]
            date = row[0]

            dates.append(date)
            colors.append(color)

    print(dates)
    print(colors)

if __name__ == '__main__':
    main()
