#!/usr/bin/env python
"""Ticket train system"""

__author__ = "Petar Stoyanov"

class Ticket():
    def __init__(self, destination, price, card=None, discounted=False):
        self.destination = destination
        if discounted:
            self.price = 0.5 * price
            self.card = card
        else:
            self.price = price
            self.card = ''

class Client():
    def __init__(self, name, card=None):
        self.name = name
        if card:
            self.cards = [card]
        else:
            self.cards = []
        self.tickets = []
    
    def get_total(self):
        sum = 0
        for ticket in self.tickets:
            sum += ticket.price
        return sum

def main():
    """Docstring"""

    clients = []
    existing_cards_count = int(input())
    for n in range(existing_cards_count):
        tokens = input().split(' ')
        name = tokens[0] + ' ' + tokens[1]
        card = tokens[2]
        existing_client = find_client_by_name(clients, name)
        if existing_client:
            existing_client.cards.append(card)
        else:
            clients.append(Client(name, card))
    while True:
        tokens = input()
        if tokens == 'time to leave!':
            break
        tokens = tokens.split(' ')
        name = tokens[1] + ' ' + tokens[2]
        destination = tokens[3]
        attempted_card = tokens[4]
        client = find_client_by_name(clients, name)
        if client:
            existing_for_this_client = attempted_card in client.cards
            if existing_for_this_client:
                new_ticket = Ticket(destination, get_price(destination), attempted_card, discounted=True)
                client.tickets.append(new_ticket)
            else:
                if card_is_valid(attempted_card):
                    client_with_this_card = find_client_by_card(clients, attempted_card)
                    if client_with_this_card:
                        print(f'card {attempted_card} already exists for another passenger!')
                        new_ticket = Ticket(destination, get_price(destination))
                        client.tickets.append(new_ticket)
                    else:
                        print(f'issuing card {attempted_card}')
                        client.cards.append(attempted_card)
                        new_ticket = Ticket(destination, get_price(destination), attempted_card, discounted=True)
                        client.tickets.append(new_ticket)
                else:
                    print(f'card {attempted_card} is not valid!')
                    new_ticket = Ticket(destination, get_price(destination))
                    client.tickets.append(new_ticket)
        else:
            client = Client(name)
            if card_is_valid(attempted_card):
                client_with_this_card = find_client_by_card(clients, attempted_card)
                if client_with_this_card:
                    print(f'card {attempted_card} already exists for another passenger!')
                    new_ticket = Ticket(destination, get_price(destination))
                    client.tickets.append(new_ticket)
                    clients.append(client)
                else:
                    print(f'issuing card {attempted_card}')
                    client.cards.append(attempted_card)
                    new_ticket = Ticket(destination, get_price(destination), attempted_card, discounted=True)
                    client.tickets.append(new_ticket)
                    clients.append(client)
            else:
                print(f'card {attempted_card} is not valid!')
                new_ticket = Ticket(destination, get_price(destination))
                client.tickets.append(new_ticket)
                clients.append(client)

    
    sorted_clients = sorted([c for c in clients if c.get_total() > 0], key=lambda x: x.get_total(), reverse=True)
    for client in sorted_clients:
        print(f'{client.name}:')
        sorted_tickets = sorted(client.tickets, key=lambda x: x.price, reverse=True)
        for ticket in sorted_tickets:
            addition = f' (using card {ticket.card})' if ticket.card != '' else ''
            print(f'--{ticket.destination}: {ticket.price:.2f}lv' + addition)
        print(f'total: {client.get_total():.2f}lv')


def card_is_valid(attempted_card):
    sum = 0
    for ch in attempted_card:
        sum += int(ch)
    return sum % 7 == 0

def get_price(destination):
    price = 0.00
    for ch in destination:
        price += ord(ch)
    return price / 100

def find_client_by_card(clients, card):
    for c in clients:
        if card in c.cards:
            return c


def find_client_by_name(clients, name):
    for c in clients:
        if c.name == name:
            return c

if __name__ == '__main__':
    main()
