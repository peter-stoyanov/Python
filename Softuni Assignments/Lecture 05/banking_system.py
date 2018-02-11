#!/usr/bin/env python
"""Create a class BankAccount which has 
a Name (string), Bank (string) and Balance (decimal)"""

__author__ = "Petar Stoyanov"

from operator import attrgetter

class BankAccount:
    def __init__(self, bank, account, balance):
        self.data = {}
        self.bank = bank
        self.account = account
        self.balance = float(balance)


def main():
    """Docstring"""

    accounts = []
    
    while True:
        inputLine = input().split(" | ")
        if inputLine[0] == "end":
            break
        accounts.append(BankAccount(inputLine[0], inputLine[1], inputLine[2]))
    
    for item in sorted(
        (sorted(accounts, key=attrgetter('bank'))), key=attrgetter('balance'),reverse=True):
        print("{0} -> {1:.2f} ({2})".format(item.account, item.balance, item.bank))


if __name__ == '__main__':
    main()
