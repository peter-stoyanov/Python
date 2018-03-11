#!/usr/bin/env python
"""Caesar Login"""

__author__ = "Petar Stoyanov"

import re

def main():
    """Docstring"""

    while True:
        login = input()
        if login == '/end/':
            break
        credentials = extract_credentials(login)
        if not credentials:
            continue
        trash_chars = get_trash_chars(login)
        decrypted_username = decrypt(credentials[0], len(trash_chars))
        decrypted_password = decrypt(credentials[1], len(trash_chars))
        print(f'user: {decrypted_username}, pass: {decrypted_password}')


def get_trash_chars(text):
    #return [ch for ch in re.findall(r'\W', text) if ch not in '\\\///']
    regex = re.compile(r"""
        ^
        (?P<boundary>[\\/]{1})
        \W*(?P<username>[^_\W]+)
        \W*(?P=username)
        \W*(?P<password>[^_\W]+)
        \W*(?P=password)
        \W*(?P=username)
        \W*(?P=password)
        \W*(?P=boundary)
        $
        """, re.VERBOSE)

    matches = regex.finditer(text)
    for match in matches:
        text = text.replace(match.group('username'), '')
        text = text.replace(match.group('password'), '')
        text = text[1:-1]
        return text


def decrypt(text, offset):
    return ''.join([chr(ord(ch) - offset) for ch in text])


def extract_credentials(text):
    regex = re.compile(r"""
        ^
        (?P<boundary>[\\/]{1})
        \W*(?P<username>[^_\W]+)
        \W*(?P=username)
        \W*(?P<password>[^_\W]+)
        \W*(?P=password)
        \W*(?P=username)
        \W*(?P=password)
        \W*(?P=boundary)
        $
        """, re.VERBOSE)

    matches = regex.finditer(text)
    for match in matches:
        return (match.group('username'), match.group('password'))


if __name__ == '__main__':
    main()
